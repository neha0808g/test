def difference(n):
    squareofsum=(n*(n+1)*(2*n+1))/6

    sumofsquares=(n*(n+1))/2

    sumofsquares=sumofsquares**2

    diff=abs(squareofsum-sumofsquares)

    return diff

print(difference(5))