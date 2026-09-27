from ...constants import AreaType
from .. import RegionTypeEnum


class Regions(RegionTypeEnum):
    PALM_BAY_HEIGHTS = AreaType.PALM_BAY_HEIGHTS.value
    SILVER_LAKE = AreaType.SILVER_LAKE.value
    WHITE_MOUNTAIN = AreaType.WHITE_MOUNTAIN.value
    HARBOR_TOWN = AreaType.HARBOR_TOWN.value
    DOWNTOWN_PARADISE = AreaType.DOWNTOWN_PARADISE.value
    BIG_SURF_ISLAND = AreaType.BIG_SURF_ISLAND.value

    PALM_BAY_HEIGHTS_BREAKABLES = f"{AreaType.PALM_BAY_HEIGHTS.value} Breakables"
    SILVER_LAKE_BREAKABLES = f"{AreaType.SILVER_LAKE.value} Breakables"
    WHITE_MOUNTAIN_BREAKABLES = f"{AreaType.WHITE_MOUNTAIN.value} Breakables"
    HARBOR_TOWN_BREAKABLES = f"{AreaType.HARBOR_TOWN.value} Breakables"
    DOWNTOWN_PARADISE_BREAKABLES = f"{AreaType.DOWNTOWN_PARADISE.value} Breakables"
    BIG_SURF_ISLAND_BREAKABLES = f"{AreaType.BIG_SURF_ISLAND.value} Breakables"

    PALM_BAY_HEIGHTS_SMASHES = f"{AreaType.PALM_BAY_HEIGHTS.value} Smashes"
    SILVER_LAKE_SMASHES = f"{AreaType.SILVER_LAKE.value} Smashes"
    WHITE_MOUNTAIN_SMASHES = f"{AreaType.WHITE_MOUNTAIN.value} Smashes"
    HARBOR_TOWN_SMASHES = f"{AreaType.HARBOR_TOWN.value} Smashes"
    DOWNTOWN_PARADISE_SMASHES = f"{AreaType.DOWNTOWN_PARADISE.value} Smashes"
    BIG_SURF_ISLAND_SMASHES = f"{AreaType.BIG_SURF_ISLAND.value} Smashes"

    PALM_BAY_HEIGHTS_BILLBOARDS = f"{AreaType.PALM_BAY_HEIGHTS.value} Billboards"
    SILVER_LAKE_BILLBOARDS = f"{AreaType.SILVER_LAKE.value} Billboards"
    WHITE_MOUNTAIN_BILLBOARDS = f"{AreaType.WHITE_MOUNTAIN.value} Billboards"
    HARBOR_TOWN_BILLBOARDS = f"{AreaType.HARBOR_TOWN.value} Billboards"
    DOWNTOWN_PARADISE_BILLBOARDS = f"{AreaType.DOWNTOWN_PARADISE.value} Billboards"
    BIG_SURF_ISLAND_BILLBOARDS = f"{AreaType.BIG_SURF_ISLAND.value} Billboards"

    PALM_BAY_HEIGHTS_SUPER_JUMPS = f"{AreaType.PALM_BAY_HEIGHTS.value} Super Jumps"
    SILVER_LAKE_SUPER_JUMPS = f"{AreaType.SILVER_LAKE.value} Super Jumps"
    WHITE_MOUNTAIN_SUPER_JUMPS = f"{AreaType.WHITE_MOUNTAIN.value} Super Jumps"
    HARBOR_TOWN_SUPER_JUMPS = f"{AreaType.HARBOR_TOWN.value} Super Jumps"
    DOWNTOWN_PARADISE_SUPER_JUMPS = f"{AreaType.DOWNTOWN_PARADISE.value} Super Jumps"
    BIG_SURF_ISLAND_MEGA_JUMPS = f"{AreaType.BIG_SURF_ISLAND.value} Mega Jumps"

areas = [
    Regions.PALM_BAY_HEIGHTS,
    Regions.SILVER_LAKE,
    Regions.WHITE_MOUNTAIN,
    Regions.HARBOR_TOWN,
    Regions.DOWNTOWN_PARADISE,
    Regions.BIG_SURF_ISLAND,
]

breakable_regions = [
    Regions.PALM_BAY_HEIGHTS_BREAKABLES,
    Regions.SILVER_LAKE_BREAKABLES,
    Regions.WHITE_MOUNTAIN_BREAKABLES,
    Regions.HARBOR_TOWN_BREAKABLES,
    Regions.DOWNTOWN_PARADISE_BREAKABLES,
    Regions.BIG_SURF_ISLAND_BREAKABLES,
]
smash_regions = [
    Regions.PALM_BAY_HEIGHTS_SMASHES,
    Regions.SILVER_LAKE_SMASHES,
    Regions.WHITE_MOUNTAIN_SMASHES,
    Regions.HARBOR_TOWN_SMASHES,
    Regions.DOWNTOWN_PARADISE_SMASHES,
    Regions.BIG_SURF_ISLAND_SMASHES,
]
billboard_regions = [
    Regions.PALM_BAY_HEIGHTS_BILLBOARDS,
    Regions.SILVER_LAKE_BILLBOARDS,
    Regions.WHITE_MOUNTAIN_BILLBOARDS,
    Regions.HARBOR_TOWN_BILLBOARDS,
    Regions.DOWNTOWN_PARADISE_BILLBOARDS,
    Regions.BIG_SURF_ISLAND_BILLBOARDS,
]
jump_regions = [
    Regions.PALM_BAY_HEIGHTS_SUPER_JUMPS,
    Regions.SILVER_LAKE_SUPER_JUMPS,
    Regions.WHITE_MOUNTAIN_SUPER_JUMPS,
    Regions.HARBOR_TOWN_SUPER_JUMPS,
    Regions.DOWNTOWN_PARADISE_SUPER_JUMPS,
    Regions.BIG_SURF_ISLAND_MEGA_JUMPS,
]

