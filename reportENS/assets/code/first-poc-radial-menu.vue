<template>
  <RadialMenu>
    <RadialWheel
      :innerRadius="innerRadius"
      :outerRadius="midRadius"
      :beginAngle="0"
      :endAngle="360"
    >
      <RadialWheelItem
        v-for="item in items"
        :label="item.label"
      />
    </RadialWheel>

    <RadialWheel
      :innerRadius="midRadius"
      :outerRadius="outerRadius"
      :beginAngle="180"
      :endAngle="360"
    >
      <RadialWheelItem label="test1" />
      <RadialWheelItem label="test2" />
      <RadialWheelItem label="test3" />
      <RadialCheckbox :size="3" label="CHECKBOX" />
    </RadialWheel>
  </RadialMenu>
</template>

<script setup>
import RadialWheelItem from './RadialWheelItem.vue';
import RadialWheel from './RadialWheel.vue';
import RadialMenu from './RadialMenu.vue';
import RadialCheckbox from './RadialCheckbox.vue';

const innerRadius = 40;
const midRadius = 120;
const outerRadius = 250;

defineProps([
  "items",
]);
</script>