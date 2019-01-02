from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # init contact edition
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact
        self.fill_contact_form(new_contact_data)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.mainaddress)
        self.change_field_value("home", contact.phone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_dropdown_value("bday", contact.bday)
        self.change_dropdown_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_dropdown_value("aday", contact.aday)
        self.change_dropdown_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.secondaryaddress)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_dropdown_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.switch_to_default_content()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
