import pymysql.cursors
from model.group import Group


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


    def destroy(self):
        self.connection.close()




