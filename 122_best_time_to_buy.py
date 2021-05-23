a = [7,1,5,3,6,4]
sum1 = a[0]
b = []
for i in a[1:]:
    if sum1 - i > 0:
        sum1 = i
    else:
        k = i - sum1
        sum1 = i
        b.append(k)
print(sum(b))