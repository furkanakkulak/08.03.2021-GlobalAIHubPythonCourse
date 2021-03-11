#!/usr/bin/env python
# coding: utf-8

# In[1]:


CV1 = {"Ad":"Furkan","Soyad":"AKKULAK","Cinsiyet":"Erkek","MD":"Bekar","DYT":"Aydın/Nazilli - 06/07/2000","Adres":"Eskişehir","Mail":"akkulak.furkan26@gmail.com","Telefon":"5051233212","EB":"Burdur Mehmet Akif Ersoy Üniversitesi","Is":"Öğrenci","Beceri":"PHP, C#, C++, Python","INGS":"B1","BB":"Orta Düzey Office ve Programlama","Referans":"-"}
CV2 = {"Ad":"Onur","Soyad":"SEVER","Cinsiyet":"Erkek","MD":"Bekar","DYT":"Adana/Kozan - 22/02/2000","Adres":"Eskişehir","Mail":"redkulus26@hotmail.com","Telefon":"5061233212","EB":"Düzce Üniversitesi","Is":"Öğrenci","Beceri":"C++, Java, Python, Blender, Resim","INGS":"A2","BB":"Orta Düzey Office ve Programlama","Referans":"-"}
CV3 = {"Ad":"Ahmet Murat","Soyad":"TÜRKER","Cinsiyet":"Erkek","MD":"Bekar","DYT":"Eskişehir/Merkez - 19/10/2000","Adres":"Eskişehir","Mail":"muratturker2k@gmail.com","Telefon":"5071233212","EB":"Dumlupınar Üniversitesi","Is":"Öğrenci","Beceri":"Python,Resim,AutoCAD,SolidWorks, Catia","INGS":"B1","BB":"Orta Düzey Office ve Başlangıç Düzeyi Programlama","Referans":"-"}
CV4 = {"Ad":"Musa","Soyad":"BIYIKLI","Cinsiyet":"Erkek","MD":"Bekar","DYT":"İstanbul/Bahçelievler - 14/10/2000","Adres":"Kocaeli","Mail":"musabiyikli@hotmail.com.tr","Telefon":"5081233212","EB":"Burdur Mehmet Akif Ersoy Üniversitesi","Is":"Öğrenci","Beceri":"Python,AutoCAD,Proteus","INGS":"B1","BB":"Orta Düzey Office ve Programlama","Referans":"-"}
CV5 = {"Ad":"Melisa","Soyad":"Diken","Cinsiyet":"Kız","MD":"Evli","DYT":"İzmir/Balçova - 13/04/2000","Adres":"İstanbul","Mail":"melisadiken@hotmail.com","Telefon":"5091233212","EB":"Yıldız Teknik Üniversitesi","Is":"Yazılım Mühendisi","Beceri":"C#, R, Yapay Zeka ","INGS":"C1","BB":"Üst Düzey Office ve Programlama","Referans":"-"}
for i in range (6):
    print(" — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — ")
    if i == 0:
        print("|  Ad:", CV1["Ad"],"                                                              |")
        print("|  Soyad:", CV1["Soyad"],"                                                          |")
        print("|  Cinsiyet:", CV1["Cinsiyet"],"                                                         |")
        print("|  Medeni Durum:", CV1["MD"],"                                                     |")
        print("|  Doğum Yeri ve Tarihi:", CV1["DYT"],"                        |")
        print("|  Adres:", CV1["Adres"],"                                                        |")
        print("|  Mail:", CV1["Mail"],"                                        |")
        print("|  Telefon Numarası:", CV1["Telefon"],"                                            |")
        print("|  Eğitim Bilgisi:", CV1["EB"],"                   |")
        print("|  İşi:", CV1["Is"],"                                                            |")
        print("|  Becerileri:", CV1["Beceri"],"                                        |")
        print("|  İngilizce Seviyesi:", CV1["INGS"],"                                                  |")
        print("|  Bilgisayar Bilgisi:", CV1["BB"],"                    |")
        print("|  Referans:", CV1["Referans"],"                                                             |")
    elif i == 1:
        print("|  Ad:", CV2["Ad"],"                                                                |")
        print("|  Soyad:", CV2["Soyad"],"                                                            |")
        print("|  Cinsiyet:", CV2["Cinsiyet"],"                                                         |")
        print("|  Medeni Durum:", CV2["MD"],"                                                     |")
        print("|  Doğum Yeri ve Tarihi:", CV2["DYT"],"                          |")
        print("|  Adres:", CV2["Adres"],"                                                        |")
        print("|  Mail:", CV2["Mail"],"                                            |")
        print("|  Telefon Numarası:", CV2["Telefon"],"                                            |")
        print("|  Eğitim Bilgisi:", CV2["EB"],"                                      |")
        print("|  İşi:", CV2["Is"],"                                                            |")
        print("|  Becerileri:", CV2["Beceri"],"                           |")
        print("|  İngilizce Seviyesi:", CV2["INGS"],"                                                  |")
        print("|  Bilgisayar Bilgisi:", CV2["BB"],"                    |")
        print("|  Referans:", CV2["Referans"],"                                                             |")
    elif i == 2:
        print("|  Ad:", CV3["Ad"],"                                                         |")
        print("|  Soyad:", CV3["Soyad"],"                                                           |")
        print("|  Cinsiyet:", CV3["Cinsiyet"],"                                                         |")
        print("|  Medeni Durum:", CV3["MD"],"                                                     |")
        print("|  Doğum Yeri ve Tarihi:", CV3["DYT"],"                     |")
        print("|  Adres:", CV3["Adres"],"                                                        |")
        print("|  Mail:", CV3["Mail"],"                                           |")
        print("|  Telefon Numarası:", CV3["Telefon"],"                                            |")
        print("|  Eğitim Bilgisi:", CV3["EB"],"                                 |")
        print("|  İşi:", CV3["Is"],"                                                            |")
        print("|  Becerileri:", CV3["Beceri"],"                      |")
        print("|  İngilizce Seviyesi:", CV3["INGS"],"                                                  |")
        print("|  Bilgisayar Bilgisi:", CV3["BB"],"   |")
        print("|  Referans:", CV3["Referans"],"                                                             |")
    elif i == 3:
        print("|  Ad:", CV4["Ad"],"                                                                |")
        print("|  Soyad:", CV4["Soyad"],"                                                          |")
        print("|  Cinsiyet:", CV4["Cinsiyet"],"                                                         |")
        print("|  Medeni Durum:", CV4["MD"],"                                                     |")
        print("|  Doğum Yeri ve Tarihi:", CV4["DYT"],"                |")
        print("|  Adres:", CV4["Adres"],"                                                          |")
        print("|  Mail:", CV4["Mail"],"                                        |")
        print("|  Telefon Numarası:", CV4["Telefon"],"                                            |")
        print("|  Eğitim Bilgisi:", CV4["EB"],"                   |")
        print("|  İşi:", CV4["Is"],"                                                            |")
        print("|  Becerileri:", CV4["Beceri"],"                                      |")
        print("|  İngilizce Seviyesi:", CV4["INGS"],"                                                  |")
        print("|  Bilgisayar Bilgisi:", CV4["BB"],"                    |")
        print("|  Referans:", CV4["Referans"],"                                                             |")
    elif i == 4:
        print("|  Ad:", CV5["Ad"],"                                                              |")
        print("|  Soyad:", CV5["Soyad"],"                                                            |")
        print("|  Cinsiyet:", CV5["Cinsiyet"],"                                                           |")
        print("|  Medeni Durum:", CV5["MD"],"                                                      |")
        print("|  Doğum Yeri ve Tarihi:", CV5["DYT"],"                        |")
        print("|  Adres:", CV5["Adres"],"                                                         |")
        print("|  Mail:", CV5["Mail"],"                                           |")
        print("|  Telefon Numarası:", CV5["Telefon"],"                                            |")
        print("|  Eğitim Bilgisi:", CV5["EB"],"                              |")
        print("|  İşi:", CV5["Is"],"                                                  |")
        print("|  Becerileri:", CV5["Beceri"],"                                          |")
        print("|  İngilizce Seviyesi:", CV5["INGS"],"                                                  |")
        print("|  Bilgisayar Bilgisi:", CV5["BB"],"                     |")
        print("|  Referans:", CV5["Referans"],"                                                             |")
    else:
        print("5 Tane CV Bulundu")


# In[ ]:





# In[ ]:




