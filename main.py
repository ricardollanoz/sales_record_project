print("*** SALES RECORDING SYSTEM ***")
print("\n")

def system():    
    income = True
    
       
    while income:
        record = []
        contador = 1
        for i in range(contador):

        # A variable is generated to get the number of products to be recorded
            
            print(f"Record product informacion #{i + 1}") 
            name_product = str(input("Product name: "))
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            print("\n")
                # A dictionary is created to store product information
            product = {
                    "name": name_product,
                    "price": price,
                    "quantity": quantity

                }
                
                # The new product was added to the list called record
            record.append(product)
                
            income = str(input("Do you want to register another product? yes/no: "))
            if income == "yes":
                    contador=+ 1
            else: 
                break
    print(record)


system()


                




                

            
                


   

        
                     






