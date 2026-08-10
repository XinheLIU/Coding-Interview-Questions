<script setup lang="ts">
/**
 * Every problem filed in a chapter, grouped by section, plus a cross-reference
 * block for problems homed elsewhere that still carry one of this chapter's
 * topics — so #337 House Robber III (chapter: dynamic-programming) is still
 * discoverable from Trees & Heaps.
 */
import { computed } from 'vue'
import { withBase } from 'vitepress'
import graphData from '../problem-graph.json'

const props = defineProps<{ chapter: string }>()

interface ChapterSection {
  name: string
  count: number
}

interface Chapter {
  id: string
  title: string
  page?: string
  parent: string | null
  level: number
  sections: ChapterSection[]
}

interface ProblemNode {
  id: number
  title: string
  dir: string
  topics: string[]
  difficulty: string
  chapter: string
  section: string
  langs: string[]
}

const graph = graphData as unknown as {
  chapters: Chapter[]
  nodes: ProblemNode[]
  edges: { source: number; target: number }[]
}

const connected = computed(() => {
  const ids = new Set<number>()
  for (const edge of graph.edges) {
    ids.add(edge.source)
    ids.add(edge.target)
  }
  return ids
})

const chapterMeta = computed(() =>
  graph.chapters.find((chapter) => chapter.id === props.chapter)
)

const childIds = computed(() =>
  graph.chapters
    .filter((chapter) => chapter.parent === props.chapter)
    .map((chapter) => chapter.id)
)

const members = computed(() =>
  graph.nodes
    .filter((node) =>
      chapterMeta.value?.level === 1
        ? childIds.value.includes(node.chapter)
        : node.chapter === props.chapter
    )
    .sort((a, b) => a.id - b.id)
)

/** Sections in the taxonomy's declared order, empty ones dropped. */
const sections = computed(() => {
  if (chapterMeta.value?.level === 1) return []
  const order = chapterMeta.value?.sections.map((section) => section.name) ?? []
  return order
    .map((name) => ({
      name,
      problems: members.value.filter((node) => node.section === name)
    }))
    .filter((section) => section.problems.length > 0)
})

/**
 * Topics that belong to this chapter, derived from the problems actually filed
 * here — avoids duplicating the taxonomy table in the client.
 */
const chapterTopics = computed(() => {
  const counts = new Map<string, number>()
  for (const node of members.value) {
    for (const topic of node.topics) {
      counts.set(topic, (counts.get(topic) ?? 0) + 1)
    }
  }
  // A topic is "this chapter's" when most of its problems land here.
  const owned = new Set<string>()
  for (const [topic, countHere] of counts) {
    const total = graph.nodes.filter((node) => node.topics.includes(topic)).length
    if (countHere * 2 > total) owned.add(topic)
  }
  return owned
})

const crossReferenced = computed(() =>
  chapterMeta.value?.level === 1
    ? []
    : graph.nodes
    .filter(
      (node) =>
        node.chapter !== props.chapter &&
        node.topics.some((topic) => chapterTopics.value.has(topic))
    )
    .sort((a, b) => a.id - b.id)
)

const chapterTitleById = computed(
  () => new Map(graph.chapters.map((chapter) => [chapter.id, chapter.title]))
)

function problemLink(node: ProblemNode): string {
  return withBase(`/problems/${node.dir}/`)
}

function chapterTitle(chapterId: string): string {
  return chapterTitleById.value.get(chapterId) ?? chapterId
}
</script>

<template>
  <section class="chapter-index" aria-labelledby="chapter-index-title">
    <h2 id="chapter-index-title">Problems in this chapter</h2>
    <p class="lede">
      <template v-if="chapterMeta?.level === 1">
        {{ members.length }} problems across {{ childIds.length }} concept chapters.
      </template>
      <template v-else>
        {{ members.length }} problems, grouped by the section their topics place them in.
        A dot marks a problem that already has at least one recorded relationship.
      </template>
    </p>

    <ul v-if="chapterMeta?.level === 1" class="meta-summary">
      <li v-for="childId in childIds" :key="childId">
        <a :href="withBase(graph.chapters.find((chapter) => chapter.id === childId)?.page ?? '')">
          {{ chapterTitle(childId) }}
        </a>
        <span>{{ graph.nodes.filter((node) => node.chapter === childId).length }} problems</span>
      </li>
    </ul>

    <div v-for="section in sections" :key="section.name" class="section">
      <h3>{{ section.name }} <span class="count">{{ section.problems.length }}</span></h3>
      <ul>
        <li v-for="problem in section.problems" :key="problem.id">
          <span
            class="dot"
            :class="{ linked: connected.has(problem.id) }"
            :title="connected.has(problem.id) ? 'has relationships' : 'no relationships yet'"
          />
          <a :href="problemLink(problem)">#{{ problem.id }} {{ problem.title }}</a>
          <span class="langs">{{ problem.langs.join(' · ') || '—' }}</span>
        </li>
      </ul>
    </div>

    <details v-if="crossReferenced.length" class="cross-ref">
      <summary>
        {{ crossReferenced.length }} related problems filed in other chapters
      </summary>
      <ul>
        <li v-for="problem in crossReferenced" :key="problem.id">
          <a :href="problemLink(problem)">#{{ problem.id }} {{ problem.title }}</a>
          <span class="home">{{ chapterTitleById.get(problem.chapter) }}</span>
        </li>
      </ul>
    </details>
  </section>
</template>

<style scoped>
.chapter-index {
  margin: 44px 0 0;
  padding-top: 24px;
  border-top: 1px solid var(--vp-c-divider);
}

.chapter-index h2 {
  margin: 0;
  border: 0;
  padding-top: 0;
  font-size: 20px;
  letter-spacing: 0;
}

.lede {
  margin: 8px 0 24px;
  max-width: 68ch;
  color: var(--vp-c-text-2);
  font-size: 14px;
  line-height: 1.6;
}

.section {
  margin-bottom: 26px;
}

.meta-summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 6px 28px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.meta-summary li {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  border-bottom: 1px solid var(--vp-c-divider);
  padding: 6px 0;
  font-size: 14px;
}

.meta-summary span {
  color: var(--vp-c-text-3);
  white-space: nowrap;
}

.section h3 {
  margin: 0 0 10px;
  border: 0;
  padding-top: 0;
  color: var(--vp-c-text-2);
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.section h3 .count {
  margin-left: 6px;
  color: var(--vp-c-text-3);
  font-weight: 400;
  text-transform: none;
  letter-spacing: 0;
}

.section ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2px 28px;
}

.section li {
  display: flex;
  align-items: baseline;
  gap: 8px;
  padding: 4px 0;
  font-size: 14px;
}

.dot {
  flex: none;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--vp-c-divider);
}

.dot.linked {
  background: var(--vp-c-brand-1);
}

.section li a {
  flex: 1;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.langs {
  flex: none;
  color: var(--vp-c-text-3);
  font-family: var(--vp-font-family-mono);
  font-size: 11.5px;
}

.cross-ref {
  margin-top: 8px;
  border-top: 1px solid var(--vp-c-divider);
  padding-top: 16px;
}

.cross-ref summary {
  cursor: pointer;
  color: var(--vp-c-text-2);
  font-size: 13.5px;
}

.cross-ref ul {
  margin: 14px 0 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2px 28px;
}

.cross-ref li {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 10px;
  padding: 4px 0;
  font-size: 14px;
}

.home {
  flex: none;
  color: var(--vp-c-text-3);
  font-size: 11.5px;
}
</style>
