emails = "ali@gmail.com,vali@mail.ru,karim@gmail.com"
# Vergul bo'yicha bo'lamiz
ro_yxat = emails.split(",")
# Domenlarni ajratamiz ( @ belgisi bor joydan boshlab )
domenlar = [email[email.find('@'):] for email in ro_yxat]
# set() orqali faqat takrorlanmaslarini qoldiramiz
print(list(set(domenlar)))  # ['@mail.ru', '@gmail.com']