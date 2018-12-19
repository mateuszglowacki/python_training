# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("TestName")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("TestMiddleName")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("TestLastName")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("TestNickName")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("TestTitle")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("TestCompany")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("TestAddress")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("111111111")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("222222222")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("333333333")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("444444444")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("testmail1@test.com")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("testmail2@test.com")
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("testmail3#test.com")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("test.com")
        Select(driver.find_element_by_name("bday")).select_by_visible_text("1")
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("January")
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1990")
        Select(driver.find_element_by_name("aday")).select_by_visible_text("1")
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("February")
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("2000")
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("TestSecondaryAddress")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("TestHome")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("TestNotes")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("home").click()
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
