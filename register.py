def register(record):
    
    print(f"Record product information ") 
    name_product = str(input("Product name: "))
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    print("\n")
        # A dictionary is created to store product information
    product = {
            'name': name_product,
            'price': price,
            'quantity': quantity

        }
        
        # The new product was added to the list called record
    record.append(product)