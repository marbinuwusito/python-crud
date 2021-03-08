def listCourses(courses):

    print("\nCourses: \n")

    count = 1

    for cour in courses:

        data = "{0}. Code: {1} | Name: {2} ({3} credits)"
        print(data.format(count, cour[0], cour[1], cour[2]))
        count = count + 1
    print(" ")


def askDataRegiste():

    name = input("Insert Name: ")
    correctCredits = False

    while(not correctCredits):

        credits = input("Insert credits: ")

        if credits.isnumeric():

            if (int(credits) > 0):

                correctCredits = True
                credits = int(credits)

            else:

                print("The credits must be higher 0")

        else:

            print("Incorrect credits, must be only a number")

    course = (name, credits)

    return course


def askDataUpdate(courses):

    listCourses(courses)

    codeExist = False

    codeToUpdate = int(input("Insert course code to update: "))

    for cour in courses:

        if cour[0] == codeToUpdate:

            codeExist = True
            break

    if codeExist:

        name = input("insert name to update: ")
        correctCredits = False

        while(not correctCredits):

            credits = input("Insert credits update: ")

            if credits.isnumeric():

                if (int(credits) > 0):

                    correctCredits = True
                    credits = int(credits)

                else:

                    print("The credits must be higher 0")

            else:

                print("Incorrect credits, must be only a number")

        course = (codeToUpdate, name, credits)

    else:

        course = None

    return course


def askDataEliminate(courses):

    listCourses(courses)

    codeExist = False

    codeToEliminate = int(input("Insert course code to eliminate: "))

    for cour in courses:

        if cour[0] == codeToEliminate:

            codeExist = True
            break


    if not codeExist:

        codeToEliminate = ""

    return codeToEliminate
