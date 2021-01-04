import sqlite3
con=sqlite3.connect("kutuphane_1.db")
cursor=con.cursor()
def acma():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar(Kitap adı TEXT,Yazar TEXT)")
    con.commit()
def ekleme():
    cursor.execute("INSERT INTO kitaplar VALUES('Python','Deitel')")
    con.commit()
def ekleme2():
    cursor.execute("INSERT INTO kitaplar VALUES('Brief History Of Time','Feynmann')")
    con.commit()
def güncelleme():
    cursor.execute("UPDATE kitaplar SET Yazar='Hawking' WHERE Yazar='Feynmann'")
    con.commit()
def silme():
    cursor.execute("DELETE FROM kitaplar WHERE Yazar='Deitel'")
    con.commit()
def ekranabas():
    cursor.execute("SELECT * FROM kitaplar")
    con.commit()
    data=cursor.fetchall()
    for i in data:
        print(i)

acma()
ekleme()
ekleme2()
güncelleme()
ekranabas()
