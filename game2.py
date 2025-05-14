uzb_eng = {
    "Arabcha/arab": "Arabic",
    "Argentinalik": "Argentinian",
    "Avstriya": "Austria",
    "Avstriyalik": "Austrian",
    "Braziliya": "Brazil",
    "Braziliyalik": "Brazilian",
    "Bolgariya": "Bulgaria",
    "Bolgar": "Bulgarian",
    "Misr": "Egypt",
    "Misrlik": "Egyptian",
    "Nemis": "German",
    "Yaponiya": "Japan",
    "Yapon": "Japanese",
    "Meksikalik": "Mexican",
    "Meksika": "Mexico",
    "Polsha": "Poland",
    "Polyak/polshalik": "Polish",
    "Portugal": "Portuguese",
    "Rossiya": "Russia",
    "Rus": "Russian",
    "Ispancha": "Spanish",
    "Shveytsariyalik": "Swiss",
    "Shveytsariya": "Switzerland",
    "Tay": "Thai",
    "Tailand": "Thailand",
    "Turkiya": "Turkey",
    "Turkcha": "Turkish",
    "Insho Yozmoq": "Do An Essay",
    "Mashq Qilmoq": "Do An Exercise",
    "Uy Vazifasini Bajarmoq": "Do Homework",
    "Ingliz Tilini O'rganmoq": "Do/Study English",
    "Imtihon Topshirmoq": "Do/Take An Exam",
    "Xato Qilmoq": "Make A Mistake",
    "Yodlamoq": "Memorise",
    "Amaliyot": "Practice",
    "Amaliyot qilmoq": "Practise",
    "Qayta Ko'rib Chiqmoq": "Revise",
    "Qayta Ko'rib Chiqish": "Revision",
    "Talaba": "Student",
    "O'qimoq/tahsil olmoq": "Study",
    "Tarjima Qilmoq": "Translate",
    "Tarjima": "Translation",
    "Noqonuniy": "Illegal",
    "Imkonsiz": "Impossible",
    "Noto'g'ri": "Incorrect",
    "Norasmiy": "Informal",
    "Ko'rinmas": "Invisible",
    "Noto’g’ri": "Irregular",
    "Baxtsiz": "Unhappy",
    "G'ayrioddiy/noodatiy": "Unusual",
    "Turar Joy": "Accommodation",
    "Hudud": "Area",
    "Sun'iy": "Artificial",
    "Tomoshabinlar": "Audience",
    "Asoslangan": "Based on",
    "Blok qilmoq": "Block",
    "Tana Tili": "Body Language",
    "Xarakter": "Character",
    "Yaqindan": "Closely",
    "Birga mavjud bo’lmoq": "Co-Exist",
    "Yig'moq": "Collect",
    "Diqqatni jamlagan": "Concentrated",
    "Chalkashlik": "Confusion",
    "Madaniyat": "Culture",
    "Ma'lumotlar": "Data",
    "Batafsil": "Detailed",
    "Biznes Qilmoq": "Do Business",
    "Tajriba": "Experiment",
    "Tushuntirmoq": "Explanation",
    "O’ziga jalb qiladigan/maftunkor": "Fascinating",
    "Buklamoq": "Fold",
    "Imo-Ishora": "Gesture",
    "Qo'pol": "Impolite",
    "Xatarli/xavfli": "Insecure",
    "Intervyu": "Interview",
    "Asosiy": "Main",
    "Xarita": "Map",
    "Ko'p Millatli Kompaniya": "Multinational Company",
    "Bosh irg’amoq": "Nod",
    "Og'zaki Bo'lmagan": "Non-Verbal",
    "Shimoliy Amerika": "North America",
    "Kelib Chiqishi": "Origin",
    "Tinchlik": "Peace",
    "Muloyim": "Polite",
    "Tayyorlamoq": "Prepare",
    "Ommaviy": "Public",
    "Kamalak": "Rainbow",
    "Mintaqa": "Region",
    "Xavfsiz": "Secure",
    "Seriya/qism": "Series",
    "Silkitmoq": "Shake",
    "Samimiylik": "Sincerity",
    "Ijtimoiy Tarmoq": "Social Network",
    "Yumshoq": "Soft",
    "To'g'riga": "Straight",
    "Filippin": "The Philippines",
    "Turizm": "Tourism",
    "Universal": "Universal",
    "Og'zaki": "Verbal",
    "Ovoz": "Voice",
    "Urush": "War"
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












