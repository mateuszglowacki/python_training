# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("TestName", "TestMiddleName", "TestLastName", "TestNickName", "TestTitle",
        "TestCompany", "TestAddress", "111111111", "222222222", "333333333", "444444444",
        "testmail1@test.com", "testmail2@test.com", "testmail3#test.com", "test.com", "1",
        "January", "1990", "1", "February", "2000", "TestNdAddress", "TestHome", "TestNotes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
