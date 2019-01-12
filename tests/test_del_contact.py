from model.contact import Contact
import random
import re


def test_some_contact_deletion(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Created for deletion"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.contact_id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(cn):
            return Contact(contact_id=cn.contact_id, first_name=re.sub(r'\s+', ' ', cn.first_name.strip()),
                           last_name=re.sub(r'\s+', ' ', cn.last_name.strip()))

        ui_contacts = sorted(app.contact.get_simple_contact_list(), key=Contact.id_or_max)
        db_contacts = sorted(map(clean, db.get_contact_list()), key=Contact.id_or_max)

        assert ui_contacts == db_contacts

