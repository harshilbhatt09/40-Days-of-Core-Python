def your_vat():
    price = float(input("Enter price: "))
    VAT = float(input("Enter VAT: "))
    while price < 0 or VAT < 0:
        print("Enter positive price")
        price = float(input("Enter price: "))
        VAT = float(input("Enter VAT: "))
        result = price + ((price * VAT) / 100)
    result = price + ((price * VAT) / 100)
    return result


print(your_vat())
