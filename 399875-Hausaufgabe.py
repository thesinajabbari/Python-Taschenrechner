import math
from math import pi

print("Herzlich Willkommen")
print("Hallo Benutzer\n")


def operation():
    print("Für Addition geben Sie bitte '+' ein")
    print("Für Subtraktion geben Sie bitte '-'ein")
    print("Für Division geben Sie bitte '/' ein")
    print("Für Multiplikation geben Sie bitte '*' ein")
    print("Für Summe einer Liste an Zahlen geben Sie bitte 's' ein")
    print("Für Mittelwert geben Sie bitte  'm' ein")
    print("Für Maximum einer Liste an Zahlen bitte  'max' ein")
    print("Für Minimum einer Liste an Zahlen geben Sie bitte 'min' ein")
    print("Für den Umfang des Kreises geben Sie 'r' ein")
    print("Um die dritte Seite eines Dreiecks zu finden, geben Sie 'd' ein")


operation()
i = 0
while i < 1:
    i += 1
    userInput = input("Bitte wählen Sie Ihre gewünschte Operation: \t")

    if userInput == "+":
        num1 = float(input("Geben Sie bitte die erste Nummer ein:\n"))
        num2 = float(input("Geben Sie bitte die zweite Nummer ein:\n"))
        print(f"{num1} + {num2} = " + str(int(num1) + int(num2)))

    elif userInput == "-":
        num1 = float(input("Geben Sie bitte die erste Nummer ein:\n"))
        num2 = float(input("Geben Sie bitte die zweite Nummer ein:\n"))
        print(f"{num1} - {num2} = " + str(int(num1) - int(num2)))

    elif userInput == "*":
        num1 = float(input("Geben Sie bitte die erste Nummer ein:\n"))
        num2 = float(input("Geben Sie bitte die zweite Nummer ein:\n"))
        print(f"{num1} * {num2} = " + str(int(num1) * int(num2)))

    elif userInput == "/":
        num1 = float(input("Geben Sie bitte die erste Nummer ein:\n"))
        num2 = float(input("Geben Sie bitte die zweite Nummer ein:\n"))
        print(f"{num1} / {num2} = " + str(int(num1) / int(num2)))

    elif userInput == "m":

        sum = 0
        values = []

        n = int(input("Bitte geben Sie die Anzahl der Elemente ein : "))

        for j in range(0, n):
            ele = int(input())
            values.append(ele)

        for j in values:
            sum = sum + j

        mean = sum/len(values)
        print('Der Mittelwert ist: ' + str(mean))

    elif userInput == "s":
        userInput = list(map(float, input("Geben Sie bitte mehrere Zahlen ein\t").split()))
        sumUser = sum(userInput)

        def sumprint():
            for j in userInput[:-1]:
                print(f"{j} + ", end='')
        sumprint()
        print(userInput[-1], "=", sumUser)

    elif userInput == "max":
        a = []
        size = int(input("Geben Sie bitte die Größe der Liste ein\t"))
        for j in range(size):
            val = int(input("Nummer eingeben:"))
            a.append(val)
        max = a[0]
        for j in range(size):
            if a[j] > max:
                max = a[j]
        print("Maximale Nummer = ", max)

    elif userInput == "min":
        a = []
        size = int(input("Geben Sie bitte die Größe der Liste ein\t"))
        for j in range(size):
            val = int(input("Nummer eingeben:"))
            a.append(val)
        min = a[0]
        for j in range(size):
            if a[j] < min:
                min = a[j]
        print("Mindestzahl = ", min)

    elif userInput == "r":
        r = float(input(" Radius des Kreises eingeben : "))
        perimeter = math.pi * 2 * r
        print("Umfang des Kreises : ", perimeter)

    elif userInput == "d":
        userInput = input("Was ist auszurechnen? Hypotenuse(c) oder Kathete(a,b): ")
        if userInput == "a":
            b = float(input("Länge der Kathete  b : "))
            c = float(input("Gib Hypotenuse c an: "))
            a = math.sqrt(c ** 2 - b ** 2)
            print(f"die Länge der Kathete a ist {a}")

        elif userInput == "b":
            a = float(input("Länge der Kathete a : "))
            c = float(input("Gib Hypotenuse c an: "))
            b = math.sqrt(c ** 2 - a ** 2)
            print(f"die Länge der Kathete b ist {b}")
        elif userInput == "c":
            a = float(input("Länge der Kathete  a : "))
            b = float(input("Länge der Kathete  b : "))
            c = math.sqrt(a ** 2 + b ** 2)
            print(f"Die Länge der Hypotenuse c ist {c}")
    else:
        print("Ungültige Eingabe")

    Bedingung = input("Möchten Sie eine neue Berechnugn durchführen? j/n  ")
    if Bedingung == "j":
        i = i-1
    else:
        print("\nAuf Wiedersehen! ")
