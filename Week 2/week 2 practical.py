total = 100
print("The total is", total)
total = total + 99
print("The total is now", total)
total -= 1
print("The total is", total)
total *= 4
print("The total is", total)
total /= 2
print("The total is", total)
total = 98.2
code = 5
total /= 5
print("the average is", total)
value = False
value_type = type(value)
print(value_type)
value = 1000
value_type = type(value)
print(value_type)
value = 100.111
value_type = type(value)
print(value_type)
value = "Hello"
value_type = type(value)
print(value_type)
value = True
value_type = type(value)
print(value_type)
value = 100/5
value_type = type(value)
print(value_type)
value = 100//5
value_type = type(value)
print(value_type)
print(10 + 10)
print("10" + "10")
print("ABC" * 10)
name = "Bilaal"
address = "Headingley Campus, City, Leeds"
contact_details = "Name123@gmail.com"

print("name:", name)
print("address:", address)
print("contact Details:", contact_details)
name_length =len(name)
print("The length of your name is:", name_length)
age = input("Enter your age ")
age = int(age)
print("in one year your will be", age + 1)
Value1 = input ("Enter value 1 ")
Value2 = input ("Enter value 2")
Value1 = int(Value1)
Value2 =int(Value2)
print (Value1 * Value2)
comment = ("I would have 'thought' you knew better!")
print (comment)
text = ("This text includes characters such as '\\', '\"' and \"'\"")
text += ("\nThis is a new line that starts with a tab")
text += ("\n\tThis new line starts with two tabs")
print(text)
print ("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Hello there! \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ")
print("""This text spans three lines,
and includes both single('),
and double quotes(").""")

surname = "Palin"
initial = surname [2]
print (initial)

surname = "palin"
last = surname[-2]
print (last)

surname = "Palin"
middle = surname[1:5]
print (middle)

surname = "Palin"
Except_last = surname [:-1]
print (Except_last)

primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
First_four = primes [:4]
print (First_four)

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
names [6:0] = ["tim", "Bill"]
print (names)