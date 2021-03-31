import json

class Monster:

    def __init__(self, info):
        self.id = info.get('id', 'null') or 'null'
        self.name = info.get('name', 'null') or 'null'
        self.incomplete = info.get('incomplete', 'null') or 'null'
        self.members	= info.get('members', 'null') or 'null'
        self.release_date = info.get('release_date', 'null') or 'null'
        self.combat_level = info.get('combat_level', 'null') or 'null'
        self.size = info.get('size', 'null') or 'null'
        self.hitpoints = info.get('hitpoints', 'null') or 'null'
        self.max_hit	= info.get('max_hit', 'null') or 'null'

        attack_types = info.get('attack_type', 'null') or 'null'
        # self.attack_type	= str(set(attack_types))
        self.attack_type = 'null'
        
        self.attack_speed = info.get('attack_speed', 'null') or 'null'
        self.aggressive = info.get('aggressive', 'null') or 'null'
        self.poisonous = info.get('poisonous', 'null') or 'null'
        self.immune_poison = info.get('immune_poison', 'null') or 'null'
        self.immune_venom = info.get('immune_venom', 'null') or 'null'

        # self.attributes = str(set(info.get('attributes', 'null') or 'null'))
        # self.category = str(set(info.get('category', 'null') or 'null'))
        self.attributes = 'null'
        self.category = 'null'
        
        self.slayer_monster = info.get('slayer_monster', 'null') or 'null'
        self.slayer_level = info.get('slayer_level', 'null') or 'null'
        self.slayer_xp = info.get('slayer_xp', 'null') or 'null'

        # self.slayer_masters = str(set(info.get('slayer_masters', 'null') or 'null'))
        self.slayer_masters = 'null'

        self.duplicate = info.get('duplicate', 'null') or 'null'
        self.examine	= str(info.get('examine', 'null') or 'null')
        self.icon = info.get('icon', 'null') or 'null'
        self.wiki_name = info.get('wiki_name', 'null') or 'null'
        self.wiki_url = info.get('wiki_url', 'null') or 'null'
        self.attack_level = info.get('attack_level', 0)
        self.strength_level = info.get('strength_level', 0)
        self.defence_level = info.get('defence_level', 0)	
        self.magic_level = info.get('magic_level', 0)
        self.ranged_level	= info.get('ranged_level', 0)
        self.attack_stab	= info.get('attack_stab', 0)
        self.attack_slash	= info.get('attack_slash', 0)	
        self.attack_crush	= info.get('attack_crush', 0)	
        self.attack_magic	= info.get('attack_magic', 0)	
        self.attack_ranged	= info.get('attack_ranged', 0)
        self.defence_stab	= info.get('defence_stab', 0)
        self.defence_slash	= info.get('defence_slash', 0)
        self.defence_crush	= info.get('defence_crush', 0)	
        self.defence_magic	= info.get('defence_magic', 0)	
        self.defence_ranged	= info.get('defence_ranged', 0)	
        self.attack_accuracy	= info.get('attack_accuracy', 0)	
        self.melee_strength	= info.get('melee_strength', 0)	
        self.ranged_strength	= info.get('ranged_strength', 0)
        self.magic_damage	= info.get('magic_damage', 0)
        
        # self.drops = json.dumps(info.get('drops', 'null') or 'null')
        self.drops = 'null'

