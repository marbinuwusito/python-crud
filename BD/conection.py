import mysql.connector
from mysql.connector import Error

class DataAccessObject():

    def __init__(self):

        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = "marbin",
                password = "patata12345",
                db = "university"
            )
        except Error as ex:

            print("Failed to attemp to connect to db: {0}".format(ex))


    def listCourses(self):

        if self.connection.is_connected():

            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM courses ORDER BY name ASC")
                results = cursor.fetchall()
                return results

            except Error as ex:

                print("Failed to attemp to connect to db: {0}".format(ex))


    def registCourse(self, course):

        if self.connection.is_connected():

            try:

                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO courses (name, credits) VALUES ('{0}', {1})".format(course[0], course[1]))
                self.connection.commit()
                print("Course succesfully registered\n")

            except Error as ex:

                print("Failed to attemp to connect to db: {0}".format(ex))


    def updateCourse(self, course):

        if self.connection.is_connected():

            try:

                cursor = self.connection.cursor()
                cursor.execute("UPDATE courses SET name = '{0}', credits = {1} WHERE ID = {2}".format(course[1], course[2], course[0]))
                self.connection.commit()
                print("Course succesfully updated\n")

            except Error as ex:

                print("Failed to attemp to connect to db: {0}".format(ex))


    def eliminateCourse(self, codeToEliminate):

        if self.connection.is_connected():

            try:

                cursor = self.connection.cursor()
                cursor.execute("DELETE FROM courses WHERE ID = {0}".format(codeToEliminate))
                self.connection.commit()
                print("Course succesfully deleted")

            except Error as ex:

                print("Failed to attemp to connect to db: {0}".format(ex))

