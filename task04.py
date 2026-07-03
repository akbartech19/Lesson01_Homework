def ortacha(*args):
    if len(args) == 0:
        return 0

    yigindi = 0
    for son in args:
        yigindi += son

    return yigindi / len(args)


print(ortacha(10, 20, 30, 40))