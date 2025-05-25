def factorial(n):
    result= 1
    for i in range(1,n+1):
        result = result * i
    return result
input_by_user= 5
print("Factorial of" ,input_by_user ,"is:",factorial(input_by_user))
