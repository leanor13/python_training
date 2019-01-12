import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        gr_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                gr_list.append(Group(gr_id=str(id), gr_name=name, gr_header=header, gr_footer=footer))
        finally:
            cursor.close()
        return gr_list

    def get_contact_list(self):
        cont_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                cont_list.append(Contact(contact_id=str(id), first_name=firstname, last_name=lastname))
        finally:
            cursor.close()
        return cont_list

    def destroy(self):
        self.connection.close()
