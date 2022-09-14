#create a cashier software that will 
# accept product details 
# get price 
# get discount based on membership

def getDetails():
    buyingData={}
    product_details= True
    while product_details:
        to_add=input('press A to continue and Q to quit')
        if to_add == 'A':
            product= input("Product: ")
            quantity=int(input("Quantity: "))
            #update the dictionary
            buyingData.update({product:quantity})
            print(buyingData)
        elif to_add=='Q':
            product_details= False
        else:
            print('wrong input')
   
    allProducts={
        'apple':8,
        'orange':9,
        'corn':6,
        'milk':2
    }
    subtotal=int(allProducts[product]) * quantity
    print(str(subtotal))
   
    discount=0
    member=str(input('membership: '))
    print(buyingData.items())
    if subtotal >= 25 :
        if member=='gold':
            subtotal =subtotal * 0.80
            discount= 10
        elif member == 'silver':
            subtotal = subtotal * 0.90
            discount= 15
        elif member == 'bronze':
            subtotal =subtotal * 0.95
            discount= 20
            
        print(str(discount)+ '% off for '+ str(member)+' subtotal = '+ str(subtotal))
    else:
        print('no discount for goods less than 25$')
getDetails()    
   