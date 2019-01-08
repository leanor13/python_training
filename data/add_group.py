from model.group import Group
import random
import string


constant = [
    Group(gr_name="name", gr_header="header", gr_footer="footer"),
    Group(gr_name="name2", gr_header="header2", gr_footer="footer2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    # generate string of random length and random symbols
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_punctuation(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    # generate string of random length and random symbols
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata_no_punctuation = [Group(gr_name="", gr_header="", gr_footer="")] + [
    Group(gr_name=random_string("name", 10), gr_header=random_string("header", 20), gr_footer=random_string("footer", 20))
    for i in range(2)
]


testdata_combination = [
    Group(gr_name=name, gr_header=header, gr_footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]


testdata = [Group(gr_name="", gr_header="", gr_footer="")] + [
    Group(gr_name=random_string_punctuation("name", 10), gr_header=random_string_punctuation("header", 20),
          gr_footer=random_string_punctuation("footer", 20))
    for i in range(2)
]