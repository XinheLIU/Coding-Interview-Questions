<script setup lang="ts">
/**
 * Per-chapter prerequisite graph, laid out as a layered DAG.
 *
 * A node's depth on screen is its longest path along the *directed* relation
 * types (builds-on / specializes / generalizes), so horizontal position literally
 * means prerequisite depth. Undirected types (same-pattern, contrasts) are drawn
 * dashed and do not affect ranking.
 *
 * Only problems that carry at least one relation are drawn — an unconnected
 * problem has nothing to show here, and its absence is the signal that the graph
 * still needs an edge for it. ChapterIndex lists every problem regardless.
 */
import { computed } from 'vue'
import { withBase } from 'vitepress'
import graphData from '../problem-graph.json'

const props = defineProps<{ chapter: string }>()

type RelationType =
  | 'builds-on'
  | 'contrasts'
  | 'generalizes'
  | 'same-pattern'
  | 'specializes'

interface ProblemNode {
  id: number
  title: string
  dir: string
  chapter: string
  section: string
}

interface ProblemEdge {
  source: number
  target: number
  type: RelationType
  reason: string
}

const graph = graphData as unknown as {
  nodes: ProblemNode[]
  edges: ProblemEdge[]
}

/** Types where direction encodes "comes before"; used for ranking. */
const DIRECTED: ReadonlySet<RelationType> = new Set([
  'builds-on',
  'specializes',
  'generalizes'
])

const RELATION_LABEL: Record<RelationType, string> = {
  'builds-on': 'builds on',
  contrasts: 'contrasts with',
  generalizes: 'generalizes',
  'same-pattern': 'same pattern',
  specializes: 'specializes'
}

const NODE_W = 168
const NODE_H = 38
const COL_GAP = 78
const ROW_GAP = 14
const PAD = 16

const chapterNodes = computed(() =>
  graph.nodes.filter((node) => node.chapter === props.chapter)
)

/** Edges with both endpoints inside this chapter. */
const localEdges = computed(() => {
  const ids = new Set(chapterNodes.value.map((node) => node.id))
  return graph.edges.filter(
    (edge) => ids.has(edge.source) && ids.has(edge.target)
  )
})

const drawnNodes = computed(() => {
  const touched = new Set<number>()
  for (const edge of localEdges.value) {
    touched.add(edge.source)
    touched.add(edge.target)
  }
  return chapterNodes.value.filter((node) => touched.has(node.id))
})

/**
 * Rank = longest directed path ending at this node. Computed by relaxing until
 * stable, which also tolerates the accidental cycle without hanging.
 */
const ranks = computed(() => {
  const rank = new Map<number, number>()
  for (const node of drawnNodes.value) rank.set(node.id, 0)

  const directed = localEdges.value.filter((edge) => DIRECTED.has(edge.type))
  for (let pass = 0; pass < drawnNodes.value.length; pass++) {
    let changed = false
    for (const edge of directed) {
      const next = (rank.get(edge.source) ?? 0) + 1
      if (next > (rank.get(edge.target) ?? 0)) {
        rank.set(edge.target, next)
        changed = true
      }
    }
    if (!changed) break
  }
  return rank
})

const layout = computed(() => {
  const columns = new Map<number, ProblemNode[]>()
  for (const node of [...drawnNodes.value].sort((a, b) => a.id - b.id)) {
    const rank = ranks.value.get(node.id) ?? 0
    const column = columns.get(rank) ?? []
    column.push(node)
    columns.set(rank, column)
  }

  const placed = new Map<number, { x: number; y: number }>()
  const tallest = Math.max(1, ...[...columns.values()].map((c) => c.length))
  for (const [rank, column] of columns) {
    // Centre each column vertically against the tallest one.
    const offset = ((tallest - column.length) * (NODE_H + ROW_GAP)) / 2
    column.forEach((node, index) => {
      placed.set(node.id, {
        x: PAD + rank * (NODE_W + COL_GAP),
        y: PAD + offset + index * (NODE_H + ROW_GAP)
      })
    })
  }

  const maxRank = Math.max(0, ...columns.keys())
  return {
    positions: placed,
    width: PAD * 2 + (maxRank + 1) * NODE_W + maxRank * COL_GAP,
    height: PAD * 2 + tallest * NODE_H + (tallest - 1) * ROW_GAP
  }
})

const links = computed(() =>
  localEdges.value
    .map((edge) => {
      const from = layout.value.positions.get(edge.source)
      const to = layout.value.positions.get(edge.target)
      if (!from || !to) return null

      const startX = from.x + NODE_W
      const startY = from.y + NODE_H / 2
      const endX = to.x
      const endY = to.y + NODE_H / 2
      // A cubic with horizontal control points reads cleanly for left-to-right
      // ranks and still looks sane when an edge points backwards.
      const midX = (startX + endX) / 2
      return {
        key: `${edge.source}-${edge.type}-${edge.target}`,
        path: `M ${startX} ${startY} C ${midX} ${startY}, ${midX} ${endY}, ${endX} ${endY}`,
        dashed: !DIRECTED.has(edge.type),
        title: `#${edge.source} ${RELATION_LABEL[edge.type]} #${edge.target} — ${edge.reason}`
      }
    })
    .filter((link): link is NonNullable<typeof link> => link !== null)
)

