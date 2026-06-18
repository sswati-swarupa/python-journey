def digit(n):
    sum = 0
    while n>0:
        digit = n%10
        sum = sum + digit
        n = n//10
    return sum
       
print(digit(3421))