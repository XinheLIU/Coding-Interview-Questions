<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'
import CurriculumMap from './CurriculumMap.vue'
import RecentProblems from './RecentProblems.vue'

const DefaultLayout = DefaultTheme.Layout
</script>

<template>
  <DefaultLayout>
    <!-- Homepage: personal history appears before the shared curriculum map. -->
    <template #home-features-after>
      <RecentProblems />
      <CurriculumMap />
    </template>
  </DefaultLayout>
</template>
