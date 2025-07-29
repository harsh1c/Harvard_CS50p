def main():
    prompt = input("Input: ")
    new_word = shorten(prompt)

    print(new_word)

def shorten(word):
    vovels = ["a" , "e" , "i" , "o" , "u" , "A" , "E" , "I" , "O" , "U" ]
    consonents = []
    print("Output: " , end = "")

    for i in word:
        if i in vovels:
            continue
        else:
            consonents.append(i)
    return "".join(consonents)



if __name__ == "__main__":
    main()