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
      { text: 'Chapters', link: '/book/linear-structures' },
      { text: 'By Topic', link: '/book/by-topic/array' }
    ],

    sidebar: [
      {
        text: 'Getting Started',
        items: [{ text: 'Interview Principles', link: '/' }]
      },
      {
        // Curriculum order — mirrors CHAPTERS in scripts/taxonomy.py. Keep the
        // two in sync: the taxonomy decides which problems land in each chapter,
        // this list decides the reading order shown in the sidebar.
        text: 'Chapters',
        items: [
          { text: 'Linear Structures', link: '/book/linear-structures' },
          { text: 'Trees & Heaps', link: '/book/trees' },
          { text: 'Recursion & Divide and Conquer', link: '/book/recursion' },
          { text: 'Search & Sort', link: '/book/search-and-sort' },
          { text: 'Dynamic Programming', link: '/book/dynamic-programming' },
          { text: 'Techniques', link: '/book/techniques' },
          { text: 'SQL', link: '/book/sql' }
        ]
      },
      {
        text: 'Template Deep Dives',
        collapsed: true,
        items: [
          { text: 'Binary Search', link: '/book/binary-search' },
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
