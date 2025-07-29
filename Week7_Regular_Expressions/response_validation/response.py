from validator_collection import checkers
def main():
    email = input("Enter email: ")
    email_check(email)

def email_check(email):
    if checkers.is_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__" :
    main()