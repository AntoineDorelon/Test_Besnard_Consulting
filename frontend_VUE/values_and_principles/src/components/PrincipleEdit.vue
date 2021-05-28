<template>
  <div v-if="principle">
    <p>{{principle.description}}</p>

  </div>
</template>

<script>
export default {
  name: "PrincipleEdit",
  props: ['principle']
}
</script>

<style scoped>

</style>