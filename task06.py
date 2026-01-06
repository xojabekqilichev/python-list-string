gap = "olol radar makka non"
sozlar = gap.split()
# So'zni o'zi va teskarisi ([::-1]) teng bo'lsa ro'yxatga qo'shamiz
palindromlar = [s for s in sozlar if s == s[::-1]]
print(palindromlar)  # ['olol', 'radar', 'non']