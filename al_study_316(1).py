import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    else:
        data = []
        for i in range(len(food_times)):
            heapq.heappush(data, [food_times[i], i+1])
        
        length = len(data)
        
        while length * data[0][0] <= k:
            min_value = heapq.heappop(data)[0]
            for i in range(len(data)):
                data[i][0] -= min_value
            k -= length * min_value
            length -= 1

        data.sort(key=lambda x: x[1])
        result = data[k%length][1]
        return result
