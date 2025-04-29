# 🧰 Bot Bulk Wallet EVM Generator

Bot ini ngebantu kamu buat generate banyak wallet EVM (Ethereum Virtual Machine) secara massal. Bisa langsung bikin ratusan sampai ribuan wallet dalam satu kali jalanin script.

---

## ⚙️ Fitur
- 🪪 Generate wallet EVM (address & private key)
- 📄 Output disimpan ke file `addresses.txt` dan `privatekeys.txt`
- 🧵 Bisa generate banyak wallet sekaligus (bulk)
- ⏱️ Proses cepat dan efisien
- 🔐 Gak konek ke jaringan apapun, semuanya lokal

---

## 📦 Cara Install

1. **Clone repo-nya**
```bash
git clone https://github.com/kamu/bot-bulk-wallet-evm.git
cd bot-bulk-wallet-evm
```


## ▶️ Cara Jalanin Bot

```bash
python buat_wallet.py
```

Kamu bakal ditanya mau bikin berapa wallet. Setelah selesai, hasilnya otomatis disimpan ke dua file:
- `addresses.txt` → alamat wallet
- `privatekeys.txt` → private key wallet

---

## 📁 Contoh Output
**addresses.txt**
```
0xAbC123...
0xDeF456...
```

**privatekeys.txt**
```
0xabc123...
0xdef456...
```

---

## ❗ Tips Keamanan
- Jangan upload file hasil generate ke internet (publik).
- Simpen baik-baik, private key rawan disalahgunakan.
- Pakai wallet ini hanya buat testing atau keperluan khusus.

---

## 📞 Kontak / Bantuan
- Twitter: [@dwifahrissal](https://x.com/dwifahrissal)
- Buka issue kalo nemu bug atau pengen request fitur


