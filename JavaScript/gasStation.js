let dizel = 52.10;
let benzin = 51.58;
let lpg = 36.24;

let yakitMetni = "1-Motorin(Dizel) -> 52.10 TL/L \n2-Benzin -> 51.58 TL/L\n3-LPG -> 36.24 TL/L\nAlmak istediğiniz yakıt türünü giriniz:";
let yakitTipi = prompt(yakitMetni).toLowerCase();
let yakitMiktari = Number(prompt("Kaç litre yakıt almak istersiniz?"));
let toplamFiyat = 0;

if (yakitTipi == "motorin" || yakitTipi == "dizel" || yakitTipi == "1") {
    toplamFiyat = yakitMiktari * dizel;
} 
else if (yakitTipi == "benzin" || yakitTipi == "2") {
    toplamFiyat = yakitMiktari * benzin;
} 
else if (yakitTipi == "lpg" || yakitTipi == "3") {
    toplamFiyat = yakitMiktari * lpg;
} 
else {
    console.log("Geçersiz yakıt türü girdiniz!");
}


let odenecekTutar = Number(prompt("Ödenecek toplam tutar: " + toplamFiyat))

if(odenecekTutar == toplamFiyat){
    console.log("Ödemeniz başarıyla tamamlandı.")
}
else if (odenecekTutar > toplamFiyat){
    console.log("Fazla girdiniz. Para üstünüz: " + (odenecekTutar - toplamFiyat) + " TL")
}
else{
    console.log("Eksik girdiniz. Yeniden denersiniz artık.")
}


