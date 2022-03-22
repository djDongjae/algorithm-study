#311페이지_'모험가 길드'
n = int(input())
data = list(map(int, input().split()))
data.sort()

count = 0
group = 0

for i in data:
    count += 1
    if i <= count:
        group += 1
        count = 0

print(group)
