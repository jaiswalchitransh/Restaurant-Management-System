import json


def get_rating(reviews):
    rating = 5
    if reviews:  
        rating = sum(reviews) // len(reviews)
    return "⭐️" * rating


with open("menu.json", "r") as f:
    data = json.load(f)

items = data.get("items", [])

print()
print("-" * 60)
print("            NAMASTE")
print("WELCOME TO CHITRANSH'S RESTAURANT")
print("-" * 60)
while True:
    print()
    print("1. Show Menu")
    print("2. Order Items")
    print("3. Add Item")
    print("4. Add Ratings")
    print("5. Exit")
    print()
    print("-" * 60)
    choice = int(input())

    if choice == 1:
        print("-" * 60)
        print("ID\tName\t\tPrice\tRatings")
        print("-" * 60)
        for item in items:
            print(
                f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}\t{get_rating(item.get("reviews", []))}'
            )
        print("-" * 60)
    elif choice == 2:
        ordered_items = {}
        order_items = list(map(int, input("What you want to try today? ").split(",")))
        print("-" * 60)
        print("ID\tName\t\tPrice\tQuantity\tAmount")
        print("-" * 60)
        total_bill = 0
        for order_item in order_items:
            for item in items:
                if item["id"] == order_item:
                    if order_item in ordered_items:
                        ordered_items[order_item]["quantity"] += 1
                    else:
                        ordered_items[order_item] = item
                        ordered_items[order_item]["quantity"] = 1
                    break
        for item in ordered_items:
            name = ordered_items[item]["name"]
            price = ordered_items[item]["price"]
            quantity = ordered_items[item]["quantity"]
            amount = price * quantity
            print(f"{item}\t{name}\t{price}\t{quantity}\t\t{amount}")
            total_bill += amount
        print("-" * 60)
        print(f"\t Total Amount is : {total_bill}")
        print("-" * 60)
    elif choice == 3:
        name = input("Enter item name : ")
        item_price = int(input("Enter the price : "))
        item_type = input("Veg or Non-Veg : ")
        items.append(
            {
                "id": len(items) + 1,
                "name": name,
                "price": item_price,
                "veg": True if item_type == "veg" else False,
                "reviews": [],
            }
        )

        data["items"] = items
        with open("menu.json", "w") as f:
            json.dump(data, f)
        print("Item has been added.")
    elif choice == 4:
        item_id = int(input("Enter the item id :"))
        rating = int(input("Give your ratings (1-5): "))
        for i, item in enumerate(items):
            if item["id"] == item_id:
                items[i]["reviews"].append(rating)
                break
        print("Thank you. Your rating has been recorded.")
    else:
        data["items"] = items
        with open("menu.json", "w") as f:
            json.dump(data, f)
        print("Thank you !")
        print("Visit the Restaurant Again")
        break
