import re

email = input("Enter Your Mail Id: ")
psswd = input("Enter Your Password: ")


email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$)")
psswd_pattern = re.compile(r"[a-zA-z0-9%_%@#*]{8,}\d")

matched_email = email_pattern.match(email)
matched_psswd = psswd_pattern.match(psswd)
if bool(matched_email) and bool(matched_psswd):
    print(
        f"Your \nEmail: {email} \nPassword: {psswd} \nis verified!!")
elif bool(matched_email):
    print(
        f"Your \nEmail: {email} is verified \nPassword: {psswd} is incorrect")
else:
    print(
        f"Your \nPassword: {psswd} is verified \nEmail: {email} is incorrect")
