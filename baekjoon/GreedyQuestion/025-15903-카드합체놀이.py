import heapq as hq

n, m = map(int, input().split())
c_heap = list(map(int, input().split()))
hq.heapify(c_heap)
k = 0
while k < m:
    c1 = hq.heappop(c_heap)
    c2 = hq.heappop(c_heap)
    hq.heappush(c_heap, c1+c2)
    hq.heappush(c_heap, c1+c2)
    k += 1

print(sum(c_heap))