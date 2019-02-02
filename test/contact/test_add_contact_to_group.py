# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, db2):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    groups = db.get_group_list()
    group = random.choice(groups)
    old_relations = db2.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_relations = db2.get_contacts_in_group(group)
    assert len(old_relations) + 1 == len(new_relations)
