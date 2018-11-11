# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact_creation(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.add_contact(Contact(first_name="Test Contact", middle_name="Tes_midd", last_name="T", nick_name="L"))
    app.session.logout()


