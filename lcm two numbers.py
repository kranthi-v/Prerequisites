def lcm(a, b):
    
    # Larger value
    #checking multiplies
    g = max(a, b) 
    
    # Smaller value
    s = min(a, b)  

    # a*b? bcoz lcm always <= a*b
    for i in range(g, a * b + 1, g):
        if i % s == 0:
            return i
    return a * b 

#the below code is run only when this file is excuted directly, not when imported
if __name__ == '__main__':
    a = 10
    b = 5
    print(lcm(a, b))