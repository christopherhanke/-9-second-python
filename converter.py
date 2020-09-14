#################################################
#                                               #
#  This program converts kilometers in miles.   #
#                                               #
#################################################

KM_RATIO = 1.609344

print("##################################")
print("Welcome to the distance converter.")
print("Here you can convert km in miles.")
print("##################################")
while True:
    answer = None
    try:
        km_input = float(input("Please, insert your distance in km: ").replace(",", "."))
    except ValueError:
        print("Please enter a valid number.")
        continue
    miles = km_input / KM_RATIO
    print("This equals ", "%.2f" % miles, " miles.")
    print("##################################")
    while answer != "y" and answer != "n":
        answer = input("Do you want to convert another distance? [y]/[n] :")
    if answer == "n":
        break

print("Thank you for using the distance converter.")
print("Goodbye.")
