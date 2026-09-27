from BaseClasses import ItemClassification
from worlds.burnout_paradise_remastered.constants import BreakableType, AreaType, ITEMS_OFFSET_BREAKABLES
from worlds.burnout_paradise_remastered.data import ItemTypeEnum
from worlds.burnout_paradise_remastered.data.locations.breakables import name_lookup

class Discoverables(ItemTypeEnum):
        PALM_BAY_HEIGHTS_SMASHES = (f"{AreaType.PALM_BAY_HEIGHTS.value} Breakable {name_lookup[BreakableType.SMASH]}es", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.PALM_BAY_HEIGHTS.index + BreakableType.SMASH.value, ItemClassification.progression)
        PALM_BAY_HEIGHTS_BILLBOARDS = (f"{AreaType.PALM_BAY_HEIGHTS.value} Breakable {name_lookup[BreakableType.BILLBOARD]}s", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.PALM_BAY_HEIGHTS.index + BreakableType.BILLBOARD.value, ItemClassification.progression)
        PALM_BAY_HEIGHTS_SUPER_JUMPS = (f"{AreaType.PALM_BAY_HEIGHTS.value} {name_lookup[BreakableType.SUPER_JUMP]}s", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.PALM_BAY_HEIGHTS.index + BreakableType.SUPER_JUMP.value, ItemClassification.progression)

        SILVER_LAKE_SMASHES = (f"{AreaType.SILVER_LAKE.value} Breakable {name_lookup[BreakableType.SMASH]}es", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.SILVER_LAKE.index + BreakableType.SMASH.value, ItemClassification.progression)
        SILVER_LAKE_BILLBOARDS = (f"{AreaType.SILVER_LAKE.value} Breakable {name_lookup[BreakableType.BILLBOARD]}s", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.SILVER_LAKE.index + BreakableType.BILLBOARD.value, ItemClassification.progression)
        SILVER_LAKE_SUPER_JUMPS = (f"{AreaType.SILVER_LAKE.value} {name_lookup[BreakableType.SUPER_JUMP]}s", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.SILVER_LAKE.index + BreakableType.SUPER_JUMP.value, ItemClassification.progression)

        WHITE_MOUNTAIN_SMASHES = (f"{AreaType.WHITE_MOUNTAIN.value} Breakable {name_lookup[BreakableType.SMASH]}es", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.WHITE_MOUNTAIN.index + BreakableType.SMASH.value, ItemClassification.progression)
        WHITE_MOUNTAIN_BILLBOARDS = (f"{AreaType.WHITE_MOUNTAIN.value} Breakable {name_lookup[BreakableType.BILLBOARD]}s", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.WHITE_MOUNTAIN.index + BreakableType.BILLBOARD.value, ItemClassification.progression)
        WHITE_MOUNTAIN_SUPER_JUMPS = (f"{AreaType.WHITE_MOUNTAIN.value} {name_lookup[BreakableType.SUPER_JUMP]}s", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.WHITE_MOUNTAIN.index + BreakableType.SUPER_JUMP.value, ItemClassification.progression)

        HARBOR_TOWN_SMASHES = (f"{AreaType.HARBOR_TOWN.value} Breakable {name_lookup[BreakableType.SMASH]}es", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.HARBOR_TOWN.index + BreakableType.SMASH.value, ItemClassification.progression)
        HARBOR_TOWN_BILLBOARDS = (f"{AreaType.HARBOR_TOWN.value} Breakable {name_lookup[BreakableType.BILLBOARD]}s", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.HARBOR_TOWN.index + BreakableType.BILLBOARD.value, ItemClassification.progression)
        HARBOR_TOWN_SUPER_JUMPS = (f"{AreaType.HARBOR_TOWN.value} {name_lookup[BreakableType.SUPER_JUMP]}s", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.HARBOR_TOWN.index + BreakableType.SUPER_JUMP.value, ItemClassification.progression)

        DOWNTOWN_PARADISE_SMASHES = (f"{AreaType.DOWNTOWN_PARADISE.value} Breakable {name_lookup[BreakableType.SMASH]}es", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.DOWNTOWN_PARADISE.index + BreakableType.SMASH.value, ItemClassification.progression)
        DOWNTOWN_PARADISE_BILLBOARDS = (f"{AreaType.DOWNTOWN_PARADISE.value} Breakable {name_lookup[BreakableType.BILLBOARD]}s", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.DOWNTOWN_PARADISE.index + BreakableType.BILLBOARD.value, ItemClassification.progression)
        DOWNTOWN_PARADISE_SUPER_JUMPS = (f"{AreaType.DOWNTOWN_PARADISE.value} {name_lookup[BreakableType.SUPER_JUMP]}s", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.DOWNTOWN_PARADISE.index + BreakableType.SUPER_JUMP.value, ItemClassification.progression)

        BIG_SURF_ISLAND_SMASHES = (f"{AreaType.BIG_SURF_ISLAND.value} Breakable {name_lookup[BreakableType.SMASH]}es", ITEMS_OFFSET_BREAKABLES + AreaType.BIG_SURF_ISLAND.index + 10 * BreakableType.SMASH.value, ItemClassification.progression)
        BIG_SURF_ISLAND_BILLBOARDS = (f"{AreaType.BIG_SURF_ISLAND.value} Breakable {name_lookup[BreakableType.BILLBOARD]}s", ITEMS_OFFSET_BREAKABLES + AreaType.BIG_SURF_ISLAND.index + 10 * BreakableType.BILLBOARD.value, ItemClassification.progression)
        BIG_SURF_ISLAND_MEGA_JUMPS = (f"{AreaType.BIG_SURF_ISLAND.value} Mega Jumps", ITEMS_OFFSET_BREAKABLES + 10 * AreaType.BIG_SURF_ISLAND.index + BreakableType.SUPER_JUMP, ItemClassification.progression)

