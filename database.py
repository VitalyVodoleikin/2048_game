import sqlite3

bd = sqlite3.connect("2048.sqlite")

cur = bd.cursor()

cur.execute(
    """
    create table if not exists RECORDS (
        name text,
        score integer
    );
    """
)


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


print(get_best())

# cur.close()
