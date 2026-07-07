class Solution:
	class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        used_rooms = 0
        start, end = sorted([i[0] for i in intervals]), sorted([i[1] for i in intervals])
        start_p, end_p = 0, 0
        while start_p < len(intervals):
            if start[start_p] >= end[end_p]: # one used rooms free, update latest end
                used_rooms -= 1
                end_p += 1
            # allocate a room, update latest start
            used_rooms += 1
            start_p += 1
        return used_rooms

'''
import heapq
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        rooms = []
        intervals.sort(key = lambda x: x[0])
        heapq.heappush(rooms, intervals[0][1])
        for i in intervals[1:]:
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])
        return len(rooms)
'''