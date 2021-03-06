import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated is null")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_detailed_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, phone2, email, email2, email3, address from addressbook where deprecated is null")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, phone2, email, email2, email3, address) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, phone=home, mobile=mobile, work=work, phone2=phone2, email1=email, email2=email2, email3=email3, mainaddress=address))
        finally:
            cursor.close()
        return list

    def get_relations_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (contact_id, group_id) = row
                list.append((contact_id, group_id))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
