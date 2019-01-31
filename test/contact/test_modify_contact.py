from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact_to_change = random.choice(old_contacts)
    contact = Contact("EditName", "EditMiddleName", "EditLastName", "EditNickName", "EditTitle",
        "EditCompany", "EditAddress", "111111111", "222222222", "333333333", "444444444",
        "editmail1@test.com", "editmail2@test.com", "editmail3@test.com", "edit.com", "1",
        "January", "1990", "1", "February", "2000", "EditNdAddress", "EditHome", "EditNotes")
    contact.id = contact_to_change.id
    app.contact.modify_contact_by_id(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[old_contacts.index(contact_to_change)] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    def clean(contact):
        return Contact(id=contact.id, firstname=" ".join(contact.firstname.split()), lastname=" ".join(contact.lastname.split()))
    if check_ui:
        assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_contact_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(firstname="New name"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_contact_title(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(title="New title"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
