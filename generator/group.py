from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    # generate string of random length and random symbols
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_punctuation(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    # generate string of random length and random symbols
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(gr_name="", gr_header="", gr_footer="")] + [
    Group(gr_name=random_string_punctuation("name", 10), gr_header=random_string_punctuation("header", 20),
          gr_footer=random_string_punctuation("footer", 20))
    for i in range(n)
]


testdata_no_punctuation = [Group(gr_name="", gr_header="", gr_footer="")] + [
    Group(gr_name=random_string("name", 10), gr_header=random_string("header", 20),
          gr_footer=random_string("footer", 20))
    for i in range(n)
]


testdata_combination = [
    Group(gr_name=name, gr_header=header, gr_footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


