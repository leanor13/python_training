from model.group import Group
import random


def test_modify_group(app, db, json_group_modiff, check_ui):
    group = json_group_modiff
    if len(db.get_group_list()) == 0:
        app.group.create(Group(gr_name="Created for Group Modification Test"))
    old_groups = db.get_group_list()

    # choose group that will be modified
    chosen_group = random.choice(old_groups)
    group.gr_id = chosen_group.gr_id
    app.group.modify_group_by_id(chosen_group.gr_id, group)
    new_groups = db.get_group_list()
    old_groups.remove(chosen_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(gr):
            return Group(gr_id=gr.gr_id, gr_name=gr.gr_name.strip())

        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                             key=Group.id_or_max)
