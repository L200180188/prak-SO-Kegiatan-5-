a = [[2,3], [5,7]]
b = [[0 for j in range(3)]for i in range(3)]
"""membuat list kuadrat bilangan dari 0 sampai 6""""
[x**2 for x in range(0,7)]
#membuat list yang berisi tuple pasangan dan kuadratnya dari 0 samapi 6
[(x,x**2)for x in range(7)]
#membuat list kuadrat bilangan genap antara 0 smapai 15
[x**2 for x in range(15)if x%2==0]
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,9,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if n%i==0:
                return False
        return True
