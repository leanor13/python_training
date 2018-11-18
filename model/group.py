from sys import maxsize


class Group:

    def __init__(self, gr_name=None, gr_header=None, gr_footer=None, gr_id=None):
        self.gr_name = gr_name
        self.gr_header = gr_header
        self.gr_footer = gr_footer
        self.gr_id = gr_id

    def __repr__(self):
        return "%s:%s" % (self.gr_id, self.gr_name)

    def __eq__(self, other):
        return (self.gr_id is None or other.gr_id is None or self.gr_id == other.gr_id) \
               and self.gr_name == other.gr_name

    def id_or_max(self):
        if self.gr_id:
            return int(self.gr_id)
        else:
            return maxsize





