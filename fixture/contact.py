

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact(self, Contact):
        wd = self.app.wd
        # click on add new
        wd.find_element_by_link_text("add new").click()
        # fill in form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nick_name)
        # submit form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
