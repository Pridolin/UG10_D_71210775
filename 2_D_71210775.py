#input data
a = int(input("Nilai a : "))
b = int(input("Nilai b : "))
c = int(input("Nilai c : "))
d = b**2 - 4 * a * c

x1 = ( -b + d / 2 ) / 2 * a
x2 = ( -b - d / 2 ) / 2 * a

if d < 0 :
    print("Fungsi tersebut tidak memiliki akar riil)")
elif d > 0 :
    print("Akar akar dari persamaan tersebut adalah ",x2,x1 )
elif d == 0 :
    print("Fungsi tersebut memiliki akar kembar yaitu ",x1 )

