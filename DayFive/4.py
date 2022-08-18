for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print(f"{number} FIZZBUZZ")
        else:
            print(f"{number} FIZZ")
    elif number % 5 == 0:
        print(f"{number} BUZZ")
    else:
        print(f"{number}")
