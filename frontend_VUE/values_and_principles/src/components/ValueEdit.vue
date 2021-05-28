<template>
 <div v-if="value">
   <p>{{value.title.charAt(0).toUpperCase() + value.title.slice(1)}}</p>
 </div>
</template>

<script>
export default {
  name: "ValueEdit",
  props: ['value']
}
</script>

<style scoped>

</style>