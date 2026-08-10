<script setup lang="ts">
import { computed } from 'vue'
import { withBase } from 'vitepress'
import graphData from '../problem-graph.json'

const props = defineProps<{ parent: string }>()

interface Chapter {
  id: string
  title: string
  page: string
  blurb: string
  parent: string | null
  level: number
  count: number
}

const graph = graphData as unknown as { chapters: Chapter[] }
const children = computed(() =>
  graph.chapters.filter((chapter) => chapter.parent === props.parent)
)

function pageLink(chapter: Chapter): string {
  return withBase(chapter.page)
}
</script>

<template>
  <section v-if="children.length" class="chapter-children" aria-labelledby="chapter-children-title">
    <h2 id="chapter-children-title">Concept chapters</h2>
    <div class="cards">
      <a v-for="chapter in children" :key="chapter.id" :href="pageLink(chapter)" class="card">
        <h3>{{ chapter.title }} <span>{{ chapter.count }}</span></h3>
        <p>{{ chapter.blurb }}</p>
      </a>
    </div>
  </section>
</template>

<style scoped>
.chapter-children {
  margin: 36px 0;
}

.chapter-children h2 {
  margin-bottom: 16px;
  border: 0;
  padding-top: 0;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
}

.card {
  display: block;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 14px 16px;
  color: inherit;
  transition: border-color 0.2s, background-color 0.2s;
}

.card:hover {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-bg-soft);
}

.card h3 {
  margin: 0;
  border: 0;
  padding: 0;
  font-size: 16px;
}

.card h3 span {
  color: var(--vp-c-text-3);
  font-weight: 400;
}

.card p {
  margin: 8px 0 0;
  color: var(--vp-c-text-2);
  font-size: 13px;
  line-height: 1.5;
}
</style>
