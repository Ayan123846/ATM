class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your current balance is : S.R. 2394580")

    def withdrawl1(self,money):
        new_amount = 2394580 - money
        print("You have successfully withdrawl amount "+str(money) + ". Your remaining balance is "+ str(new_amount))   


def main():
    print("Welcome to Fransi Bank of Saudi Arabia!!")
    print("Our Respected Chief Executive Officer : Mohd. Ayan")
    print("Our Respected Chief Operating Officer : Rahat Shaikh")
    Account = input("Please enter your account number:  ")
    Card_number = input("Please enter your card number: ")
    pin_number  = input("Please enter your pin: ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("What do you want to do?")
    print("1.  Check your bank balance ")
    print("2.  Withdrawl Money ")
    activity = int(input("Choose your want number : "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
           money = int(input("Please enter the amount you want to withdrawl:  "))
           new_user.withdrawl1(money)
        
           
    else:
        print("The pin is not valid. Please enter a valid pin")

if __name__ == "__main__":
    main()