# Metrics App

Este é um aplicativo para visualização de métricas, incluindo Receita Recorrente Mensal (MRR) e Churn Rate. O aplicativo é construído com Vue.js para o frontend e Flask para o backend.

## Pré-requisitos

Certifique-se de ter Docker instalado em sua máquina antes de prosseguir.

- Docker: [Instalação do Docker](https://docs.docker.com/get-docker/)

## Instalação e Execução

Siga estas etapas para instalar e executar o aplicativo localmente:

1. Clone este repositório para o seu ambiente de desenvolvimento:

```bash
git clone https://github.com/zawarudobngdev/MetricsApp.git
```

2. Navegue até o diretório do projeto:

```bash
cd MetricsApp
```

3. Construa e execute os contêineres Docker usando o docker-compose:

```bash
docker-compose up --build
```

Isso criará e iniciará os contêineres Docker para o frontend e o backend.

4. Acesse o aplicativo em seu navegador:

Abra um navegador da web e navegue até `http://localhost:8080` para acessar o aplicativo.

## Uso

Após acessar o aplicativo, você pode fazer upload de uma planilha de métricas para visualizar os gráficos de MRR e Churn Rate.

'''
No momento a aplicação só funcionará corretamente utilizando a planilha específica do desafio ou uma que contenha os mesmos campos, para que os cálculos de MRR e Churn Rate sejam feitos corretamente.
'''

## Contribuição

Se você quiser contribuir com este projeto, siga estas etapas:

1. Faça um fork do repositório
2. Crie uma branch para sua contribuição: `git checkout -b feature/NovaFeature`
3. Faça commit de suas alterações: `git commit -m 'Adiciona NovaFeature'`
4. Faça push para a branch: `git push origin feature/NovaFeature`
5. Abra um pull request no repositório original

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

## Contato
### Murilo Meranca
![dog](https://avatars.githubusercontent.com/u/129321279?v=4)

[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DC?style=for-the-badge)](https://web.dio.me/users/murilo_m_17570/)
[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:murilo.m@hotmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=30A3DC)](https://www.linkedin.com/in/murilo-meranca/)
