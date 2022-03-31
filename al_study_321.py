n = int(input())
s = str(n)
length = len(s)
sum1 = 0
sum2 = 0
for i in range(0, length//2):
    sum1 += int(s[i])
for i in range(length//2, length):
    sum2 += int(s[i])
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
