def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2,numero):
        if numero % i == 0: return False
    return True

def son_primos(numero):
    lista_primos = []
    for i in range(2,numero+1):
        respuesta = es_primo(i)
        if respuesta == True:
            lista_primos.append(i)
    return lista_primos

numero = int(input("Ingresa un número para ver cuantos primos se le acercan: "))

resultado = son_primos(numero)

print(f"Estos los lo números primos que se acercan a tu número: \n{resultado}")