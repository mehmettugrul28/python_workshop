let boy = Number(prompt("Boyunuzun kaç cm olduğunu giriniz: "))
let kilo = Number(prompt("Kaç kilogram olduğunuzu giriniz: "))
let boyMetre = boy/100

if (isNaN(boy)) {
    console.log("Boyunuzu sayı cinsinden giriniz.");
}

if (isNaN(kilo)) {
    console.log("Kilonuzu sayı cinsinden giriniz.");
}

vki = kilo / (boyMetre ** 2)

if(vki <= 18.5){
    console.log("Vücut kitle indexiniz: " + vki)
    console.log("İdeal kilonun altındasınız.")
}
if(vki > 18.5 && vki <= 24.9){
    console.log("Vücut kitle indexiniz: " + vki)
    console.log("İdeal kilodasınız.")
}
if(vki >= 25 && vki <= 29.9){
    console.log("Vücut kitle indexiniz: " + vki)
    console.log("İdeal kilonun üstündesiniz.")
}
if(vki >= 30 && vki <= 39.9){
    console.log("Vücut kitle indexiniz: " + vki)
    console.log("İdeal kilonun fazla üstündesiniz(obez).")
}
if(vki >= 40){
    console.log("Vücut kitle indexiniz: " + vki)
    console.log("İdeal kilonun aşırı üstündesiniz(morbid obez")
}