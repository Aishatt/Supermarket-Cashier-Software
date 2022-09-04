# Function to accept the product name and quantity
def accept_product():
    buyingData={}
    product_details= True
    
    while product_details:
        details = str( input("Press A to continue and Q to quit: \n "))
        if details == 'A':
            product= str(input("Enter product: "))
            quantity= int(input("Enter quantity: "))
            buyingData.update({product:quantity})
        elif details == 'Q':
            product_details = False
        else:
            print("please select correct option")
           
    return buyingData 
accept_product() 

#Function to calculate products
#price_data contains product value and its price as key
def get_price(product,quantity):
    price_Data={
        'chocolate':4,
        'milk':7,
        'Apple':3,
        'orange':8,
    }
    subtotal= int(price_Data[product] * quantity)
    print (product +':$' + str(price_Data[product])+ 'x' + str(quantity) + ' = ' + str(subtotal))
    return subtotal
get_price('milk',3)

def discount(subtotal):
    amt= str(input("enter membership"))
    #check condition
    if (amt== 'gold') :
        d_price= subtotal*0.05
    elif(amt=='silver'):
        d_price= subtotal*0.12
    elif(amt=='silver'):
        d_price= subtotal*0.20
    else:
        d_price= subtotal
        print('not a member')
    return d_price
discount()        