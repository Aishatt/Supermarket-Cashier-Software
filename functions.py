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
    print (product +':$' + str(price_Data[product])+ 'x' + str(quantity) + ' = '+'$' + str(subtotal))
    return subtotal


def discounts(billAmount,membership):
    discount=0
    #check conditionq
    if billAmount >= 25:
        if (membership == 'gold') :
            billAmount=int(billAmount*0.80)
            discount=20 
        elif(membership =='silver'):
            billAmount=int(billAmount*0.90)
            discount=10  
        elif(membership =='bronze'):
           billAmount=int(billAmount*0.95)
           discount=5
        print(str(discount)+'% off for '+ membership +" "+"membership on total amount: $"
        + str(billAmount))
    else:
        print('No discount on amount less than $25')
    
    return billAmount


def makeBill(buyingData,membership):

    billAmount=0
    #for purchased goods n quantity in our dictionary
    for key,value in buyingData.items():
        #get price and save it in billamount
        billAmount+=get_price(key,value)
        #get discount and save it in billamount
        billAmount= discounts(billAmount,membership)
        print('the discounted amount is : $'+ str(billAmount))

#function call
buyingData=accept_product()
membership=input('Enter customer membership:')       
makeBill(buyingData,membership)