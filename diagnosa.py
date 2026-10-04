from main import settings

req_secret = 'WGcmtmMRKcXjCiv6QFpCnpKMpsxAtdJKRwXsQoi45ec'
settings_secret = settings.client_secret

print("=" * 70)
print("PANJANG STRING:")
print(f"  Yang dikirim (req)        : {len(req_secret)} karakter")
print(f"  Yang dibaca server (env)  : {len(settings_secret)} karakter")
print()

if len(req_secret) != len(settings_secret):
    print(">>> PANJANG BEDA! Ada karakter ekstra.")
    if len(settings_secret) > len(req_secret):
        print(">>> Ekstra di .env:", repr(settings_secret[len(req_secret):]))
    else:
        print(">>> Ekstra di req :", repr(req_secret[len(settings_secret):]))
    print()

print("=" * 70)
print("PERBANDINGAN KARAKTER PER KARAKTER:")
print(f"{'Pos':>4} | {'req':^8} | {'kode':>6} | {'env':^8} | {'kode':>6} | Status")
print("-" * 70)

max_len = max(len(req_secret), len(settings_secret))
beda_ditemukan = False

for i in range(max_len):
    a = req_secret[i] if i < len(req_secret) else '<kosong>'
    b = settings_secret[i] if i < len(settings_secret) else '<kosong>'
    kode_a = ord(a) if len(a) == 1 else '-'
    kode_b = ord(b) if len(b) == 1 else '-'
    
    if a != b:
        status = "  <<< BEDA!"
        beda_ditemukan = True
    else:
        status = ""
    
    print(f"{i:>4} | {a!r:>8} | {kode_a:>6} | {b!r:>8} | {kode_b:>6} |{status}")

print("=" * 70)
if not beda_ditemukan:
    print("Semua karakter terlihat SAMA, tapi tetap False?")
    print("Kemungkinan masalah encoding (Unicode vs UTF-8) di .env.")
else:
    print(">>> Ketemu posisi yang beda! Lihat baris dengan '<<< BEDA!'")