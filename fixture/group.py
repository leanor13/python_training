

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.gr_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.gr_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.gr_footer)

    def create(self, group):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to groups page
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # delete first group
        wd.find_element_by_name("delete").click()
        # return to groups page
        self.return_to_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # click on Edit button
        wd.find_element_by_name("edit").click()
        self.fill_form(group)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()











