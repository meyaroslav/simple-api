from fastapi import FastAPI
from connection import db_connection

app = FastAPI()

# get
@app.get("/books")
def get_books():
    with db_connection() as con, con.cursor() as cur:
        cur.execute("SELECT * FROM books")
        return cur.fetchall()

# post
@app.post("/books")
def post_book(title: str, author: str, year: int):
    with db_connection() as con, con.cursor() as cur:
        cur.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s) RETURNING id", (title, author, year))
        con.commit()
        return cur.fetchall()

# put 
@app.put("/books")
def put_book(id: int, title: str, author: str, year: int):
    with db_connection() as con, con.cursor() as cur:
        cur.execute("UPDATE books SET title=%s, author=%s, year=%s WHERE id=%s", (title, author, year, id))
        con.commit()
        return {"message": "book update"}
    
# delete    
@app.delete("/books")
def delete_book(id: str):
    with db_connection() as con, con.cursor() as cur:
        cur.execute("DELETE FROM books WHERE id=%s", (id))
        con.commit()
        return {"message": "book delete"}