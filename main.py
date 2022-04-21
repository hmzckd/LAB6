user_number = int(input("Please enter a number:"))
new_list = []
n = 1
equation = lambda x: (x - 3) / (x * x)
while n <= user_number:
    new_list.append(equation(n))
    n = n + 1
print(sum(new_list))

x = 1


def calc(n):
    global x
    if n == 0:
        return 1
    else:
        x = x * (n / (n + 2) - 10)
        print(x)
        return x * calc(n - 1)


calc(2)
