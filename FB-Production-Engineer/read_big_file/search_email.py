# read innate file and parse the strings to count how many times an email address is found


import re

# s = 'Hello from shubhamg199630@gmail.com to priya@yahoo.com about the ' \
#     'meeting @2PM and then we will go to the bakery with shubhamg199630@gmail.com'

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

email_count = {}
with open('test.txt', 'r') as fob:
    for line in fob:
        for word in line.split(' '):
            if re.fullmatch(regex, word):
                if word in email_count:
                    email_count[word] += 1
                else:
                    email_count[word] = 1
    fob.close()
print(email_count)
