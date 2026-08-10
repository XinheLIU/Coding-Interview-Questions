import { defineConfig } from 'vitepress'
// Topic/difficulty sidebar groups are generated from problem frontmatter by
// `scripts/gen_index.py` — re-run it after adding/retagging a problem.
import problemsSidebar from './sidebar-problems.json'
import chaptersSidebar from './sidebar-chapters.json'

// Docs live at the repo root (srcDir defaults to '.'), so VitePress's `@`
// alias resolves to the repo root. That lets any chapter embed any solution
// file with a stable path, e.g.  <<< @/problems/1-two-sum/solution.py
export default defineConfig({
  title: 'Coding Interview Notes',
  description: 'A book of interview patterns with code kept in sync with the actual solution files.',

  // Required for GitHub project Pages: https://<user>.github.io/Coding-Interview-Questions/
  base: '/Coding-Interview-Questions/',

  lastUpdated: true,
  cleanUrls: true,

  // Each problem's page is README.md (so GitHub renders it in the folder view).
  // Serve it as the directory index so /problems/<id>-<slug>/ resolves cleanly.
  rewrites: {
    'problems/:slug/README.md': 'problems/:slug/index.md'
  },

  markdown: {
    config(md) {
      // Problem metadata lives in README frontmatter. Insert its renderer after
      // the title so every problem page exposes the same source of truth.
      md.core.ruler.after('block', 'problem-metadata', (state) => {
        const relativePath = String(state.env.relativePath ?? '')
        const realPath = String(state.env.realPath ?? '')
        const isProblemReadme =
          /^problems\/[^/]+\/README\.md$/.test(relativePath) ||
          /\/problems\/[^/]+\/README\.md$/.test(realPath)
        if (!isProblemReadme) return

        const headingCloseIndex = state.tokens.findIndex(
          (token) => token.type === 'heading_close' && token.tag === 'h1'
        )
        if (headingCloseIndex === -1) return

        const component = new state.Token('html_block', '', 0)
        component.content = '<ProblemMeta />\n'
        state.tokens.splice(headingCloseIndex + 1, 0, component)
      })
    }
  },

  themeConfig: {
    search: { provider: 'local' },

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Chapters', link: '/book/linear-structures' },
      { text: 'By Topic', link: '/book/by-topic/array' }
    ],

    sidebar: [
      {
        text: 'Getting Started',
        items: [{ text: 'Interview Principles', link: '/docs/INTERVIEW_GUIDE' }]
      },
      {
        // Both levels are generated from scripts/taxonomy.py so curriculum order
        // and problem placement share one source of truth.
        text: 'Chapters',
        items: chaptersSidebar
      },
      {
        text: 'Template Deep Dives',
        collapsed: true,
        items: [
          { text: 'BFS', link: '/book/bfs' },
          { text: 'DFS', link: '/book/dfs' }
        ]
      },
      ...problemsSidebar
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/' }
    ]
  }
})
