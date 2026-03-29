# Optimized GCD 
def gcd(x,y):
    cf = []
    for i in range(1, min(x,y)+1):
        if x % i == 0 and y % i == 0:
            cf.append(i)
    return cf[-1] # or return max(cf)
print(gcd(int(input()), int(input())))


# A little more optimized version by eliminating the lists:
def optimized_gcd(a, b):
    gcd_value = 1
    for i in range(2, min(a,b)):
        if a % i == 0 and b % i == 0:
            gcd_value = i
    return gcd_value
print(optimized_gcd(int(input()), int(input())))