#!"C:\Python27\python.exe"
yn = ["y", "n"]
def showMenu():
    title = """ 
    --------------------------------
    Amy's Auto - Loan Report Menu
    --------------------------------
    """
    loan_opt = ["1: 12-month loan", "2: 24-month loan", "3: 36-month loan", "4: 48-month loan", "5: 60-month loan", "6: EXIT"]

    print(title)
    choice = 10
    while choice > 5: 
         print('\n1. 12-month loan')
         print('2. 24-month loan')
         print('3. 36-month loan')
         print('4. 48-month loan')
         print('5. 60-month loan')
         print('0. EXIT')
         choice = int(input('Choice:'))

    return choice*12
def inputLoanData(): 
        amount = truncate(float(input('Enter loan amount: ')))
        rate = truncate(float(input('Enter annual interest: ')))
  
        return amount, rate
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
   table = [["Payment Amount", pv + balance]]
   return pmtAmt
#   showReport(table) 
def showReport(pv, ratePeriod, numPeriod, pmtAmt):
    print("Pmt#\t", "PmtAmt\t", "Int\t", "Princ\t", "Balance\t")
    print("----", "---------","-----", "------", " --------")


        
    for row in range(1,13):
        print(row, end="\t")
        print(truncate(pmtAmt), end="\t")
        
        interest = truncate(pv * ratePeriod)
        print(interest, end="\t")
         

        print(truncate((pmtAmt - interest)), end="\t")

        print(truncate((pv - pmtAmt)), end="\n")
def truncate(n):
        return round(n, 2)
def main():
        loanAmount, loanInterest = inputLoanData()
        numOfmon = showMenu()
        if numOfmon > 0:
                pmt = payment(loanInterest, numOfmon, loanAmount)
                showReport(loanAmount,(loanInterest / (100*12)), numOfmon, pmt)
main()
