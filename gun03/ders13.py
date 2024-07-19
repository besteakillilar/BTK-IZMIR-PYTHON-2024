oyuncular = {"redbull": ["max","checo", "newey"],
             "ferrari": ["leclerc", "carlos", "enzo"],
             "mercedes": ["hamilton", "george", "toto"]}
print(oyuncular["ferrari"])
for i in oyuncular:
    #    print(i)
    #    print(oyuncular[i])
    print(i, "takımının oyuncuları : ", oyuncular[i])
    for oyuncu in oyuncular[i]:
        print("\t", oyuncu)
