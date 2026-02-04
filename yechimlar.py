
# #1
# class Transport:
#     def __init__(self, model: str, yil: int) -> None:
#         self.model = model
#         self.yil = yil
#
#     def malumot(self) -> str:
#         return f"Model: {self.model}, Yil: {self.yil}"
#
# class Avtomobil(Transport):
#     def __init__(self, model: str, yil: int,  yonilgi_turi: str) -> None:
#         super().__init__(model, yil)
#         self.yonilgi_turi = yonilgi_turi
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, Yonil'gi: {self.yonilgi_turi} "
#
# class Avtobus(Transport):
#     def __init__(self, model: str, yil: int, orinlar_soni: int) -> None:
#         super().__init__(model, yil)
#         self.orinlar_soni = orinlar_soni
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, O'rinlar: {self.orinlar_soni}"
#
# a = Avtomobil("Cobalt", "2022", "benzin")
# print(a.malumot())
#
# b = Avtobus("Isuzu", "2018", "40")
# print(b.malumot())

# #2
# class Kitob:
#     def __init__(self, nom, muallif, yil):
#         self.nom = nom
#         self.muallif = muallif
#         self.yil = yil
#
#     def taqdimot(self):
#         return f"\"{self.nom}\" - {self.muallif} ({self.yil})"
#
# class Elektronkitob(Kitob):
#     def __init__(self, nom, muallif, yil, fayl_hajmi_mb):
#         super().__init__(nom, muallif, yil)
#         self.fayl_hajmi_mb = fayl_hajmi_mb
#
#     def taqdimot(self):
#         baza = super().taqdimot()
#         return f"{baza}, [Elektron, {self.fayl_hajmi_mb}MB]"
#
# class Audiokitob(Kitob):
#     def __init__(self, nom, muallif, yil, davomiylik_soat):
#         super().__init__(nom, muallif, yil)
#         self.davomiylik_soat = davomiylik_soat
#
#     def taqdimot(self):
#         baza = super().taqdimot()
#         return f"{baza}, [Audio, {self.davomiylik_soat} soat]"
#
# e = Elektronkitob("Python asoslari", "Ali", "2023", "5")
# a = Audiokitob("O'tgan kunlar", "Abdulla Qodiriy", "2020", "12")
#
# print(e.taqdimot())
# print(a.taqdimot())

# #3
# class Xodim:
#     def __init__(self, ism, asosiy_maosh):
#         self.ism = ism
#         self.asosiy_maosh = asosiy_maosh
#
#     def oylik(self):
#         return self.asosiy_maosh
#
#     def malumot(self):
#         return f"Ism: {self.ism}, Oylik: {self.oylik()}"
#
# class Oqsoch(Xodim):
#     def __init__(self, ism, asosiy_maosh, bonus_foiz):
#         super().__init__(ism, asosiy_maosh)
#         self.bonus_foiz = bonus_foiz
#
#     def oylik(self):
#         bonus = self.asosiy_maosh * self.bonus_foiz // 100
#         return f"{bonus}, Bonus foiz: {self.bonus_foiz}"
#
# class SoatbayXodim(Xodim):
#     def __init__(self, ism, soat, soatlik_stavka):
#         super().__init__(ism, soat * soatlik_stavka)
#         self.soat = soat
#         self.soatlik_stavka = soatlik_stavka
#
#
# o = Oqsoch("Dilshod", 5_000_000, 20)
# s = SoatbayXodim("Aziza", soat=160, soatlik_stavka=50_000)
#
# print(o.malumot())
# print(s.malumot())

# #4
# class Mahsulot:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
#
#     def chegirmali_narx(self, foiz):
#         chegirma_miqdori = self.narx * (foiz / 100)
#         yangi_narx = self.narx - chegirma_miqdori
#         return yangi_narx
#
# class Elektronika(Mahsulot):
#     def __init__(self, nom, narx, kafolat_oy):
#         super().__init__(nom, narx)
#         self.kafolat_oy = kafolat_oy
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: {self.narx}, Kafolat: {self.kafolat_oy} oy"
#
# class OziqOvqat(Mahsulot):
#     def __init__(self, nom, narx, yaroqlilik_kuni):
#         super().__init__(nom, narx)
#         self.yaroqlilik_kuni = yaroqlilik_kuni
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: {self.narx}, Yaroqlilik: {self.yaroqlilik_kuni}"
#
#
# q = Elektronika("MacBook Air", 1200, 12)
# p = OziqOvqat("Lazzat Suti", 12000, "2025-05-10")
#
# print(p.malumot())
# print(q.malumot())

