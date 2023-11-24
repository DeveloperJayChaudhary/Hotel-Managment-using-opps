class HotelManage():

    def __init__(self,name='',address='',checkin='',checkout='',roombill=0,laundaryBill=0,gameBill=0,roomNumber=101,foodbill=0,add=1800):
        self.name=name
        self.address=address
        self.checkin=checkin
        self.checkout=checkout
        self.roombill=roombill
        self.laundaryBill=laundaryBill
        self.gameBill=gameBill
        self.foodbill=foodbill
        self.roomNumber=roomNumber
        self.add=add

        
    def customer_data(self):
        self.name=input("\nEnter the Name: ")
        self.address=input("\nEnter the Address: ")
        self.checkin=input("\nEnter your Check in Date: ")
        self.checkout=input("\nEnter your Check out Date: ")
        print("Your Room Number is ",self.roomNumber)
        

    def roomtype(self):
        self.room=input("We have the following rooms for you :-\n1.  Type A---->rs 6000 PN\-  \n2.  Type B---->rs 5000 PN\- \n3.  Type c---->rs 4000 PN\- \n4.  Type A---->rs 3000 PN\- \nEnter Your Choice Please->  ")
        self.nights=int(input("For How Many nights Did you want to stay : "))

        if self.room=="1":
            self.roombill=6000*self.nights
            print("You Have Opted room Type A \nYour room rent is=",self.roombill)
        elif self.room=="2":
            self.roombill=5000*self.nights
            print("You Have Opted room Type B \nYour room rent is=",self.roombill)

        elif self.room=="3":
            self.roombill=4000*self.nights
            print("You Have Opted room Type C \nYour room rent is=",self.roombill)

        elif self.room=="4":
            self.roombill=3000*self.nights
            print("You Have Opted room Type D \nYour room rent is=",self.roombill)
        else:
            print("Worng input")

            
    def restaurant(self):
        print("**** Restaurant Menu **** \n1.Water---->Rs20  \n2.Tea---->Rs10 \n3.Breakfast combo---->Rs90 \n4.Lunch---->Rs110 \n5.Dinner---->Rs150\n6.Exit \n")
        while(1):
            self.a=input("Enter your Choice: ")

            if self.a=="1":
                self.b=int(input("Enter your Quantity: "))
                self.foodbill=self.foodbill+20*self.b
            elif self.a=="2":
                self.b=int(input("Enter your Quantity: "))
                self.foodbill=self.foodbill+10*self.b
            elif self.a=="3":
                self.b=int(input("Enter your Quantity: "))
                self.foodbill=self.foodbill+90*self.b
            elif self.a=="4":
                self.b=int(input("Enter your Quantity: "))
                self.foodbill=self.foodbill+110*self.b
            elif self.a=="5":
                self.b=int(input("Enter your Quantity: "))
                self.foodbill=self.foodbill+150*self.b
            elif self.a=="6":
                break
            else:
                print("Wrong Input")
        print("Total Food Cost: ",self.foodbill)
                
    def laundary(self):
        print("*****LAUNDARY MENU*****")
        while(1):
            self.a=input("1.Shorts--->Rs3 \n2.Trousers--->Rs4 \n3.Shirt--->Rs5 \n4.Jeans--->Rs6 \n5.Girlsuit--->Rs8 \n6.Exit\nEnter Your Choice: ")
            if self.a=="1":
                self.b=int(input("Enter the Quantity"))
                self.laundaryBill=self.laundaryBill + 3*self.b
            elif self.a=="2":
                self.b=int(input("Enter the Quantity"))
                self.laundaryBill=self.laundaryBill + 4*self.b
            elif self.a=="3":
                self.b=int(input("Enter the Quantity"))
                self.laundaryBill=self.laundaryBill + 5*self.b
            elif self.a=="4":
                self.b=int(input("Enter the Quantity"))
                self.laundaryBill=self.laundaryBill + 6*self.b
            elif self.a=="5":
                self.b=int(input("Enter the Quantity"))
                self.laundaryBill=self.laundaryBill + 8*self.b
            elif self.a=="6":
                break
            else:
                print("Wrong input")

        print("Your Total Laundary Bill :",self.laundaryBill)

    def game(self):
        print ("****GAME MENU ****")
        while(1):
            self.a=input("1.Table Tennis--->Rs60 \n2.Bowling --->Rs80 \n3.Snooker--->Rs70 \n4.Video Games--->Rs90 5.Pool--->Rs50 \n6.Exit \nEnter your Choice :")
            if self.a=="1":
                self.b=int(input("Enter the Quantity"))
                self.gameBill=self.gameBill + 60*self.b
            elif self.a=="2":
                self.b=int(input("Enter the Quantity"))
                self.gameBill=self.gameBill + 80*self.b
            elif self.a=="3":
                self.b=int(input("Enter the Quantity"))
                self.gameBill=self.gameBill + 70*self.b
            elif self.a=="4":
                self.b=int(input("Enter the Quantity"))
                self.gameBill=self.gameBill + 90*self.b
            elif self.a=="5":
                self.b=int(input("Enter the Quantity"))
                self.gameBill=self.gameBill + 50*self.b
            elif self.a=="6":
                break
            else:
                print("wrong Input")
            
        print("Your Total Game Bill:",self.gameBill)
    def total(self):
        print("**** HOTEL BILL ****")
        print("Customer Details: ")
        print("Customer Name : ",self.name)
        print("Customer Address: ",self.address)
        print("Check in date: ",self.checkin)
        print("Check out date: ",self.checkout)
        print("Room number ",self.roomNumber)
        print("Your room rent is : ",self.roombill)
        print("Your Food bill is : ",self.foodbill)
        print("Your Laundary bill is : ",self.laundaryBill)
        print("Your Game bill is : ",self.gameBill)
        print("Your Total Bill is : ",self.roombill+self.foodbill+self.laundaryBill+self.gameBill)
        print("Additional Service Charges is ",self.add)
        print("Your Grand Total Bill is :",self.roombill+self.foodbill+self.laundaryBill+self.gameBill+self.add)


def main():
    obj=HotelManage()
    while(True):
        input1=input("\n\n******** WELCOME TO RADISSON BLUE HOTEL ******** \n1.Enter the Customer Data \n2.Calculate Room Rent \n3.Calculate Restaurant Bill \n4.Calculate laundary Bill \n5.Calculate Game Bill \n6.Show Total Cost \n7.Exit \n")
        if input1=="1":
            obj.customer_data()
        elif input1=="2":
            obj.roomtype()
        elif input1=="3":
            obj.restaurant()
        elif input1=="4":
            obj.laundary()
        elif input1=="5":
            obj.game()
        elif input1=="6":
            obj.total()
        elif input1=="7":
            quit()
        else:
            print("Wrong Input")

main()
