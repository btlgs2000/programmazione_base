import string

piggy_words = []
vowels = ["a", "e", "i", "o", "u", "y"]
consonants = [letter for letter in string.ascii_lowercase if letter not in vowels]

sentence = input("Inserisci una frase in inglese che verrà tradotta in piggy latin: ")

# Prende una stringa e restituisce una lista di parole
# "a b c" -> ["a", "b", "c"]
words = sentence.split(" ")

for word in words:
    # testa se la parola comincia per vocale
    if word[0] in vowels:
        piggy_words.append(word + "yay")
    # testa se la parola comincia per consonante
    elif word[0] in consonants:
        while word[0] in consonants:
            word = word[1:] + word[0]
        piggy_words.append(word + "ay")
    else:
        piggy_words.append(word)
        
piggy_sentence = " ".join(piggy_words)

print(piggy_sentence)
