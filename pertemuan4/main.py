import kurs
import konverter
from tabulate import tabulate
from colorama import Fore, init

init(autoreset=True)

def main():
    print(Fore.CYAN + "=== KONVERTER MATA UANG ===")
    
    # Ambil data dari kurs.py
    data_tabel = [[k, f"{v:,}"] for k, v in kurs.data_kurs.items()]
    
    # Tampilkan tabel (Pastikan baris ini sejajar dengan data_tabel di atasnya)
    print(tabulate(data_tabel, headers=["Kode", "Kurs"], tablefmt="grid"))

    try:
        dari = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
        ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
        jumlah = float(input("Jumlah: "))

        hasil = konverter.convert(jumlah, dari, ke)
        
        if dari == "IDR":
            print(f"\nRp {jumlah:,.0f} = {hasil:.2f} {ke}")
        else:
            print(f"\n{jumlah} {dari} = Rp {hasil:,.2f}")
            
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    main()