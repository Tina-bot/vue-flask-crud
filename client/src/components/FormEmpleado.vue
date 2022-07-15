<template>
  <div class="container">
    <h2>{{ titulo }}</h2>

    <div class="card">
      <h4 class="card-header">Sus datos 📝</h4>
      <div class="card-header">
        <form @submit.prevent="enviarDatos" class="row g-3">
          <!-- Nombre -->
          <div class="col-md-6">
            <label for="nombre" class="form-label">Nombre</label>
            <input v-model="nombre" type="text" id="nombre" class="form-control" />
          </div>

          <!-- Apellido -->
          <div class="col-md-6">
            <label for="apellido" class="form-label">Apellido</label>
            <input v-model="apellido" type="text" id="apellido" class="form-control" />
          </div>

          <!-- Edad -->
          <div class="col-md-3">
            <label for="edad" class="form-label">Edad</label>
            <input v-model="edad" type="number" id="edad" class="form-control" />
          </div>

          <!-- Cargo -->
          <div class="col-md-3">
            <label for="cargo" class="form-label">Cargo</label>
            <input v-model="cargo" type="text" id="cargo" class="form-control" />
          </div>

          <!-- Salario -->
          <div class="col-md-3">
            <label for="salario" class="form-label">Salario</label>
            <input v-model="salario" type="number" id="salario" class="form-control" />
          </div>

          <!-- Fecha de Nacimiento -->
          <div class="col-md-3">
            <label for="fecha_nacimiento" class="form-label">Fecha de Nacimiento</label>
            <input
              v-model="fecha_nacimiento"
              type="date"
              id="fecha_nacimiento"
              class="form-control"
            />
          </div>

          <div class="col-12">
            <button class="btn btn-success" href="/">Enviar datos</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    titulo: {
      type: String,
      default: 'Nuevo empleado'
    },
    empleado: {
      type: Object,
      default: () => {}
    }
  },
  data () {
    // Cada variable agarra un input
    return {
      nombre: '',
      apellido: '',
      edad: 0,
      cargo: '',
      salario: 0,
      fecha_nacimiento: ''
    }
  },
  watch: {
    empleado () {
      this.popularDatos()
    }
  },
  methods: {
    // Esto rellena el formulario
    popularDatos () {
      if (!this.empleado) {
        return
      }
      this.nombre = this.empleado.nombre
      this.apellido = this.empleado.apellido
      this.edad = this.empleado.edad
      this.cargo = this.empleado.cargo
      this.salario = this.empleado.salario
      this.fecha_nacimiento = this.empleado.fecha_nacimiento
    },
    // Esto arma el objeto empleado para crear o editar
    enviarDatos () {
      const empleado = {
        nombre: this.nombre,
        apellido: this.apellido,
        edad: this.edad,
        cargo: this.cargo,
        salario: this.salario,
        fecha_nacimiento: this.fecha_nacimiento
      }
      // Esto lo recibe el NuevoEmpleadoView o EditarEmpleadoView
      this.$emit('submit-empleado', empleado)
      this.$router.push('/')
    }
  }
}
</script>
