klawisze_wejsciowe = ['1','2','3','4','5','6','7','8','9','0','-','=', 
                       'W','E','R','T','Y','U','I','O','P','[',']','\\',
                       'S','D','F','G','H','J','K','L',';','\'',
                       'X','C','V','B','N','M',',','.','/']

klawisze_prawidlowe = ['`','1','2','3','4','5','6','7','8','9','0','-',
                        'Q','W','E','R','T','Y','U','I','O','P','[',']',
                        'A','S','D','F','G','H','J','K','L',';',
                        'Z','X','C','V','B','N','M',',','.']

t = int(input())
for _ in range(t):
    wiersz = input()
    odkodowany = ''
    for znak in wiersz:
        if znak in klawisze_wejsciowe:
            idx = klawisze_wejsciowe.index(znak)
            odkodowany += klawisze_prawidlowe[idx]
        else:
            odkodowany += znak
    print(odkodowany)