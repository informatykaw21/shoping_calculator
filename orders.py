import decimal
from decimal import Decimal

p = {"UT": 0.0685, "NV": 0.08, "TX": 0.0625, "AL": 0.04, "CA": 0.0825}
r = {1000: 0.03, 5000: 0.05, 7000: 0.07, 10000: 0.1, 50000: 0.15}


def input_code():
    code = input("Please, input countryCode. Example: CA: ")
    return code


def value_of_whole_order():
    prodNo=1
    d1 = int(input(
        "Enter number, of items to be bought. For example for two items, that will be later added, with quantity and price,  write 2: "))
    quantity_li = []
    price_li = []
    print("Now, input quantity and price, for ", d1, "products, you want to purchase")
    for i in range(0, d1):
        print("Now data for product nr", prodNo,":")
        i1 = round(Decimal((input("quantity for product: "))), 2)
        c1 = round(Decimal((input("price for product: "))), 2)
        prodNo+=1
        quantity_li.append(i1)
        price_li.append(c1)
    pairs = list(zip(price_li, quantity_li))
    multiplied = [(x * y) for x, y in pairs]

    produktnr=1
    for i in multiplied:
        ir = round(i, 2)
        print(f"Before discount, value, of product nr",produktnr,"{:>30,}".format(ir))
        produktnr+=1
    total = sum(multiplied)
    return total


def cena_po_obnizce(total):
    for (k, v) in r.items():
        if total < k:
            percent = Decimal(v)
            after_discount = total * (1 - Decimal(percent))
            discount_value = total - after_discount
            rr = round(discount_value, 2)
            sp = " "
            print("Discount value.........................", f"{rr:>30,}")
            rpo = round(after_discount, 2)
            print("Price with discount....................", f"{rpo:>30,}")
        else:
            after_discount = total * (1 - Decimal(0.15))
            discount_value = total - after_discount
            rr = round(discount_value, 2)
            print("Discount value (-):....................", f"{rr:>30,}")
            rpo = round(after_discount, 2)
            print("Price with discount....................", f"{rpo:>30,}")
        return after_discount


def cena_z_podatkiem(po_obnizce, code):
    for k, v in p.items():
        if code == k:
            v1 = Decimal(v)
            v1d = round(v1, 2)
            tax_value = v1 * po_obnizce
            wpr = round(tax_value, 2)
            print("Tax value added:.......................", f"{wpr:>30,}")

            v2 = po_obnizce + tax_value
            v2d = round(v2, 2)
            print("Price with tax added...................", "{:>30,}".format(v2d))



if __name__ == '__main__':
    k1 = input_code()
    value_order = value_of_whole_order()
    c = cena_po_obnizce(value_order)
    cena_z_podatkiem(c, k1)
