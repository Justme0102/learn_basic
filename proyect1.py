weight = float(input("Enter your weight: "))
uni = input("kilograms or puuds? (K or L): ")

if uni == "K":
    weight = weight * 2.205
    uni = "lsb."
elif uni == "L":
    weight = weight / 2.205
    uni = "kgs"
else:
    print (f"{uni} was not valid")

print (f"your weight is {round(weight)} {uni}")
    