def encrypy(s):
    azlist = list(range(ord('a'),ord('z')+1))
    AZlist = list(range(ord('A'),ord('Z')+1))
    switchs = []
    for i in s:
        if ord(i) in azlist or ord(i) in AZlist:
            if i == 'z':
                si1 = 'a'
                switchs.append(si1)
            elif i == 'Z':
                si2 = 'A'
                switchs.append(si2)
            else:
                switchs.append(chr(ord(i)+1))
        else:
            switchs.append(i)
    return ''.join(switchs)
def main():
    n = int(input())
    sws = []
    for j in range(n):
        sws.append(encrypy(input()))
    for ss in sws:
        print(ss)

if __name__ =='__main__':
    main()
# test = 'Hello! How are you!'

# print(encrypy(test))