import json
from urllib.request import urlopen
import psycopg2

from monster import Monster

url = 'https://www.osrsbox.com/osrsbox-db/monsters-complete.json'
resp = urlopen(url)
data = resp.read().decode('utf-8')
json = json.loads(data)

monsters = []

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()
cur.execute('set search_path = "runescape"')

for monster_id in json:
    monster_json = json[monster_id]
    monster = Monster(monster_json)
    sql = '''INSERT INTO monsters ( id,
        name,
        incomplete,
        members,
        release_date,
        combat_level,
        size,
        hitpoints,
        max_hit,
        attack_type,
        attack_speed,
        aggressive,
        poisonous,
        immune_poison,	
        immune_venom,	
        attributes,
        category,	
        slayer_monster,
        slayer_level,
        slayer_xp,	
        slayer_masters,	
        duplicate,	
        examine,	
        icon,	
        wiki_name,	
        wiki_url,	
        attack_level,	
        strength_level,
        defence_level,		
        magic_level,	
        ranged_level,		
        attack_stab,
        attack_slash,	
        attack_crush,	
        attack_magic,	
        attack_ranged,
        defence_stab,
        defence_slash,
        defence_crush,	
        defence_magic,	
        defence_ranged,	
        attack_accuracy,	
        melee_strength,	
        ranged_strength,		
        magic_damage,		
        drops) VALUES (%s, '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '%s', %s, '%s', '%s', %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s );''' % (monster.id, str(monster.name).replace("'", "").replace('(', '').replace(')', ''), monster.incomplete, monster.members,
        monster.release_date, monster.combat_level, monster.size, monster.hitpoints, monster.max_hit, monster.attack_type,
        monster.attack_speed, monster.aggressive, monster.poisonous, monster.immune_poison, monster.immune_venom, monster.attributes,
        monster.category, monster.slayer_monster, monster.slayer_level, monster.slayer_xp, monster.slayer_masters,
        monster.duplicate, str(monster.examine).replace("'", "").replace('(', '').replace(')', ''), monster.icon, str(monster.wiki_name).replace("'", "").replace('(', '').replace(')', ''), 
        str(monster.wiki_url).replace("'", "").replace('(', '').replace(')', ''), monster.attack_level, monster.strength_level, monster.defence_level, monster.magic_level,
        monster.ranged_level, monster.attack_stab, monster.attack_slash, monster.attack_crush, monster.attack_magic, monster.attack_ranged,
        monster.defence_stab, monster.defence_slash, monster.defence_crush, monster.defence_magic, monster.defence_ranged, monster.attack_accuracy,
        monster.melee_strength, monster.ranged_strength, monster.magic_damage, monster.drops)
    cur.execute(sql)

    conn.commit()
    
if conn:
    conn.close()