<template>
  <div>
    <p class="item">{{ principle.description }}</p>

    <font-awesome-icon
      class="edit"
      icon="edit"
      @click="$emit('principleEdit', principle.id)"
    />

    <font-awesome-icon
      class="trash"
      icon="trash"
      @click="$emit('principleDelete', principle.id)"
    />
  </div>
</template>

<script>
export default {
  name: "PrincipleItem",
  props: ["principle"],
};
</script>

<style scoped>
p {
  text-align: left;
  width: 70%;
  display: inline-block;
  margin-bottom: 0;
  padding: 5px 0;
}

.edit {
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
