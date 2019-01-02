from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="editedName", header="editedHeader", footer="editedFooter"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
