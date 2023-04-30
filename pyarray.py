def maxarray(xs):
    m = xs[0]
    for x in xs:
        if m < x:
            m = x
    return m


data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
t = maxarray(data)
print("[+] Max: " + str(t))

def minarray(xs):
    m = xs[0]
    for x in xs:
        if m > x:
            m = x
    return m

u = minarray(data)
print("[+] Min: " + str(u))