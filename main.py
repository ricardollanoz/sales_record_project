from register import register
from operations import calculation
from summary import summary_generation
print("*** SALES RECORDING SYSTEM ***")
print("\n")

record = [] 

# A variable is generated to get the number of products to be recorded
register(record)


status = "si"
while status == "si":
    status = str(input("\nDo you want to register another profuct? si / no : "))
    
    print("\n")
    if status == "no":
       total_amount = calculation(record)
       
       summary_generation(record, total_amount)

    else:
        register(record)






                
            
    


                




                

            
                


   

        
                     






