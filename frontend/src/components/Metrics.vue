<template>
  <div class="metrics">
    <h2>Métricas</h2>
    <div v-if="loading">Carregando...</div>
    <div v-else>
      <div class="metric">
        <h3>MRR (Receita Recorrente Mensal)</h3>
        <canvas id="mrrChart" width="400" height="200"></canvas>
      </div>
      <div class="metric">
        <h3>Churn Rate</h3>
        <canvas id="churnRateChart" width="400" height="200"></canvas>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Chart from 'chart.js/auto';

export default {
  name: 'MetricsDashboard',
  data() {
    return {
      loading: false,
      metricsData: null,
      colors: [
        'rgba(255, 140, 0, 0.6)', 'rgba(32, 178, 170, 0.6)', 'rgba(147, 112, 219, 0.6)', 'rgba(50, 205, 50, 0.6)',
        'rgba(30, 144, 255, 0.6)', 'rgba(255, 105, 180, 0.6)', 'rgba(255, 99, 71, 0.6)', 'rgba(138, 43, 226, 0.6)',
        'rgba(0, 255, 126, 0.6)', 'rgba(255, 215, 0, 0.6)', 'rgba(0, 206, 209, 0.6)', 'rgba(255, 160, 122, 0.6)'
      ]
    };
  },
  async mounted() {
    await this.fetchMetrics(); // Chama a função para buscar as métricas ao montar o componente
    await this.renderCharts(); // Chama a função para renderizar as Charts
  },
  methods: {
    async fetchMetrics() {
      this.loading = true; // Define loading como true ao iniciar a busca das métricas

      await axios.get('http://localhost:5000/api/metrics')
          .then(response => {
            this.metricsData = response.data;
            this.loading = false; // Define loading como false após a conclusão da busca
          })
          .catch(error => {
            console.error('Erro ao obter métricas:', error);
            this.loading = false; // Define loading como false em caso de erro
          });
    },
    async renderCharts() {
      if (!this.metricsData) return; // Verifica se metricsData está definido

      const mrrCtx = document.getElementById('mrrChart');
      const churnRateCtx = document.getElementById('churnRateChart')

      if (!mrrCtx || !churnRateCtx) {
        console.error('Elemento do canvas não encontrado.');
        return;
      }

      const months = this.metricsData["mês início"]
      const mrr = this.metricsData["valor"]
      const churnRate = this.metricsData["churn rate"]

      const backgroundColors = months.map((month, index) => this.colors[index % this.colors.length]);

      await new Chart(mrrCtx, {
        type: 'bar',
        options: {
          animation: true,
          plugins: {
            legend: {
              display: true
            },
            tooltip: {
              enabled: true
            }
          }
        },
        data: {
          labels: months,
          datasets: [{
            label: 'MRR',
            data: mrr,
            backgroundColor: backgroundColors,
            borderColor: '#000000',
            borderWidth: 1
          }]
        }
      });
      await new Chart(churnRateCtx, {
        type: 'bar',
        options: {
          animation: true,
          plugins: {
            legend: {
              display: true
            },
            tooltip: {
              enabled: true
            }
          }
        },
        data: {
          labels: months,
          datasets: [{
            label: 'Churn Rate',
            data: churnRate,
            backgroundColor: backgroundColors,
            borderColor: 'rgba(0, 0, 0, 1)',
            borderWidth: 1
          }]
        }
      });
    }
  }
};
</script>


<style scoped>
.metrics {
  margin-top: 20px;
}

.metric {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}

.metric h3 {
  margin-top: 0;
}
</style>
