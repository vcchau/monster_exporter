from osrsbox import monsters_api
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()
cur.execute('set search_path = "runescape"')

monsters = monsters_api.load()
print()
for monster in monsters:
    print(vars(monster))
    sql = '''INSERT INTO monsters (attack_type) VALUES (%s)''' % (monster.attack_type)
    cur.execute(sql)
    break

if conn:
    conn.close()