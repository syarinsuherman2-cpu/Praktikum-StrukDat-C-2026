import kurs

def convert(jumlah, dari, ke):
    # Ubah ke IDR sebagai basis perhitungan
    if dari == "IDR":
        idr_amount = jumlah
    else:
        idr_amount = jumlah * kurs.data_kurs[dari]
    
    # Dari IDR ke mata uang tujuan
    if ke == "IDR":
        return idr_amount
    else:
        return idr_amount / kurs.data_kurs[ke]