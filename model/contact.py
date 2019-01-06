from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None,
                 address=None,
                 email=None, email2=None, email3=None, all_emails_from_home_page=None,
                 home_phone=None, mobile_phone=None, work_phone=None,
                 fax_phone=None, nick_name=None, all_phones_from_home_page=None,
                 contact_id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.contact_id = contact_id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.contact_id, self.last_name, self.first_name, self.home_phone, self.email)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None
                or self.contact_id == other.contact_id) \
               and self.last_name == other.last_name and self.first_name == other.first_name

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize


