#313페이지_'문자열 뒤집기'
s = input()

count_0 = 0#0의 묶음의 개수
count_1 = 0#1의 묶음의 개수

if s[0] == '0':#첫 시작이 0인지 1인지 판단
    count_0 += 1
else:
    count_1 += 1
    
for i in range(1, len(s)):#이후 수가 바뀔 때마다 새롭게 저장
    if s[i-1] != s[i]:
        if s[i] == '1':
            count_1 += 1
        else:
            count_0 += 1


result = min(count_0, count_1)#두 묶음 중 작은 것을 반환
print(result)
