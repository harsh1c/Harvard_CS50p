def main():
    the_output()

def the_output():

    try:
        my_list =[]

        while True:
            item = input("").upper()

            my_list.append(item)
    except EOFError:
        sorted_list = sorted(my_list)
        my_dict ={}
        for i in sorted_list:
            my_dict[i] = sorted_list.count(i)

        for i in my_dict:
            print(my_dict[i], i)


main()