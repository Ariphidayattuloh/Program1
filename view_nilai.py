from model.daftar_nilai import data

def header():
    print("|==========================================================================|")
    print("|==================== PROGRAM INPUT DATA MAHASISWA ========================|")
    print("|==========================================================================|")
    print("| NO |   NAMA         |     NIM    |  TUGAS   |  UTS  |   UAS  |   AKHIR   |")
    print("|--------------------------------------------------------------------------|")
    print("| 1  | ARIP HIDAYAT   |  312010244 |   78     |   89  |    98  |    89     |")
    print("| 2  | GUNAWAN        |  312010191 |   76     |   86  |    84  |    76     |")
    print("| 3  | DIFA WIJAYA    |  312010024 |   86     |   82  |    87  |    94     |")
    print("|==========================================================================|")


def notoption():
    print("|==========================|")
    print("| Pilih opsi yang tersedia |")
    print("|==========================|")
    print("     NAMA       NIM      TUGAS     UTS      UAS     AKHIR  ")


def cetak():
    print("\n|=========================================================================|")
    print("|========================= DAFTAR DATA MAHASISWA =========================|")
    print("|=========================================================================|")
    print("| |")
    print("|=========================================================================|")
    no = 1
    for tabel in data.values():
        print("|{0:3} | {1:15} | {2:16} | {3:5} | {4:5} | {5:5} | {6:5} |"
              .format(no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
        no += 1
    print("|=========================================================================|")
    print("\n    NAMA       NIM      TUGAS     UTS      UAS     AKHIR   ")


def nyari():
    from view.input_nilai import cari
    cari()
    print("  NAMA       NIM      TUGAS     UTS      UAS     AKHIR     ")