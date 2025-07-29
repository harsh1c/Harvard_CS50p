def convert():
    emoji = input('how are you ? ')
    emoji = emoji.replace(':)' , '🙂')
    emoji = emoji.replace(":(" , "🙁")
    return emoji

def main():
    print(convert())

main()