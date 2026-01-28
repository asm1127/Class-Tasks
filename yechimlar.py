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

