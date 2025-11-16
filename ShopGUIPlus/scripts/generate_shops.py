from pathlib import Path

# Always write the generated shop files to the ShopGUIPlus/shops directory even
# if this script is executed from another working directory.
base_dir = Path(__file__).resolve().parents[1] / 'shops'
base_dir.mkdir(parents=True, exist_ok=True)

slot_order = [i for i in range(54) if i not in (45, 49, 53)]

def resolve_slot(index: int) -> int:
    """Return a GUI slot while keeping navigation buttons reserved per page."""
    per_page = len(slot_order)
    slot = slot_order[(index - 1) % per_page]
    page = (index - 1) // per_page
    return slot + 54 * page

class Shop:
    def __init__(self, shop_id, title):
        self.shop_id = shop_id
        self.title = title
        self.items = []
    def add(self, material, quantity, buy, sell):
        self.items.append((material, quantity, buy, sell))

shops = {
    'blocks': Shop('blocks', 'Building Blocks (page %page%)'),
    'tools': Shop('tools', 'Tools (page %page%)'),
    'weapons': Shop('weapons', 'Weapons (page %page%)'),
    'armor': Shop('armor', 'Armor (page %page%)'),
    'farming': Shop('farming', 'Farming (page %page%)'),
    'mining': Shop('mining', 'Mining Materials (page %page%)'),
    'redstone': Shop('redstone', 'Redstone Lab (page %page%)'),
    'utility': Shop('utility', 'Utility Items (page %page%)'),
    'food': Shop('food', 'Food (page %page%)'),
    'drops': Shop('drops', 'Mob Drops (page %page%)'),
    'dyes': Shop('dyes', 'Dyes (page %page%)'),
    'brewing': Shop('brewing', 'Brewing Supplies (page %page%)'),
    'decorations': Shop('decorations', 'Decorations (page %page%)'),
    'miscellaneous': Shop('miscellaneous', 'Miscellaneous (page %page%)'),
}

colors = [
    'WHITE','ORANGE','MAGENTA','LIGHT_BLUE','YELLOW','LIME','PINK','GRAY','LIGHT_GRAY',
    'CYAN','PURPLE','BLUE','BROWN','GREEN','RED','BLACK'
]

wood_types = ['OAK','SPRUCE','BIRCH','JUNGLE','ACACIA','DARK_OAK','MANGROVE','CHERRY','BAMBOO','CRIMSON','WARPED']

stone_blocks = [
    ('STONE', 64, 50), ('COBBLESTONE', 64, 40), ('MOSSY_COBBLESTONE', 64, 60),
    ('SMOOTH_STONE', 64, 60), ('STONE_BRICKS', 64, 70), ('MOSSY_STONE_BRICKS', 64, 80),
    ('CRACKED_STONE_BRICKS', 64, 70), ('CHISELED_STONE_BRICKS', 64, 70),
    ('ANDESITE', 64, 50), ('POLISHED_ANDESITE', 64, 60), ('DIORITE', 64, 50),
    ('POLISHED_DIORITE', 64, 60), ('GRANITE', 64, 50), ('POLISHED_GRANITE', 64, 60),
    ('TUFF', 64, 50), ('CALCITE', 64, 80),
    ('DEEPSLATE', 64, 60), ('POLISHED_DEEPSLATE', 64, 70), ('DEEPSLATE_BRICKS', 64, 75),
    ('DEEPSLATE_TILES', 64, 80), ('BASALT', 64, 60), ('POLISHED_BASALT', 64, 70),
    ('BLACKSTONE', 64, 80), ('POLISHED_BLACKSTONE', 64, 90),
    ('POLISHED_BLACKSTONE_BRICKS', 64, 95), ('GILDED_BLACKSTONE', 32, 200)
]

