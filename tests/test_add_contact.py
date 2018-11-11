# -*- coding: utf-8 -*-
from model.contact import Contact

def test_contact_creation(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.contact(Contact(first_name="Test Contact", middle_name="Tes_midd", last_name="T", nick_name="L"))
    app.session.logout()


