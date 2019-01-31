from model.group import Group
import random


def test_modify_first_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group_to_change = random.choice(old_groups)
    group = Group(name="editedName", header="editedHeader", footer="editedFooter", id=group_to_change.id)
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[old_groups.index(group_to_change)] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    if check_ui:
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name="New group"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#   app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
