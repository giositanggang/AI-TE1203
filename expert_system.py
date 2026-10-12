def expert_system():
    print("=== EXPERT SYSTEM ===")
    print("Sistem Pakar Pemeriksaan Awal Komputer")

    power = input("Apakah komputer menyala? (ya/tidak): ").strip().lower()

    if power == "tidak":
        print("Rekomendasi: periksa kabel daya, stopkontak,")
        print("dan sambungan adaptor.")
        return
    elif power != "ya":
        print("Input tidak valid.")
        return

    display = input("Apakah layar menampilkan gambar? (ya/tidak): ").strip().lower()

    if display == "tidak":
        print("Rekomendasi: periksa kabel monitor,")
        print("sumber input, dan koneksi layar.")
        return
    elif display != "ya":
        print("Input tidak valid.")
        return

    slow = input("Apakah komputer terasa lambat? (ya/tidak): ").strip().lower()

    if slow == "ya":
        print("Rekomendasi: periksa penggunaan CPU dan RAM,")
        print("aplikasi berjalan, serta ruang penyimpanan.")
    elif slow == "tidak":
        print("Kesimpulan: tidak ditemukan gejala utama")
        print("dari pemeriksaan sederhana ini.")
    else:
        print("Input tidak valid.")

if __name__ == "__main__":
    expert_system()
