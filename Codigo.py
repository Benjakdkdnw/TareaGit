def encontrar_letras(guia,barrera):
    for i in range(len(guia)):
        resultado=barrera.find(guia[i])
        if resultado==-1:
            return False
    return True

guia=input()
barrera_uno=input()
barrera_dos=input()
barrera_tres=input()

print(encontrar_letras(guia,barrera_uno))
print(encontrar_letras(guia,barrera_dos))
print(encontrar_letras(guia,barrera_tres))