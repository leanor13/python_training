#-*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(gr_name="First Test Group", gr_header="Test", gr_footer="Test footer"))


def test_add_empty_group(app):
    app.group.create(Group(gr_name="", gr_header="", gr_footer=""))

