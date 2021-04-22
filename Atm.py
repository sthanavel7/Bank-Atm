class Atm:
    def __init__(self,cardno,pin):
        self.cardno = cardno
        self.pin = pin

    def check_balance(self):
        print("Your balance is 10000")

    def withdrawl(self,amount):
        if amount <= 10000:
            print("More money required")
            
        else:
            new_amount = 10000 - amount
            print("you have withdrawn  "+str(amount) +". your remaining balance is "+ str(new_amount))

            
        

def main():
    Card_no = input("enter your card number:- ")
    pin_no = input("enter your pin number:- ")

    new_user =  Atm(Card_no ,pin_no)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity no :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid nnumber")


if __name__ == "__main__":
    main()

