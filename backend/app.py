import os
import traceback

import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo encontrado'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        return jsonify({'message': 'Arquivo salvo em: ' + filepath}), 200
    else:
        return jsonify({'error': 'Tipo de arquivo não suportado'}), 400



def calculate_churn_rate(df):
    # Filtrar as assinaturas que foram canceladas
    cancelled_subs = df[df['status'] == 'Cancelada']

    # Agrupar pelo mês de início e contar o número de assinaturas canceladas
    churn_data = cancelled_subs.groupby('mês início').size().reset_index(name='cancelamentos')

    # Calcular o número total de assinaturas ativas no início de cada mês
    active_subs = df[df['status'] == 'Ativa'].groupby('mês início')['ID assinante'].nunique().reset_index(
        name='assinantes')

    # Mesclar os dados de cancelamentos e assinantes ativos
    churn_data = pd.merge(active_subs, churn_data, on='mês início', how='left').fillna(0)

    # Calcular a taxa de churn para cada mês
    churn_data['churn rate'] = churn_data['cancelamentos'] / churn_data['assinantes']

    return churn_data[['mês início', 'churn rate']]


@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    try:
        uploaded_files = os.listdir(UPLOAD_FOLDER)
        if not uploaded_files:
            return jsonify({'error': 'Nenhum arquivo de planilha enviado'}), 400

        # Assume que há apenas um arquivo de planilha para fins do projeto proposto
        filepath = os.path.join(UPLOAD_FOLDER, uploaded_files[0])

        df = pd.read_excel(filepath)

        # Converte as colunas de datas para o tipo datetime, se necessário
        df['data início'] = pd.to_datetime(df['data início'])
        df['próximo ciclo'] = pd.to_datetime(df['próximo ciclo'])

        # Cria uma coluna para o mês de início de cada assinatura
        df['mês início'] = df['data início'].dt.to_period('M')

        # Calcular o MRR para cada mês
        mrr_data = df.groupby('mês início')['valor'].sum().reset_index()

        # Calcular o churn rate para cada mês
        churn_data = calculate_churn_rate(df)

        # Converter períodos para strings antes de serializar em JSON
        mrr_data['mês início'] = mrr_data['mês início'].astype(str)
        churn_data['mês início'] = churn_data['mês início'].astype(str)

        # Mesclar os dados de MRR e churn rate
        metrics_data = pd.merge(mrr_data, churn_data, on='mês início')

        # Converter para dicionário para serialização em JSON
        metrics_json = metrics_data.to_dict(orient='list')

        return jsonify(metrics_json), 200
    except Exception as e:
        traceback.print_exc()  # Isso imprime o traceback completo da exceção no console
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
