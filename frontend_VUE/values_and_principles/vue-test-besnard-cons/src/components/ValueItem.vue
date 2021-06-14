<template>
  <div>
    <p>
      {{ value.title.charAt(0).toUpperCase() + value.title.slice(1) }}
    </p>

    <font-awesome-icon
      class="edit"
      :icon="EditIcon"
      @click="$emit('ValueEdit', value.id)"
    />

    <font-awesome-icon
      class="trash"
      :icon="TrashIcon"
      @click="$emit('ValueDelete', value.id)"
    />
  </div>
</template>

<script>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faEdit } from "@fortawesome/free-solid-svg-icons";
import { faTrash } from "@fortawesome/free-solid-svg-icons";

export default {
  name: "ValueItem",
  props: ["value"],
  components: {
    FontAwesomeIcon,
  },
  data() {
    return {
      EditIcon: faEdit,
      TrashIcon: faTrash,
    };
  },
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
