# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_creation(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Test Contact_now", middle_name="Tes_midd", last_name="T_now", nick_name="L")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




