import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            first, second = heapq.heappop(heap), heapq.heappop(heap)
            first_val, second_val = -first, -second
            # print(first_val, second_val)
            if first_val != second_val:
                heapq.heappush(heap, -1 *(first_val - second_val))
                # print(-1 * (first_val - second_val))
        return -heap[0] if heap else 0
