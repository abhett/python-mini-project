import random

def main():
    print("=======================================")
    print("   SELAMAT DATANG DI DOCKER GAME! 🐳   ")
    print("=======================================")
    print("Saya memikirkan angka antara 1 sampai 10.")
    
    angka_rahasia = random.randint(1, 10)
    tebakan = 0
    
    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Tebakan Anda: "))
            
            if tebakan < angka_rahasia:
                print("Terlalu rendah! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"BENAR! Angkanya adalah {angka_rahasia}. Kamu menang!")
        except ValueError:
            print("Masukkan angka woi!")

if __name__ == "__main__":
    main()