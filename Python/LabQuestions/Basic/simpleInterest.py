num = float(input("Enter Amount: "))
interest = float(input("Enter interest: "))
years = float(input("Enter number of years: "))
simpleInterest = ((num/100)*interest)*years
totalAmouunt = num + simpleInterest
print("The simple interest on",num ,"for" , years,"years at",interest,"% year is" ,simpleInterest)
print("total amount:" , totalAmouunt)