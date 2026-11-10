card = input("Enter Card Number: ").strip().replace(" ", "")


if card.isdigit() and len(card) in [13, 15, 16]:
    
    summa = 0
    reversed_card = card[::-1]
    
    for index in range(len(reversed_card)):
        digit = int(reversed_card[index])
        if index % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        summa = summa + digit
        
    if summa % 10 == 0:
        print("Valid")
        length = len(card)
        prefix = card[:2]
        if (length == 13 or length == 16) and card.startswith("4"):
            print("Visa")
        elif length == 15 and (prefix == "34" or prefix == "37"):
            print("American Express")
        elif length == 16 and prefix in ["51", "52", "53", "54", "55"]:
            print("Master Card")
        else:
            print("Unknown")
            
    else:
        print("Invalid checksum")
else:
    print("Wrong Input. Try again...")
