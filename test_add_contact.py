# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.create_contact(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def create_contact(self, wd):
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("TestName")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("TestMiddleName")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("TestLastName")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("TestNickName")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("TestTitle")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("TestCompany")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("TestAddress")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("111111111")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("222222222")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("333333333")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("444444444")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("testmail1@test.com")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("testmail2@test.com")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("testmail3#test.com")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("test.com")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("February")
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("TestSecondaryAddress")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("TestHome")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("TestNotes")
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
