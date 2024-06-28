import heapq

nums = [1, 4, 3, 2, 5, 6, 7, 3, 2]
pq = []
for i in nums:
    heapq.heappush(pq, i)
print(pq)
for i in range(len(nums)):
    heapq.heappop(pq)
    print(pq)
