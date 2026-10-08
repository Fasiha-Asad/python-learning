a="5"
b="6" #Output is 56 because both are string
print(a+b)
# for addition write in integer
a=5
b=6
print(a+b)

a="Fasiha"
b="Asad"
print(a+b)
#Typecasting: The conversion of one data type into another data type.
#Take valid values for conversion
a="2"
b="5"
print(int(a)+int(b)) # firstly convert string datatype into into data type  and the print
#Two types of typecasting
#1) Implicit: Python is doing that automatically
c=788
d=7.6       
print(c+d) #Automatically convert in float datatype
#2) Explicit: I am doing it with my own (covert into to string)
string="15"
num=7
string_num=int(string)
sum=num+string_num
print("Sum of both number is:",sum)
