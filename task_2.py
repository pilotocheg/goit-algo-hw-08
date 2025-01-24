import heapq


def merge_k_lists(lists):
    heap = []
    for list in lists:
        for value in list:
            heapq.heappush(heap, value)

    return [heapq.heappop(heap) for _ in range(len(heap))]


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
