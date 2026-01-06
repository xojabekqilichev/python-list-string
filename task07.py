data = "Ism:Ali, Familiya:Valiyev, Yil:2002"
# Avval vergul bo'yicha bo'lamiz
qismlar = data.split(",")
for qism in qismlar:
    # Ikki nuqta atrofidagi bo'shliqlarni chiroyli formatlaymiz
    kalit, qiymat = qism.split(":")
    print(f"{kalit.strip()}: {qiymat.strip()}")