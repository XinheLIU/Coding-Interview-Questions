<script setup lang="ts">
/**
 * The homepage curriculum map: one node per chapter, sized by how many problems
 * are filed there, joined by the prerequisite edges declared in
 * scripts/taxonomy.py (CHAPTER_FLOW). Grid coordinates come from the taxonomy
 * too, so the layout is deterministic — no force simulation, no dependency.
 */
import { computed } from 'vue'
import { withBase } from 'vitepress'
import graphData from '../problem-graph.json'

interface ChapterSection {
  name: string
  count: number
}

interface Chapter {
  id: string
  title: string
  page: string
  blurb: string
  col: number
  row: number
  count: number
  sections: ChapterSection[]
}

interface Flow {
  source: string
  target: string
}

const graph = graphData as unknown as {
  chapters: Chapter[]
  flow: Flow[]
  nodes: unknown[]
  edges: unknown[]
}

// Layout constants — a chapter box is placed at its (col, row) grid slot.
const CELL_W = 232
const CELL_H = 132
const BOX_W = 190
const BOX_H = 86
const PAD = 24

const chapters = computed(() => graph.chapters.filter((c) => c.count > 0))

const bounds = computed(() => {
  const cols = chapters.value.map((c) => c.col)
  const rows = chapters.value.map((c) => c.row)
  return {
    width: (Math.max(...cols) + 1) * CELL_W + PAD * 2,
    height: (Math.max(...rows) + 1) * CELL_H + PAD * 2
  }
})

function boxOf(chapter: Chapter) {
  return {
    x: PAD + chapter.col * CELL_W + (CELL_W - BOX_W) / 2,
    y: PAD + chapter.row * CELL_H + (CELL_H - BOX_H) / 2,
    w: BOX_W,
    h: BOX_H
  }
}

const positioned = computed(() =>
  chapters.value.map((chapter) => ({ chapter, box: boxOf(chapter) }))
)

const byId = computed(
  () => new Map(chapters.value.map((chapter) => [chapter.id, chapter]))
)

/** Edge endpoints are clipped to the box borders so arrows never sit under text. */
const arrows = computed(() =>
  graph.flow
    .map((edge) => {
      const from = byId.value.get(edge.source)
      const to = byId.value.get(edge.target)
      if (!from || !to) return null

      const a = boxOf(from)
      const b = boxOf(to)
      const ac = { x: a.x + a.w / 2, y: a.y + a.h / 2 }
      const bc = { x: b.x + b.w / 2, y: b.y + b.h / 2 }
      const start = clipToBox(ac, bc, a)
      const end = clipToBox(bc, ac, b)
      return { key: `${edge.source}->${edge.target}`, start, end }
    })
    .filter((arrow): arrow is NonNullable<typeof arrow> => arrow !== null)
)

/** Walk from a box's centre toward `toward` until we exit the box rectangle. */
function clipToBox(
  centre: { x: number; y: number },
  toward: { x: number; y: number },
  box: { x: number; y: number; w: number; h: number }
) {
  const dx = toward.x - centre.x
  const dy = toward.y - centre.y
  if (dx === 0 && dy === 0) return centre

  const halfW = box.w / 2 + 6
  const halfH = box.h / 2 + 6
  const scale = Math.min(
    dx === 0 ? Infinity : Math.abs(halfW / dx),
    dy === 0 ? Infinity : Math.abs(halfH / dy)
  )
  return { x: centre.x + dx * scale, y: centre.y + dy * scale }
}

const totals = computed(() => ({
  problems: graph.nodes.length,
  relations: graph.edges.length,
  chapters: chapters.value.length
}))

function pageLink(chapter: Chapter): string {
  return withBase(chapter.page)
}

function sectionSummary(chapter: Chapter): string {
  return chapter.sections
    .filter((section) => section.count > 0)
    .map((section) => `${section.name} (${section.count})`)
    .join(' · ')
}
</script>

<template>
  <section class="curriculum-map" aria-labelledby="curriculum-map-title">
    <h2 id="curriculum-map-title">Knowledge map</h2>
    <p class="lede">
      {{ totals.problems }} problems across {{ totals.chapters }} chapters, joined by
      {{ totals.relations }} explicit relationships. Arrows point from a chapter to the
      one it prepares you for.
    </p>

    <div class="map-scroll">
      <svg
        class="map"
        :viewBox="`0 0 ${bounds.width} ${bounds.height}`"
        :style="{ minWidth: `${bounds.width}px` }"
        role="img"
        aria-label="Chapter prerequisite map"
      >
        <defs>
          <marker
            id="curriculum-arrow"
            viewBox="0 0 10 10"
            refX="9"
            refY="5"
            markerWidth="6"
            markerHeight="6"
            orient="auto-start-reverse"
          >
            <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--vp-c-divider)" />
          </marker>
        </defs>

        <line
          v-for="arrow in arrows"
          :key="arrow.key"
          :x1="arrow.start.x"
          :y1="arrow.start.y"
          :x2="arrow.end.x"
          :y2="arrow.end.y"
          class="flow"
          marker-end="url(#curriculum-arrow)"
        />

        <a
          v-for="{ chapter, box } in positioned"
          :key="chapter.id"
          :href="pageLink(chapter)"
          class="chapter"
        >
          <title>{{ chapter.blurb }}</title>
          <rect :x="box.x" :y="box.y" :width="box.w" :height="box.h" rx="8" />
          <text :x="box.x + box.w / 2" :y="box.y + 30" class="chapter-title">
            {{ chapter.title }}
          </text>
          <text :x="box.x + box.w / 2" :y="box.y + 52" class="chapter-count">
            {{ chapter.count }} problems
          </text>
        </a>
      </svg>
    </div>

    <ul class="legend">
      <li v-for="chapter in chapters" :key="chapter.id">
        <a :href="pageLink(chapter)">{{ chapter.title }}</a>
        <span class="sections">{{ sectionSummary(chapter) }}</span>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.curriculum-map {
  max-width: 1152px;
  margin: 8px auto 64px;
  padding: 0 24px;
}

.curriculum-map h2 {
  margin: 0;
  border: 0;
  font-size: 24px;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.lede {
  margin: 8px 0 24px;
  max-width: 62ch;
  color: var(--vp-c-text-2);
  font-size: 15px;
  line-height: 1.6;
}

.map-scroll {
  overflow-x: auto;
  padding-bottom: 8px;
}

.map {
  display: block;
  width: 100%;
  height: auto;
}

.flow {
  stroke: var(--vp-c-divider);
  stroke-width: 1.5;
}

.chapter rect {
  fill: var(--vp-c-bg-soft);
  stroke: var(--vp-c-divider);
  stroke-width: 1;
  transition: fill 0.2s, stroke 0.2s;
}

.chapter:hover rect {
  fill: var(--vp-c-bg-elv);
  stroke: var(--vp-c-brand-1);
}

.chapter-title {
  fill: var(--vp-c-text-1);
  font-size: 14px;
  font-weight: 600;
  text-anchor: middle;
}

.chapter-count {
  fill: var(--vp-c-text-3);
  font-size: 12px;
  text-anchor: middle;
}

.legend {
  margin: 28px 0 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 14px 32px;
}

.legend li {
  border-top: 1px solid var(--vp-c-divider);
  padding-top: 10px;
}

.legend a {
  font-size: 14px;
  font-weight: 600;
}

.sections {
  display: block;
  margin-top: 3px;
  color: var(--vp-c-text-3);
  font-size: 12.5px;
  line-height: 1.5;
}
</style>
