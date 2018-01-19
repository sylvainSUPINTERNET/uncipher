
# TEST only

for index, word_2 in enumerate(dico_trim):
    for char in word_2:

# CLEAN array for only alphabet without special chars
if char == '.' or char == '-' or char == "'":
    dico_trim.remove(word_2)
if char == 'é':
    word_changed = dico_trim[index].replace('é', 'e')
    dico_trim.__setitem__(index, word_changed)
if char == 'è':
    word_changed = dico_trim[index].replace('è', 'e')
    dico_trim.__setitem__(index, word_changed)
if char == 'ê':
    word_changed = dico_trim[index].replace('ê', 'e')
    dico_trim.__setitem__(index, word_changed)
if char == 'â':
    word_changed = dico_trim[index].replace('â', 'a')
    dico_trim.__setitem__(index, word_changed)
if char == 'à':
    word_changed = dico_trim[index].replace('à', 'a')
    dico_trim.__setitem__(index, word_changed)
if char == 'î':
    word_changed = dico_trim[index].replace('î', 'i')
    dico_trim.__setitem__(index, word_changed)
if char == 'ï':
    word_changed = dico_trim[index].replace('ï', 'i')
    dico_trim.__setitem__(index, word_changed)
if char == 'û':
    word_changed = dico_trim[index].replace('û', 'u')
    dico_trim.__setitem__(index, word_changed)
if char == 'ù':
    word_changed = dico_trim[index].replace('û', 'u')
    dico_trim.__setitem__(index, word_changed)
if char == 'ô':
    word_changed = dico_trim[index].replace('ô', 'i')
    dico_trim.__setitem__(index, word_changed)