<template>
    <div class="container">
        <h1>Empleados</h1>
      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h4 class="card-title"> Lista de Empleados🔎</h4>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <table class="table">
                  <thead class="text-primary">
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>Edad</th>
                    <th>Puesto</th>
                    <th>Salario</th>
                    <th>Fecha de Nacimiento</th>
                    <th>Acciones</th>
                  </thead>
                  <tbody>
                    <tr v-for="empleado in empleados" :key="empleado">
                      <td>
                        {{ empleado.nombre }}
                      </td>
                      <td>
                        {{ empleado.apellido }}
                      </td>
                      <td>
                        {{ empleado.edad }}
                      </td>
                      <td>
                        {{ empleado.cargo }}
                      </td>
                      <td>
                        ${{ empleado.salario }}
                      </td>
                      <td>
                        {{ empleado.fecha_nacimiento }}
                      </td>
                      <td>
                        <button class="btn btn-primary" @click="editarEmpleado(empleado)">
                          <i class="fas fa-edit"> Editar </i>
                        </button>
                        <button class="btn btn-danger" @click="eliminarEmpleado(empleado)">
                          <i class="fas fa-trash"> Eliminar</i>
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

                <div class="row">
                  <div class="col-md-12">
                    <button class="btn btn-success" type="button" @click="nuevoEmpleado">
                      <i class="fas fa-plus"> Nuevo Empleado</i>
                    </button>
                  </div>

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      empleados: []
    }
  },
  methods: {
    nuevoEmpleado () {
      this.$router.push('/empleados/nuevo')
    },
    editarEmpleado (empleado) {
      this.$router.push(`/empleados/editar/${empleado.id}`)
    },
    eliminarEmpleado (empleado) {
      this.$router.push(`/empleados/eliminar/${empleado.id}`)
    },
    async fetchEmpleados () {
      const response = await fetch('http://localhost:5000/empleados')
      const data = await response.json()
      this.empleados = data
    }
  },
  created () {
    this.fetchEmpleados()
  }
}
</script>
