import heapq


if __name__ == '__main__':
    li = [10, 10, 20, 15, 30, 40]
    heapq.heapify(li)
    print("heap queue: ", li)

    while li:
        smallest = heapq.heappop(li)
        print("Removed:", smallest)
