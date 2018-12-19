# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/index.php")
        # login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        # open groups page
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("testname")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("testheader")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("testfooter")
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to groups page
        wd.find_element_by_link_text("group page").click()
        # logout
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
