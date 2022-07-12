def sum_of_multiples(n, a, b):
    sum = 0
    for i in range(0, n, 1):

        if (i % a == 0 or i % b == 0):
            sum += i

    return sum

if __name__ == '__main__':
    n = 20
    a = 3
    b = 5
    print(sum_of_multiples(n, a, b))
