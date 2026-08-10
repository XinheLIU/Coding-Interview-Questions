import DefaultTheme from 'vitepress/theme'
import Layout from './Layout.vue'
import ChapterGraph from './ChapterGraph.vue'
import ChapterChildren from './ChapterChildren.vue'
import ChapterIndex from './ChapterIndex.vue'
import CurriculumMap from './CurriculumMap.vue'
import ProblemMeta from './ProblemMeta.vue'

export default {
  extends: DefaultTheme,
  Layout,
  // Registered globally so chapter Markdown can use them without an import.
  enhanceApp({ app }) {
    app.component('ChapterGraph', ChapterGraph)
    app.component('ChapterChildren', ChapterChildren)
    app.component('ChapterIndex', ChapterIndex)
    app.component('CurriculumMap', CurriculumMap)
    app.component('ProblemMeta', ProblemMeta)
  }
}
