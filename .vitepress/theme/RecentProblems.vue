<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { withBase } from 'vitepress'
import { readRecentProblems, type RecentProblem } from './recentProblems'

const recentProblems = ref<RecentProblem[]>([])

onMounted(() => {
  recentProblems.value = readRecentProblems()
})

function problemLink(problem: RecentProblem): string {
  return withBase(`/problems/${problem.dir}/`)
}
</script>

<template>
  <section v-if="recentProblems.length" class="recent-problems" aria-labelledby="recent-problems-title">
    <h2 id="recent-problems-title">Recently viewed</h2>
    <ul>
      <li v-for="problem in recentProblems" :key="problem.id">
        <a :href="problemLink(problem)">#{{ problem.id }} {{ problem.title }}</a>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.recent-problems {
  max-width: 1152px;
  margin: 8px auto 40px;
  padding: 0 24px;
}

.recent-problems h2 {
  margin: 0 0 16px;
  border: 0;
  font-size: 24px;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.recent-problems ul {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 8px 24px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.recent-problems li {
  border-top: 1px solid var(--vp-c-divider);
  padding-top: 9px;
  font-size: 14px;
}

.recent-problems a {
  font-weight: 500;
}
</style>
