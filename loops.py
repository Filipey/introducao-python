def readPerson():
    name = str(input("Type your name: "))
    while len(name) <= 3:
        name = str(input("Invalid value. Type your name: "))

    age = int(input("Type your age: "))
    while age > 150 or age < 0:
        age = int(input("Invalid value. Type your age: "))

    salary = float(input("Type your salary: "))
    while salary < 0:
        salary = float(input("Invalid value. Type your salary: "))

    gender = str(input("Type your gender: ")).upper()
    while gender != 'F' and gender != 'M':
        gender = str(input("Invalid value. Type your gender: ")).upper()

    maritalStatus = str(input("Type your marital status: ")).upper()
    while maritalStatus != 'S' and maritalStatus != 'C' and maritalStatus != 'V' and maritalStatus != 'D':
        maritalStatus = str(input("Invalid value. Type your marital status: ")).upper()


def biggerNumber():
    numbersList = []
    for i in range(0, 5):
        number = float(input("Type a number: "))
        numbersList.append(number)

    bigger = numbersList[0]
    for number in numbersList:
        if number > bigger:
            bigger = number

    print(f"The bigger number typed is: {bigger}")


def sumAndAverage():
    sum = 0
    average = 0
    for i in range(0, 5):
        number = float(input("Type a number: "))
        sum += number

    average = sum / 5
    print(f"The sum is: {sum} and the average is: {average}")


def countPairAndOddNumbers():
    pairCount = 0
    oddCount = 0

    for i in range(0, 10):
        number = float(input("Type a number: "))

        if number % 2 == 0:
            pairCount += 1
        else:
            oddCount += 1

    print(f"The quantity of pair numbers typed are: {pairCount} and odd numbers are: {oddCount}")


def primeNumber():
    number = int(input("Type a number: "))
    divisible = []

    for i in range(2, number):
        if number % i == 0:
            divisible.append(i)

    if len(divisible) != 0:
        print(f"Isnt prime. is divisible by: {divisible}")

    else:
        print("Is prime.")


def asteriskSquare():
    n = int(input("Type a number: "))

    print(" *" * n)
    for i in range(n - 2):
        print(" * " + "  " * (n - 2) + "* ")
    print(" *" * n)


def asteriskTriangle():
    n = int(input("Type a number: "))

    count = 1

    while count <= n:
        print("* " * count)
        count += 1


def listAllNotes():

    conceptA = []
    conceptB = []
    conceptC = []
    conceptD = []
    conceptE = []

    note = float(input("Type a note: "))

    while note != -1:

        if 9 <= note <= 10:
            conceptA.append(note)
        elif 8 <= note <= 8.9:
            conceptB.append(note)
        elif 7 <= note <= 7.9:
            conceptC.append(note)
        elif 6 <= note <= 6.9:
            conceptD.append(note)
        elif 0 < note <= 5.9:
            conceptE.append(note)

        note = float(input("Type a note: "))

    print(f"Concept A: {conceptA}\nConcept B: {conceptB}\nConcept C: {conceptC}\nConcept D: {conceptD}\nConcept E: {conceptE}")