def calcArea():
    radius = float(input("Type the radius of the circle: "))

    area = 3.14 * (radius ** 2)
    perimeter = 2 * 3.14 * radius

    print(f"The area is {area:.2f}")
    print(f"The perimeter is {perimeter:.2f}")
    print("------------------------")


def farenheintToCelsius():
    temperature = float(input("Type the temperature in ªF: "))

    temperature = 5 * ((temperature - 32) / 9)

    print(f"The temperature in ªC is {temperature:.2f}")
    print("------------------------")


def brazilianRealToDolar():
    money = float(input("Type the amount in reais: "))

    money = money / 5.32

    print(f"The value in USD is {money:0.2f}$")
    print("------------------------")


def salaryCounter():
    moneyPerHour = float(input("Type how many you receive per hour: "))
    hoursPerMonth = float(input("Type how many hours you work in a month: "))

    salary = moneyPerHour * hoursPerMonth
    incomeTax = salary * 0.15
    inss = salary * 0.10
    syndicate = salary * 0.02

    netSalary = salary - incomeTax - inss - syndicate

    print(f"Your gross salary is: {salary}")
    print(f"The total paid to the INSS is: {inss:0.2f}")
    print(f"The total paid to the syndicate is: {syndicate:0.2f}")
    print(f"Your net salary is {netSalary}")
    print("------------------------")


def calcInkValue():
    area = float(input("Type the area of the room in m²: "))

    liters = area / 3
    cans = int(liters / 18)

    if liters % 18 != 0:
        cans += 1

    totalPrice = cans * 80

    print(f"You should buy {cans} cans")
    print(f"The total price is {totalPrice}")
    print("------------------------")


def calcDownloadTime():
    file = float(input("Type the size of the file in MB: "))
    internetSpeed = float(input("Type your internet speed in Mb/s: "))

    downloadTime = (file / internetSpeed) / 60

    print(f"The total time spend to download the file is {downloadTime:0.2f} minutes")
    print("------------------------")
