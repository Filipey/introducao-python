# Return the based raised to exponent
def calcPotency(base: int, exponent: int) -> int:
    result: int = base ** exponent

    return print(f"The result of {base} raised to {exponent} is: {result}")


# Return a new list with only positive numbers of the original list
def onlyPositiveNumbers(list: list) -> list:
    newList = []
    for number in list:
        if number > 0:
            newList.append(number)

    return print(f"The new list is: {newList}")


# Return the reversed string
def reverseString(string: str) -> str:
    return print(f"The reverse string is: {string[::-1]}")

# Return True if the string is a palindrome and false if not
def isPalindrome(string: str) -> str:

    if string == string[::-1]:
        print(f"{string} is a palindrome")
        return True
    else:
        print(f"{string} isnt a palindrome")
        return False

# Return the ocurrencies of the char on the string
def countCharOcurrency(string: str, char: chr) -> int:
    count = 0

    for caracter in string:
        if caracter == char:
            count += 1

    return print(f"The caracter `{char}` appears {count} in the string {string}")


# Return the time in seconds
def daysHoursMinutesToSeconds(days: int, hours: int, minutes: int, seconds: int) -> float:
    convertedDays = days * 86400
    convertedHours = hours * 3600
    convertedMinutes = minutes * 60
    finalTime = seconds + convertedMinutes + convertedHours + convertedDays

    return print(f"The final time in seconds is: {finalTime}")


# Return the quantity of vowels in a string
def countVowels(string: str) -> int:
    vowels = ('A', 'E', 'I', 'O', 'U')

    count = 0

    for char in string:
        if vowels.__contains__(char.upper()):
            count += 1

    return print(f"The number of vowels in {string} is: {count}")


# Return the MDC of two numbers
def calcMdc(nmr: int, nmr2: int) -> int:

    while nmr2 != 0:
        rest = nmr % nmr2
        nmr = nmr2
        nmr2 = rest

    return print(f"The MDC of is {nmr}")


class Employee:

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary


class Car:

    def __init__(self, fuelConsumption: float, fuelCapacity: float):
        self.fuelConsumption = fuelConsumption
        self.fuelCapacity = fuelCapacity

    def speedUp(self, distance: int) -> float:
        actualCapacity = self.fuelCapacity = self.fuelConsumption * distance

        return print(f"The actual capacity is: {actualCapacity}")

    def toFuel(self, quantity: int) -> float:
        actualCapacity = self.fuelCapacity + quantity

        if actualCapacity > self.fuelCapacity:
            print("Full capacity obtained")
            return

        return  print(f"The actual capacity is: {actualCapacity}")