# FASTag Highway Toll Tax Calculator
fastag = input("Is FASTag active? (yes/no): ")
vehicle = input("Enter vehicle type: ")
holiday = input("Is it a national holiday? (yes/no): ")

if fastag == "no":
    print("Double toll penalty applied: cash mode")

elif fastag == "yes":
    if holiday == "yes":
        print("Festive waiver applied: half toll")

    else:
        if vehicle == "car":
            print("Toll amount: 100 rupees")

        elif vehicle == "SUV":
            print("Toll amount: 150 rupees")

        elif vehicle == "truck":
            print("Toll amount: 300 rupees")

        else:
            print("Invalid vehicle category")
