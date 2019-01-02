from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact("EditName", "EditMiddleName", "EditLastName", "EditNickName", "EditTitle",
        "EditCompany", "EditAddress", "111111111", "222222222", "333333333", "444444444",
        "editmail1@test.com", "editmail2@test.com", "editmail3@test.com", "edit.com", "1",
        "January", "1990", "1", "February", "2000", "EditNdAddress", "EditHome", "EditNotes"))
    app.session.logout()


def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New name"))
    app.session.logout()


def test_modify_contact_title(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(title="New title"))
    app.session.logout()
