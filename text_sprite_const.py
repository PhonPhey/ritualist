''' Header file with texture and  sprite const'''

import arcade


def add_player_sprite(sprite):
    ''' Add player sprite '''

    sprite.center_x = 200
    sprite.center_y = 20

    return sprite

STONE_WALL = "res/texture/stone_wall.jpeg"  # Каменная стена

STONE_FLOOR = "res/texture/stone_floor.jpeg"  # Каменный пол

STONE_TRAPDOOR = "res/texture/stone_trapdoor.jpeg"  # Ловушка в каменном полу

# Магическая Ловушка в каменном полу
STONE_MAGIC_TRAPDOOR = "res/texture/stone_magic_trapdoor.jpeg"


# Кислотная Ловушка в каменном полу
STONE_ACID_TRAPDOOR = "res/texture/stone_acid_trapdoor.jpeg"

# Ловушка-иллюзия в каменном полу
STONE_ILLUSION_TRAPDOOR = "res/texture/stone_illusion_trapdoor.jpeg"

# Список из всех спрайтов
ALL_SPRITES = arcade.SpriteList()

# Блок добавления спрайтов в список спрайтов
MAGE_1_SPRITE = arcade.Sprite("res/sprite/MAGE/mage_1.png")
ALL_SPRITES.append(add_player_sprite(MAGE_1_SPRITE))

MAGE_2_SPRITE = arcade.Sprite("res/sprite/MAGE/mage_2.png")
ALL_SPRITES.append(add_player_sprite(MAGE_2_SPRITE))

MAGE_3_SPRITE = arcade.Sprite("res/sprite/MAGE/mage_3.png")
ALL_SPRITES.append(add_player_sprite(MAGE_3_SPRITE))

MAGE_4_SPRITE = arcade.Sprite("res/sprite/MAGE/mage_4.png")
ALL_SPRITES.append(add_player_sprite(MAGE_4_SPRITE))
