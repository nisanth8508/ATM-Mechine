customer={
    '1001': {
        "name":"Kumar ",
        'pin':1234,
        'amount':10000
    },
    '1002': {
        'name':'Raja',
        'pin':5678,
        'amount':5000

    }
}


while True:
    print("1 /  Customer login")
    print("2 / Admin Login")
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
                        print("Amount Credit / Total Amount :",customer[card]['amount'])
                        print("----------------------------------------------------------------------------------")
                    elif("3"==option):
                        print("balance : ",customer[card]['amount'])
                        print("----------------------------------------------------------------------------------")
                    else:
                        print ("thank you ")
                        break
                    
            else:
                print("invalid Pin ")
        else:
            print("Customer id Not found !!!")
    ## admin Login
    elif(2==optin):
        admin=input("Enter the Admin Id :")
        password=input("Enter the Password : ")
        if(admin=="admin1" and password=="admin123"):
             while True:
                 print("1 / Customer Add ")
                 print("2 / Show Customer details : ")
                 print("3 / logout ")
                 select=input("enter the value :")
                 if(select=="1"):
                     cardid=input("enter the card id : ")
                     if cardid in customer:
                        print("card id already exists ")
                     else:
                        name=input("enter name : ")
                        pin=int(input("enter the Pin : "))
                        amount=int(input("enter the amount : "))
                        customer[cardid]={
                        'name':name,
                        'pin': pin,
                        'amount':amount
                        }
                        print("----------------------------------------------------------------------------------")
                        print("Customer add Successfully ")
                        print("Your id :",cardid )
                        print("your Pin : ",pin)
                        print("----------------------------------------------------------------------------------")
                 elif(select=="2"):
                         for i in customer:
                             print("--------------------------------------------------------------------------------")
                             print("Name:",customer[i]['name'])
                             print("PIN :",customer[i]['pin'])
                             print("Amount :",customer[i]['amount'])
                             print("-----------------------------------------------------------------------------")
                 else:
                     print("---------------------------------------------------------------------------------------")
                     break
    else:
        print("Thank you Visiting ATM ")
        break




    

