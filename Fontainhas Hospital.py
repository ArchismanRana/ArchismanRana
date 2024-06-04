import mysql.connector as q
from tabulate import tabulate

con = q.connect(host='localhost', user='root', password='qwerty')


def update_doc(t):
    q = "select * from doctor_details where d_id={}".format(t)
    cursor.execute(q)
    got = cursor.fetchall()
    print(got)
    put = int(
        input("Enter column number out of \n (1.Name/ 2.Age/ 3.sex \n 4.contact/ 5.monthly_salary/ 6.join_date):"))
    if put == 1:
        j = input("Enter new value:")
        cursor.execute("update doctor_details set name='" + j + "' where d_id= '" + t + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif put == 2:
        j = input("Enter new value:")
        cursor.execute("update doctor_details set age='" + j + "' where d_id= '" + t + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif put == 3:
        j = input("Enter new value:")
        cursor.execute("update doctor_details set sex='" + j + "' where d_id= '" + t + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif put == 4:
        j = int(input("Enter new value:"))
        cursor.execute("update doctor_details set contact={} where d_id={}".format(j,t))
        print("Data updated successfully!!")
        con.commit()
    elif put == 5:
        j = input("Enter new value:")
        cursor.execute("update doctor_details set monthly_salary='" + j + "' where d_id= '" + t + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif put == 6:
        j = input("Enter new value (YYYY-MM-DD):")
        cursor.execute("update doctor_details set join_date='" + j + "' where d_id= '" + t + "' ")
        print("Data updated successfully!!")
        con.commit()


def update_nur(g):
    cursor.execute("select * from nurse_details where n_id='" + g + "'")
    wo = cursor.fetchall()
    print(wo)
    pix = int(
        input("Enter column number out of \n (1.Name/ 2.Age/ 3.sex \n 4.contact/ 5.monthly_salary/ 6.join_date):"))
    if pix == 1:
        j = input("Enter new value:")
        cursor.execute("update nurse_details set name='" + j + "' where n_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif pix == 2:
        j = input("Enter new value:")
        cursor.execute("update nurse_details set age='" + j + "' where n_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif pix == 3:
        j = input("Enter new value:")
        cursor.execute("update nurse_details set sex='" + j + "' where n_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif pix == 4:
        j = int(input("Enter new value:"))
        cursor.execute("update nurse_details set contact={} where n_id={}".format(j, g))
        print("Data updated successfully!!")
        con.commit()
    elif pix == 5:
        j = input("Enter new value:")
        cursor.execute("update nurse_details set monthly_salary='" + j + "' where n_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif pix == 6:
        j = input("Enter new value (YYYY-MM-DD):")
        cursor.execute("update nurse_details set join_date='" + j + "' where n_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()


def update_worker(g):
    cursor.execute("select * from other_workers_details where w_id='" + g + "'")
    jaw = cursor.fetchall()
    print(jaw)
    lo = int(input("Enter column number out of \n (1.Name/ 2.Age/ 3.sex \n 4.contact/ 5.monthly_salary/ 6.join_date):"))
    if lo == 1:
        j = input("Enter new value:")
        cursor.execute("update other_workers_details set name='" + j + "' where w_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif lo == 2:
        j = input("Enter new value:")
        cursor.execute("update other_workers_details set age='" + j + "' where w_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif lo == 3:
        j = input("Enter new value:")
        cursor.execute("update other_workers_details set sex='" + j + "' where w_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif lo == 4:
        j = int(input("Enter new value:"))
        cursor.execute("update other_workers_details set contact={} where w_id={}".format(j, g))
        print("Data updated successfully!!")
        con.commit()
    elif lo == 5:
        j = input("Enter new value:")
        cursor.execute("update other_workers_details set monthly_salary='" + j + "' where w_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif lo == 6:
        j = input("Enter new value (YYYY-MM-DD):")
        cursor.execute("update other_workers_details set join_date='" + j + "' where w_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()

def update_patient(g):
    cursor.execute("select * from patient_details where p_id='" + g + "'")
    jaw = cursor.fetchall()
    print(jaw)
    l = int(input("Enter column number out of \n (1.Name/ 2.Age/ 3.sex \n4.room no., 5.illness, 6.amt, 7.paid(yes/no), "
                  "8.addresss/ 9.admit date):"))
    if l == 1:
        j = input("Enter new value:")
        cursor.execute("update patient_details set name='" + j + "' where p_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 2:
        j = input("Enter new value:")
        cursor.execute("update patient_details set age='" + j + "' where p_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 3:
        j = input("Enter new value:")
        cursor.execute("update patient_details set sex='" + j + "' where p_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 4:
        j = input("Enter new value:")
        cursor.execute("update patient_details set room_no='" + j + "' where p_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 5:
        j = input("Enter new value:")
        cursor.execute("update patient_details set illness='" + j + "' where p_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 6:
        j = input("Enter new value:")
        cursor.execute("update patient_details set amt ='" + j + "' where p_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 7:
        j = input("Enter new value:")
        cursor.execute("update patient_details set paid='" + j + "' where p_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 8:
        j = input("Enter new value:")
        cursor.execute("update patient_details set address='" + j + "' where p_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 9:
        j = input("Enter new value (YYYY-MM-DD):")
        cursor.execute("update patient_details set admit_date='" + j + "' where p_id= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()


def update_bill(g):
    cursor.execute("select * from Bill_details where bill_no='" + g + "'")
    jaw = cursor.fetchall()
    print(jaw)
    l = int(input(
        "Enter column number out of \n (1.Bill no./ 2.date/ 3.name \n4.room type, 5.room charge, 6.pathology fees, 7.doctor fees, 8.total amt.):"))
    if l == 1:
        j = input("Enter new value:")
        cursor.execute("update Bill_details set bill_no='" + j + "' where bill_no= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 2:
        j = input("Enter new value(YYYY-MM-DD):")
        cursor.execute("update Bill_details set bill_date='" + j + "' where bill_no= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 3:
        j = input("Enter new value:")
        cursor.execute("update Bill_details set p_name ='" + j + "' where bill_no= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 4:
        j = input("Enter new value:")
        cursor.execute("update Bill_details set room_type='" + j + "' where bill_no= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 5:
        j = input("Enter new value:")
        cursor.execute("update Bill_details set room_charges='" + j + "' where bill_no= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 6:
        j = input("Enter new value:")
        cursor.execute("update Bill_details set pathology_fees ='" + j + "' where bill_no= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 7:
        j = input("Enter new value:")
        cursor.execute("update Bill_details set doctor_fees='" + j + "' where bill_no= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()
    elif l == 8:
        j = input("Enter new value:")
        cursor.execute("update Bill_details set total_amount='" + j + "' where bill_no= '" + g + "' ")
        print("Data updated successfully!!")
        con.commit()


if con.is_connected():
    print("...Database connected successfully!!...")
    cursor = con.cursor()
    cursor.execute("create database if not exists Fontainhas_Hospital")
    cursor.execute("use Fontainhas_Hospital")
    ct = '''create table if not exists patient_details
          (p_id int primary key,name varchar(30) not null,
           sex varchar(15),age int(3),room_no varchar(10) not null,illness varchar(30),
           amt int,paid varchar(5),address varchar(1000),contact char(10),admit_date date)'''
    cursor.execute(ct)
    con.commit()
    ct1 = '''create table if not exists doctor_details
          (d_id int primary key,name varchar(30) not null,sex char(2),
           age int,qualification varchar(30),designation varchar(30),
           contact varchar(15),monthly_salary int,join_date date)'''
    cursor.execute(ct1)
    con.commit()
    cursor.execute('''create table if not exists nurse_details
                    (n_id int primary key,name varchar(30) not null,
                     sex varchar(15),age int(3),contact char(10),
                     monthly_salary int,join_date date)''')
    con.commit()
    cursor.execute('''create table if not exists other_workers_details
                    (w_id int primary key, name varchar(30) not null,
                     age int(2),sex varchar(15),Role varchar(20),contact char(10),
                     monthly_salary int,join_date date)''')
    con.commit()
    cursor.execute("create table if not exists Sign_Up(u_name varchar(30) primary key,password varchar(15) not null)")
    con.commit()
    cursor.execute('''create table if not exists Bill_details(bill_no  int primary key,bill_date date,p_name varchar(20),
        room_type varchar(20),room_charges int,pathology_fees int,doctor_fees int,total_amount int)''')
    con.commit()
    while True:
        print("[FONTAINHAS HOSPITAL MANAGEMENT SYSTEM]")
        print("1) Log In \n2) Sign Up\n3) Exit")
        Ch = int(input("Choice(1/2/3):"))
        if Ch == 2:
            print("[[ Sign Up with us!!]]")
            u = input("Input your username:")
            p = input("Input the password :")
            cursor.execute("insert into Sign_Up values('%s', '%s')" % (u, p))
            con.commit()
            print("[[ Sign Up done Successfully!! ]]")
        elif Ch == 1:
            t = input("Enter Username:")
            ps = input("Enter Password:")
            cursor.execute("select * from Sign_Up where (u_name ='%s' AND password='%s')" % (t, ps))
            row = cursor.fetchone()
            if row is not None:
                while True:
                    print("="*50)
                    print("1.Administration\n2.Patient(Details)\n3. Billing Information\n4.Log Out")
                    print("="*50)
                    a = int(input("ENTER YOUR CHOICE:"))
                    if a == 1:
                        print("About our:\n  1) Doctors\n  2) Nurses\n  3) Non-medical staffs")
                        b = int(input("ENTER YOUR CHOICE:"))
                        if b == 1:
                            print(
                                "[ OUR DOCTORS ]\n1. Display the details\n2. Add a new member\n3. Update details\n4. "
                                "Delete a member")
                            c = int(input("ENTER YOUR CHOICE:"))
                            if c == 1:
                                cursor.execute("select * from doctor_details")
                                data = cursor.fetchall()
                                k = ["ID", "NAME", "SEX", "AGE", "QUALIFICATION", "DESIGNATION", "CONTACT","SALARY","JOIN DATE"]
                                print(tabulate(data, headers=k, tablefmt='fancy_grid'))
                            elif c == 2:
                                p_id = input("Enter doctor's ID:")
                                nam = input("Enter doctor's name:")
                                sex = input("Enter the gender:")
                                age = input("Enter the age:")
                                room = input("Enter the qualification:")
                                ill = input("Enter designation:")
                                t_amt = input("Enter contact no.:")
                                paid = input("Enter Monthly Salary:")
                                dat = (input("Enter join date(YYYY-MM-DD):"))
                                query = "insert into doctor_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                data = (p_id, nam, sex, age, room, ill, t_amt, paid, dat)
                                cursor.execute(query, data)
                                con.commit()
                                print("DETAILS ADDED SUCCESSFULLY!!!.......")
                            elif c == 3:
                                print("UPDATE details")
                                t = input("Enter Doctor's ID who needs update:")
                                chk = '''select name from doctor_details where d_id={}'''.format(t)
                                cursor.execute(chk)
                                q = cursor.fetchone()
                                if q == None:
                                    print("No such record present.......")
                                else:
                                    update_doc(t)
                            elif c == 4:
                                p_id = input("Enter Doctor's ID:")
                                cursor.execute("select * from doctor_details where d_id='" + p_id + "'")
                                row = cursor.fetchall()
                                print(tabulate(row, tablefmt='fancy_grid'))
                                p = input("you really want to delete this data? (y/n):")
                                if p == "y":
                                    cursor.execute("delete from doctor_details where d_id='" + p_id + "'")
                                    con.commit()
                                    print("SUCCESSFULLY DELETED!!")
                                else:
                                    continue
                            else:
                                print("Error!! Enter correct option(1/2/3/4)")
                        elif b == 2:
                            print("[ OUR NURSES ]\n1. Display the details\n2. Add a new member\n3. Update details\n4. "
                                  "Delete a member")
                            c = int(input("ENTER YOUR CHOICE:"))
                            if c == 1:
                                cursor.execute("select * from nurse_details")
                                data = cursor.fetchall()
                                k = ["ID", "NAME", "SEX", "AGE", "CONTACT", "SALARY","JOIN DATE"]
                                print(tabulate(data, headers=k, tablefmt='fancy_grid'))
                            elif c == 2:
                                n_id = input("Enter nurse ID:")
                                g = input("Enter the nurse's name:")
                                sex = input("Enter the gender:")
                                age = input("Enter the age:")
                                t_amt = input("Enter contact no.:")
                                paid = input("Enter Monthly Salary:")
                                dat = (input("Enter join date(YYYY-MM-DD):"))
                                query = "insert into nurse_details values(%s,%s,%s,%s,%s,%s,%s)"
                                data = (n_id, g, sex, age, t_amt, paid, dat)
                                cursor.execute(query, data)
                                con.commit()
                                print("DETAILS ADDED SUCCESSFULLY!!!.......")
                            elif c == 3:
                                print("UPDATE details")
                                g = input("Enter Nurse's ID who needs update:")
                                chk = '''select name from nurse_details where n_id={}'''.format(g)
                                cursor.execute(chk)
                                q = cursor.fetchone()
                                if q == None:
                                    print("No such record present.......")
                                else:
                                    update_nur(g)
                            elif c == 4:
                                n_id = input("Enter Nurse's ID:")
                                cursor.execute("select * from nurse_details where n_id='" + n_id + "'")
                                row = cursor.fetchall()
                                print(tabulate(row, tablefmt='fancy_grid'))
                                p = input("you really want to delete this data? (y/n):")
                                if p == "y":
                                    cursor.execute("delete from nurse_details where n_id='" + n_id + "'")
                                    con.commit()
                                    print("SUCCESSFULLY DELETED!!")
                                else:
                                    continue
                        elif b == 3:
                            print("[ OUR NON-MEDICAL STAFFS ]\n1. Display the details\n2. Add a new member\n3. Update "
                                  "details\n4. Delete a member")
                            c = int(input("ENTER YOUR CHOICE:"))
                            if c == 1:
                                cursor.execute("select * from other_workers_details")
                                data = cursor.fetchall()
                                k = ["ID", "NAME", "AGE", "Gender", "ROLE", "CONTACT", "SALARY", "JOIN DATE"]
                                print(tabulate(data, headers=k, tablefmt='fancy_grid'))
                            elif c == 2:
                                g = int(input("Enter ID of non-medical staff:"))
                                n = input("Enter staff's name")
                                age = int(input("Enter the age:"))
                                sex = input("Gender:")
                                role = input("Enter role:")
                                t_amt = input("Enter contact no.:")
                                paid = int(input("Enter Monthly Salary:"))
                                dat = (input("Enter join date(YYYY-MM-DD):"))
                                query = "insert into other_workers_details values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                data = (g, n, age, sex, role, t_amt, paid, dat)
                                cursor.execute(query, data)
                                con.commit()
                                print("DETAILS ADDED SUCCESSFULLY!!!.......")
                            elif c == 3:
                                print("UPDATE details")
                                g = input("Enter ID of non-medical staff who needs update:")
                                chk = '''select name from other_workers_details where w_id={}'''.format(g)
                                cursor.execute(chk)
                                q = cursor.fetchone()
                                if q == None:
                                    print("No such record present.......")
                                else:
                                    update_worker(g)
                            elif c == 4:
                                g = input("Enter ID of non-medical staff:")
                                cursor.execute("select * from other_workers_details where w_id='" + g + "'")
                                row = cursor.fetchall()
                                print(tabulate(row, tablefmt='fancy_grid'))
                                p = input("you really want to delete this data? (y/n):")
                                if p == "y":
                                    cursor.execute("delete from other_workers_details where name='" + g + "'")
                                    con.commit()
                                    print("SUCCESSFULLY DELETED!!")
                                else:
                                    continue
                            else:
                                print("Error!!")
                                continue
                    elif a == 2:  # patients
                        print(
                            "[ PATIENT DETAILS ]\n1. Display the details\n2. Add a Patient\n3. Update Patient's "
                            "details\n4. Delete a Patient's detail")
                        c = int(input("ENTER YOUR CHOICE:"))
                        if c == 1:
                            cursor.execute("select * from patient_details")
                            data = cursor.fetchall()
                            k = ["ID", "NAME", "SEX", "AGE", "ROOM NO.", "ILLNESS", "TOTAL AMT.", "PAID[yes/no]",
                                 "ADDRESS", "CONTACT", "ADMIT DATE"]
                            print(tabulate(data, headers=k, tablefmt='fancy_grid'))
                        elif c == 2:
                            p_id = input("Enter patient's ID:")
                            nam = input("Enter patient's name:")
                            sex = input("Enter the gender:")
                            age = int(input("Enter the age:"))
                            room = int(input("Enter the room no.:"))
                            ill = input("Enter illness:")
                            t_amt = int(input("Enter total amt. need to pay:"))
                            paid = input("Amt paid[yes/no]:")
                            Add = input("House Address of patient:")
                            ph = input("phone no.:")
                            dat = (input("Enter admit date(YYYY-MM-DD):"))
                            query = "insert into patient_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            data = (p_id, nam, sex, age, room, ill, t_amt, paid, Add, ph, dat)
                            cursor.execute(query, data)
                            con.commit()
                            print("DETAILS ADDED SUCCESSFULLY!!!.......")
                        elif c == 3:
                            print("UPDATE details")
                            t = input("Enter Patient's ID who needs update:")
                            chk = '''select name from patient_details where p_id={}'''.format(t)
                            cursor.execute(chk)
                            q = cursor.fetchone()
                            if q==None:
                                print("No such record present.......")
                            else:
                                update_patient(t)
                        elif c == 4:
                            p_id = input("Enter Patient's ID:")
                            cursor.execute("select * from patient_details where p_id='" + p_id + "'")
                            row = cursor.fetchall()
                            print(tabulate(row, tablefmt='fancy_grid'))
                            p = input("You really want to delete this data? (y/n):")
                            if p == "y":
                                cursor.execute("delete from patient_details where p_id='" + p_id + "'")
                                con.commit()
                                print("SUCCESSFULLY DELETED!!")
                            else:
                                continue
                        else:
                            print("Error!! Enter correct option(1/2/3/4)")
                            continue
                    elif a == 3:
                        print("[ BILLING INFO ]\n1. Display the details\n2. Add a Bill\n3. Update Bill details\n4. "
                              "Delete a Bill detail")
                        c = int(input("ENTER YOUR CHOICE:"))
                        if c == 1:
                            cursor.execute("select * from Bill_details")
                            data = cursor.fetchall()
                            k = ["BILL NO.", "DATE", "NAME", "ROOM TYPE", "ROOM CHARGE", "PATHOLOGY FEES",
                                 "DOCTOR FEES", "TOTAL"]
                            print(tabulate(data, headers=k, tablefmt='fancy_grid'))
                        elif c == 2:
                            b_id = int(input("Enter Bill no.:"))
                            date = input("Enter Bill date(YYYY-MM-DD):")
                            nam = input("Enter patient name:")
                            rtype = input("Enter room type:")
                            rcharge = int(input("Enter room charge:"))
                            pfees = int(input("Enter pathology fees:"))
                            dfees = int(input("Enter doctor fees"))
                            t_amt = rcharge + pfees + dfees
                            query = "insert into Bill_details values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            data = (b_id, date, nam, rtype, rcharge, pfees, dfees, t_amt)
                            cursor.execute(query, data)
                            con.commit()
                            print("DETAILS ADDED SUCCESSFULLY!!!.......")
                        elif c == 3:
                            print("UPDATE details")
                            t = input("Enter Bill no. you want to update:")
                            chk = '''select p_name from Bill_details where Bill_no={}'''.format(t)
                            cursor.execute(chk)
                            q = cursor.fetchone()
                            if q == None:
                                print("No such record present.......")
                            else:
                                update_bill(t)
                        elif c == 4:
                            bill_no = input("Enter Bill no.:")
                            cursor.execute("select * from Bill_details where bill_no='" + bill_no + "'")
                            row = cursor.fetchall()
                            print(tabulate(row, tablefmt='fancy_grid'))
                            p = input("You really want to delete this data? (y/n):")
                            if p == "y":
                                cursor.execute("delete from Bill_details where bill_no='" + bill_no + "'")
                                con.commit()
                                print("SUCCESSFULLY DELETED!!")
                            else:
                                continue
                        else:
                            print("Error!! Enter correct option(1/2/3/4)")
                    elif a == 4:
                        break
                    else:
                        print("Error!! Enter correct option(1/2/3)")
                        continue
        else:
            break
else:
    print("...Error while connecting to database!!...")
