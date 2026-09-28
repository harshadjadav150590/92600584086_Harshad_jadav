x = 10

def outer():
    y = 20

    def inner():
        nonlocal y
        y = 30
        print("Nonlocal:", y)

    inner()

    def local():
        z = 40
        print("Local:", z)

    local()

print("Global:", x)

outer()
