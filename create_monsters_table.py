import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

create = '''create table monsters (
    id	integer,
    name	text,
    incomplete	boolean,
    members	boolean,
    release_date	text,
    combat_level	integer,
    size	integer,
    hitpoints	integer,
    max_hit	integer,
    attack_type	text[],
    attack_speed	integer,
    aggressive	boolean,
    poisonous	boolean,
    immune_poison	boolean,	
    immune_venom	boolean,	
    attributes	text[],
    category	text[],	
    slayer_monster	boolean,
    slayer_level	integer,
    slayer_xp	float,	
    slayer_masters	text[],	
    duplicate	boolean,	
    examine	text,	
    icon	text,	
    wiki_name	text,	
    wiki_url	text,	
    attack_level	integer,	
    strength_level	integer,
    defence_level	integer,		
    magic_level	integer,	
    ranged_level	integer,		
    attack_stab	integer,
    attack_slash	integer,	
    attack_crush	integer,	
    attack_magic	integer,	
    attack_ranged	integer,
    defence_stab	integer,
    defence_slash	integer,
    defence_crush	integer,	
    defence_magic	integer,	
    defence_ranged	integer,	
    attack_accuracy	integer,	
    melee_strength	integer,	
    ranged_strength	integer,		
    magic_damage	integer,		
    drops	text[]
);
'''

cur.execute(create)
conn.commit()

cur.close()