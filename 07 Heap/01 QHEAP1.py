# Enter your code here. Read input from STDIN. Print output to STDOUT


import heapq

heap=[]
lookup=set()


for i in range(0, int(input())):
    sample=list(map(int,input().split(" ")))
    if sample[0]==1:
        heapq.heappush(heap, sample[1])
        lookup.add(sample[1])
    elif sample[0]==2:
        lookup.discard(sample[1])
    else:
        while heap[0] not in lookup:
            heapq.heappop(heap)
        print(heap[0])