for mat, qty, buy in stone_blocks:
    shops['blocks'].add(mat, qty, buy, buy//5)

for wood in wood_types:
    plank = f'{wood}_PLANKS'
    stairs = f'{wood}_STAIRS'
    slab = f'{wood}_SLAB'
    if wood in {'CRIMSON', 'WARPED'}:
        log = f'{wood}_STEM'
        stripped = f'STRIPPED_{wood}_STEM'
    elif wood == 'BAMBOO':
        log = 'BAMBOO_BLOCK'
        stripped = 'STRIPPED_BAMBOO_BLOCK'
    else:
        log = f'{wood}_LOG'
        stripped = f'STRIPPED_{wood}_LOG'
    fence = f'{wood}_FENCE'
    door = f'{wood}_DOOR'
    shops['blocks'].add(plank, 64, 70, 14)
    shops['blocks'].add(stairs, 64, 70, 14)
    shops['blocks'].add(slab, 64, 60, 12)
    shops['blocks'].add(log, 32, 120, 24)
    shops['blocks'].add(stripped, 32, 130, 26)
    shops['blocks'].add(fence, 64, 65, 13)
    shops['blocks'].add(door, 16, 50, 10)

sand_set = [('SAND',64,40),('RED_SAND',64,60),('SANDSTONE',64,70),('CUT_SANDSTONE',64,75),
            ('SMOOTH_SANDSTONE',64,80),('RED_SANDSTONE',64,70),('CUT_RED_SANDSTONE',64,75),
            ('SMOOTH_RED_SANDSTONE',64,80),('GLASS',64,60),('TINTED_GLASS',64,90),
            ('GLASS_PANE',64,40),('SEA_LANTERN',32,160),('PRISMARINE',64,90),
            ('PRISMARINE_BRICKS',64,95),('DARK_PRISMARINE',64,110)]
for mat, qty, buy in sand_set:
    shops['blocks'].add(mat, qty, buy, buy//5)

for color in colors:
    shops['blocks'].add(f'{color}_WOOL', 64, 60, 12)
    shops['blocks'].add(f'{color}_CONCRETE', 64, 80, 16)
    shops['blocks'].add(f'{color}_CONCRETE_POWDER', 64, 70, 14)
    shops['blocks'].add(f'{color}_TERRACOTTA', 64, 70, 14)
    shops['blocks'].add(f'{color}_GLAZED_TERRACOTTA', 64, 90, 18)
    shops['blocks'].add(f'{color}_STAINED_GLASS', 64, 70, 14)
    shops['blocks'].add(f'{color}_STAINED_GLASS_PANE', 64, 50, 10)
    shops['blocks'].add(f'{color}_CARPET', 64, 40, 8)

extra_blocks = [
    ('BRICKS',64,90),('NETHER_BRICKS',64,90),('RED_NETHER_BRICKS',64,110),
    ('QUARTZ_BLOCK',64,110),('CHISELED_QUARTZ_BLOCK',64,115),('QUARTZ_BRICKS',64,115),
    ('SMOOTH_QUARTZ',64,120),('PURPUR_BLOCK',64,130),('PURPUR_PILLAR',64,135),
    ('END_STONE',64,90),('END_STONE_BRICKS',64,95),('WHITE_CONCRETE',64,80),
    ('GLOWSTONE',64,110),('BLUE_ICE',32,200),('PACKED_ICE',64,120),('ICE',64,80),
    ('OBSIDIAN',32,180),('CRYING_OBSIDIAN',32,200),('HONEY_BLOCK',32,140),
    ('SLIME_BLOCK',32,140),('AMETHYST_BLOCK',32,150),('BUDDING_AMETHYST',1,500),
    ('MUD_BRICKS',64,80),('MUD',64,50),('MANGROVE_ROOTS',64,60),('MOSS_BLOCK',64,70),
    ('MOSS_CARPET',64,40),('DRIPSTONE_BLOCK',64,70),('POINTED_DRIPSTONE',32,80)
]
for mat, qty, buy in extra_blocks:
    shops['blocks'].add(mat, qty, buy, max(2, buy//5))

# Tools shop
tool_materials = ['WOODEN','STONE','IRON','GOLDEN','DIAMOND']
for mat in tool_materials:
    pickaxe_buy = 100 if mat=='WOODEN' else 160 if mat=='STONE' else 320 if mat=='IRON' else 260 if mat=='GOLDEN' else 900
    axe_buy = 90 if mat=='WOODEN' else 150 if mat=='STONE' else 300 if mat=='IRON' else 240 if mat=='GOLDEN' else 800
    shovel_buy = 60 if mat=='WOODEN' else 90 if mat=='STONE' else 180 if mat=='IRON' else 120 if mat=='GOLDEN' else 500
    hoe_buy = 50 if mat=='WOODEN' else 80 if mat=='STONE' else 150 if mat=='IRON' else 110 if mat=='GOLDEN' else 400
    shops['tools'].add(f'{mat}_PICKAXE', 1, pickaxe_buy, pickaxe_buy//5)
    shops['tools'].add(f'{mat}_AXE', 1, axe_buy, axe_buy//5)
    shops['tools'].add(f'{mat}_SHOVEL', 1, shovel_buy, shovel_buy//5)
    shops['tools'].add(f'{mat}_HOE', 1, hoe_buy, hoe_buy//5)

additional_tools = [
    ('SHEARS',1,150),('FISHING_ROD',1,200),('FLINT_AND_STEEL',1,120),
    ('COMPASS',1,250),('CLOCK',1,250),('SPYGLASS',1,300),('LEAD',1,180),
    ('NAME_TAG',1,220),('BRUSH',1,120),('CARROT_ON_A_STICK',1,90),('WARPED_FUNGUS_ON_A_STICK',1,100),
    ('STONECUTTER',1,200),('ANVIL',1,450),('SMITHING_TABLE',1,220),('CARTOGRAPHY_TABLE',1,160),
    ('LOOM',1,140),('COMPOSTER',1,120),('BARREL',1,100),('GRINDSTONE',1,180),('FLETCHING_TABLE',1,160),
    ('BLAST_FURNACE',1,320),('SMOKER',1,220),('FURNACE',1,150),('CRAFTING_TABLE',1,80),
    ('ENCHANTING_TABLE',1,600),('BREWING_STAND',1,250),('CAULDRON',1,200),('CAMPFIRE',1,160),
    ('SOUL_CAMPFIRE',1,200),('BELL',1,400)
]
for mat, qty, buy in additional_tools:
    shops['tools'].add(mat, qty, buy, buy//5)

# Weapons
weapon_materials = ['WOODEN','STONE','IRON','GOLDEN','DIAMOND']
for mat in weapon_materials:
    sword_buy = 90 if mat=='WOODEN' else 140 if mat=='STONE' else 260 if mat=='IRON' else 200 if mat=='GOLDEN' else 700
    shops['weapons'].add(f'{mat}_SWORD',1,sword_buy,sword_buy//5)
axe_materials = ['WOODEN','STONE','IRON','GOLDEN','DIAMOND']
for mat in axe_materials:
    axe_buy = 90 if mat=='WOODEN' else 150 if mat=='STONE' else 300 if mat=='IRON' else 240 if mat=='GOLDEN' else 800
    shops['weapons'].add(f'{mat}_AXE',1,axe_buy,axe_buy//5)
weapon_extras = [
    ('BOW',1,220),('CROSSBOW',1,260),('TRIDENT',1,600),('SHIELD',1,200),
    ('ARROW',64,120),('SPECTRAL_ARROW',64,150),('TIPPED_ARROW',64,200),('FIREWORK_ROCKET',64,200),
    ('FIREWORK_STAR',64,140),('FIRE_CHARGE',16,160),('FLINT_AND_STEEL',1,120),('SNOWBALL',16,60),
    ('EGG',16,60),('ENDER_PEARL',16,260),('ENDER_EYE',16,320),('TNT',16,220),('TNT_MINECART',16,360),
    ('LAVA_BUCKET',1,240),('RESPAWN_ANCHOR',1,700),('END_CRYSTAL',16,260),('LIGHTNING_ROD',1,120),
    ('FISHING_ROD',1,200),('POTION',16,140),('SPLASH_POTION',16,150),('LINGERING_POTION',16,180),
    ('FLINT',64,80),('FEATHER',64,90),('STRING',64,120),('STICK',64,40),('GUNPOWDER',64,160),
    ('BLAZE_ROD',64,220),('BLAZE_POWDER',64,200),('SLIME_BALL',64,180),('HONEY_BLOCK',32,140),
    ('POWDER_SNOW_BUCKET',1,240),('WATER_BUCKET',1,220)
]
for mat, qty, buy in weapon_extras:
    shops['weapons'].add(mat,qty,buy,buy//5)

# Armor
armor_materials = ['LEATHER','CHAINMAIL','IRON','GOLDEN','DIAMOND']
slots = ['HELMET','CHESTPLATE','LEGGINGS','BOOTS']
price_map = {
    'LEATHER': (150, 200, 180, 120),
    'CHAINMAIL': (200, 260, 240, 180),
    'IRON': (220, 320, 280, 200),
    'GOLDEN': (200, 280, 240, 180),
    'DIAMOND': (600, 800, 700, 500)
}
for mat in armor_materials:
    p = price_map[mat]
    for slot_name, cost in zip(slots, p):
        shops['armor'].add(f'{mat}_{slot_name}',1,cost,cost//5)
armor_extras = [
    ('SHIELD',1,200),('TURTLE_HELMET',1,400),('CARVED_PUMPKIN',1,60),('ARMOR_STAND',1,140),
    ('LEATHER_HORSE_ARMOR',1,200),('IRON_HORSE_ARMOR',1,300),
    ('GOLDEN_HORSE_ARMOR',1,320),('DIAMOND_HORSE_ARMOR',1,450)
]
for mat, qty, buy in armor_extras:
    shops['armor'].add(mat,qty,buy,buy//5)
trim_templates = [
    'COAST_ARMOR_TRIM_SMITHING_TEMPLATE','DUNE_ARMOR_TRIM_SMITHING_TEMPLATE',
    'EYE_ARMOR_TRIM_SMITHING_TEMPLATE','HOST_ARMOR_TRIM_SMITHING_TEMPLATE',
    'RAISER_ARMOR_TRIM_SMITHING_TEMPLATE','RIB_ARMOR_TRIM_SMITHING_TEMPLATE',
    'SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE','SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE',
    'SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE','SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE',
    'SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE','TIDE_ARMOR_TRIM_SMITHING_TEMPLATE',
    'VEX_ARMOR_TRIM_SMITHING_TEMPLATE','WARD_ARMOR_TRIM_SMITHING_TEMPLATE',
    'WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE','WILD_ARMOR_TRIM_SMITHING_TEMPLATE'
]
for template in trim_templates:
    shops['armor'].add(template,1,250,50)
shops['armor'].add('ELYTRA',1,0,0)

# Farming
crops = [
    ('WHEAT_SEEDS',64,60),('BEETROOT_SEEDS',64,60),('MELON_SEEDS',64,80),('PUMPKIN_SEEDS',64,80),
    ('CARROT',64,80),('POTATO',64,80),('BEETROOT',64,80),('SUGAR_CANE',64,80),('BAMBOO',64,80),
    ('KELP',64,70),('COCOA_BEANS',64,80),('NETHER_WART',64,120),('GLOW_BERRIES',32,100),
    ('SWEET_BERRIES',64,80),('CHORUS_FRUIT',64,120),('WHEAT',64,90),('HAY_BLOCK',64,150),
    ('TORCHFLOWER_SEEDS',64,120),('TORCHFLOWER',64,80),('PITCHER_POD',64,120),('PITCHER_PLANT',64,80),
    ('SNIFFER_EGG',4,400)
]
for mat, qty, buy in crops:
    shops['farming'].add(mat, qty, buy, buy//5)

for wood in wood_types:
    if wood == 'MANGROVE':
        sapling = 'MANGROVE_PROPAGULE'
    elif wood == 'BAMBOO':
        sapling = 'BAMBOO'
    elif wood == 'CRIMSON':
        sapling = 'CRIMSON_NYLIUM'
    elif wood == 'WARPED':
        sapling = 'WARPED_NYLIUM'
    else:
        sapling = f'{wood}_SAPLING'
    qty = 32
    buy = 140 if wood in {'CRIMSON','WARPED'} else 120
    shops['farming'].add(sapling, qty, buy, buy//5)
fungi = [('CRIMSON_FUNGUS',32,140),('WARPED_FUNGUS',32,140),('NETHER_SPROUTS',64,80),('WARPED_ROOTS',64,80),('CRIMSON_ROOTS',64,80)]
for mat, qty, buy in fungi:
    shops['farming'].add(mat, qty, buy, buy//5)
farmsupplies = [
    ('BONE_MEAL',64,80),('COMPOSTER',1,120),('WATER_BUCKET',1,200),('LAVA_BUCKET',1,220),('MILK_BUCKET',1,200),
    ('BEEHIVE',1,250),('BEE_NEST',1,260),('SHEARS',1,150),('HONEYCOMB',32,160),('HONEY_BOTTLE',16,160),
    ('FLOWER_POT',16,90),('SCULK_SENSOR',1,220),('BRUSH',1,120)
]
for mat, qty, buy in farmsupplies:
    shops['farming'].add(mat, qty, buy, buy//5)

# Mining
minerals = [
    ('COAL',64,120),('CHARCOAL',64,100),('RAW_IRON',64,220),('RAW_COPPER',64,200),('RAW_GOLD',64,260),
    ('IRON_INGOT',64,320),('COPPER_INGOT',64,260),('GOLD_INGOT',64,420),('LAPIS_LAZULI',64,220),
    ('REDSTONE',64,200),('EMERALD',32,450),('DIAMOND',32,600),('AMETHYST_SHARD',64,240),
    ('PRISMARINE_CRYSTALS',64,260),('PRISMARINE_SHARD',64,240),('QUARTZ',64,200),('NETHER_QUARTZ_ORE',64,260),
    ('ECHO_SHARD',16,400)
]
for mat, qty, buy in minerals:
    shops['mining'].add(mat, qty, buy, buy//5)

ore_blocks = [
    ('COAL_ORE',32,240),('IRON_ORE',32,300),('COPPER_ORE',32,260),('GOLD_ORE',32,340),('LAPIS_ORE',32,260),
    ('REDSTONE_ORE',32,280),('DIAMOND_ORE',16,650),('EMERALD_ORE',16,700),('NETHER_GOLD_ORE',32,320),
    ('NETHER_QUARTZ_ORE',32,260),('DEEPSLATE_COAL_ORE',32,260),('DEEPSLATE_IRON_ORE',32,320),
    ('DEEPSLATE_COPPER_ORE',32,300),('DEEPSLATE_GOLD_ORE',32,360),('DEEPSLATE_REDSTONE_ORE',32,320),
    ('DEEPSLATE_DIAMOND_ORE',16,700),('DEEPSLATE_EMERALD_ORE',16,720)
]
for mat, qty, buy in ore_blocks:
    shops['mining'].add(mat, qty, buy, buy//5)

mining_blocks = [
    ('COAL_BLOCK',64,400),('IRON_BLOCK',64,600),('COPPER_BLOCK',64,520),('GOLD_BLOCK',64,800),
    ('LAPIS_BLOCK',64,500),('REDSTONE_BLOCK',64,480),('DIAMOND_BLOCK',32,1600),('EMERALD_BLOCK',32,1700),
    ('AMETHYST_BLOCK',32,400),('HONEYCOMB_BLOCK',64,260),('RAW_IRON_BLOCK',32,420),('RAW_GOLD_BLOCK',32,480),
    ('RAW_COPPER_BLOCK',32,400)
]
for mat, qty, buy in mining_blocks:
    shops['mining'].add(mat, qty, buy, buy//5)

# Redstone
redstone_items = [
    ('REDSTONE',64,200),('REDSTONE_TORCH',64,220),('REDSTONE_BLOCK',64,480),('REPEATER',64,260),('COMPARATOR',64,300),
    ('REDSTONE_LAMP',64,280),('LEVER',64,120),('STONE_BUTTON',64,80),('OAK_BUTTON',64,80),('STONE_PRESSURE_PLATE',64,120),
    ('HEAVY_WEIGHTED_PRESSURE_PLATE',64,180),('LIGHT_WEIGHTED_PRESSURE_PLATE',64,160),('OBSERVER',64,320),
    ('PISTON',64,260),('STICKY_PISTON',64,320),('SLIME_BLOCK',32,140),('HONEY_BLOCK',32,140),('DISPENSER',64,260),
    ('DROPPER',64,200),('HOPPER',64,320),('TARGET',64,220),('DAYLIGHT_DETECTOR',64,260),('LECTERN',64,220),
    ('NOTE_BLOCK',64,200),('SCULK_SENSOR',32,220),('SCULK_SHRIEKER',32,260),('TRIPWIRE_HOOK',64,140),
    ('STRING',64,120),('TRAPPED_CHEST',64,260),('BARREL',64,120),('CHAIN',64,160),('BELL',16,400),
    ('LIGHTNING_ROD',32,120),('COPPER_BLOCK',64,520),('CHISELED_BOOKSHELF',64,220),('ITEM_FRAME',64,160)
]
for mat, qty, buy in redstone_items:
    shops['redstone'].add(mat, qty, buy, buy//5)

rail_items = [
    ('RAIL',64,200),('POWERED_RAIL',64,320),('DETECTOR_RAIL',64,280),('ACTIVATOR_RAIL',64,280),
    ('MINECART',16,260),('CHEST_MINECART',16,320),('HOPPER_MINECART',16,360),('FURNACE_MINECART',16,300),
    ('TNT_MINECART',16,360),('COMMAND_BLOCK_MINECART',1,0)
]
for mat, qty, buy in rail_items:
    if 'COMMAND_BLOCK' in mat:
        continue
    shops['redstone'].add(mat, qty, buy, buy//5)

# Utility
utility_items = [
    ('BUCKET',1,200),('WATER_BUCKET',1,220),('LAVA_BUCKET',1,240),('POWDER_SNOW_BUCKET',1,240),
    ('MINECART',1,260),('SADDLE',1,220),('LEAD',1,180),('NAME_TAG',1,220),('ENDER_CHEST',1,600),
    ('SHULKER_BOX',1,420),('CLOCK',1,250),('COMPASS',1,250),
    ('MAP',1,200),('FILLED_MAP',1,220),('RECOVERY_COMPASS',1,400),('FIREWORK_ROCKET',64,200),
    ('SPYGLASS',1,300),('GLOW_INK_SAC',32,200),('ENDER_PEARL',16,260),('ENDER_EYE',16,320),
    ('HEART_OF_THE_SEA',1,600),('NAUTILUS_SHELL',16,260)
]
for mat, qty, buy in utility_items:
    shops['utility'].add(mat, qty, buy, buy//5)

boat_materials = ['OAK','SPRUCE','BIRCH','JUNGLE','ACACIA','DARK_OAK','MANGROVE','CHERRY']
for wood in boat_materials:
    shops['utility'].add(f'{wood}_BOAT',1,120,24)
    shops['utility'].add(f'{wood}_CHEST_BOAT',1,160,32)
shops['utility'].add('BAMBOO_RAFT',1,120,24)
shops['utility'].add('BAMBOO_CHEST_RAFT',1,160,32)

for color in colors:
    shops['utility'].add(f'{color}_BED',1,160,32)
    shops['utility'].add(f'{color}_SHULKER_BOX',1,420,84)

# Food
foods = [
    ('APPLE',64,80),('GOLDEN_APPLE',16,600),('CARROT',64,80),('GOLDEN_CARROT',64,200),
    ('POTATO',64,80),('BAKED_POTATO',64,90),('POISONOUS_POTATO',64,80),('BEETROOT',64,80),
    ('BEETROOT_SOUP',32,120),('WHEAT',64,90),('BREAD',64,90),('COOKIE',64,80),('CAKE',16,200),
    ('PUMPKIN_PIE',32,150),('MELON_SLICE',64,70),('GLISTERING_MELON_SLICE',64,220),('SUGAR',64,60),
    ('SWEET_BERRIES',64,80),('GLOW_BERRIES',32,100),('CHORUS_FRUIT',64,120),('DRIED_KELP',64,60),
    ('DRIED_KELP_BLOCK',64,120),('BEEF',64,90),('COOKED_BEEF',64,140),('PORKCHOP',64,90),
    ('COOKED_PORKCHOP',64,140),('MUTTON',64,80),('COOKED_MUTTON',64,120),('CHICKEN',64,80),
    ('COOKED_CHICKEN',64,120),('RABBIT',64,80),('COOKED_RABBIT',64,120),('RABBIT_STEW',32,160),
    ('MUSHROOM_STEW',32,120),('SUSPICIOUS_STEW',32,140),('COD',64,80),('COOKED_COD',64,120),
    ('SALMON',64,80),('COOKED_SALMON',64,140),('PUFFERFISH',32,90),('TROPICAL_FISH',32,90),
    ('HONEY_BOTTLE',32,160),('ROTTEN_FLESH',64,40),('SPIDER_EYE',64,60),('MILK_BUCKET',1,200),
    ('EGG',64,80)
]
for mat, qty, buy in foods:
    shops['food'].add(mat, qty, buy, buy//5)

# Drops
mob_drops = [
    ('BONE',64,80),('ARROW',64,120),('ENDER_PEARL',16,260),('GUNPOWDER',64,160),('SLIME_BALL',64,180),
    ('MAGMA_CREAM',64,200),('BLAZE_ROD',64,220),('GHAST_TEAR',16,260),('PHANTOM_MEMBRANE',32,200),
    ('SHULKER_SHELL',16,240),('WITHER_SKELETON_SKULL',8,400),('TURTLE_SCUTE',32,220),('RABBIT_HIDE',64,120),
    ('RABBIT_FOOT',32,180),('LEATHER',64,140),('FEATHER',64,90),('STRING',64,120),
    ('SPIDER_EYE',64,60),('ROTTEN_FLESH',64,40),('GLOW_INK_SAC',32,200),('INK_SAC',64,90),('NAUTILUS_SHELL',16,260),
    ('PRISMARINE_CRYSTALS',64,260),('PRISMARINE_SHARD',64,240),('HEART_OF_THE_SEA',1,600),('TOTEM_OF_UNDYING',1,800),
    ('DRAGON_BREATH',16,300),('WITHER_ROSE',32,150),('DISC_FRAGMENT_5',32,200),('MUSIC_DISC_5',1,220),
    ('VERDANT_FROGLIGHT',32,200),('OCHRE_FROGLIGHT',32,200),('PEARLESCENT_FROGLIGHT',32,200),('FROGSPAWN',16,200),
    ('SCULK_CATALYST',16,220),('SCULK',64,120),('SCULK_VEIN',64,120),('SCULK_SENSOR',32,220),
    ('SPONGE',32,220),('WET_SPONGE',32,220),('ZOMBIE_HEAD',8,300),('SKELETON_SKULL',8,300),
    ('CREEPER_HEAD',8,320),('PIGLIN_HEAD',8,320),('DRAGON_HEAD',1,400),('SADDLE',1,220)
]
for mat, qty, buy in mob_drops:
    if mat in {'ELYTRA','NETHER_STAR'}:
        continue
    shops['drops'].add(mat, qty, buy, max(2, buy//5))

# Dyes
for color in colors:
    shops['dyes'].add(f'{color}_DYE',64,90,18)
shops['dyes'].add('INK_SAC',64,90,18)
shops['dyes'].add('GLOW_INK_SAC',64,140,28)
shops['dyes'].add('BONE_MEAL',64,80,16)
shops['dyes'].add('BLACK_DYE',64,90,18)
shops['dyes'].add('BROWN_DYE',64,90,18)
dye_sources = ['LAPIS_LAZULI','COCOA_BEANS','BEETROOT','CACTUS','SEA_PICKLE','WITHER_ROSE',
               'OXEYE_DAISY','BLUE_ORCHID','CORNFLOWER','ALLIUM','AZURE_BLUET','PINK_PETALS',
               'LILY_OF_THE_VALLEY','PEONY','SUNFLOWER','ROSE_BUSH']
for src in dye_sources:
    shops['dyes'].add(src,64,80,16)
extra_dye_flowers = ['POPPY','DANDELION','RED_TULIP','WHITE_TULIP','ORANGE_TULIP','PINK_TULIP',
                     'LILAC','FLOWERING_AZALEA','TORCHFLOWER','PITCHER_PLANT']
for flower in extra_dye_flowers:
    shops['dyes'].add(flower,64,80,16)

# Brewing
brewing_items = [
    ('BREWING_STAND',1,250),('CAULDRON',1,200),('GLASS_BOTTLE',64,80),('POTION',16,140),('SPLASH_POTION',16,150),
    ('LINGERING_POTION',16,180),('BLAZE_ROD',64,200),('BLAZE_POWDER',64,200),('NETHER_WART',64,120),
    ('FERMENTED_SPIDER_EYE',64,160),('MAGMA_CREAM',64,200),('GHAST_TEAR',32,260),('PHANTOM_MEMBRANE',32,200),
    ('RABBIT_FOOT',32,180),('PUFFERFISH',32,90),('SUGAR',64,60),('GLISTERING_MELON_SLICE',64,220),
    ('GUNPOWDER',64,160),('REDSTONE',64,200),('GLOWSTONE_DUST',64,200),('DRAGON_BREATH',16,300),
    ('TURTLE_HELMET',1,400),('TURTLE_SCUTE',32,220),('EXPERIENCE_BOTTLE',32,260),('SPIDER_EYE',64,60),
    ('SOUL_SAND',64,120),('SOUL_SOIL',64,120),('NETHER_BRICKS',64,130),('NETHER_BRICK_FENCE',64,120),
    ('NETHER_WART_BLOCK',64,140),('WARPED_WART_BLOCK',64,140),('CRIMSON_ROOTS',64,80),('WARPED_ROOTS',64,80),
    ('CRIMSON_FUNGUS',32,140),('WARPED_FUNGUS',32,140),('NETHER_SPROUTS',64,80),('WEEPING_VINES',64,100),
    ('TWISTING_VINES',64,100),('SHROOMLIGHT',32,180),('SOUL_TORCH',64,120),('SOUL_LANTERN',32,220),
    ('GLOWSTONE',64,200),('HONEYCOMB',32,160),('HONEY_BOTTLE',32,160),('SUGAR_CANE',64,80),
    ('BROWN_MUSHROOM',64,80),('RED_MUSHROOM',64,80),('MILK_BUCKET',1,200),('GOLDEN_CARROT',64,200)
]
for mat, qty, buy in brewing_items:
    shops['brewing'].add(mat, qty, buy, buy//5)

# Decorations
decor_items = [
    ('PAINTING',16,150),('ITEM_FRAME',16,140),('FLOWER_POT',32,90),('ARMOR_STAND',16,140),('BOOKSHELF',64,160),
    ('LECTERN',16,220),('GLOW_ITEM_FRAME',16,180),('CHAIN',64,160),('LANTERN',32,200),('SOUL_LANTERN',32,220),
    ('CANDLE',64,100),('BLACK_CANDLE',64,110),('WHITE_CANDLE',64,110),('TORCH',64,90),('SOUL_TORCH',64,120),
    ('FLOWERING_AZALEA',32,160),('AZALEA',32,150),('HANGING_ROOTS',64,80),('SMALL_DRIPLEAF',32,120),
    ('BIG_DRIPLEAF',32,150),('GLOW_LICHEN',64,90),('VINE',64,80),('LILY_PAD',32,80),('SEA_PICKLE',32,90),
    ('SPORE_BLOSSOM',16,200),('FLOWER_BANNER_PATTERN',1,140),('GLOBE_BANNER_PATTERN',1,160),
    ('PIGLIN_BANNER_PATTERN',1,160),('CREEPER_BANNER_PATTERN',1,160),('SKULL_BANNER_PATTERN',1,160),
    ('MOJANG_BANNER_PATTERN',1,200),('MUSIC_DISC_13',1,200),('MUSIC_DISC_CAT',1,200),('MUSIC_DISC_BLOCKS',1,200),
    ('MUSIC_DISC_CHIRP',1,200),('MUSIC_DISC_FAR',1,200),('MUSIC_DISC_MALL',1,200),('MUSIC_DISC_MELLOHI',1,200),
    ('MUSIC_DISC_STAL',1,200),('MUSIC_DISC_STRAD',1,200),('MUSIC_DISC_WARD',1,200),('MUSIC_DISC_11',1,200),
    ('MUSIC_DISC_WAIT',1,200),('MUSIC_DISC_OTHERSIDE',1,240),('MUSIC_DISC_PIGSTEP',1,260),('MUSIC_DISC_RELIC',1,260),
    ('ALLIUM',64,70),('ROSE_BUSH',64,80),('SUNFLOWER',64,80),('LILAC',64,80),('PEONY',64,80),('WITHER_ROSE',32,150),
    ('BLUE_ORCHID',64,70),('CORNFLOWER',64,70),('OXEYE_DAISY',64,70),('POPPY',64,70),('DANDELION',64,70),
    ('RED_TULIP',64,70),('WHITE_TULIP',64,70),('PINK_TULIP',64,70),('ORANGE_TULIP',64,70)
]
for mat, qty, buy in decor_items:
    shops['decorations'].add(mat, qty, buy, buy//5)

# Miscellaneous
misc_items = [
    ('BOOK',64,120),('WRITABLE_BOOK',16,150),('ENCHANTED_BOOK',1,250),('EXPERIENCE_BOTTLE',32,260),
    ('TURTLE_SCUTE',32,220),('ECHO_SHARD',16,400),('BRUSH',1,120),('SADDLE',1,220),('TOTEM_OF_UNDYING',1,800),
    ('HEART_OF_THE_SEA',1,600),('NAUTILUS_SHELL',16,260),
    ('FIREWORK_ROCKET',64,200),('FIREWORK_STAR',64,140),('LEATHER_HORSE_ARMOR',1,200),('IRON_HORSE_ARMOR',1,300),
    ('GOLDEN_HORSE_ARMOR',1,320),('DIAMOND_HORSE_ARMOR',1,450),('SADDLE',1,220),('LEAD',1,180),('NAME_TAG',1,220),
    ('CLOCK',1,250),('COMPASS',1,250),('RECOVERY_COMPASS',1,400),('ENDER_EYE',16,320),('ENDER_PEARL',16,260)
]
for mat, qty, buy in misc_items:
    shops['miscellaneous'].add(mat, qty, buy, buy//5)


def build_yaml(shop: Shop):
    lines = []
    lines.append(f"{shop.shop_id}:")
    lines.append(f"  name: \"{shop.title}\"")
    lines.append("  size: 54")
    lines.append("  fillItem:")
    lines.append("    material: GRAY_STAINED_GLASS_PANE")
    lines.append("  buttons:")
    lines.append("    goBack:")
    lines.append("      slot: 49")
    lines.append("    previousPage:")
    lines.append("      slot: 45")
    lines.append("    nextPage:")
    lines.append("      slot: 53")
    lines.append("  items:")
    for index, (material, quantity, buy, sell) in enumerate(shop.items, start=1):
        slot = resolve_slot(index)
        lines.append(f"    {index}:")
        lines.append("      type: item")
        lines.append("      item:")
        lines.append(f"        material: {material}")
        lines.append(f"        quantity: {quantity}")
        lines.append(f"      buyPrice: {buy}")
        lines.append(f"      sellPrice: {sell}")
        lines.append(f"      slot: {slot}")
    return "\n".join(lines) + "\n"

for shop in shops.values():
    yaml_text = build_yaml(shop)
    (base_dir / f"{shop.shop_id}.yml").write_text(yaml_text)
