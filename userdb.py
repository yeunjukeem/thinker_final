# dummy emails

import random
import string
import pymysql

# for the random string
letter_set = string.ascii_lowercase
random_data = random.sample(letter_set, 4)

# join(): attaching each random 4 characters

data = "". join(random_data)


# random, but genereating text length ranged as 4 to 6
text_length = range(4,6)
email = ['@naver.com', '@gmail.com', '@hanmail.net','@yahoo.com']

email_list = []
for i in range(1000):
    if(len(email_list) == 100):
        break

    random_data = random.sample(letter_set, random.choice(text_length))

    data = "".join(random_data) + random.choice(email)

    if(data not in email_list):
        email_list.append(data)

# generating dummy ID
uname = string.ascii_lowercase
rand_name = random.sample(uname, 5)

data2 = "".join(rand_name)
print(data2)

text_length = range(6,9)

username = []
for i in range(1000):
    if(len(username) == 100):
        break
    rand_name = random.sample(uname, random.choice(text_length))
    data2 = "".join(rand_name)
    if(data not in username):
        username.append(data2)

# password
password = '1234'

_db = pymysql.connect(
    host = 'kimmm.mysql.pythonanywhere-services.com',
    user = 'kimmm',
    password = 'pyflask9',
    db = 'kimmm$thinker',
    port = 3306
)

cursor = _db.cursor(pymysql.cursors.DictCursor)

sql = """
    INSERT
    INTO
    user
    VALUES
    (%s,%s, %s)
"""

for i in range(100):
    cursor.execute(sql, [email_list[i], username[i], password])

    _db.commit()