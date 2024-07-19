kume1 = {"a", "b", "c", 2}
kume2 = {1, 2, 3}

kume3 = kume1.union(kume2)  # birleştirme
# kume3 = kume1 | kume2  #aynı sekilde kullanılır
print(kume1, kume2, kume3)  # 2 sonucta 2 defa yazılmadı çünkü tekillik söz konusu

# kume3 = kume4.union(kume2,kume1) == kume3 = kume4 | kume2 | kume1

kume4 = {"8", 9, 45}
demet = (7, 8, 9)
kume3 = kume4.union(demet)
print(kume3)

kume4.update(demet)
print(kume4)

kume3 = kume4.intersection(demet)
kume3 = kume4 & set(demet)
print(kume3)
