<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'
import CurriculumMap from './CurriculumMap.vue'
import ProblemRelations from './ProblemRelations.vue'

const DefaultLayout = DefaultTheme.Layout
</script>

<template>
  <DefaultLayout>
    <!-- Homepage: the curriculum map sits under the hero feature cards. -->
    <template #home-features-after>
      <CurriculumMap />
    </template>

    <!-- Problem pages: incoming/outgoing relationships after the solution. -->
    <template #doc-after>
      <ProblemRelations />
    </template>
  </DefaultLayout>
</template>
