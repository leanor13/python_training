from model.group import Group
import random
from generator.group import random_string


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(gr_name="Created for Group Modification Test"))
    old_groups = db.get_group_list()
    chosen_group = random.choice(old_groups)
    group = Group(gr_name=random_string("Modiff", 13), gr_footer=random_string("Modiff", 13),
                  gr_header=random_string("Modiff", 13), gr_id=chosen_group.gr_id)
    app.group.modify_group_by_id(chosen_group.gr_id, group)
    new_groups = db.get_group_list()
    old_groups.remove(chosen_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(gr):
            return Group(gr_id=gr.gr_id, gr_name=gr.gr_name.strip())

        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(gr_name="Created for Group Deletion Test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(gr_header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
