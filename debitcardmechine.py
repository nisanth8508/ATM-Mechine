customer={
    '1001': {
        "name":"A",
        'pin':1234,
        'amount':10000
    },
    '1002': {
        'name':'B',
        'pin':5678,
        'amount':5000

    }
}


while True:
    print("1 / login")
    print("2 / Add id")
    print("3 / exit")

    ## login
    optin=int(input("enter the option : "))

    if(optin==1):

        card=input("enter the id : ")
        if card in customer:
            pinnum=int(input("enter the pin : "))
            if(pinnum==customer[card]['pin']):
                while True:
                    print("----------------------------------------------------------------------------------")
                    print("Welcome ",customer[card]['name'])
                    print("1 / Deposit ")
                    print("2 / credit ")
                    print("3 / Balance Check  ")
                    print("4 / exit ")
                    option=input("enter the Option : ")
                    if("1"==option):
                        amount=int(input("enter the amount : "))
                        if customer[card]['amount']>=amount:

                             customer[card]['amount']-=amount
                             print("amount deposit remaining ",customer[card]['amount'])
                             print("----------------------------------------------------------------------------------")
                        else:
                            print("Invalid balance Check Balance !!! ")
                        
                    elif("2"==option):
                        amount=int(input("enter the amount : "))
                        customer[card]['amount']+=amount
                        print("Amount Credit / Total Amount :",customer[card]['balance'])
                        print("----------------------------------------------------------------------------------")
                    elif(3==option):
                        print("balance : ",customer[card]['balance'])
                        print("----------------------------------------------------------------------------------")
                    else:
                        print ("thank you ")
                        break
                    
            else:
                print("invalid Pin ")
        else:
            print("Customer id Not found !!!")
    ## admin Login
    elif("2"==optin):
        cardid=int(input("enter the card id "))
        if cardid in customer:
            print("card id already exists ")
        else:
            name=input("enter name : ")
            pin=int(input("enter the PiN"))
            amount=int(input("enter the amount "))
            customer[card]={
                'name':name,
                'pin': pin,
                'amount':amount
            }
            print("Customer add Successfully ")
            print("Your id :",cardid )
            print("your Pin : ",pin)
            
    else:
        print("Thank You for Comeing ATM ")





    

