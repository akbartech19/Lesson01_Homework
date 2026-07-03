def mashq(*args, **kwargs):
    print("Oddiy argumentlar:")
    for arg in args:
        print(arg)

    print("\nKalit-qiymatli argumentlar:")
    for kalit, qiymat in kwargs.items():
        print(f"{kalit}: {qiymat}")

mashq(
    "Python",
    "Dasturlash",
    2026,
    ism="Akbar",
    yosh=17,
    shahar="Samarqand"
)