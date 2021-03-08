from BD.conection import DataAccessObject
import crud_operations

def menu():

    flag = True

    while(flag):

        validFlag = False

        while(not validFlag):

            print("=== PRINCIPAL MENU ===")
            print("1. List Courses")
            print("2. Create Course")
            print("3. Update Course")
            print("4. Delete Course")
            print("5. Exit")
            print("======================")

            option = int(input("Select an option: "))

            if option < 1 or option > 5:

                print("Invalid option, please enter a valid option")

            elif option == 5:

                flag = False
                print("Exiting...")
                break

            else:
                validFlag = True
                executeOption(option)


def executeOption(option):

    dao = DataAccessObject()

    if option == 1:

        try:

            courses = dao.listCourses()

            if len(courses) > 0:

                crud_operations.listCourses(courses)

            else:

                print("No courses to list")

        except:

            print("An exception has been")

    elif option == 2:

        course = crud_operations.askDataRegiste()

        try:

            dao.registCourse(course)

        except:

            print("An exception has been")

    elif option == 3:

         try:

            courses = dao.listCourses()

            if len(courses) > 0:

                course = crud_operations.askDataUpdate(courses)

                if course:

                    dao.updateCourse(course)

                else:

                    print("Course code not finded...\n")

         except:

            print("An exception has been")


    elif option == 4:

        try:

            courses = dao.listCourses()

            if len(courses) > 0:

                eliminateCode = crud_operations.askDataEliminate(courses)

                if not (eliminateCode == ""):

                    dao.eliminateCourse(eliminateCode)

                else:

                    print("Course code not finded...\n")

        except:

            print("An exception has been")


menu()
