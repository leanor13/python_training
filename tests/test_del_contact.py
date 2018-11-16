from model.contact import Contact


def test_first_contact_deletion(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Created for deletion"))
    app.contact.delete_first_contact()
