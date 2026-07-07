import { defineConfig } from 'vitepress'
// Topic/difficulty sidebar groups are generated from problem frontmatter by
// `scripts/gen_index.py` — re-run it after adding/retagging a problem.
import problemsSidebar from './sidebar-problems.json'

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

  themeConfig: {
    search: { provider: 'local' },

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Book', link: '/book/dynamic-programming' }
    ],

    sidebar: [
      {
        text: 'Getting Started',
        items: [{ text: 'Interview Principles', link: '/' }]
      },
      {
        text: 'Patterns',
        items: [
          { text: 'Dynamic Programming', link: '/book/dynamic-programming' },
          { text: 'Binary Search', link: '/book/binary-search' },
          { text: 'BFS', link: '/book/bfs' },
          { text: 'DFS', link: '/book/dfs' }
        ]
      },
      {
        text: 'SQL',
        items: [{ text: 'Window Functions & Ranking', link: '/book/sql' }]
      },
      ...problemsSidebar
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/' }
    ]
  }
})
