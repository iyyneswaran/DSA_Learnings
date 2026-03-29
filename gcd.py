#  Minimally Optimized GCD 
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

# optimizing the GCD further by backward iteration:
def gcd_god(c, d):
    mgcd = 1
    for i in range(min(c, d), 1, -1):
        if c % i == 0 and d % i == 0:
            mgcd = i
            break
    return mgcd
print(gcd_god(int(input()), int(input())))

# GCD using while loop 
def gcd_whileLoop(m, n):
    i = min(m, n)
    while i > 0:
        if m % i == 0 and n % i == 0:
            return i
        else:
            i = i - 1
print(gcd_whileLoop(int(input()), int(input())))