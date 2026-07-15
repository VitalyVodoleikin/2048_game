import sqlite3

bd = sqlite3.connect("2048.sqlite")

cur = bd.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS records (
        name text,
        score integer
    );
    """
)


def insert_result(name, score):
    cur.execute(
        """
        INSERT INTO records VALUES (
            ?, ?
        );
        """,
        (name, score)
    )
    bd.commit()


def get_best():
    cur.execute(
        """
        SELECT name gamer, MAX(score) score
        FROM records
        GROUP BY name
        ORDER BY score DESC
        LIMIT 3;
        """
    )
    return cur.fetchall()

# print(get_best())

# cur.close()
