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
