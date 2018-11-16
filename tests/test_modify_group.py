
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="Created for Group Modification Test"))
    app.group.modify_first_group(Group(gr_name="New group 2"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="Created for Group Deletion Test"))
    app.group.modify_first_group(Group(gr_header="New header"))
