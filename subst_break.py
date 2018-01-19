import string
import sys

# color syntax shell (optionnal) debug only
# from colorama import init, Fore

#count occurence
from collections import Counter, OrderedDict


# for windows powershell (debug)
#init(convert=True)

# Open dict and read
lines = list(open(sys.argv[1], encoding='utf-8').read().splitlines())


#format return array 2D
render = [[]]

# / *** METHOD *** / #
# search word in dictionnary
def search(shift, possibilites, file_open_lines, word_input, turn):
    decalage = shift  # int
    possibility_table = possibilties # word find in dico and possible

    print("decalage :" + str(decalage), " possibility : " + possibility_table[decalage - 1] + "\n")



    # paramters for research
    word_possible_len = len(possibilties.__getitem__(0))

    dico_trim = []
    result = []  # store word found


    #rendu final + formatted
    render = []



    # 1 trim dico by word's len
    for word in lines:
        if (len(word) == word_possible_len):
            dico_trim.append(word)

    for index, word_found in enumerate(dico_trim):
        # 2 check by value (same value) basic
        if (possibility_table[decalage - 1] == word_found):
            #print(Fore.CYAN + "FOUND : " + word_found  )
            print("FOUND : " + word_found)
            #print("" + Fore.WHITE)
            result.append(word_found)


    render.append(result) #display word found
    render.append(dico_trim) # usefull for the test after result is => not matched words found

    return render






# Check if paramters are OK
arg_status = True
if (len(lines) > 0):
    arg_status = True
else:
    arg_status = False

if (len(sys.argv) > 2):
    arg_status = True
else:
    arg_status = False

# IF paramters are OK we start, else error
if (arg_status is True):

    #print("\n" + Fore.GREEN + "Cypher sequence : " + sys.argv[2] + "\n\n")
    print("\n" + "Cypher sequence : " + sys.argv[2] + "\n\n")


    alphabet = string.ascii_lowercase * 2
    words = sys.argv[2].split()  # array of words (into the str parameter)

    possibilties = []  # array of possibilites for each word find (reset each new word to place for new try)
    phrase_final = []
    word_possible = [] # array with firstword find for probably word (search by occurence)
    word_possible_formatted = {} # same as word_possible but formatted for final render
    word_possible_formatted_full = {} # same as word_possible_formatted with full list of possible word

    for word in words:
        possibilties.clear()  # clear each itteration to let place for the next word
        #print("\n" + Fore.YELLOW + "For string : " + word)
        print("\n" + "For string : " + word)
        #print(Fore.WHITE + "")
        for turn,shift in enumerate(range(1, 27)):
            # print(Fore.WHITE + ''.join([alphabet[alphabet.index(x) + shift] if x in alphabet else x for x in word]))
            possibilties.append("".join([alphabet[alphabet.index(x) + shift] if x in alphabet else x for x in word.lower()]))

            #basic search by same word in dico
            motResult = search(shift, possibilties, lines, word.lower(),turn)

            #render + checking words found and not found for display of all possibilities if not matched
            word_found_count = 0
            word_notFound_count = 0
            if len(motResult[0]) > 0 :
                phrase_final.append(motResult[0])
                word_found_count += 1
            if word_found_count == 0 and turn == 24:
                #print( Fore.RED + " 0 words matched")
                print(" 0 words matched")
                #print(Fore.WHITE + "")
                word_notFound_count += 1


                most_probable = []
                char_from_word_not_found = []

                for index,char_word in enumerate(word): #char in word input not find during the resolution
                    char_from_word_not_found.append(char_word)


                print(char_from_word_not_found)
                # print(char_from_word_not_found)
                print(Counter(char_from_word_not_found))
                print(word)  # word => mot non trouvé


                for word_dico in motResult[1]:
                    count_char_word_dico = Counter(word_dico)
                    #print(count_char_word_dico.most_common()[0]) # return letter most present in the word
                    count_char_word_input = Counter(word)
                    #print("input" + str(count_char_word_input.most_common()[0]))
                    if count_char_word_dico.most_common()[0] == count_char_word_input.most_common()[0]: #0 return the character most common in the str
                        most_probable.append(word_dico)
                print("Mot probablé list : ", most_probable, " for the word ", word)


                if len(most_probable) > 0 :
                    word_possible.append(most_probable[0])
                    word_possible_formatted.__setitem__(word, most_probable[0])
                    word_possible_formatted_full.__setitem__(word, most_probable)


    print("\n\n")
    print("")
    print("# ======================= #")
    print("#     ANALYSE RESULTS     #")
    print("# ======================= #")
    print("\n")
    #phrase final (si tous matched parfaitement)
    decrypt_phrase = "Votre phrase decrypter : " + ' - '.join(str(v) for v in phrase_final)
    print(str(decrypt_phrase))
    print("\n\n")
    #Mot plausible
    print("#     ----------------     #")
    print("#     ONE POISSIBILITY     #")
    print("                            ")
    print("#     ----------------     #")
    print("\n")
    print("Certains de vos mots n'ont pas matché, voici une possibilité : ", word_possible_formatted)
    print("\n\n")
    #list detailles
    print("#     ````````````````    #")
    print("#     ALL POSSIBILITES    #")
    print("                           ")
    print("#     ````````````````    #")
    print("\n")
    #for index,element in enumerate(word_possible_formatted_full):
    for key, words in word_possible_formatted_full.items():
        print("word : " + key)
        print(words)
        print("\n")



#invalid arguments
else:
    #print(Fore.RED + "Args not valid, please first its dic and second its string!")
    print("Args not valid, please first its dic and second its string!")