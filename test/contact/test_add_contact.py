# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact("TestName", "TestMiddleName", "TestLastName", "TestNickName", "TestTitle",
        "TestCompany", "TestAddress", "111111111", "222222222", "333333333", "444444444",
        "testmail1@test.com", "testmail2@test.com", "testmail3#test.com", "test.com", "1",
        "January", "1990", "1", "February", "2000", "TestNdAddress", "TestHome", "TestNotes"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)