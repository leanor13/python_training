# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="Created for Group Deletion Test"))
    app.group.delete_first_group()
