from AuctionClasses.Auction import Auction

def print_menu():
    print("\n==== Auction Menu ====")
    print("1. Add Item")
    print("2. Check In Bidder")
    print("3. Record Sale")
    print("4. Print Bidder Receipt")
    print("5. Print Auction Summary")
    print("6. Save Auction Data")
    print("7. Save and Exit")


def getInt(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def getFloat(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid price.")

def getType(prompt: str) -> str:
    while True:
        type = input(prompt).lower()
        if type in ["live", "silent"]:
            return type
        print("Please enter 'live' or 'silent'.")

def main():
    auction = Auction()
    sentinal = str
    while True:
        sentinal = input("Would you like to load existing auction data? (y/n): ").strip().lower()

        if sentinal == 'y':
            filename = input("Filename to load: ")
            try:
                auction.loadFromExcel(filename)
            except Exception as e:
                print("Failed to load data:", e)
            else:
                print("Auction data loaded.")
                break
        elif sentinal == 'n':
            print("Starting new auction.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    while True:
        print_menu()
        choice = input("Select an option: ").strip()

        try:
            if choice == "1":
                itemNumber = getInt("Item Number: ")
                name = input("Item Name: ")
                itemType = getType("Item Type (live/silent): ")
                auction.addItem(itemNumber, name, itemType)
                print("Item added.")

            elif choice == "2":
                bidderId = getInt("Bidder ID: ")
                name = input("Bidder Name: ")
                auction.checkInBidder(bidderId, name)
                print("Bidder checked in.")

            elif choice == "3":
                itemNumber = getInt("Item Number: ")
                bidderId = getInt("Winning Bidder ID: ")
                salePrice = getFloat("Sale Price: ")
                auction.recordSale(itemNumber, bidderId, salePrice)
                print("Sale recorded.")

            elif choice == "4":
                bidderId = getInt("Bidder ID: ")
                auction.printBidderReceipt(bidderId)

            elif choice == "5":
                auction.printAuctionSummary()

            elif choice == "6":
                filename = input("Filename to save to Excel: ")
                auction.saveToExcel(filename)
                print("Auction data saved to Excel.")

            elif choice == "7":
                auction.saveToExcel(filename)
                print("Saved and exiting...")
                break
            else:
                print("Invalid option.")

        except ValueError as e:
            print("Error:", e)

        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    main()