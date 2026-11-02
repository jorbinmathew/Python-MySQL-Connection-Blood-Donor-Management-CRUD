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

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()
            return records
        except Exception as e:
            print(e)

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

            # for data in records:
            #     print(data)
            return records

        except Exception as e:
            return []

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record != None:
                self.cursor = self.connection.cursor()
                placeholder =[]
                for k in kwargs.keys():
                    placeholder += k + "=%s,"

                    placeholder = placeholder.rstrip(",")
                    query = f"update donor set {placeholder} where id = %s"
                    values = [v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query, values)
                    print("Donor updated successfully..!")
                else:
                    print("Donor not found..!")
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





# donor_instance = BloodDonorManager()
# donor_instance.post(
#     name="Amal",
#     blood_group="A+",
#     phone="129478789",
#     city="Kollam",
#     last_donor="2026-08-29"
# )
# print("______________________________________")
# donor_instance.get()
# print("____________after retrieval____________")
#
# donor_instance.retrieve(1)
# print("____________after deletion____________")
# donor_instance.delete(6)

# donor_instance.put(1,name="Jorbin")
# donor_instance.retrieve(1)