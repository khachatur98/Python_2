products = {"candy": 10, "juice": 5, "pen": 50}

def check(product, num):
    global products
    n_prod = products.get(product, -1)

    return num <= n_prod
