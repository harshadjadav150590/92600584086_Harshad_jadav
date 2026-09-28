def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for i in numbers():
    print(i)
