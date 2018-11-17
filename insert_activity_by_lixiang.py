#insert 活动表
def insert_act(act_id,key,wen,sta,time):
    import sqlite3
    conn = sqlite3.connect('alpha.sqlite')

    c = conn.cursor()

    c.execute("""INSERT INTO Activity VALUES (?,?,?,?,?)""", (act_id, key, wen, sta, time))

    conn.commit()
    conn.close() 
