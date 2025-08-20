import random

var = "234"
print(int(var))

# bentuk_goa = "|_|"
# goa = bentuk_goa * 4

# print(f"goa 1 {goa}" )
#4 goa tersebut itu string bukan array

#kita butuh array agar bisa di ubah dengan mudah dalammnya nanti

# goa = [bentuk_goa] * 4
# print(f"goa 2 {goa}" )

# goa_cuypy = "|0_^|"
# goa[2] = goa_cuypy
# print(f"goa 3  {goa}")

bentuk_goa = "|_|"
goa = [bentuk_goa] * 4

goa_kosong = goa.copy()
goa_kosong[2] = "|0_^|"


print(goa)
print(goa_kosong)


