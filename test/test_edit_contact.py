from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact("EditName", "EditMiddleName", "EditLastName", "EditNickName", "EditTitle",
        "EditCompany", "EditAddress", "111111111", "222222222", "333333333", "444444444",
        "editmail1@test.com", "editmail2@test.com", "editmail3#test.com", "edit.com", "1",
        "January", "1990", "1", "February", "2000", "EditNdAddress", "EditHome", "EditNotes"))
    app.session.logout()
