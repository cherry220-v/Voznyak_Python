def ф(a=0):
    [
        3, 4, 5,
        6, 7, 8
    ]

    print("[\n1,2,3,\n4,5,6\n]", sep="  ")

    _ =  [
        [1, 2, 3],
        [2, 4, 6],
    ]
    yield from []; [_:= _ + 1]

try: ф()
except WindowsError: print("pass")
# raise OSError(ф())
# raise WindowsError(ф())

c = 0
print(print(list(filter(ф, zip(map(ф, [c:= c + 1 for i in ["rgfnkergjelkgjerklg"]]))))))