soru=["Motorsuz uçağa ne ad verilir?",
      "İzmit hangi tatlısıyla meşhurdur?",
      "Balık tutma aracı, bir ip ya da misinaya bağlanan, ucuna metal bir çengel iğne takarak ırmak,deniz veya göllerde balık tutmaya yarayan aracın adı nedir?",
      "Bir duyguyu, düşünceyi estetik ses tonunda yazma, anlatma sanatına ne ad verilir.",
      "Bir olayı anlık olarak kayıt altına sesli ve görüntülü olarak kaydeden cihazlara ne ad verilir?",
      "Mahalle ve sokaklarda güvenliği sağlamak için polisle birlikte görev yapan kişilerin mesleği nedir?",
      "Domates, biber ve yumurta ile yapılan her öğünde yenilebilen yemeğin adı nedir?",
      "Sesin şiddetini büyüklüğü birim cinsinden nedir?",
      "Kağıt ve demir paraları basan matbaaların adı nedir?",
      "Sağlıkta son yılların en büyük sorunlarından biridir. Bedenin yağ kütlesinin yağsız kütleye oranının aşırı artması sonucu boy uzunluğuna göre vücut ağırlığının arzu edilen düzeyin üstüne çıkmasıdır. Tıp dilinde bu sağlık sorununun adı nedir?"]
cevap=["Planör","Pişmaniye","Olta","Şiir","Kamera","Bekçi","Melemen","Desibel","Darphane","Obezite"]
dogrucevapsayisi=0
print(" — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —  ")
print("|                      Merhaba, bilgi yarışmasına hoşgeldiniz.                    |")
print("| Testten geçebilmek için 10 sorudan 5 tanesini doğru cevaplamanız gerekmektedir. |")
print("|                                İyi şanslar..!                                   |")
print(" — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — ")
for i in range(len(soru)):
    print("")
    print("Yarışmamızın {}. Sorusu".format(i+1))
    print("-"*23)
    print(soru[i])
    cevapp=input("{}. Soru İçin Cevap: ".format(i+1))
    if (cevapp.lower()==cevap[i].lower()):
        print("Cevabınız Doğru")        
        dogrucevapsayisi +=1        
    else:
        print("Cevabınız Yanlış. Doğru cevap: {}".format(cevap[i].capitalize()))
    print("Şuan {} doğru cevabınız var.".format(dogrucevapsayisi))
if (dogrucevapsayisi>=5):
    print("")
    print("Tebrikler, bilgi yarışmasını başarıyla tamamladınız. {} Tane soruyu doğru bildiniz".format(dogrucevapsayisi))
else:
    print("")
    print("Üzgünüz, bilgi yarışmasını başarıyla tamamlayamadınız. {} Tane soruyu doğru bildiniz".format(dogrucevapsayisi))
