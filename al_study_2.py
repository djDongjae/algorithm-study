n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

#입력받은 데이터 역순으로 정리하기
data.sort(reverse=True)
data1 = data[0]#가장 큰 수 
data2 = data[1]#두번째 큰 수 

#두 수가 같을 경우
if data1 == data2:
    result = data1 * m
#다를 경우
else:
    rotate = data1*k + data2#반복되는 수열
    count = m // (k+1)#몇번 반복되는지
    r = m%(k+1)#나머지 개수
    result = rotate*count + data1*r#결과값
print(result)
