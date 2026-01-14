str1, str2 = map(str, input().split())

if int(str1[1]) > int(str2[1]):
    print(str1)
elif int(str1[1]) < int(str2[1]):
    print(str2)
else:
    print(str2)