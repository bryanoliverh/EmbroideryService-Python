import os

CHAR_PRICING_FILE = "characters.txt"
FONT_PRICING_FILE = "fonts.txt"
# FONT_MULTIPLIERS = {24: 1.0, 36: 1.5, 48: 2.0}


def readPricing(filename: str, pricing: dict):
    with open(filename) as file:
        for line in file:
            parts = line.split()
            pricing[parts[0]] = float(parts[1])


def showPricing(charPricing: dict, fontPricing: dict, fontSize: int):
    print(f"Pricing for font size {fontSize}pts")
    print("=" * 27)

    formattedFontPricing = {int(k): v for k, v in fontPricing.items()}

    for i, (char, price) in enumerate(charPricing.items()):
        rounded_price = round(price * formattedFontPricing[fontSize])
        if char in fontPricing:
            rounded_price += fontPricing[char]
        print(f"{char}\t{rounded_price:.2f}", end="\t")
        if (i + 1) % 10 == 0:
            print()
    print()



def requestQuote(charPricing: dict, fontPricing: dict):
    string = input("Enter characters that you want to print: ").replace(" ", "")
    fontSize = int(input("Enter font size (24/36/48): "))
    formattedFontPricing = {int(k): v for k, v in fontPricing.items()}

    if fontSize not in formattedFontPricing:
        print("Invalid font size")
        return

    total_price = 0
    for char in string:
        if char not in charPricing:
            print("Invalid character")
            return
        total_price += charPricing[char] * formattedFontPricing[fontSize]

    for char, price in fontPricing.items():
        if char in string:
            total_price += price * formattedFontPricing[fontSize]

    if total_price > 1000:
        discount = 0.0
        lowest_char_price = min(charPricing.values())
        if total_price >= 1000:
            # Apply 5% discount
            discount = total_price * 0.15
        else:
            discount = lowest_char_price * formattedFontPricing[fontSize]
        discounted_price = max(total_price - discount, 0.0)
        print(f"Total price: ${total_price/100:.2f}")
        print(f"Discount: ${discount/100:.2f}")
        print(f"Discounted price: ${discounted_price/100:.2f}")
    else:
        print(f"Total price: ${total_price/100:.2f}")

    print()

def addUpdateCharPricing(charPricing: dict, filename: str):
    char = input("Enter character: ")
    if char not in charPricing:
        print("Adding new character...")
    else:
        print(f"Current price for {char}: {charPricing[char]} cents")
    price = float(input("Enter price: "))
    charPricing[char] = price

    with open(filename, "w") as file:
        for char, price in charPricing.items():
            file.write(f"{char} {price}\n")

def main():
    charPricing = {}
    fontPricing = {}

    readPricing("characters.txt", charPricing)
    readPricing("fonts.txt", fontPricing)
    while True:
        print("Welcome to Bryan's Embroidery Services!")
        print("==========================================")
        print("1. Display Pricing Table")
        print("2. Request for Quote")
        print("3. Add/Update Characters' Pricings")
        print("4. Exit")

        choice = input("Please enter your choice (1-4): ")

        if choice == "1":
            fontSize = int(input("Please enter font size (24, 36, or 48): "))
            if fontSize == 24 or fontSize == 36 or fontSize == 48:
                showPricing(charPricing, fontPricing, fontSize)
            else:
                print("Invalid font size.")
        elif choice == "2":
                requestQuote(charPricing, fontPricing)
        elif choice == "3":
            char = input("Please enter the character to add/update pricing: ")
            if char in charPricing:
                print("The current pricing for", char, "is", charPricing[char], "cents.")
                price = float(input("Please enter the new pricing: "))
                charPricing[char] = price
            else:
                price = float(input("Please enter the pricing for " + char + ": "))
                charPricing[char] = price

            # Update the pricing in the file
            with open("characters.txt", "w") as f:
                for char, price in charPricing.items():
                    f.write(char + " " + str(price) + "\n")

            print("The pricing for", char, "has been updated.")
        elif choice == "4":
            print("Thank you for using MonkeyPrint Embroidery Services!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
