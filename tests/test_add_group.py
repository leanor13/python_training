#-*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(gr_name="First Test Group", gr_header="Test", gr_footer="Test footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(gr_name="", gr_header="", gr_footer=""))
    app.logout()
