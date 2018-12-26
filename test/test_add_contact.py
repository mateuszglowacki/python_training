# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("TestName", "TestMiddleName", "TestLastName", "TestNickName", "TestTitle",
        "TestCompany", "TestAddress", "111111111", "222222222", "333333333", "444444444",
        "testmail1@test.com", "testmail2@test.com", "testmail3#test.com", "test.com", "1",
        "January", "1990", "1", "February", "2000", "TestNdAddress", "TestHome", "TestNotes"))
    app.session.logout()
