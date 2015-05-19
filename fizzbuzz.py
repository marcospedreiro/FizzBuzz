

print("FizzBuzz: ")
fb = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0: #  i % 15 == 0:  #  more efficient with only one boolean check
        fb.append("FizzBuzz:" + str(i))
        # print("FizzBuzz")
    elif i % 3 == 0:
        fb.append("Fizz:" + str(i))
        # print("Fizz")
    elif i % 5 == 0:
        fb.append("Buzz:" + str(i))
        # print("Buzz")
    else:
        fb.append(str(i))
        # print(i)
print(fb)


print("FizzBuzz no modulo: ")
fbnm = []
for i in range(1, 101):
    div3 = i/3.0 - i/3 == 0
    div5 = i/5.0 - i/5 == 0
    if div3 and div5:
        fbnm.append("FizzBuzz:" + str(i))
        # print("FizzBuzz:" + str(i))
    elif div3:
        fbnm.append("Fizz:" + str(i))
        # print("Fizz:" + str(i))
    elif div5:
        fbnm.append("Buzz:" + str(i))
        # print("Buzz:" + str(i))
    else:
        fbnm.append(str(i))
        # print(str(i))
print(fbnm)