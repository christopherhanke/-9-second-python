#################################
#                               #
#   This is a little FizzBuzz   #
#                               #
#################################

number = None

print("Select a number between 1 and 100.")
try:
    number = int(input())
except ValueError:
    while True:
        print("Please enter a valid Number:")
        try:
            number = int(input())
        except ValueError:
            continue
        break

for x in range(number):
    if x == 0:
        continue

    if x % 3 == 0:
        if x % 5 == 0:
            print("fizzbuzz")
        else:
            print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
