<template>
  <div class="home">
    <EmpleadosTable />
  </div>
</template>

<script>
import EmpleadosTable from '@/components/EmpleadosTable.vue'

export default {
  name: 'HomeView',
  components: {
    EmpleadosTable
  }
}
</script>
