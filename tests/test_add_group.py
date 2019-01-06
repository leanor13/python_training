# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    # generate string of random length and random symbols
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_punctuation(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    # generate string of random length and random symbols
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(gr_name="", gr_header="", gr_footer="")] + [
    Group(gr_name=random_string("name", 10), gr_header=random_string("header", 20), gr_footer=random_string("footer", 20))
    for i in range(5)
]


testdata_combination = [
    Group(gr_name=name, gr_header=header, gr_footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]


testdata_punctuation = [Group(gr_name="", gr_header="", gr_footer="")] + [
    Group(gr_name=random_string_punctuation("name", 10), gr_header=random_string_punctuation("header", 20),
          gr_footer=random_string_punctuation("footer", 20))
    for i in range(5)
]


@pytest.mark.parametrize("group", testdata_punctuation, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
