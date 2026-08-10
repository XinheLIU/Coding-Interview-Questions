export interface RecentProblem {
  id: number
  title: string
  dir: string
}

const STORAGE_KEY = 'coding-interview-notes.recent-problems'
export const MAX_RECENT_PROBLEMS = 10

function isRecentProblem(value: unknown): value is RecentProblem {
  if (typeof value !== 'object' || value === null) return false

  const problem = value as Record<string, unknown>
  return (
    Number.isInteger(problem.id) &&
    typeof problem.title === 'string' &&
    typeof problem.dir === 'string'
  )
}

export function readRecentProblems(): RecentProblem[] {
  if (typeof window === 'undefined') return []

  try {
    const stored = JSON.parse(window.localStorage.getItem(STORAGE_KEY) ?? '[]')
    if (!Array.isArray(stored)) return []

    const seenIds = new Set<number>()
    return stored
      .filter(isRecentProblem)
      .filter((problem) => {
        if (seenIds.has(problem.id)) return false
        seenIds.add(problem.id)
        return true
      })
      .slice(0, MAX_RECENT_PROBLEMS)
  } catch {
    return []
  }
}

export function recordRecentProblem(problem: RecentProblem): RecentProblem[] {
  const recent = readRecentProblems().filter((item) => item.id !== problem.id)
  const next = [problem, ...recent].slice(0, MAX_RECENT_PROBLEMS)

  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(next))
  } catch {
    // Browsing still works when storage is unavailable.
  }

  return next
}
