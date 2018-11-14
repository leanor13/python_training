# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(gr_name="First Test Group Edited", gr_header="Test Edited", gr_footer="Test footer Edited"))
