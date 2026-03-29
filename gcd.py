# Optimized GCD 
def gcd(x,y):
    cf = []
    for i in range(1, min(x,y)+1):
        if x % i == 0 and y % i == 0:
            cf.append(i)
    return cf[-1] # or return max(cf)
print(gcd(int(input()), int(input())))