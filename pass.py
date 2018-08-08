import string
import random
import csv
import os.path
import sys

# print("enter the name of the website")
name = input("enter the name of the website: ")

filename = "names.csv"
file_exists = os.path.isfile(filename)

def id_generator(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

class NewPass():
    def __init__ (self, site):
        self.site = site
        try:
            f = open(filename, "x")
        except:
             print("File exists:")
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['web_site', 'pass']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'web_site': self.site , 'pass': id_generator()})

        return print("new pass created!")

newpassword = NewPass(name)

