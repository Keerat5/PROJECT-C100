class atm(object):
    def __init__(self,pinNumber,atmNumber):
        self.pinNumber=pinNumber
        self.atmNumber=atmNumber
        self.balance = 0

    def CashDeposit(self):
        amount = int(input("Enter amount to be Deposited: "))
        self.balance = self.balance+amount
        print("The amount has been deposited and the balance in the account is:", amount)

    def CashWithdraw(self):
        amount1 = int(input("Enter amount to be Withdraw: "))
        if(self.balance >= amount1):
            self.balance = self.balance-amount1
            print("The withdrawl is successfull, You Withdrew:", amount1)
        else:
            print('Insufficient balance')
          
    def CashBalanceEnquiry(self):
        print("Net Available Balance=",self.balance)
     
s = atm(1234,98765)
   
s.CashDeposit()
s.CashWithdraw()
s.CashBalanceEnquiry()
