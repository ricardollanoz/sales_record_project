
def calculation(record):
    total_amount = 0
    for index in record:
        total_amount+= index['price']*index['quantity']
    return total_amount