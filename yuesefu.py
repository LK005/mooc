n,m = input().split()
num = list(range(1,int(n)+1))
lennum = len(num1)
i = 0
count = 0
count0 = 0
while True:
    index = i%lennum
#     print(index,end=' ')
    if num1[index] != 0:
        count += 1
        if count == int(m):
            count = 0
            num1[index] = 0
            print(num1)
            count0 += 1
            if count0 == lennum - 1:
                print(index)
                break
            i += 1
        else:
            i += 1
    else:
        i += 1
print([num1.index(x) for x in num1 if x != 0][0]+1)
