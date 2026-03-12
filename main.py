from register import register
from operations import calculation
from summary import summary_generation
print("*** SALES RECORDING SYSTEM ***")
print("\n")

record = [] 
# A variable is generated to get the number of products to be recorded
register(record)

status = "yes"
while status == "yes":
    status = str(input("\nDo you want to register another profuct? yes / no : ").lower())
    print("\n")
    while status not in ["no", "yes"]:
        print("ERROR! Ingresar solamente la opcion (yes) o (no)")
        status = (input("\nDo you want to register another profuct? yes / no : ").lower())
        print()
    if status == "no":
       total_amount = calculation(record)
       
       summary_generation(record, total_amount)
    
    else:
        register(record)






                
            
    


                




                

            
                


   

        
                     






