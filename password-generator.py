import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Halo, selamat datang di password generator!")
karakter = int(input("Berapa jumlah karakter yang kamu butuhkan?\n"))
angka = int(input("Berapa jumlah angka yang kamu butuhkan?\n"))
simbol = int(input("Berapa jumlah simbol yang kamu butuhkan?\n"))

password = ""
for x in range (0,karakter):
    letter = random.choice(letters)
    password += letter
for y in range (0,angka):
    kumpulan_angka = random.choice(numbers)
    password += kumpulan_angka
for z in range (0, simbol):
    kumpulan_simbol = random.choice(symbols)
    password += kumpulan_simbol
new_password = list(password)
random.shuffle(new_password)
random_password = (''.join(new_password))
print(f"Password yang dapat kamu gunakan adalah: {random_password}")
