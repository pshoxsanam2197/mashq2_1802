# 6-masala
talaba = {'ism': "Dilnoza",
          'yosh': 20,
          'shahar': "Andijon",
          'kurs':2
          }
del talaba['shahar']
print(talaba)

# 7-masala
meva = {"olma": 15000, "nok": 12000, "uzum": 20000, "shaftoli": 18000}

kalitlar = meva.keys()
print(kalitlar)

# 8-masala
meva = {"olma": 15000, "nok": 12000, "uzum": 20000, "shaftoli": 18000}

qiymatlar = meva.values()

for qiymat in qiymatlar:
    print(qiymat)

# 9-masala
kitob = {"nomi": "O'tkan kunlar", "muallif": "Abdulla Qodiriy", "yil": 1925, "sahifa": 320}
juftliklar = kitob.items()

for kalit, qiymat in juftliklar:
    print(kalit, ":", qiymat)

# 10-masala
kitob = {"nomi": "Mehrobdan chayon", "muallif": "Abdulla Qahhor", "sahifa": 280}

if "muallif" in kitob:
    print("Lug‘atda 'muallif' kaliti bor")
else:
    print("Lug‘atda 'muallif' kaliti yo‘q")

# 11-masala
rang = {"qizil": "red",
        "ko'k": "blue",
        "yashil": "green",
        "sariq": "yellow",
        "qora": "black"}
print(len(rang))
