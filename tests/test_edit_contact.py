# -*- coding: utf-8 -*-
from model.contact import Contact


def test_first_contact_editing_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Created for editing"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Was really created for editing", contact_id=old_contacts[0].contact_id)
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact.last_name = old_contacts[0].last_name
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#def test_first_contact_editing_middle_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="Created for editing2"))
#    app.contact.edit_first_contact(Contact(middle_name="Edited Contact Mid 2"))


#def test_first_contact_editing_last_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="Created for editing2"))
#    app.contact.edit_first_contact(Contact(last_name="Edited Last 2"))


#def test_first_contact_editing_nick_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="Created for editing2"))
#    app.contact.edit_first_contact(Contact(nick_name="Edited Nick 2"))

