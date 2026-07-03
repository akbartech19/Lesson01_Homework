def eng_katta(*args):
    katta = args[0]

    for son in args:
        if son > katta:
            katta = son

    return katta

print(eng_katta(5, 8, 2, 10, 7))