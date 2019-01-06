from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("index.php") and len(wd.find_elements_by_link_text("Last name")) > 0
                and len(wd.find_elements_by_link_text("All phones")) > 0):
            wd.find_element_by_link_text("home").click()

    def fill_form(self, contact):
        # fill in form
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nick_name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # click on add new
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        # submit form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        self.open_contacts_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_contacts_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        self.open_contact_to_edit_by_index(0)
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_contacts_page()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            # for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            #    last_name = element.find_element_by_css_selector("td:nth-child(2)").get_attribute("innerText")
            #    first_name = element.find_element_by_css_selector("td:nth-child(3)").get_attribute("innerText")
            #    id = element.find_element_by_name("selected[]").get_attribute("value")
            #    self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, contact_id=id))
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                id = row.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, contact_id=id,
                                                  home_phone= all_phones[0], mobile_phone= all_phones[1], work_phone= all_phones[2]))

        return list(self.contact_cache)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        faxphone = wd.find_element_by_name("fax").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, contact_id=id, home_phone=homephone, mobile_phone=mobilephone,
                       work_phone=workphone, fax_phone=faxphone, middle_name=middlename, nick_name=nickname)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        faxphone = re.search("F: (.*)", text).group(1)
        return Contact(home_phone=homephone, mobile_phone=mobilephone, work_phone=workphone, fax_phone=faxphone)






















