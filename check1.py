import mysql.connector
mycon = mysql.connector.connect(host = "localhost", user = "root", passwd = "abc123", database = "testing")
if mycon.is_connected():
        print('Successfully Connected')
c = mycon.cursor()
print('-------------------------JEE REGISTRATION-------------------------')
print('1: Register for JEE')
print('2: Login')
print('3: Examiner Login')
print('4: Exit')
ans = int(input('Enter your choice (1 or 2 or 3 or 4)...'))
if ans==1:
        c.execute('select * from registration')
        dat = c.fetchall()
        rollno = len(dat) + 1
        print('Roll No. of Candidate:',rollno)
        fname = input('Enter your First Name:')
        lname = input('Enter your Last Name:')
        g = input('Enter your Gender (M or F or O) :')
        dob = input('Enter your Date of Birth (DD/MM/YYYY):')
        faname = input("Enter your Father's Name:")
        mname = input("Enter your Mother's Name:")
        nat = input('Enter your Nationality:')
        comm = input('Enter your Community(General or SC or ST or OBC):')
        mi = input('Does your community comes under Minority group? (yes/no)..')
        ad1 = input('Enter Address line 1:')
        ad2= input('Enter Address line 2:')
        dist = input('Enter district area:')
        state = input('Enter the State you reside in:')
        pin = int(input('Enter pincode of your area:'))
        phno = int(input('Enter your phone number:'))
        mail = input('Enter your email id:')
        adcn = int(input('Enter your Aadhar Card Number:'))
        indat = "insert into registration values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',{},{}, '{}',{},'{}')".format(fname,lname,g,dob,faname,mname,nat,comm,mi,ad1,ad2,dist,state,pin,phno,mail,adcn,rollno)
        c.execute(indat)
        mycon.commit()


        passw = input('Enter a new password:')
        inlo = "insert into login values({},'{}')".format(rollno,passw)
        c.execute(inlo)
        mycon.commit()
        print('Registration Complete')

if ans==2:
        c.execute('select * from login')
        dat1 = c.fetchall()
        user = input('Enter roll no.:')
        passwd = input('Enter password:')
        if (user,passwd) in dat1:
                print('WELCOME')
                print("1: View Candidate's form details")
                print("2: View Candidate's Result")
                print('3: Exit')
                Ans = int(input('Enter your choice (1 or 2 or 3)...'))
                if Ans==1:
                        c.execute('select * from registration')
                        dat2 = c.fetchall()
                        for i in range(len(dat2)):
                                if dat2[i][-1]== user:
                                        print('Hello',dat2[i][0])
                                        print('Rollno',dat2[i][17])
                                        print('Name of the Candidate:',dat2[i][0],dat2[i][1])
                                        print('Gender of Candidate:',dat2[i][2])
                                        print('Date of Birth:',dat2[i][3])
                                        print('Name of Father of Candidate:',dat2[i][4])
                                        print('Name of Mother of Candidate:',dat2[i][5])
                                        print('Nationality:',dat2[i][6])
                                        print('Community of Cadidate:',dat2[i][7])
                                        print('Minority:',dat2[i][8])
                                        print('Address line 1:',dat2[i][9])
                                        print('Address line 2:',dat2[i][10])
                                        print('City:',dat2[i][11])
                                        print('State;',dat2[i][12])
                                        print('Pin code',dat2[i][13])
                                        print('Phone Number ;',dat2[i][14])
                                        print('Email ID of Cadidate',dat2[i][15])
                                        print('Aadhar Card no.',dat2[i][16])

                if Ans==2:
                        c.execute('select * from result')
                        dat3 = c.fetchall()
                        for i in range(len(dat3)):
                                if dat3[i][0]==user:
                                        print('Here is your JEE Exams Result')
                                        print('Roll no. of Candidate:', dat3[i][0])
                                        print('Marks in Physics:',dat3[i][1])
                                        print('Rank in Physics:',dat3[i][2])
                                        print('Marks in Chemistry:',dat3[i][3])
                                        print('Rank in Chemistry:',dat3[i][4])
                                        print('Marks in Maths:',dat3[i][5])
                                        print('Rank in Maths:',dat3[i][6])
                                        print('Total Marks:',dat3[i][7])
                                        print('Rank in CRL:',dat3[i][8])
                                else:
                                        print('Your result is not yet published and is being reviewed')
                        if len(dat3)==0:
                                print('Your result is not yet published and will be published soon')
                                
                if Ans==3:
                        print('Thank You')


                                        
        else:
                print('Incorrect Roll number or password')
        
if ans==3:
        usern = input('Enter Username:')
        passwor = input('Enter Password:')
        if usern=='examiner' and passwor=='result':
                choi='y'
                while choi=='y':
                        rolln = input('Enter Roll No.:')
                        c.execute('select * from login')
                        dat4 = c.fetchall()
                        for i in range(len(dat4)):
                                if dat4[i][0]==rolln:
                                        pm = int(input('physics marks'))
                                        pp = float(input('physics %ile'))
                                        cm= int(input('chem marks'))
                                        cp = float(input('chem %ile'))
                                        mm = int(input('maths marks'))
                                        mp = float(input('maths %ile'))
                                        tm = int(input('total marks'))
                                        tp = float(input('net %ile'))
                                        inres = "insert into result values('{}',{},{},{},{},{},{},{},{})".format(rolln,pm,pp,cm,cp,mm,mp,tm,tp)
                                        c.execute(inres)
                                        mycon.commit()
                        choi=input('Do u want to input more records?(y or n)...')


        else:
                print('Incorrect Username or Password')

if ans==4:
        print('Thank You')
                  
