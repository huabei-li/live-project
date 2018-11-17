#insert_user
def insert_user(id,nk,num,wei):
    import sqlite3
    conn = sqlite3.connect('alpha.sqlite')

    c = conn.cursor()
    c.execute("""INSERT INTO user VALUES (?,?,?,?)""", (id, nk, num, wei))
        
    conn.commit()
    conn.close()