# Factorial calculator
def fact(n):
    result = 1
    if n < 0:
        print('Enter a +ve number!')
    elif n == 0:
        return 1
    elif n > 0:
        for i in range(n, 1, -1):
            result = result * i
        return result


n = int(input('Enter a number: '))
print('factorila: ', fact(n))
