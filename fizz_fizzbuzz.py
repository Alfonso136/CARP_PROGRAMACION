
rango = int(input("Ingresa de 1 a que rango será el FizzBuzz: "))

for i in range(1,rango + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")
    
    elif i % 5 == 0:
        print("Buzz")
    
    else:
        print(i)