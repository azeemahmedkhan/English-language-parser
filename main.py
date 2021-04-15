input_file = "input5.txt"
output_file = "output5.txt"

def create_list(file_name):
    list = []
    with open(file_name, 'r') as file:
        for line in file:
            for word in line.split():
                list.append(word.lower())
    return list

def input_from_file():
    global input_file
    f = open(input_file, "r")
    return f.readline()

def output_to_file():
    global output_file
    f = open(output_file, "w")
    if (flag == 1):
        f.write("Incorrect Structure")
    else:
        for i in reversed(range(len(list))):
            for j in range(len(list[i])):
                f.write(list[i][j] + " ")
            f.write("\n")
    return


def in_which_dic(n, v, a, p, pn, d, pr, c, word):
    if word in n or (word == "Noun"):
        return "Noun"
    if word in v:
        return "Verb"
    if word in a:
        return "Adjective"
    if word in p:
        return "Pronoun"
    if word in pn:
        return "Proper-Noun"
    if word in d:
        return "Determiner"
    if word in pr:
        return "Preposition"
    if word in c:
        return "conjunction"
    if(word == "S"):
        return "S"
    if(word == "NP"):
        return "NP"
    if(word == "Nominal"):
        return "Nominal"
    if(word == "VP"):
        return "VP"
    if(word == "PP"):
        return "PP"
    if(word == "Y"):
        return "Y"

