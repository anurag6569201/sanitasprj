def mult(a, b):
    print(a, b) 
    if b == 1:
        return a
    else:
        return a + mult(a, b-1) # mult(4,1)==4
    
print(mult(4,5))