#input data
a = int(input("harga makanan sebesar Rp: "))
b = int(input("harga snack sebesar Rp: "))
c = int(input("harga minuman sebesar Rp: "))
d = int(input("uang yang anda bawa sebesar Rp: "))
print("total yang harus anda bayar sebesar Rp",a+b+c)

if (d == a+b+c):
    print("uang anda pas! tidak ada kembalian dan utang :D")
elif (d < a+b+c):
    print("uang anda kurang! anda memiliki utang sebesar Rp",(a+b+c)-d)
else:
    (d > a+b+c)
    print("anda memiliki kembalian sebesar Rp",d-(a+b+c))
    