def summary_generation(record, total_amount):
    print("*** SALES SUMMARY ***")
    
    for index in record:
        print(f"Product: {index['name']}")
        print(f"Total quantity sold: {index['quantity']}\n")
        

    print(f"Total amount:{total_amount}")
    
        