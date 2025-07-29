import re
def main():
    question = input("Date: ").strip()
    the_1stconverter(question)

def the_1stconverter(question):
    pattern = "/"
    text = question
    match =re.search(pattern , text)

    if match:
        month,date,year = question.split(sep = "/")

        if month.isalpha():
            while True:
                question = input("Date: ").strip()

        if 1<= int(date) <=9:
            new_date = "0"+str(date)
        elif int(date) > 31 :
            while True:
                question = input("Date: ").strip()
        else:
            new_date = date

        if 1<= int(month) <=9:
            new_month = "0"+str(month)
        elif int(month) > 12:
            while True:
                question = input("Date: ").strip()
        else:
            new_month = month

        print(f"{year}-{new_month}-{new_date}" , end=" ")
    else:
        the_2ndconverter(question)

def the_2ndconverter(question):
    while True:
        try:
            months = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"

        ]
            numeric_form = ["01" , "02" , "03" , "04" , "05" , "06" , "07" , "08" , "09" , "10" , "11" , "12" ]
            all_months =dict(zip(months,numeric_form))


            one_part,year = question.split(sep = ", ")
            month,date = one_part.split(sep = " ")

            if month.isdigit():
                    while True:
                        question = input("Date: ").strip()

            for month in months:
                    if month in question:
                        if 1<= int(date) <=9:
                            new_date = "0"+str(date)
                        elif int(date) > 31 :
                            while True:
                                question = input("Date: ").strip()
                        else:
                            new_date = date

                        print(f"{year}-{all_months[month]}-{new_date}")
            break
        except ValueError:
                while True:
                    question = input("Date: ").strip()
                    continue
main()