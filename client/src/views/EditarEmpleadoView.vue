<template>
  <FormEmpleado
    :empleado="empleado"
    titulo="Editar Empleado"
    @submit-empleado="editarEmpleado"
  />
</template>

<script>
import FormEmpleado from '@/components/FormEmpleado.vue'

export default {
  data () {
    return {
      empleado: {}
    }
  },
  components: {
    FormEmpleado
  },
  created () {
    this.obtenerEmpleado(this.$route.params.id)
  },
  methods: {
    async editarEmpleado (empleado) {
      const result = await fetch(`http://localhost:5000/empleados/${this.$route.params.id}`, {
        method: 'PUT',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(empleado)
      })
      console.log(result)
    },
    async obtenerEmpleado (id) {
      const empleado = await fetch(`http://localhost:5000/empleados/${id}`)
      this.empleado = await empleado.json()
    }
  }
}
</script>
