

def net_price(price, discount=0, tex= 0.00):
    return price * (1 - discount) * (1 + tex)


print(net_price(500, 0 ,0.05))