# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import re


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


testdata = [Contact(first_name="", middle_name="", last_name="", nick_name="", email="", address="")] + [
    Contact(first_name=random_string("f_name", 10), last_name=random_string("l_name", 10),
            nick_name=random_string("n_name", 10), middle_name=random_string("m_name", 10),
            address=random_string("address", 30), email=random_email("email", 20), email2=random_email("email2", 20),
            email3=random_email("email3", 20), home_phone=random_phone('812', 10),
            mobile_phone=random_phone('911', 15), work_phone=random_phone("000", 10), fax_phone=random_phone("777", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_contact_creation(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




