

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def fill_form(self, Contact):
        # fill in form
        self.change_field_value("firstname", Contact.first_name)
        self.change_field_value("middlename", Contact.middle_name)
        self.change_field_value("lastname", Contact.last_name)
        self.change_field_value("nickname", Contact.nick_name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, Contact):
        wd = self.app.wd
        self.open_contacts_page()
        # click on add new
        wd.find_element_by_link_text("add new").click()
        self.fill_form(Contact)
        # submit form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # delete first contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        self.open_contacts_page()

    def edit_first_contact(self, Contact):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_form(Contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_contacts_page()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))












