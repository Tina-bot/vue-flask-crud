<template>
  <div class="container">
    <h2>Desea eliminar el empleado?</h2>
    <button class="btn btn-danger" @click="eliminarEmpleado">
      <i class="fas fa-trash"> Eliminar</i>
    </button>
    <button class="btn btn-success" @click="cancelar">
      <i class="fas fa-times"> Cancelar</i>
    </button>
  </div>
</template>
<script>
export default
{
  data () {
    return {
      empleados: []
    }
  },
  methods: {
    async eliminarEmpleado () {
      const result = await fetch(`https://vue-flask-crud.herokuapp.com/empleados/${this.$route.params.id}`, {
        method: 'DELETE'
      })
      console.log(result)
      this.$router.push('/')
    },
    cancelar () {
      this.$router.push('/')
    }
  },
  created () {
    this.fetchEmpleados()
  }

}
</script>
