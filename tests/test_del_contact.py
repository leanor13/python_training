from model.contact import Contact


def test_first_contact_deletion(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Created for deletion"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) == app.contact.count() + 1
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


