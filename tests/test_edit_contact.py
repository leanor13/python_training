# -*- coding: utf-8 -*-
from model.contact import Contact


def test_first_contact_editing_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Created for editing"))
    app.contact.edit_first_contact(Contact(first_name="Was really created for editing"))


def test_first_contact_editing_middle_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Created for editing2"))
    app.contact.edit_first_contact(Contact(middle_name="Edited Contact Mid 2"))


def test_first_contact_editing_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Created for editing2"))
    app.contact.edit_first_contact(Contact(last_name="Edited Last 2"))


def test_first_contact_editing_nick_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Created for editing2"))
    app.contact.edit_first_contact(Contact(nick_name="Edited Nick 2"))

