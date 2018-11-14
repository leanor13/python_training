
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(gr_name="New group 2"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(gr_header="New header"))
