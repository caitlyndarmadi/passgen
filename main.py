#import random

#chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#random_string = ""
#x = int(input("Mau berapa password?"))
#for i in range(x):
    #random_string += random.choice(chars)
#print(random_string)

import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_gombalan():
    list_gombal = [
        "Kamu tahu bedanya kamu sama bintang? Bintang di langit, kalau kamu di hatiku ♡",
        "Rasa sayang aku kepadamu seperti kuku, walaupun dipotong, tetap bakal tumbuh terus ♡",
        "Kalau aku menjadi superhero, aku tahu bakal jadi apa. Jadi YourMan ♡",
        "Kamu tahu gak nama asliku Dion. Dionly man for you ♡",
        "Kamu tahu bedanya Borobudur sama kamu? Kalau Borobudur itu candi, kalau kamu bikin candu ♡",
        "Kamu tahu bedanya kamu sama jam 12? Kalau jam 12 kesiangan kalau kamu kesayanganku ♡",
    ]

    return random.choice(list_gombal)

def transportasi():
    list_transportasi = [
        "Bersepeda atau jalan kaki jika tempat yang akan ditempui berjarak dekat denganmu",
        "Mulai menggunakan kendaraan listrik seperti mobil listrik dan motor listrik",
        "Gunakanlah transportasi umum seperti bis dan angkot untuk mengurangi emisi karbon",
    ]

    return random.choice(list_transportasi)

def mengurangi():
    list_mengurangi = [
        "Gunakanlah botol yang dapat digunakan lebih dari sekali seperti botol tumbler dan botol untuk menggantikan botol plastik sekali pakai",
        "Gunakanlah tas belanja tote bag atau paper bag untuk mengurangi penggunaan plastik",
        "Gunakanlah sedotan berbahan besi untuk mengurangi penggunaan sedotan plastik",
     ]

    return random.choice(list_mengurangi)

def menghemat():
    list_menghemat = [
        "Matikanlah lampu dan alat lain yang menggunakan listrik seperti TV atau AC saat tidak digunakan",
        "Tutuplah keran jika sudah selesai digunakan untuk menghemat air",
        "Gunakanlah air dan listrik secukupnya dan sesuai dengan kebutuhanmu",
     ]

    return random.choice(list_menghemat)

