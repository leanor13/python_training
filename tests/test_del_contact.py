from model.contact import Contact


def test_first_contact_deletion(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Created for deletion"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts) + 1
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


