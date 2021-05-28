<template>
  <div>
    <p>
      {{ value.title.charAt(0).toUpperCase() + value.title.slice(1) }}
    </p>

    <font-awesome-icon class="edit" icon="edit" @click="$emit('value-edit',value.id)" />

    <font-awesome-icon class="trash" icon="trash" @click="$emit('value-delete', value.id)" />

  </div>
</template>

<script>
export default {
  name: "ValueItem",
  props: ['value']
}
</script>

<style scoped>
p {
  text-align: left;
  width: 70%;
  display: inline-block;
  margin-bottom: 0px;
  padding: 5px 0;
}
.edit{
  color: blue;
  cursor: pointer;
  float: end;
  margin-right: 15px;
  font-size: 200%;
}
.trash {
  color: red;
  cursor: pointer;
  float: end;
  margin-left: 15px;
  font-size: 200%;
}
</style>