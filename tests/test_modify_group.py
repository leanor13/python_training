from model.group import Group
from random import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(gr_name="Created for Group Modification Test"))
    old_groups = db.get_group_list()
    id = random.choice(old_groups).gr_id
    group = Group(gr_name="MODIFF", gr_id=old_groups[id].gr_id)
    app.group.modify_group_by_id(id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert old_groups == new_groups


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(gr_name="Created for Group Deletion Test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(gr_header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
