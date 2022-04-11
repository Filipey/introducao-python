def calcImc():
    height = float(input("Type your height: "))
    weight = float(input("Type your weight: "))

    imc = weight / (height ** 2)

    if 18.5 <= imc <= 25.0:
        print("Normal weight")
        return
    if imc > 25.0:
        print("Overweight")
        return
    if imc < 18.5:
        print("Under weight")
        return


def calcIncomeTax():
    salary = float(input("Type your salary: "))

    if salary <= 1903.98:
        print("Exempt")
        return

    if 1903.99 <= salary <= 2826.55:
        incomeTax = (salary * 0.075) + 142.80
        print(f"Your income tax is: {incomeTax:0.2f}")
        return

    if 2826.66 <= salary <= 3751.05:
        incomeTax = (salary * 0.15) + 354.80
        print(f"Your income tax is: {incomeTax:0.2f}")
        return

    if 3751.05 <= salary <= 4664.68:
        incomeTax = (salary * 0.225) + 636.13
        print(f"Your income tax is: {incomeTax:0.2f}")
        return

    if salary > 4664.69:
        incomeTax = (salary * 0.275) + 869.36
        print(f"Your income tax is: {incomeTax:0.2f}")
        return


def fuelValue():
    fuel = input("Type what fuel you wanna use: \nA-Alcohol G-Gasoline: ")
    liters = float(input("Type how many liters you wanna fuel: "))

    fuel = fuel.upper()

    if fuel == 'A':
        if liters <= 20:
            price = (2.80 * liters) - (0.08 * liters)
            print(f"The fuel value to pay is {price}")
        else:
            price = (2.80 * liters) - (0.14 * liters)
            print(f"The fuel value to pay is {price}")

    elif fuel == 'G':
        if liters <= 20:
            price = (4.20 * liters) - (0.16 * liters)
            print(f"The fuel value to pay is {price}")
        else:
            price = (4.20 * liters) - (0.25 * liters)
            print(f"The fuel value to pay is {price}")

    else:
        if fuel != 'A' and fuel != 'G':
            print("That's not a valid fuel")
            return


def cashMachine():
    withdraw = int(input("Type how many you wanna withdraw: "))

    if 10 > withdraw < 1000:
        print("Invalid value! Is not among the acceptable values")
        return

    if withdraw % 10 != 0:
        print("Invalid value! Should be multiple of ten!")
        return

    twoHundred = withdraw // 200
    withdraw -= 200 * twoHundred

    hundred = withdraw // 100
    withdraw -= 100 * hundred

    fifty = withdraw // 50
    withdraw -= fifty * 50

    ten = withdraw // 10
    withdraw -= ten * 10

    if twoHundred > 0:
        print(f"{twoHundred} notes of R$200")

    if hundred > 0:
        print(f"{hundred} notes of R$100")

    if fifty > 0:
        print(f"{fifty} notes of R$50")

    if ten > 0:
        print(f"{ten} notes of R$10")
