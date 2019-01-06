from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact("EditName", "EditMiddleName", "EditLastName", "EditNickName", "EditTitle",
        "EditCompany", "EditAddress", "111111111", "222222222", "333333333", "444444444",
        "editmail1@test.com", "editmail2@test.com", "editmail3@test.com", "edit.com", "1",
        "January", "1990", "1", "February", "2000", "EditNdAddress", "EditHome", "EditNotes"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(title="New title"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
