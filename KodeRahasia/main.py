import random
from libs import nagi
def generate_code(length):
    charakter = 'qwertyuiopasdfghjklzxcvbnm123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    code = '' . join(random.choice(charakter) for _ in range(length))
    return code

 
def main():
    pilihan = input("Mau generate Kode? y/n: ")
    if pilihan == 'y':
        while True :
            try :
                length = int(input("Masukan panjang kodenya: "))
                generated_code = generate_code(length)
                print(f"kode yang dihasilkan: {generated_code}")
                break
            except ValueError:
                print("Masukan angka bukan huruf")
    if pilihan == 'n':
        nagi()

if __name__ == "__main__":
    main()