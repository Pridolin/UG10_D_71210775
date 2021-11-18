#input data
a = int(input("Masukkan bilangan 1 : "))
b = int(input("Masukkan bilangan 2 : "))
c = int(input("Masukkan bilangan 3 : "))

if a >= b and a >= c and b >= c :
    print("Urutan bilangan dari yang terbesar adalah ", a, b, c)
elif b >= a and b >= c and c >= a :
    print("Urutan bilangan dari yang terbesar adalah ", b, c, a)
elif b >= a and b >= c and c >= a :
    print("Urutan bilangan dari yang terbesar adalah ", b, a, c)
elif c >= a and c >= b and b >= a :
    print("Urutan bilangan dari yang terbesar adalah ", c, b, a)
    