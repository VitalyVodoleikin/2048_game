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

cur.execute(
    """
    SELECT name, MAX(score) score
    FROM records
    GROUP BY name
    ORDER BY score DESC
    LIMIT 3;
    """
)

result = cur.fetchall()
print(result)

cur.close()
