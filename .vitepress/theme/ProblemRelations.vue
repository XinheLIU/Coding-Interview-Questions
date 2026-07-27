<script setup lang="ts">
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'
import graphData from '../problem-graph.json'

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

const relationGroups = computed<RelationGroup[]>(() => {
  const currentId = Number(frontmatter.value.id)
  if (!Number.isInteger(currentId)) return []

  const groups = new Map<string, DisplayRelation[]>()
  for (const edge of graph.edges) {
    const isOutgoing = edge.source === currentId
    const isIncoming = edge.target === currentId
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

function problemLink(node: ProblemNode): string {
  return withBase(`/problems/${node.dir}/`)
}
</script>

<template>
  <section v-if="relationGroups.length" class="problem-relations" aria-labelledby="knowledge-graph-title">
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
</template>

<style scoped>
.problem-relations {
  margin-top: 40px;
  padding-top: 8px;
  border-top: 1px solid var(--vp-c-divider);
}

.problem-relations h2 {
  margin: 16px 0 4px;
  border: 0;
  font-size: 20px;
  letter-spacing: 0;
}

.relation-group {
  display: grid;
  grid-template-columns: minmax(112px, 0.28fr) minmax(0, 1fr);
  gap: 16px;
  padding: 18px 0;
  border-bottom: 1px solid var(--vp-c-divider);
}

.relation-group h3 {
  margin: 2px 0 0;
  border-left: 3px solid var(--vp-c-brand-1);
  padding-left: 10px;
  color: var(--vp-c-text-2);
  font-size: 13px;
  font-weight: 600;
  line-height: 1.5;
  letter-spacing: 0;
}

.relation-group ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

.relation-group li + li {
  margin-top: 14px;
}

.relation-group a {
  font-weight: 600;
}

.relation-group p {
  margin: 3px 0 0;
  color: var(--vp-c-text-2);
  font-size: 14px;
  line-height: 1.55;
}

@media (max-width: 640px) {
  .relation-group {
    grid-template-columns: 1fr;
    gap: 10px;
  }
}
</style>
