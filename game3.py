print("Assalomu aleykum")
print("Men hozir sizga o'zbekcha so'z beraman siz uni ingilizchasini yozasiz")
uzb_eng = {
    "bahs": "argument",
    "diqqat": "concentration",
    "ishonch": "confidence",
    "tavsif/tasvir": "description",
    "farq": "difference",
    "munozara": "discussion",
    "takomillashtirish": "improvement",
    "mustaqillik": "independence",
    "ma'lumot": "information",
    "harakat": "movement",
    "iste'fo/nafaqaga chiqish": "retirement",
    "qabul qilmoq": "accept",
    "maslahat": "advice",
    "yolg'iz": "alone",
    "taxminan": "approximately",
    "bahslashmoq": "argue",
    "xotirjamlik bilan": "calmly",
    "imkoniyat": "chance",
    "muloqot qilmoq": "communicate",
    "butunlay": "completely",
    "kompyuter ustasi": "computer technician",
    "hissa qo'shmoq": "contribute",
    "qulay": "convenient",
    "qaror": "decision",
    "talab": "demand",
    "kelishmovchilik": "disagreement",
    "muhokama qilmoq": "discuss",
    "elektron do'st": "e-pal",
    "mashq qilmoq": "exercise",
    "mutaxassis": "expert",
    "muzlatgich": "fridge",
    "hukumat": "government",
    "qiyin vaqt": "hard time",
    "naushniklar": "headphones",
    "imkonsiz": "impossible",
    "xalaqit bermoq": "interrupt",
    "taqillatmoq": "knock",
    "kech": "late",
    "chegara": "limit",
    "baland ovozda": "loud",
    "ishonch hosil qilmoq": "make sure",
    "ovqat": "meal",
    "buyurtma": "order",
    "shaxsiy": "personal",
    "maxfiylik/shax": "privacy",
    "shaxsiy hudud": "private space",
    "ta'minlamoq": "provide",
    "anglamoq": "realize",
    "oqilona": "reasonable",
    "hurmat qilmoq/hurmat": "respect",
    "mas'uliyat": "responsibility",
    "o'ng/haq/haq-huquq": "right",
    "baqirmoq": "shout",
    "maxsus": "special",
    "uslub": "style",
    "jadval": "timetable",
    "(musiqani) pasaytirmoq": "turn (music) down",
    "noyob/yagona": "unique",
    "tartibsiz": "untidy",
    "ovoz hajm": "volume"



}
xato =[]
togri =[]
x = 1
# Foydalanuvchidan so'zni so'raymiz
for soz , tarjima in uzb_eng.items():
    savol = input(f"{x}.\"{soz.title()}\" so'zi ingiliz tilida qanday tarjima qilinadi: ").lower()
    x = x+1
# javobni tekshiramiz
    if savol.lower().strip() == tarjima.strip().lower():
        togri.append(savol)
        print("Tog'ri topdingiz")
    else:
        xato.append(savol)
        print(f"Xato \"{soz.title()}\" so'zi ingiliz tilida \"{tarjima.title()}\" degani")

print(f"{len(xato)} ta xato! ")
print(f"{len(togri)} ta tog'ri! ")

if len(togri) == 60:
    print("\nSo'ni 100 % yodlabsiz 🤯")
elif len(xato) >= 20:
    print("\n Yana ozgina yodlang 😶")
elif len(togri) >= 50:
    print("Zo'r")
else:
    print("\n Yaxshi 👌😇 ")

























