from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys
import re


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contact_modiff.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + re.sub("['`\"]", "", string.punctuation) + " "*10
    # generate string of random length and random symbols
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "_" + "-" + "*" + "#" + "%" + ";" + "." + "," + "@"*10
    # generate string of random length and random symbols
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits + re.sub("['`\"]", "", string.punctuation)
    # generate string of random length and random symbols
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(first_name=random_string("f_name", 10), last_name=random_string("l_name", 10),
            nick_name=random_string("n_name", 10), middle_name=random_string("m_name", 10),
            address=random_string("address", 30), email=random_email("email", 20), email2=random_email("email2", 20),
            email3=random_email("email3", 20), home_phone=random_phone('812', 10),
            mobile_phone=random_phone('911', 15), work_phone=random_phone("000", 10), fax_phone=random_phone("777", 10))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