if __name__ == "__main__":
    #terminals

    """
    n = ["flight", "breeze", "trip", "morning"]
    v = ["is", "prefer", "like", "need", "want", "fly", "do"]
    a = ["cheapest", "non-stop", "first", "latest", "other", "direct"]
    p = ["me", "you", "I", "it"]
    pn = ["chicago", "united"]
    d = ["the", "a", "an", "this", "these", "that"]
    pr = ["from", "to", "on", "near"]
    c = ["and", "or", "but"]"""

    n = create_list("Noun.txt")
    v = create_list("Verb.txt")
    a = create_list("Adjectives.txt")
    p = create_list("pronoun.txt")
    pn = create_list("proper_noun.txt")
    d = create_list("Determiners.txt")
    pr = create_list("preposition.txt")
    c = create_list("Conjunctions.txt")

    #variables
    S = ["NPVP"]
    NP = ["Pronoun", "Proper-Noun", "DeterminerNominal"]
    Nominal = ["NounNominal", "Noun"]
    VP = ["Verb", "VerbNP", "VerbNP", "VerbY", "VerbPP"]
    PP = ["PrepositionNP"]
    Y = ["NPPP"]

    input_string = input_from_file()
    words = []
    list = []

    for word in input_string.split():
        words.append(word.lower())

    flag = 0
    list.append(words[:])
    i = j = (len(words)) - 1

    if (i == 0):
        flag = 1
        print("Incorrect Structure")
        output_to_file()
        exit()

    while i != 0:
        #First Nominal will be evaluated
        while j != 0:
            if((j-1) == -1):
                break
            x = in_which_dic(n, v, a, p, pn, d, pr, c, words[j-1])
            y = in_which_dic(n, v, a, p, pn, d, pr, c, words[j])
            if (x == None) or (y == None):
                break
            str = x + y
            if str in Nominal:
                if (words[j-1] == "Noun"):
                    del words[j-1]
                    list.append(words[:])
                    i = i - 1
                    j = i
                    continue
                elif (x == "Noun"):
                    del words[j-1]
                    words.insert(j-1, "Noun")
                    list.append(words[:])
                    continue
            elif (y == "Noun"):
                if(x == "Noun" or x == "Determiner"):
                    del words[j]
                    words.insert(j, "Nominal")
                    list.append(words[:])
                    continue
            j = j - 1
            continue
            if((j - 1) == -1):
                j = i
                break
        j = i

        #Then Noun Phrase will be evaluated
        while (j != 0):
            if((j-1) == -1):
                break
            x = in_which_dic(n, v, a, p, pn, d, pr, c, words[j-1])
            y = in_which_dic(n, v, a, p, pn, d, pr, c, words[j])
            if (x == None) or (y == None):
                break
            str = x + y
            temp = in_which_dic(n, v, a, p, pn, d, pr, c, words[0])
            if temp in NP:
                del words[0]
                words.insert(0, temp)
                list.append(words[:])
                del words[0]
                words.insert(0, "NP")
                list.append(words[:])
                continue
            if y in NP:
                del words[j]
                words.insert(j, y)
                list.append(words[:])
                del words[j]
                words.insert(j, "NP")
                list.append(words[:])
                continue
            elif str in NP:
                del words[j-1]
                words.insert(j-1, x)
                list.append(words[:])
                del words[j-1]
                words.insert(j-1, "NP")
                del words[j]
                list.append(words[:])
                i = i - 1
                j = i
                continue
            j = j - 1
            continue
            if((j - 1) == -1):
                j = i
                break
        j = i

        #Then PP will be evaluated
        while (j != 0):
            if((j-1) == -1 ):
                break
            x = in_which_dic(n, v, a, p, pn, d, pr, c, words[j-1])
            y = in_which_dic(n, v, a, p, pn, d, pr, c, words[j])
            if (x == None) or (y == None):
                break
            str = x + y
            if str in PP:
                del words[j-1]
                words.insert(j-1, x)
                list.append(words[:])
                del words[j]
                del words[j-1]
                words.insert(j, "PP")
                i = i - 1
                j = i
                list.append(words[:])
                continue
            j = j - 1
            continue
            if((j - 1) == -1):
                j = i
                break
        j = i

        #Then Y will be evaluated
        while (j != 0):
            if((j-1) == -1 ):
                break
            x = in_which_dic(n, v, a, p, pn, d, pr, c, words[j-1])
            y = in_which_dic(n, v, a, p, pn, d, pr, c, words[j])
            if (x == None) or (y == None):
                break
            str = x + y
            if str in Y:
                del words[j]
                del words[j-1]
                words.insert(j-1, "Y")
                list.append(words[:])
                i = i - 1
                j = i
                continue
            j = j - 1
            continue
            if((j - 1) == -1):
                j = i
                break

        j = i
        #Then VP will be evaluated
        while j != 0:
            if((j-1) == -1 ):
                break
            x = in_which_dic(n, v, a, p, pn, d, pr, c, words[j-1])
            y = in_which_dic(n, v, a, p, pn, d, pr, c, words[j])
            if (x == None) or (y == None):
                break
            str = x + y
            if str in VP:
                del words[j-1]
                words.insert(j-1, "Verb")
                list.append(words[:])
                del words[j]
                del words[j-1]
                words.insert(j-1, "VP")
                i = i - 1
                j = i
                list.append(words[:])
                continue
            else:
                if y == "Verb":
                    del words[j]
                    words.insert(j, "Verb")
                    list.append(words[:])
                    del words[j]
                    words.insert(j, "VP")
                    list.append(words[:])
                    continue
            j = j - 1
            continue
            if((j - 1) == -1):
                j = i
                break

        j = i
        #Then S will be evaluated
        while (j != 0):
            if((j-1) == -1 ):
                break
            x = in_which_dic(n, v, a, p, pn, d, pr, c, words[j-1])
            y = in_which_dic(n, v, a, p, pn, d, pr, c, words[j])
            if (x == None) or (y == None):
                break
            str = x + y
            if str in S:
                del words[j]
                del words[j-1]
                words.insert(j-1, "S")
                i = i - 1
                j = i
                list.append(words[:])
                continue
            else:
                break
        if(i > 0) or (in_which_dic(n, v, a, p, pn, d, pr, c, words[0]) != "S"):
            flag = 1
        break



    if (flag == 1):
        print("Incorrect Structure")
    else:
        for i in reversed(range(len(list))):
            for j in range(len(list[i])):
                print(list[i][j], end = ' ')
            print()

    output_to_file()
