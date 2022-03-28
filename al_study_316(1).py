import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    else:
        data = []
        for i in range(len(food_times)):
            heapq.heappush(data, [food_times[i], i+1])
        
        length = len(data)
        
        while length * data[0][0] <= k: #남은 시간이 (배열의 길이 * 가장 적게 남은 음식) 보다 크거나 같아야함.
            min_value = heapq.heappop(data)[0]
            for i in range(len(data)):#돌아가면서 동일 최소값 빼기
                data[i][0] -= min_value
            k -= length * min_value#현재 남은 시간에서 (배열의 길이 * 가장 적게 남은 음식)을 빼준다
            length -= 1

        data.sort(key=lambda x: x[1])
        result = data[k%length][1]
        return result
