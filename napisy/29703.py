n = int(input())


for j in range(n):
    napis = input()

    result = 0
    smao = ['A', 'E', 'I', 'O', 'U']
    for char in napis:
        for sam in smao:
            if char == sam:
                result += 1
    
    print(result)