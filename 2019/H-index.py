from heapq import heapify, heappush, heappop

t = int(input())

results = list()
for i in range(0, t):
    n = int(input())

    arr = list(map(int, input().split()))
    priority_queue = []
    heapify(priority_queue)
    h = 0

    current_result = ""
    for j in range(0, len(arr)):
        if arr[j] > h:
            heappush(priority_queue, arr[j])

        if len(priority_queue) > 1 and len(priority_queue) > h >= priority_queue[0]:
            heappop(priority_queue)

        h = min(len(priority_queue), priority_queue[0])
        current_result += ' ' + str(h)

    results.append(current_result)

for i in range(1, t + 1):
    print("Case #%d:%s" % (i, results[i - 1]))
