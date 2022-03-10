n, m = map(int, input().split())
data = []#2차원 배열 저장소
min_data = []#각 행에서 가장 작은 수들의 저장소

for i in range(n):
   data.append(list(map(int, input().split())))#각 줄마다 입력받고
   min_data.append(min(data[i]))#그 줄에서 가장 작은 수를 min_data에 저장
result = max(min_data)#min_data에서 가장 큰 수 반환
print(result)
           
