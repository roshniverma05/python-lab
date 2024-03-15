#que 02) LOGICAL AND RELATIONAL OPERATORS
person1=int(input("enter your age :"))
person2=int(input("enter your age :"))
if(person1>person2 and person1>=18):
 print("person 1 is greater than person 2 and person 1 is considered as an adult and person 2 as a child")
elif(person2>person1 and person2>=18):
 print("person 1 is smaller than person 2 and person 2 is considered as an adult and person 1 and is considered as a child")
elif(person1>18 and person2>18):

 print("both are comsidrerd as a child")
 


