import mysql.connector as q


Con = q.connect(host='localhost', user='root', password='qwerty')
if Con.is_connected():
    Cursor = Con.cursor()
    Cursor.execute("create database if not exists KBC_QBank")
    Cursor.execute("use KBC_QBank")
    ct = '''
    CREATE TABLE IF NOT EXISTS KBC_Q (
        Q_id INT PRIMARY KEY,
        Question VARCHAR(255),
        `Option A` VARCHAR(255),
        `Option B` VARCHAR(255) NOT NULL,
        `Option C` VARCHAR(255),
        `Option D` VARCHAR(255),
        `Correct Option` VARCHAR(255)
    )
    '''
    Cursor.execute(ct)
    Con.commit()

    while True:
        print("1] Enter New Question \n 2] Edit \n 3] Remove \n 4] Exit ")
        X = int(input("Enter Choice:"))
        if X == 1:
            question_id = int(input("Enter Question ID:"))
            question = input("Enter the question: ")
            option_a = input("Enter option A: ")
            option_b = input("Enter option B: ")
            option_c = input("Enter option C: ")
            option_d = input("Enter option D: ")
            correct_option = input("Enter the correct option (A/B/C/D): ").upper()
            query = """
                INSERT INTO KBC_Q VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
            data = (question_id, question, option_a, option_b, option_c, option_d, correct_option)

            Cursor.execute(query, data)
            Con.commit()
            print("Question added successfully!")

        elif X == 2:
            question_id = input("Enter the ID of the question to edit: ")
            question = input("Enter the new question: ")
            option_a = input("Enter new option A: ")
            option_b = input("Enter new option B: ")
            option_c = input("Enter new option C: ")
            option_d = input("Enter new option D: ")
            correct_option = input("Enter the new correct option (A/B/C/D): ").upper()
            Cursor.execute(
                "update KBC_Q set Question='" + question + "', set Option A='" + option_a + "',set Option B='" + option_b + "', set Option C='" + option_c + "', set Option D='" + option_d + "', set Correct Option='" + correct_option + "' where Q_id= '" + question_id + "' ")
            print("Question edited successfully!")

        elif X == 3:
            question_id = input("Enter the ID of the question to remove: ")
            Cursor.execute("delete from KBC_Q where Q_id='" + question_id + "'")
            Con.commit()
            print("SUCCESSFULLY DELETED!!")

        elif X == 4:
            Con.close()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

else:
    print("Error in connecting to MySQL")
