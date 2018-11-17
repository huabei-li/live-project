def select_win():
    import sqlite3
    con = sqlite3.connect('alpha.sqlite')
    c = con.cursor()
    cursor = c.execute('select nickname, QEmail, win.ac_id, rank '
                       'from Activity, User, win where Activity.ac_id = win.ac_id and user.u_id = win.u_id')
    for row in cursor:
        print('nickname: '+row[0])
        print('Q/Email: ' + row[1])
        print('ac_id: ' + row[2])
        print('rank: ' + row[3])
        print('\n')
        return row
    con.close()
