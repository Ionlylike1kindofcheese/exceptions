from time import sleep

print("Geef hele 2 nummers om sommen mee te bereken")
sleep(2)
print("Met deze 2 nummers laten we een plus, min, keer en deel som zien")

def calculation(num1, num2):
    plus = num1 + num2
    min = num1 - num2
    keer = num1 * num2
    deel = num1 / num2
    print(str(num1), "+", str(num2), "=", plus)
    print(str(num1), "-", str(num2), "=", min)
    print(str(num1), "x", str(num2), "=", keer)
    print(str(num1), ":", str(num2), "=", deel)


completion = False
while completion == False:
    try:
        ant1 = int(input("Nummer 1: "))
        ant2 = int(input("Nummer 2: "))
        calculation(ant1, ant2)
    except ZeroDivisionError as error:
        print("Je kan niet delen door 0")
    except ValueError as error:
        print("A.U.B gebruik hele nummers")
    else:
        completion = True