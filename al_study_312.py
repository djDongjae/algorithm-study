def main():
    s = input()
    data = []
    result = 1
    #0 제거
    for i in range(len(s)):
        if s[i] != '0':
            data.append(int(s[i]))
    #1등장의 경우 양옆의 수중 작은 수와 합침
    for i in range(1, len(data)-1):
        if data[i] == 1:
            if data[i-1] <= data[i+1]:
                data[i-1] += 1
            else:
                data[i+1] += 1
            data.remove(1)
    #전부 곱하기
    for i in data:
        result = result * i
    return result
    