const boxes = computed(() =>
  drawnNodes.value
    .map((node) => ({ node, at: layout.value.positions.get(node.id) }))
    .filter(
      (entry): entry is { node: ProblemNode; at: { x: number; y: number } } =>
        entry.at !== undefined
    )
)

const isolatedCount = computed(
  () => chapterNodes.value.length - drawnNodes.value.length
)

/**
 * Edges with exactly one endpoint in this chapter. They cannot be drawn here, so
 * say how many there are rather than letting the graph imply the chapter is
 * self-contained. They are visible on both problem pages.
 */
const crossChapterCount = computed(() => {
  const ids = new Set(chapterNodes.value.map((node) => node.id))
  return graph.edges.filter(
    (edge) => ids.has(edge.source) !== ids.has(edge.target)
  ).length
})

function problemLink(node: ProblemNode): string {
  return withBase(`/problems/${node.dir}/`)
}

/** Titles are long; clip to keep them inside the box. */
function shortTitle(title: string): string {
  return title.length > 22 ? `${title.slice(0, 21)}…` : title
}
</script>

<template>
  <section v-if="boxes.length" class="chapter-graph" aria-labelledby="chapter-graph-title">
    <h2 id="chapter-graph-title">How these problems connect</h2>
    <p class="lede">
      Left to right is prerequisite depth. Solid lines are directed
      (builds&nbsp;on / specializes / generalizes); dashed lines pair problems that
      share a pattern or contrast with each other. Hover a line for the reason.
    </p>

    <div class="graph-scroll">
      <svg
        class="graph"
        :viewBox="`0 0 ${layout.width} ${layout.height}`"
        :style="{ minWidth: `${layout.width}px` }"
        role="img"
        :aria-label="`Prerequisite graph for the ${chapter} chapter`"
      >
        <defs>
          <marker
            id="chapter-graph-arrow"
            viewBox="0 0 10 10"
            refX="9"
            refY="5"
            markerWidth="5"
            markerHeight="5"
            orient="auto-start-reverse"
          >
            <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--vp-c-brand-2)" />
          </marker>
        </defs>

        <path
          v-for="link in links"
          :key="link.key"
          :d="link.path"
          class="link"
          :class="{ dashed: link.dashed }"
          :marker-end="link.dashed ? undefined : 'url(#chapter-graph-arrow)'"
        >
          <title>{{ link.title }}</title>
        </path>

        <a
          v-for="{ node, at } in boxes"
          :key="node.id"
          :href="problemLink(node)"
          class="node"
        >
          <title>#{{ node.id }} {{ node.title }} · {{ node.section }}</title>
          <rect :x="at.x" :y="at.y" :width="NODE_W" :height="NODE_H" rx="6" />
          <text :x="at.x + 11" :y="at.y + 16" class="node-id">#{{ node.id }}</text>
          <text :x="at.x + 11" :y="at.y + 29" class="node-title">
            {{ shortTitle(node.title) }}
          </text>
        </a>
      </svg>
    </div>

    <p v-if="isolatedCount || crossChapterCount" class="isolated-note">
      <template v-if="isolatedCount">
        {{ isolatedCount }} more problem{{ isolatedCount === 1 ? '' : 's' }} in this
        chapter have no relationship recorded yet — they are listed below.
        <code>python3 scripts/suggest_relations.py --chapter {{ chapter }} --isolated</code>
        names them.
      </template>
      <template v-if="crossChapterCount">
        {{ crossChapterCount }} further relationship{{ crossChapterCount === 1 ? '' : 's' }}
        link this chapter to another and so cannot be drawn here; they appear on the
        problem pages at both ends.
      </template>
    </p>
  </section>
</template>

<style scoped>
.chapter-graph {
  margin: 44px 0 8px;
  padding-top: 24px;
  border-top: 1px solid var(--vp-c-divider);
}

.chapter-graph h2 {
  margin: 0;
  border: 0;
  padding-top: 0;
  font-size: 20px;
  letter-spacing: 0;
}

.lede {
  margin: 8px 0 20px;
  max-width: 68ch;
  color: var(--vp-c-text-2);
  font-size: 14px;
  line-height: 1.6;
}

.graph-scroll {
  overflow-x: auto;
  padding-bottom: 10px;
}

.graph {
  display: block;
  width: 100%;
  height: auto;
}

.link {
  fill: none;
  stroke: var(--vp-c-brand-2);
  stroke-width: 1.4;
  opacity: 0.5;
  transition: opacity 0.2s, stroke-width 0.2s;
}

.link:hover {
  opacity: 1;
  stroke-width: 2.2;
}

.link.dashed {
  stroke: var(--vp-c-text-3);
  stroke-dasharray: 4 4;
}

.node rect {
  fill: var(--vp-c-bg-soft);
  stroke: var(--vp-c-divider);
  transition: fill 0.2s, stroke 0.2s;
}

.node:hover rect {
  fill: var(--vp-c-bg-elv);
  stroke: var(--vp-c-brand-1);
}

.node-id {
  fill: var(--vp-c-text-3);
  font-size: 10.5px;
  font-weight: 600;
}

.node-title {
  fill: var(--vp-c-text-1);
  font-size: 12px;
}

.isolated-note {
  margin: 6px 0 0;
  color: var(--vp-c-text-3);
  font-size: 13px;
  line-height: 1.6;
}

.isolated-note code {
  font-size: 12px;
}
</style>
