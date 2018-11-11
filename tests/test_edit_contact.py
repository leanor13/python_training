# -*- coding: utf-8 -*-
from model.contact import Contact


def test_first_contact_editing(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="Edited Contact First", middle_name="Edited Contact Mid", last_name="Edited Last", nick_name="Edited Nick"))
    app.session.logout()

