# a = "this is a string"
# b = 'this is a string'
# c = 12
# d = 12.5
# e = True
# f = False

# print(a);
# print(b);
# print(c);
# print(d);
# print(e);
# print(f);
# print(type(a));
# print(type(b));
# print(type(c));
# print(type(d));
# print(type(e));
# print(type(f));

# x = int("3")
# y = int(3.5)
# z = float(3)

# print(x);
# print(y);
# print(z);

# result = (x+y)
# print (result);

# x,y,z = "orange", "banana", "cherry"
# print(x);
# print(y);
# print(z);

# x = y = z = "orange"
# print(x);
# print(y);
# print(z);

# fruits = ["apple","banana","cherry"]
# print(fruits)
# print(type(fruits))
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x,y,z)
# print(x+y+z)

# x = 5
# y = 10
# print(x+y)

# x = 5
# y = "john"
# print(x,y)
# print(x+y)

#Global variables
# def addition():
#     print(1+1)
# print("thanks")
# print addition()

# x = "awesome"
# def myFunc():
#     x = "abcd"
#     print("Python is" , x)

# myFunc()
# print("Python is" ,x)

x = "awesome"
print("python is",x)
def myFunc():
    global x
    print("Python is",x)
    x = "fantastic"
    print("Python is",x)

myFunc()
print ("Python is",x)