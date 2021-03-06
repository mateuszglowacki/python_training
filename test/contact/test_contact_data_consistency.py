import re
from random import randrange
from model.contact import Contact


def test_phones_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    index = randrange(app.contact.count())
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.phone == contact_from_edit_page.phone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def test_contact_data_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.mainaddress == contact_from_edit_page.mainaddress
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def test_contact_data_on_home_page_with_db(app, db):
    def clean(contact):
        return Contact(id=contact.id, firstname=" ".join(contact.firstname.split()), lastname=" ".join(contact.lastname.split()), phone=contact.phone, mobile=contact.mobile, work=contact.work, phone2=contact.phone2, email1=" ".join(contact.email1.split()), email2=" ".join(contact.email2.split()), email3=" ".join(contact.email3.split()), mainaddress=" ".join(contact.mainaddress.split()))
    db_contacts = sorted(map(clean, db.get_detailed_contact_list()), key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(db_contacts) == len(contacts_from_home_page)
    for i in range(len(db_contacts)):
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(db_contacts[i])
        assert contacts_from_home_page[i].all_emails_from_homepage == merge_emails_like_on_home_page(db_contacts[i])
        assert contacts_from_home_page[i].mainaddress == db_contacts[i].mainaddress
        assert contacts_from_home_page[i].firstname == db_contacts[i].firstname
        assert contacts_from_home_page[i].lastname == db_contacts[i].lastname


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page (contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.phone, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page (contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3])))
