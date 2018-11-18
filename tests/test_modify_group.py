from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="Created for Group Modification Test"))
    old_groups = app.group.get_group_list()
    group = Group(gr_name="New group 2", gr_id=old_groups[0].gr_id)
#    group.gr_id = old_groups[0].gr_id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(gr_name="Created for Group Deletion Test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(gr_header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
