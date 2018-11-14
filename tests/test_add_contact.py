# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_creation(app):
    app.contact.create(Contact(first_name="Test Contact", middle_name="Tes_midd", last_name="T", nick_name="L"))


