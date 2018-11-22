from model.contact import Contact
from random import randrange


def test_some_contact_deletion(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Created for deletion"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) == app.contact.count() + 1
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