# #5
# class Shaxs:
#     def __init__(self, ism):
#         self.ism = ism
#
# class Talaba(Shaxs):
#     def __init__(self, ism, id_raqam):
#         super().__init__(ism)
#         self.id_raqam = id_raqam
#
# class ImtihonNatijasi(Talaba):
#     def __init__(self, ism, id_raqam, baholar):
#         super().__init__(ism, id_raqam)
#         self.baholar = baholar
#
#     def ortalama(self):
#         if not self.baholar:
#             return 0
#         return sum(self.baholar) / len(self.baholar)
#
#     def status(self):
#         a = self.ortalama()
#         if a >= 86:
#             return "A'lo"
#         elif 71 <= a <= 85:
#             return "Yaxshi"
#         elif 56 <= a <= 70:
#             return "Qoniqarli"
#         else:
#             return "Qoniqarsiz"
#
# natija = ImtihonNatijasi("Ali", "T001", [90, 80, 100])
# print(f"Ism: {natija.ism}")
# print(f"Id Raqam: {natija.id_raqam}")
# print(f"O'rtalama: {natija.ortalama()}")
# print(f"Status: {natija.status()}")


# #6
# class Hisob:
#     def __init__(self, raqam, egasi, balans):
#         self.raqam = raqam
#         self.egasi = egasi
#         self.balans = balans
#
#     def kirim(self, summa):
#         self.balans += summa
#
#     def chiqim(self, summa):
#         self.balans -= summa
#
#
# class JamgArmaMixin:
#     def hisobla_foiz(self):
#         return self.balans * self.foiz_stavka / 100
#
# class KreditMixin:
#     def chiqim(self, summa):
#         if self.balans - summa >= self.limit:
#             self.balans -= summa
#         else:
#             return "Kredit limiti oshib ketdi"
#
# class VIPHisob(KreditMixin, JamgArmaMixin, Hisob):
#     def __init__(self, raqam, egasi, balans, foiz_stavka, limit):
#         super().__init__(raqam, egasi, balans)
#         self.foiz_stavka = foiz_stavka
#         self.limit = limit
#
# vip = VIPHisob("001", "Karim", 2_000_000, foiz_stavka=12, limit=500_000)
# print(vip.balans)
# vip.chiqim(2_400_000)
# print(vip.balans)

# #7
# class Kurs:
#     def __init__(self, nom, davomiylik_hafta, narx):
#         self.nom = nom
#         self.davomiylik_hafta = davomiylik_hafta
#         self.narx = narx
#
#     def malumot(self):
#         return f"Kurs: {self.nom}, Davomiylik: {self.davomiylik_hafta} hafta, Narx: {self.narx}"
#
# class OnlaynKurs(Kurs):
#     def __init__(self, nom, davomiylik_hafta, narx, platforma):
#         super().__init__(nom, davomiylik_hafta, narx)
#         self.platforma = platforma
#
#     def malumot(self):
#         return f"Platforma: {self.platforma}"
#
# class OfflineKurs(Kurs):
#     def __init__(self, nom, davomiylik_hafta, narx, manzil):
#         super().__init__(nom, davomiylik_hafta, narx)
#         self.manzil = manzil
#
#     def malumot(self):
#         return f"Manzil: {self.manzil}"
#
# kurslar = [
#     OnlaynKurs("Python", "12", "1_800_000", " Coursera"),
#     OfflineKurs("Kiberhavfsizlik", "40", "25_000_000", "Toshkent")
# ]
#
# for kurs in kurslar:
#     print(kurs.malumot())

# #8
# class Taom:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
#
#     def tavsif(self):
#         return f"Taom: {self.nom}, Narx: {self.narx}"
#
# class IssiqTaom(Taom):
#     def __init__(self, nom, narx, kaloriya):
#         super().__init__(nom, narx)
#         self.kaloriya = kaloriya
#
#     def tavsif(self):
#         return f"Taom: {self.nom}, Narx: {self.narx} so'm, Kaloriya: {self.kaloriya} kkal"
#
# class Ichimlik(Taom):
#     def __init__(self, nom, narx, hajm_ml):
#         super().__init__(nom, narx)
#         self.hajm_ml = hajm_ml
#
#     def tavsif(self):
#         return f"Ichimlik: {self.nom}, Narx: {self.narx} so'm, Hajmi: {self.hajm_ml} ml"
#
#     def chegirma_qollash(taomlar, foiz):
#
#         for taom in taomlar:
#             chegirma_summasi = taom.narx * (foiz / 100)
#             taom.narx -= chegirma_summasi
#
# osh = IssiqTaom("Palov", 30000, 850)
# choy = Ichimlik("Ko'k choy", 5000, 500)
# kabob = IssiqTaom("Shashlik", 15000, 450)
#
# menyular = [osh, choy, kabob]
#
# print(osh.tavsif())
# print(choy.tavsif())
# print(kabob.tavsif())

