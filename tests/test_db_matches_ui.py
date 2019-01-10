from model.group import Group
from timeit import timeit


def test_compare_timing(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))

    def clean(group):
        return Group(gr_id=group.gr_id, gr_name=group.gr_name.strip())

    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(gr_id=group.gr_id, gr_name=group.gr_name.strip())

    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)




