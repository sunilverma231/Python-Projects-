try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error :
    print("Error")
except ValueError:
    print("Invalid error")

