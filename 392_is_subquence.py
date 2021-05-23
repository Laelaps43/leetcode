str1 = "bbaaaa"
str2 = 'aaaaaa'
isin = 0
indexs = 0
isexist = []
for i in str2:
    if i in str1[indexs:]:
        print(str1[indexs:])
        if str1.index(i) >= isin:
            print("this is ",isin)
            print(str1[indexs:].index(i))
            isin = str1.index(i)
            isexist.append(True)
        else:
            isexist.append(False)
        indexs = str1.index(i) + 1
        print("this is the ",indexs)
    else:
        isexist.append(False)
print(isexist)
print(True if not False in isexist else False)