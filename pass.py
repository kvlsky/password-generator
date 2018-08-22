import string
import random
import csv
import os.path
import sys

website_ = input("enter the name of the website: ")
login_ = input("enter your login: ")
size_ = input("enter password size: ")

while(int(size_) < 8):
    print("password is too short!")
    size_ = input("enter size for password: ")
    if int(size_) >= 8:
        break


filename = "names.csv"
file_exists = os.path.isfile(filename)

def id_generator(size=int(size_), chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

class NewPass():
    def __init__ (self, site, login):
        self.site = site
        self.login = login
        try:
            open(filename, "x")
        except:
             print("\nFile exists:",filename)
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['web_site','login', 'pass']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'web_site': self.site , 'login': self.login , 'pass': id_generator()})
        print("\nnew pass created!")

newpassword = NewPass(website_,login_)

