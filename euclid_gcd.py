# Recursion without loop
def euclid_gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        diff = a - b
        return euclid_gcd(max(b, diff), min(b, diff))
print(euclid_gcd(int(input()), int(input())))

# Recursion with while loop 
def euclid_While_gcd(a, b):
    if a < b:
        a, b = b, a
    while(a % b) != 0:
        diff = a - b
        a, b = max(b, diff), min(b, diff)
    return b
print(euclid_While_gcd(int(input()), int(input())))

# Even better 
def euclid_original(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return euclid_original(b, a % b)
print(euclid_original(int(input()), int(input())))

# while loop:
def euclid_original_while(a, b):
    if a < b:
        a, b = b, a
    while (a % b) != 0:
        a, b = b, a % b
    return b