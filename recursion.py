def out_recursion(n):
    if n ==1:
        return 1
    else:
        return n * out_recursion(n-1)
n=int(input("Input a number to compute the factiorial : "))
print("The results "+ str(out_recursion(n)))