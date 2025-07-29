def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    my_list =[]
    for i in s:
        my_list.append(i)

    if len(my_list) == 2:
        if my_list[0].isalpha() and my_list[1].isalpha():
            return True
        else:
            return False

    elif len(my_list) == 3 and my_list[2] != '0':
        if my_list[0].isalpha() and  my_list[1].isalpha() and my_list[2].isnumeric() :
            return True
        elif my_list[0].isalpha() and my_list[1].isalpha() and my_list[2].isalpha():
            return True
        else:
            return False

    elif len(my_list) == 4 and my_list[2] != '0':
        if my_list[0].isalpha() and  my_list[1].isalpha() and  my_list[2].isalpha()  and my_list[3].isnumeric() :
            return True
        elif my_list[0].isalpha() and my_list[1].isalpha() and my_list[2].isalpha() and  my_list[3].isalpha() :
            return True
        elif my_list[0].isalpha() and my_list[1].isalpha() and my_list[2].isnumeric() and  my_list[3].isnumeric() :
            return True
        else:
            return False

    elif len(my_list) == 5 and my_list[2] != '0':
        if my_list[0].isalpha() and  my_list[1].isalpha() and  my_list[2].isalpha() and my_list[3].isalpha() and my_list[4].isnumeric():
            return True
        elif my_list[0].isalpha() and my_list[1].isalpha() and my_list[2].isalpha() and my_list[3].isalpha() and my_list[4].isalpha():
            return True
        elif my_list[0].isalpha() and my_list[1].isalpha() and my_list[2].isalpha() and my_list[3].isnumeric() and  my_list[4].isnumeric() :
            return True
        elif my_list[0].isalpha() and my_list[1].isalpha() and my_list[2].isnumeric() and my_list[3].isnumeric() and  my_list[4].isnumeric() :
            return True
        else:
            return False

    elif len(my_list) == 6 and my_list[2] != '0':
        if my_list[0].isalpha() and  my_list[1].isalpha() and  my_list[2].isalpha() and my_list[3].isalpha() and my_list[4].isalpha() and my_list[5].isnumeric():
            return True
        elif my_list[0].isalpha() and my_list[1].isalpha() and my_list[2].isalpha() and my_list[3].isalpha() and my_list[4].isalpha() and my_list[5].isalpha():
            return True
        elif my_list[0].isalpha() and my_list[1].isalpha() and my_list[2].isalpha() and my_list[3].isalpha() and my_list[4].isnumeric() and  my_list[5].isnumeric() :
            return True
        elif my_list[0].isalpha() and my_list[1].isalpha() and my_list[2].isalpha() and my_list[3].isnumeric() and my_list[4].isnumeric() and  my_list[4].isnumeric() :
            return True
        elif my_list[0].isalpha() and my_list[1].isalpha() and my_list[2].isnumeric() and my_list[3].isnumeric() and my_list[4].isnumeric() and  my_list[4].isnumeric() :
            return True
        else:
            return False

    else :
        return False

if __name__ == "__main__":
    main()