from Productcheck import products, check

def buy(product, num, price):
    global products

    if check(product, num):
        print(f"You bought {product} and spent {num*price}")
        products[product] -= num
    else:
        print("Sorry! We are out of this product.")

def main():
    buy("candy", 10, 2)
    buy("candy", 1, 2)
    buy("juice", 1, 5)
    buy("pen", 1, 1.5)
    buy("vanish", 1, 1)

    print(products)

main()
