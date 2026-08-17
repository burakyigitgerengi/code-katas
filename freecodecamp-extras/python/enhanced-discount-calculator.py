price = 0
discount = 0


def apply_discount(price, discount):

    try:
        price = int(price)
        discount = int(discount)
        return f"The actual price is: {price - price * discount // 100}"

    except (TypeError, ValueError):
        return "Wrong data type."


def get_values():

    global price
    global discount

    price = input("Price: ")
    discount = input("Discount: ")


def main():
    get_values()
    print(apply_discount(price, discount))


main()
