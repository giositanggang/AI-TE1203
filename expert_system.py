# =====================================================
# SISTEM PAKAR PEMERIKSAAN AWAL KOMPUTER (Rule-Based)
# =====================================================

PERTANYAAN = [
    {"fakta": "menyala", "teks": "Apakah komputer menyala?",
     "syarat": {}},
    {"fakta": "layar", "teks": "Apakah layar menampilkan gambar?",
     "syarat": {"menyala": True}},
    {"fakta": "lambat", "teks": "Apakah komputer terasa lambat?",
     "syarat": {"menyala": True, "layar": True}},
    {"fakta": "panas", "teks": "Apakah komputer cepat panas atau kipas bising?",
     "syarat": {"menyala": True, "layar": True}},
]

# Aturan IF-THEN
ATURAN = [
    {"id": "R1",
     "jika": {"menyala": False},
     "maka": "Masalah daya listrik",
     "saran": "Periksa kabel daya, stopkontak, dan sambungan adaptor."},
    {"id": "R2",
     "jika": {"menyala": True, "layar": False},
     "maka": "Masalah tampilan",
     "saran": "Periksa kabel monitor, sumber input, dan koneksi layar."},
    {"id": "R3",
     "jika": {"menyala": True, "layar": True, "lambat": True},
     "maka": "Performa menurun",
     "saran": "Periksa penggunaan CPU dan RAM, aplikasi yang berjalan, "
              "serta ruang penyimpanan."},
    {"id": "R4",
     "jika": {"menyala": True, "layar": True, "panas": True},
     "maka": "Masalah pendinginan",
     "saran": "Bersihkan debu pada kipas dan ventilasi, "
              "serta periksa pasta termal prosesor."},
]

NAMA_FAKTA = {
    "menyala": "komputer menyala",
    "layar": "layar menampilkan gambar",
    "lambat": "komputer terasa lambat",
    "panas": "komputer cepat panas / kipas bising",
}


# ---------- 2. MESIN INFERENSI (Forward Chaining) ----------
def syarat_terpenuhi(syarat, fakta):
    return all(fakta.get(k) == v for k, v in syarat.items())


def inferensi(fakta):
    """Mencocokkan semua aturan dengan fakta yang diketahui."""
    return [a for a in ATURAN if syarat_terpenuhi(a["jika"], fakta)]


# ---------- 3. ANTARMUKA PENGGUNA ----------
def tanya_ya_tidak(teks):
    while True:
        jawab = input(f"{teks} (ya/tidak): ").strip().lower()
        if jawab in ("ya", "y"):
            return True
        if jawab in ("tidak", "t"):
            return False
        print("Input tidak valid, jawab dengan 'ya' atau 'tidak'.")


def kumpulkan_fakta():
    fakta = {}
    for p in PERTANYAAN:
        if syarat_terpenuhi(p["syarat"], fakta):
            fakta[p["fakta"]] = tanya_ya_tidak(p["teks"])
    return fakta


# ---------- 4. FASILITAS PENJELASAN ----------
def jelaskan(aturan):
    alasan = ", ".join(
        f"{NAMA_FAKTA[k]} = {'ya' if v else 'tidak'}"
        for k, v in aturan["jika"].items()
    )
    return f"Karena: {alasan}"


def tampilkan_hasil(hasil):
    print("\n=== HASIL DIAGNOSIS ===")
    if not hasil:
        print("Tidak ditemukan gejala utama dari pemeriksaan sederhana ini.")
        return
    for i, a in enumerate(hasil, 1):
        print(f"\n{i}. {a['maka']} (aturan {a['id']})")
        print(f"   Saran   : {a['saran']}")
        print(f"   {jelaskan(a)}")


# ---------- PROGRAM UTAMA ----------
def expert_system():
    print("=== EXPERT SYSTEM ===")
    print("Sistem Pakar Pemeriksaan Awal Komputer\n")
    fakta = kumpulkan_fakta()
    hasil = inferensi(fakta)
    tampilkan_hasil(hasil)


if __name__ == "__main__":
    expert_system()
