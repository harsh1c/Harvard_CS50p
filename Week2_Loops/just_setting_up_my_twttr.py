def main():
    prompt = input("Input: ")
    new_word = shorten(prompt)

    print(new_word)

def shorten(word):
    vowels = ["a" , "e" , "i" , "o" , "u" , "A" , "E" , "I" , "O" , "U"]
    consonants = []
    print("Output: " , end = "")

    for i in word:
        if i in vowels:
            continue
        else:
            consonants.append(i)
    return "".join(consonants)



if __name__ == "__main__":
    main()