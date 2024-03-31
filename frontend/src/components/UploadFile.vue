<template>
  <div>
    <h2>Upload de Planilha</h2>
    <label for="fileInput">Selecione um arquivo:</label>
    <input type="file" id="fileInput" ref="fileInput" style="display: none" @change="handleFileChange"/>
    <button @click="openFileInput">Selecionar Arquivo</button>
    <button @click="uploadFile" :disabled="!file">Enviar</button>
  </div>
</template>

<script>
export default {
  name: 'UploadFile',
  data() {
    return {
      file: null
    }
  },
  methods: {
    openFileInput() {
      this.$refs.fileInput.click()
    },
    handleFileChange(event) {
      this.file = event.target.files[0]
    },
    uploadFile() {
      if (this.file) {
        const formData = new FormData()
        formData.append('file', this.file)

        fetch('http://localhost:5000/upload', {
          method: 'POST',
          body: formData
        })
            .then(response => response.json())
            .then(() => {
              this.$emit('fileUploaded')
            })
            .catch(error => {
              console.error('Error:', error)
            })
      }
    }
  }
}
</script>
