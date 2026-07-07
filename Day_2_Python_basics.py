# Python Basics Practice Assignment

# ---------------- Dictionary (5 Methods) ----------------
employee = {"id": 101, "name": "Rahul"}

employee["department"] = "IT"
print(employee)

print(employee.get("name"))

print(employee.keys())

print(employee.values())

employee.pop("id")
print(employee)

# ---------------- List (5 Methods) ----------------
fruits = ["Apple", "Banana", "Orange"]

fruits.append("Mango")
print(fruits)

fruits.extend(["Grapes"])
print(fruits)

fruits.insert(2, "Kiwi")
print(fruits)

fruits.remove("Banana")
print(fruits)

fruits.reverse()
print(fruits)

# ---------------- Tuple (5 Methods) ----------------
marks = (85, 90, 78, 90)

print(marks.count(90))
print(marks.index(78))
print(len(marks))
print(max(marks))
print(min(marks))

# ---------------- Set (5 Methods) ----------------
colors = {"Red", "Blue", "Green"}

colors.add("Yellow")
print(colors)

colors.update(["Black", "White"])
print(colors)

colors.discard("Pink")
print(colors)

colors.remove("Blue")
print(colors)

print(colors.copy())

# ---------------- If ----------------
temperature = 35
if temperature > 30:
    print("Hot Weather")

# ---------------- If Else ----------------
age = 16
if age >= 18:
    print("Can Vote")
else:
    print("Cannot Vote")

# ---------------- If Elif Else ----------------
score = 48
if score >= 75:
    print("Distinction")
elif score >= 35:
    print("Pass")
else:
    print("Fail")

# ---------------- Nested If Else ----------------
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid User")

# ---------------- Break ----------------
for i in range(10):
    if i == 6:
        break
    print(i)

# ---------------- Continue ----------------
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print(i)

# ---------------- Pass ----------------
for letter in "Python":
    if letter == "h":
        pass
    print(letter)

# ---------------- Input ----------------
city = input("Enter your city: ")
print("Welcome from", city)

# ---------------- Range ----------------
for num in range(3, 8):
    print(num)

# ---------------- Len ----------------
message = "Programming"
print(len(message))

# ---------------- Type ----------------
price = 199.99
print(type(price))

# ---------------- For Loop ----------------
for fruit in fruits:
    print(fruit)

# ---------------- While Loop ----------------
num = 5
while num >= 1:
    print(num)
    num -= 1
