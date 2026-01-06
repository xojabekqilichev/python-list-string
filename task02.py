
text = "Dasturlash, Sun'iy intellekt, Web dizayn"

# Vergullarni o'chirish, kichik harfga o'tkazish va bo'shliqlarni '_' ga almashtirish
result = text.replace(",", "").lower().replace(" ", "_")

print(result) # dasturlash_sun'iy_intellekt_web_dizayn