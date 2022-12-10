def beolvas(fajlnev):
    fajlom = open(fajlnev, "r", encoding = 'utf-8')
    print(fajlom)
    '''fajltartalom = fajlom.read()
    print(fajltartalom)'''
    fejlec = fajlom.readline().strip()      #fejlec kiiratasa
    print(fejlec)                   #fejlec kiiratasa

    # kovetkezosor = fajlom.readline().strip()        #.strip() kiszedi a sor után lévő sortöréseket (a print + a readline is hozzá rak egyet-egyet)
    # print(kovetkezosor)

    sorok = fajlom.readlines()
    print(sorok)

    fajlom.close()

    fajlfeldolgozas(sorok)

    """ez a fejlec"""
"""    fajlom.readline()
    fajl_tartalom = fajlom.readlines()
    fajlom.close()"""

nevek = []
nemek = []
korok = []
def fajlfeldolgozas(sorok):
    """Itt dolgozom fel a kapott listát"""
    i = 0
    while i < len(sorok):
        print(sorok[i].strip())
        sor = sorok[i].strip().split(', ')
        print(sor)
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(int(sor[2]))
        i += 1
    print(nevek)
    print(nemek)
    print(korok)