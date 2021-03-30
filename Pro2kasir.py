print('====Program Kasir Sederhana====')
nama = input('Masukan Nama Konsumen : ')
tanggal = input('Tanggal Pembelian : ')
print('')
print('Nama Konsumen : ',nama)
print('Tanggal Pembelian : ',tanggal)
print('')
print('Produk Benih Padi Ngaos')

def pilihan(i):
    list_produk={
        1:'----Ngaos KPDL 01 = Rp.200.000----',
        2:'----Ngaos KPDL 02 = Rp.150.000----',
    }
    
    return list_produk.get(i)

print('1. Ngaos KPDL 01')
print('2. Ngaos KPDL 02')

jenis1 = ('Ngaos KPDL 01')
jenis2 = ('Ngaos KPDL 02')
nomor = int(input('Masukan Pilihan : '))

if nomor < 0 or nomor > 2:
    print('Masukan pilihan yang benar !')
    exit()
else:
    c = pilihan(nomor)
    print(c)

jumlah = int(input('Banyak unit yang dibeli : '))
if nomor==1:
    a = jumlah*200000
    print('Sub-total = Rp.',a)
    
elif nomor==2:
    a = jumlah*150000
    print('Sub-total = Rp.',a)
    

uang = int(input('Uang Tunai = Rp.'))
kembalian = uang - a
print('Jumlah kembalian : ',kembalian)


print('\n===========================================================================')
print('|================================== STRUK ===================================|')
print('===== Nama       :',nama)
print('===== Tanggal    :',tanggal)
print('===== Beli       :',jenis1)
print('===== Tagihan    : Rp.',a)
print('===== Bayar      : Rp.',uang)
print('===== Kembalian  : Rp.',kembalian)
print('|================================= Terima Kasih  ==============================|')
print('   |======================= Sudah belanja di Toko kami ====================|')
print('      |====================== Ngaos Ksp Berkah Family =================|')
print('\n===========================================================================')