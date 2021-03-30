function text() {
    var awal = confirm("Selamat Datang di Ngaos Ksp Berkah Family\nMenjual bibit padi Ngaos KPDL. \n1. Ngaos KPDL 01 \n2. Ngaos KPDL 02");
    if (awal == false) {
        document.write("Terima kasih sudah mengunjungi Ngaos Ksp Berkah Family");
        exit();
    }  
}
text();
stepTwo();


function back() {
    var back = confirm("Anda salah input, Apakah kamu ingin kembali ke menu utama ?");
    if (back == true){
        text();
        stepTwo();
    }else{
        document.write("Terima kasih sudah mengunjungi Ngaos Ksp Berkah Family");
        exit();
    }
}


function stepTwo() {
    var jawab = prompt("Ngaos Ksp Berkah Family\n1. Ngaos KPDL 01 \n2. Ngaos KPDL 02\nmau beli yang mana ? ");
    var ngaos1 = "Ngaos KPDL 01" && 1;
    var ngaos2   = "Ngaos KPDL 02" && 2;

    if (jawab == false) {
        back();
    }else if (jawab == ngaos1 ) {
    var beli = Number(prompt("Anda membeli benih padi Ngaos KPDL 01 4kg dengan harga Rp.300.000;\nmau berapa ?"));
    var total1 = 300000*beli;
    var total2 = 150000*beli2;
    var akhir = Number(prompt("Total Harga : Rp." + total1 + "\nSilahkan masukan uang anda "));
        if(akhir == false){
            back();
        }
    var total3 = akhir - total1;
    var akhir2 = confirm('Transaksi Berhasil !\nUang Anda Rp.' + akhir + '\nHarga Barang Rp.' + total1 + '\nKembalian Rp. ' + total3);
        if (akhir2 == true) {
        var akhir3 = confirm("Apakah anda ingin berbelanja lagi ? ");
            if(akhir3 == true){
                stepTwo();  
            }else{
                document.write("Terima kasih sudah mengunjungi Ngaos Ksp Berkah Family");
            }
        }
        
    }else if (jawab == ngaos2) {
    var beli2 = Number(prompt("Anda membeli benih padi Ngaos KPDL 02 4kg dengan harga Rp.150.000;\nmau berapa ?"));
    var total2 = 150000*beli2;
    var akhir = Number(prompt("Total Harga : Rp." + total2 + "\nSilahkan masukan uang anda "));
    var total3 = akhir - total2;
    var akhir2 = confirm('Transaksi Berhasil !\nUang Anda Rp.' + akhir + '\nHarga Barang Rp.' + total2 + '\nKembalian Rp. ' + total3);
    }else{
        back();
    }
    

}