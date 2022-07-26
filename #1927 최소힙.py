import sys
import heapq
#heapq.heappush()
#heapq.heappop()
#heapq.heappushpop()

myheap = []
N = int(sys.stdin.readline())
for i in range(N):
    T = int(sys.stdin.readline())
    if T == 0:
        if len(myheap) == 0:
            print(0)
        else:
            print(heapq.heappop(myheap))
    else:
        heapq.heappush(myheap, T)

