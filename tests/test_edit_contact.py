# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import re


def test_contact_modification(app, db, json_contact_modiff, check_ui):
    contact = json_contact_modiff
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Created for editing"))
    old_contacts = db.get_contact_list()

    chosen_contact = random.choice(old_contacts)
    contact.contact_id = chosen_contact.contact_id
    app.contact.edit_contact_by_id(contact.contact_id, contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(chosen_contact)
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        def clean(cn):
            return Contact(contact_id=cn.contact_id, first_name=re.sub(r'\s+', ' ', cn.first_name.strip()),
                           last_name=re.sub(r'\s+', ' ', cn.last_name.strip()))

        ui_contacts = sorted(app.contact.get_simple_contact_list(), key=Contact.id_or_max)
        db_contacts = sorted(map(clean, db.get_contact_list()), key=Contact.id_or_max)

        assert ui_contacts == db_contacts

