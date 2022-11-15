ascii_code = ord(" ")
print("ASCII number dari spasi : " + str(ascii_code))
data = 117
print("Character dari ascii code 117 : " + chr(data))
# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o di " + data + " : " + str(jumlah))
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)
# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)
# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)
# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)
# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)
# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)
# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)