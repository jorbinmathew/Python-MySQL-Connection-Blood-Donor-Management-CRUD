import mysql.connector
import datetime


class BloodDonorManager:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Jorbin@123",
            database="blood_db"
        )

        print("Connected Successfully")

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """
            INSERT INTO donor
            (name, blood_group, phone, city, last_donor)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Donor Successfully Added")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM donor"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for data in records:
                print(data)

        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            self.cursor=self.connection.cursor()
            query= "select * from donor where id=%s"
            values=(id,)
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()
            print(records)
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            records=self.get_object(id)
            values=(id,)
            self.cursor=self.connection.cursor()
            query="select * from donor where id =%s"
            values=(id,)
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()

            if records is not None:
                query="delete from donor where id=%s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Donor Successfully Deleted")
            else:
                print("Donor Not Found")
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id=%s"
            values=(id,)
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()
            return records
        except Exception as e:
            print(e)



donor_instance = BloodDonorManager()
donor_instance.post(
    name="Amal",
    blood_group="A+",
    phone="129478789",
    city="Kollam",
    last_donor="2026-08-29"
)
print("______________________________________")
donor_instance.get()
print("____________after retrieval____________")

donor_instance.retrieve(1)
print("____________after deletion____________")
donor_instance.delete(6)

