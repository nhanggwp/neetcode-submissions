class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
            heap_ne = []
        for num,freq in freq.items():
              heapq.heappush(heap_ne,(freq,num))
              if(len(heap_ne) >k):
                    heapq.heappop(heap_ne)
        return [num for f, num in heap_ne] 