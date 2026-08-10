<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { useData, withBase } from 'vitepress'
import graphData from '../problem-graph.json'
import { recordRecentProblem } from './recentProblems'

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
  difficulty: string
}

interface ProblemEdge {
  source: number
  target: number
  type: RelationType
  reason: string
}

interface ProblemGraph {
  nodes: ProblemNode[]
  edges: ProblemEdge[]
}

interface DisplayRelation {
  edgeKey: string
  node: ProblemNode
  reason: string
}

interface RelationGroup {
  label: string
  relations: DisplayRelation[]
}

const RELATION_LABELS: Record<RelationType, { outgoing: string; incoming: string }> = {
  'builds-on': { outgoing: 'Builds on', incoming: 'Built on by' },
  contrasts: { outgoing: 'Contrasts with', incoming: 'Contrasts with' },
  generalizes: { outgoing: 'Generalizes', incoming: 'Generalized by' },
  'same-pattern': { outgoing: 'Shares a pattern with', incoming: 'Shares a pattern with' },
  specializes: { outgoing: 'Specializes', incoming: 'Specialized by' }
}

const graph = graphData as ProblemGraph
const nodesById = new Map(graph.nodes.map((node) => [node.id, node]))
const { frontmatter } = useData()

const currentId = computed(() => {
  const id = Number(frontmatter.value.id)
  return Number.isInteger(id) ? id : null
})

const currentNode = computed(() =>
  currentId.value === null ? undefined : nodesById.get(currentId.value)
)

const difficulty = computed(() => {
  const value = frontmatter.value.difficulty
  if (typeof value === 'string' && value) return value
  return currentNode.value?.difficulty ?? ''
})

const leetcode = computed(() =>
  typeof frontmatter.value.leetcode === 'string' ? frontmatter.value.leetcode : ''
)

const topics = computed(() =>
  Array.isArray(frontmatter.value.topics)
    ? frontmatter.value.topics.filter((topic): topic is string => typeof topic === 'string')
    : []
)

const relationGroups = computed<RelationGroup[]>(() => {
  if (currentId.value === null) return []

  const groups = new Map<string, DisplayRelation[]>()
  for (const edge of graph.edges) {
    const isOutgoing = edge.source === currentId.value
    const isIncoming = edge.target === currentId.value
    if (!isOutgoing && !isIncoming) continue

    const direction = isOutgoing ? 'outgoing' : 'incoming'
    const label = RELATION_LABELS[edge.type][direction]
    const relatedId = isOutgoing ? edge.target : edge.source
    const node = nodesById.get(relatedId)
    if (!node) continue

    const relations = groups.get(label) ?? []
    relations.push({
      edgeKey: `${edge.source}-${edge.type}-${edge.target}`,
      node,
      reason: edge.reason
    })
    groups.set(label, relations)
  }

  return Array.from(groups, ([label, relations]) => ({ label, relations }))
})

onMounted(() => {
  const node = currentNode.value
  if (!node) return

  recordRecentProblem({ id: node.id, title: node.title, dir: node.dir })
})

function problemLink(node: ProblemNode): string {
  return withBase(`/problems/${node.dir}/`)
}

function topicLink(topic: string): string {
  return withBase(`/book/by-topic/${topic}`)
}

function topicLabel(topic: string): string {
  return topic.replace(/-/g, ' ')
}
</script>

<template>
  <section class="problem-meta" aria-label="Problem details">
    <p v-if="difficulty || leetcode" class="summary">
      <span v-if="difficulty" class="difficulty">{{ difficulty }}</span>
      <a v-if="leetcode" :href="leetcode" target="_blank" rel="noreferrer">LeetCode</a>
    </p>

    <section v-if="topics.length" class="meta-section" aria-labelledby="topics-title">
      <h2 id="topics-title">Topics</h2>
      <ul class="topics">
        <li v-for="topic in topics" :key="topic">
          <a :href="topicLink(topic)">{{ topicLabel(topic) }}</a>
        </li>
      </ul>
    </section>

    <section
      v-if="relationGroups.length"
      class="meta-section knowledge-graph"
      aria-labelledby="knowledge-graph-title"
    >
      <h2 id="knowledge-graph-title">Knowledge graph</h2>

      <div v-for="group in relationGroups" :key="group.label" class="relation-group">
        <h3>{{ group.label }}</h3>
        <ul>
          <li v-for="relation in group.relations" :key="relation.edgeKey">
            <a :href="problemLink(relation.node)">#{{ relation.node.id }} {{ relation.node.title }}</a>
            <p>{{ relation.reason }}</p>
          </li>
        </ul>
      </div>
    </section>
  </section>
</template>

<style scoped>
.problem-meta {
  margin: 16px 0 32px;
  padding: 16px 0 0;
  border-top: 1px solid var(--vp-c-divider);
}

.summary {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 0 16px;
  color: var(--vp-c-text-2);
  font-size: 13px;
}

.difficulty {
  color: var(--vp-c-brand-1);
  font-weight: 600;
}

.meta-section + .meta-section {
  margin-top: 22px;
}

.meta-section h2 {
  margin: 0 0 10px;
  border: 0;
  padding: 0;
  color: var(--vp-c-text-2);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  line-height: 1.4;
  text-transform: uppercase;
}

.topics {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 12px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.topics a {
  display: block;
  border-bottom: 1px solid var(--vp-c-divider);
  padding: 1px 0;
  color: var(--vp-c-text-2);
  font-size: 12px;
  line-height: 1.6;
  text-transform: capitalize;
}

.topics a:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.relation-group {
  padding: 14px 0;
  border-top: 1px solid var(--vp-c-divider);
}

.relation-group h3 {
  margin: 0 0 6px;
  color: var(--vp-c-text-2);
  font-size: 10px;
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.relation-group ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

.relation-group li + li {
  margin-top: 12px;
}

.relation-group a {
  font-weight: 600;
  text-underline-offset: 3px;
}

.relation-group p {
  margin: 2px 0 0;
  color: var(--vp-c-text-2);
  font-size: 14px;
  line-height: 1.6;
}
</style>
