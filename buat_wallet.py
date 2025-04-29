import time
import secrets
import sys
from eth_account import Account

def animasi_loading(pesan="Sedang membuat wallet", durasi=5):
    for i in range(durasi * 4):
        titik = '.' * (i % 4)
        sys.stdout.write(f'\r{pesan}{titik}   ')
        sys.stdout.flush()
        time.sleep(0.25)
    print()

def buat_wallet():
    private_key = "0x" + secrets.token_hex(32)
    akun = Account.from_key(private_key)
    return akun.address, private_key

def buat_banyak_wallet(jumlah, file_alamat="addresses.txt", file_privatekey="privatekeys.txt"):
    with open(file_alamat, "w") as fa, open(file_privatekey, "w") as fk:
        for i in range(jumlah):
            alamat, private_key = buat_wallet()
            fa.write(alamat + "\n")
            fk.write(private_key + "\n")
            if (i + 1) % 100 == 0:
                print(f"Membuat {i + 1} wallet...")

if __name__ == "__main__":
   
    print("""
    
**************************************************************************************
*                                                                                    *
*                                                                                    *
*         :::       :::     :::     :::        :::        :::::::::: :::::::::::     *
*        :+:       :+:   :+: :+:   :+:        :+:        :+:            :+:          *
*       +:+       +:+  +:+   +:+  +:+        +:+        +:+            +:+           *
*      +#+  +:+  +#+ +#++:++#++: +#+        +#+        +#++:++#       +#+            *
*     +#+ +#+#+ +#+ +#+     +#+ +#+        +#+        +#+            +#+             *
*     #+#+# #+#+#  #+#     #+# #+#        #+#        #+#            #+#              *
*     ###   ###   ###     ### ########## ########## ##########     ###               *
*             :::   :::       :::     :::    ::: :::::::::: :::::::::                *
*           :+:+: :+:+:    :+: :+:   :+:   :+:  :+:        :+:    :+:                *
*         +:+ +:+:+ +:+  +:+   +:+  +:+  +:+   +:+        +:+    +:+                 *
*        +#+  +:+  +#+ +#++:++#++: +#++:++    +#++:++#   +#++:++#:                   *
*       +#+       +#+ +#+     +#+ +#+  +#+   +#+        +#+    +#+                   *
*      #+#       #+# #+#     #+# #+#   #+#  #+#        #+#    #+#                    *
*     ###       ### ###     ### ###    ### ########## ###    ###                     *
*                                                    by mangisal                     *
*                                                                                    *
**************************************************************************************

                                                                   
   
   
    """)

    jumlah_wallet = int(input("Berapa banyak wallet yang ingin dibuat? "))
    animasi_loading()
    buat_banyak_wallet(jumlah_wallet)
    print(f"\n✅ Selesai: {jumlah_wallet} wallet disimpan ke 'addresses.txt' dan 'privatekeys.txt'.")
