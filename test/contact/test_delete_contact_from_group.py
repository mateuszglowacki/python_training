# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, db, db2):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_relations_list()) == 0:
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        groups = db.get_group_list()
        group = random.choice(groups)
        app.contact.add_contact_to_group(contact, group)
    old_relations = db.get_relations_list()
    pair = random.choice(old_relations)
    old_contacts_in_group_list = db2.get_contacts_in_group(Group(id=pair[1]))
    old_contacts_not_in_group_list = db2.get_contacts_not_in_group(Group(id=pair[1]))
    app.contact.del_contact_from_group(pair[0], pair[1])
    new_relations = db.get_relations_list()
    new_contacts_in_group_list = db2.get_contacts_in_group(Group(id=pair[1]))
    new_contacts_not_in_group_list = db2.get_contacts_not_in_group(Group(id=pair[1]))
    assert len(old_relations) - 1 == len(new_relations)
    assert len(old_contacts_in_group_list) - 1 == len(new_contacts_in_group_list)
    assert len(old_contacts_not_in_group_list) + 1 == len(new_contacts_not_in_group_list)
