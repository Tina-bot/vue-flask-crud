<template>
  <FormEmpleado
    @submit-empleado="createEmpleado"
  />
</template>

<script>
import FormEmpleado from '@/components/FormEmpleado.vue'

export default {
  components: {
    FormEmpleado
  },
  methods: {
    async createEmpleado (nuevoEmpleado) {
      const result = await fetch('https://vue-flask-crud.herokuapp.com/empleados', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(nuevoEmpleado)
      })
      console.log(result)
    }
  }
}
</script>
