#--------------------------------------------------------#
# MINI PROJECT: BILLING SYSTEM IN SUPERMARKET WITH PYTHON
#---------------------------------------------------------#






#Start Billing
while True:
    #Starting
 print("**********Welcome to the Supermarket Billing System!***********")
 print("Available Items:")
 print("Code\tItem\tPrice")
 print("1\tMILK\t₹50")
 print("2\tBREAD\t₹20")
 print("3\tEggs\t₹6")
 print("4\tRICE\t₹60")
 print("5\tSuger\t₹50")
 print("0\tEXIT\t\n")

 #Empty carts
 itemnames=[]
 itemprice=[]
 itemquantity=[]
 itemtotals=[]
 grandtotal=0
 while True:
        total=0
        code=int(input("Enter the item code:"))
        if code==1:
            name="milk"
            quantity=int(input("Enter the quantity "))
            amount=50
            total=total+quantity*50
        elif code==2:
            name="Bread"
            quantity=int(input("Enter the quantity "))
            amount=20
            total=total+quantity*20
        elif code==3:
            name="EGGS"
            quantity=int(input("Enter the quantity "))
            amount=6
            total=total+quantity*6
        elif code==4:
            name="RICE"
            quantity=int(input("Enter the quantity "))
            amount=60
            total=total+quantity*60
        elif code==5:
            name="SUGER"
            quantity=int(input("Enter the quantity "))
            amount=50
            total=total+quantity*50
        elif code==0:
            print("Exit")
            break
        else:
            print("Invalid input : TRY AGAIN")
            
        itemnames.append(name)
        itemprice.append(amount)
        itemquantity.append(quantity)
        itemtotals.append(total)
        grandtotal+=total
    
    
    #Print BILL
 print("Item\tQuantity\tPrice\ttotal")
 for i in range (len(itemnames)):
        print(f"{itemnames[i]}\t  {itemquantity[i]}\t\t{itemprice[i]}\t {itemtotals[i]}")
 print("GrandTotal\t\t\t",grandtotal)
 repeat=input("\n\n\n\nEnter YES for next person and No for EXIT :: ")
 if repeat=="No"or repeat=="no"or repeat=="NO":
        print("Thank You BILLING SYSTEM IS CLOSED")
        break
 else:
        print("New customer:")
        





