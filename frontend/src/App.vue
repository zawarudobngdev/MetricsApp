<template>
  <div id="app">
    <header>
      <h1>Aplicação de Métricas</h1>
    </header>
    <main>
      <UploadFile @fileUploaded="handleFileUploaded"/>
      <Metrics v-if="showMetrics"/>
    </main>
  </div>
</template>

<script>
import UploadFile from './components/UploadFile.vue';
import Metrics from './components/Metrics.vue';

export default {
  components: {
    UploadFile,
    Metrics
  },
  data() {
    return {
      showMetrics: false // Define showMetrics como false inicialmente
    };
  },
  methods: {
    handleFileUploaded() {
      this.showMetrics = true; // Altera showMetrics para true após o upload ser concluído
    }
  }
};
</script>


<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
}

header {
  background-color: #333;
  padding: 20px 0;
}

header h1 {
  color: #fff;
}

main {
  margin-top: 20px;
}
</style>
