import re

def main():
    user_email = input("Please enter your email: ")
    email_test_reg(user_email)


def email_test_reg(user_email):
    if matches := bool(re.search(r"^[^\.][\w!#$%&'*+\-#\/=?^`{|}~]{1,64}@[\w\-\.]{0,255}(gmail|hotmail|outlook|yahoo)\.(com|net|org|co\.uk)$", user_email, flags=re.IGNORECASE | re.ASCII)):
        return matches


if __name__ == "__main__":
    main()