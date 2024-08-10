test_var = 'Test 1'
test_var2 = "Test 2"

print(test_var)
print(test_var2)

test_var3 = 'He said "Hello World"'
print(test_var3)

test_var = '\"\''
test_var5 = "Line 1:some text \nLine 2:some text"
print(test_var5)

hi = ''' A comment write some more test 

on another line'''

test_var6 = "copy " * 10
print(hi)
print(test_var6)

name = 'Tom'
age = 40
greeting = "Hello {one}, you are {two} years old".format(one=name, two=age)
print(greeting)
