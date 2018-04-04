def test():
    fs =[]
    for i in range(6):
        def func(j):
            return j * i
        fs.append(func)
    return fs


print([f(3) for f in test()])