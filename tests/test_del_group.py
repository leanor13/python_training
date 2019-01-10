# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(gr_name="Created for Group Deletion Test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.gr_id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        def clean(gr):
            return Group(gr_id=gr.gr_id, gr_name=gr.gr_name.strip())

        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
