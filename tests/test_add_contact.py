# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_creation(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(first_name="Test Contact", middle_name="Tes_midd", last_name="T", nick_name="L"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)



