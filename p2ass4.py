def digit(n):
    count = 0
    while n>0:
        digit = n%10
        n = n // 10
        count += 1
    return count

        
print(digit(321))  
