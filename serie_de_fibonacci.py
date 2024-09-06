numero = int(input("Ingresa el número hasta donde se aproximará la serie de fibonacci: "))

a,b = 0,1
lista_fibonacci = [a]

for i in range(numero):
    if b <= numero:
        lista_fibonacci.append(b)
        a,b = b,a+b
print(lista_fibonacci)