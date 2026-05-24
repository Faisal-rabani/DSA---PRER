# Recursion Function 

def factorial(n):

    counts =0

 

    # Base case7
    if n==0 or n==1:
        return 1
    
    # Recursive case
    # The function calll itself 
    return n * factorial(n-1)

# Calling function
print(factorial(5)) # 120

