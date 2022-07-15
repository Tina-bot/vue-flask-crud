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
      const result = await fetch('http://localhost:5000/empleados', {
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
