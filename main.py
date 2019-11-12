#!"C:\Python27\python.exe"
# Import the necessary packages
#from consolemenu import *
#from consolemenu.items import *     
from pimento import menu
from tabulate import tabulate
import qprompt
#global amount
#global rate
yn = ["y", "n"]
def showMenu(amount, rate):
        title = """ 
        --------------------------------
        Amy's Auto - Loan Report Menu
        --------------------------------
        """
        loan_opt = ["1: 12-month loan", "2: 24-month loan", "3: 36-month loan", "4: 48-month loan", "5: 60-month loan", "6: EXIT"]

        print(title)
        result = menu(loan_opt)
        if len(loan_opt) == result: 
                exit()
        payment(rate, int(result[:1]), amount) 
 #      print(result)
def inputLoanData(): 
        amount = truncate(float(qprompt.ask_str("Enter loan amount:", blk=False)))
        rate = truncate(float(qprompt.ask_str("Enter annual interest rate:", blk=False)))
        print("Continue? Y/N")
        result = menu(yn)
        if (result == 1): 
               exit()
        else:
               showMenu(amount, rate)
def payment(rate, o, pv):
   p = 0
   try:
       r = rate / 100
       n = o * 12
       top = r * pv
       bottom = 1 - ((1 + r) ** -n)
       p = truncate(top / bottom)
   except:
       p = 0 
       #   print(p)
   pmtAmt = p
   intAmt = r * pv
   balance = pv - pmtAmt
   price = pmtAmt - intAmt
#      table = []
#       payments = []
#       ints = [p]
#       price = [pv]
#       balance = [pv]
#       payment_amount = [pv]
#       for i in range(n):
#                payments.append(i)
#                payment_amount.append(price[len(price) - 1] + ints[len(ints) - 1])

#       table = [["Payment \#:", payments], ["Payment Amount: ", payment_amount]]
       #               print(payments, payment_amount)
#       table = [["pmtAmt", pmtAmt], ["intAmt",intAmt] , ["balance", balance], ["price", price], ["total", pv + balance] ]
   table = [["Payment Amount", pv + balance]]
   result = menu(yn)
   if (result == 1): 
       exit()
   else:
       showReport(table) 
def showReport(table):
        print("")
        print(tabulate(table))
        result = menu(yn)
        print("Would you like to restart")
        if (result == 1):
               exit()
        else:
               inputLoanData()
def truncate(n):
        return round(n, 2)
def main():
        inputLoanData()
main()