# #9
# from abc import ABC, abstractmethod
# from typing import List
#
# class JamoaAzo(ABC):
#     def __init__(self, ism):
#         self.ism = ism
#
#     @abstractmethod
#     def vazia(self):
#         return NotImplementedError
#
# class BackendDasturchi(JamoaAzo):
#     def vazia(self):
#         return "API va ma'lumotlar bazasi bilan ishlaydi"
#
# class FrontendDasturchi(JamoaAzo):
#     def vazia(self):
#         return "UI va foydalanuvchi tajribasini yaratadi"
#
# class Tester(JamoaAzo):
#     def vazia(self):
#         return "Tizimni test qiladi"
#
# def hisobot(azolar: List[JamoaAzo]):
#     for azo in azolar:
#         print(f"Ism: {azo.ism}, Vazifa: {azo.vazia()}")
#
# jamoa = [
#     BackendDasturchi("Marjona"),
#     FrontendDasturchi("Rayhona"),
#     Tester("Maftuna")
# ]
#
# hisobot(jamoa)

# #10
# class QadamSanagich:
#     def __init__(self, kunlik_maqsad, qadamlar):
#         self.kunlik_maqsad = kunlik_maqsad
#         self.qadamlar = qadamlar
#
#     def bajarilgan_kunlar(self):
#         sanoq = 0
#         for qadam in self.qadamlar:
#             if qadam >= self.kunlik_maqsad:
#                 sanoq += 1
#             return sanoq
#
#     def ortalama_qadamlar(self):
#          if not self.qadamlar:
#              return 0
#          return sum(self.qadamlar) / len(self.qadamlar)
#
# class MotivatsionQadamSanagich(QadamSanagich):
#     def __init__(self, kunlik_maqsad, qadamlar):
#         super().__init__(kunlik_maqsad, qadamlar)
#
#     def motivatsiya_xabari(self):
#         if self.bajarilgan_kunlar() >= 5:
#             return "Barakalla! Siz juda faol ekansiz!"
#         else:
#             return "Harakatni ko'proq oshiring!"
#
# hafta = [10000, 7500, 8200, 9000, 5000, 12000, 8000]
# q = MotivatsionQadamSanagich(8000, hafta)
# print(q.bajarilgan_kunlar())
# print(q.ortalama_qadamlar())
# print(q.motivatsiya_xabari())



#               Hayotiy mavzudagi algoritmik masalalar

# #1
# def qaytim_hisobla(narx, tolangan):
#     if tolangan < narx:
#         return "Pul yetarli emas"
#     else:
#         return int(tolangan - narx)
#
# print(qaytim_hisobla(12000, 20000))
# print(qaytim_hisobla(15000, 10000))

# #2
# def borsh_orinlar(jami, yolovchilar):
#     if yolovchilar > jami:
#         return "Joy yetmaydi"
#     else:
#         return int(yolovchilar - jami)
#
# print(borsh_orinlar(40, 32))
# print(borsh_orinlar(50, 55))

# #3
# def jarima_hisobla(kechikkan_kun):
#     if kechikkan_kun <= 0:
#         return 0
#
#     jarima = 0
#
#     if kechikkan_kun <= 5:
#         jarima = kechikkan_kun * 1000
#     elif kechikkan_kun <= 10:
#         jarima = (5 * 1000) + (kechikkan_kun - 5) * 2000
#     else:
#         jarima = (5 * 1000) + (5 * 2000) + (kechikkan_kun - 10) * 3000
#
#     return jarima
#
# print(jarima_hisobla(3))
# print(jarima_hisobla(7))
# print(jarima_hisobla(12))

#4
def reyting_tahlil(baholar):
    if not baholar:
        return "Ro'yhat bo'sh"

    ortalma = sum(baholar) / len(baholar)

    eng_yuqori = max(baholar)

    eng_past = min(baholar)

    a_soni = 0
    for baho in baholar:
        if 86 <= baho <= 100:
            a_soni += 1
        return 