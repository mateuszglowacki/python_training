# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from application import Application


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_add_contact(self):
        self.app.login("admin", "secret")
        self.app.create_contact(Contact("TestName", "TestMiddleName", "TestLastName", "TestNickName", "TestTitle",
                            "TestCompany", "TestAddress", "111111111", "222222222", "333333333", "444444444",
                            "testmail1@test.com", "testmail2@test.com", "testmail3#test.com", "test.com", "1",
                            "January", "1990", "1", "February", "2000", "TestNdAddress", "TestHome", "TestNotes"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
