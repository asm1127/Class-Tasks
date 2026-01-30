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


#6
class Hisob:
    def __init__(self, raqam, egasi, balans):
        self.raqam = raqam
        self.egasi = egasi
        self.balans = balans

    def kirim(self, summa):
        self.balans += summa
        return self.balans

    def chiqim(self, summa):
        if self.balans >= summa:
            self.balans -= summa
            return self.balans
        else:
            return "Xatolik: Balansda mablag' yetarli emas"

class JamgArmaMixin:
    def __init__(self, foiz_stavka, balans):
        self.foiz_stavka = foiz_stavka
        self.balans = balans

    def foiz_qosh(self):
        foiz_miqdori = self.balans * (self.foiz_stavka / 100)
        self.balans += foiz_miqdori
        return self.balans

class KreditMixin:
    def __init__(self, foiz_stavka, balans, limit):
        self.foiz_stavka = foiz_stavka
        self.balans = balans
        self.limit = limit
        
    def chiqim(self, summa):
        if self.balans + self.limit >= summa:
            self.balans -= summa
            return self.balans
        else:
            return "Xatolik: Kredit limiti yetarli emas"

class VIPHisob(KreditMixin, JamgArmaMixin, Hisob):
    def __init__(self, raqam, egasi, balans, foiz_stavka, limit):
        super().__init__(raqam, egasi, balans)
        self.foiz_stavka = foiz_stavka
        self.limit = limit

vip = VIPHisob("001", "Karim", 2_000_000, foiz_stavka=12, limit=500_000)

print(f"Boshlang'ich balans: {vip.balans} so'm")

vip.foiz_qosh()
print(f"Foiz qo'shilgandan keyin: {vip.balans} so'm") # 2,240,000

vip.chiqim(2_400_000)
print(f"2,400,000 chiqimdan keyingi balans: {vip.balans} so'm") # -160,000
print(vip.chiqim(1_000_000))

