x=int(input("enter a year: "))

if((x%400==0) or ((x%4==0 and x%100!=0))):
 print(x ,"entered year is a leap year")

else:
  print(x ,"entered year is not a leap year")