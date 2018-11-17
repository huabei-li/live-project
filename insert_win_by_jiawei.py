def insert_win(ac_id, u_id, rank):
    import sqlite3
    if ac_id and u_id:
        con = sqlite3.connect('alpha.sqlite')
        c = con.cursor()
        c.execute('insert into win values (?,?,?)', (ac_id, u_id, rank))
        con.commit()
        con.close()
