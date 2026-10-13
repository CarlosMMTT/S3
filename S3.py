def ordenamiento_por_insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

line = [1, 4, 2, 6, 3]

print(ordenamiento_por_insercion(line))


def multiplicacion(a,b):
    c = 0
    for i in range(b):
        c += a
    return c

def dividision(a,b):

    c = 0
    divisor = a
    if b ==0:
        return "No se puede dividir entre 0"
    while a >= b:
        a = a-b
        c += 1
    resto = divisor - multiplicacion(c, b)
    return c, resto



def raiz_entera(a):
    if a < 0:
        return "No se pueden meter números negativos"
    if a == 0 or a == 1:
        return a

    x = 0
    while True:
        y = multiplicacion(x, x)

        if y > a:
            return x - 1
        elif y == a:
            return x
        x += 1
print(dividision(17,9))
print(raiz_entera(4))
