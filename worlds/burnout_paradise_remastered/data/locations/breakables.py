from .. import GeneratedLocationData
from ..regions.regions import Regions
from ...constants import AreaType, BreakableType, LOCATIONS_OFFSET_BREAKABLES

breakable_count_lookup = {
    AreaType.DOWNTOWN_PARADISE.value : {
        BreakableType.SMASH : 80,
        BreakableType.BILLBOARD : 30,
        BreakableType.SUPER_JUMP : 10,

    },
    AreaType.HARBOR_TOWN.value: {
        BreakableType.SMASH: 90,
        BreakableType.BILLBOARD : 25,
        BreakableType.SUPER_JUMP : 10,

    },
    AreaType.WHITE_MOUNTAIN.value: {
        BreakableType.SMASH: 90,
        BreakableType.BILLBOARD : 25,
        BreakableType.SUPER_JUMP : 10,

    },
    AreaType.SILVER_LAKE.value: {
        BreakableType.SMASH: 90,
        BreakableType.BILLBOARD : 20,
        BreakableType.SUPER_JUMP : 10,

    },
    AreaType.PALM_BAY_HEIGHTS.value: {
        BreakableType.SMASH: 50,
        BreakableType.BILLBOARD : 20,
        BreakableType.SUPER_JUMP : 10,

    },
    AreaType.BIG_SURF_ISLAND.value: {
        BreakableType.SMASH: 75,
        BreakableType.BILLBOARD : 45,
        BreakableType.SUPER_JUMP : 15,

    }
}

name_lookup = {
    BreakableType.SMASH: "Smash",
    BreakableType.BILLBOARD: "Billboard",
    BreakableType.SUPER_JUMP: "Super Jump"
}

region_lookup = {
    AreaType.PALM_BAY_HEIGHTS: Regions.PALM_BAY_HEIGHTS_BREAKABLES,
    AreaType.SILVER_LAKE: Regions.SILVER_LAKE_BREAKABLES,
    AreaType.WHITE_MOUNTAIN: Regions.WHITE_MOUNTAIN_BREAKABLES,
    AreaType.HARBOR_TOWN: Regions.HARBOR_TOWN_BREAKABLES,
    AreaType.DOWNTOWN_PARADISE: Regions.DOWNTOWN_PARADISE_BREAKABLES,
    AreaType.BIG_SURF_ISLAND: Regions.BIG_SURF_ISLAND_BREAKABLES,
}

type_region_lookup = {
    AreaType.PALM_BAY_HEIGHTS: {
        BreakableType.SMASH:      Regions.PALM_BAY_HEIGHTS_SMASHES,
        BreakableType.BILLBOARD:  Regions.PALM_BAY_HEIGHTS_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.PALM_BAY_HEIGHTS_SUPER_JUMPS,
    },
    AreaType.SILVER_LAKE: {
        BreakableType.SMASH:      Regions.SILVER_LAKE_SMASHES,
        BreakableType.BILLBOARD:  Regions.SILVER_LAKE_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.SILVER_LAKE_SUPER_JUMPS,
    },
    AreaType.WHITE_MOUNTAIN: {
        BreakableType.SMASH:      Regions.WHITE_MOUNTAIN_SMASHES,
        BreakableType.BILLBOARD:  Regions.WHITE_MOUNTAIN_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.WHITE_MOUNTAIN_SUPER_JUMPS,
    },
    AreaType.HARBOR_TOWN: {
        BreakableType.SMASH:      Regions.HARBOR_TOWN_SMASHES,
        BreakableType.BILLBOARD:  Regions.HARBOR_TOWN_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.HARBOR_TOWN_SUPER_JUMPS,
    },
    AreaType.DOWNTOWN_PARADISE: {
        BreakableType.SMASH:      Regions.DOWNTOWN_PARADISE_SMASHES,
        BreakableType.BILLBOARD:  Regions.DOWNTOWN_PARADISE_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.DOWNTOWN_PARADISE_SUPER_JUMPS,
    },
    AreaType.BIG_SURF_ISLAND: {
        BreakableType.SMASH:      Regions.BIG_SURF_ISLAND_SMASHES,
        BreakableType.BILLBOARD:  Regions.BIG_SURF_ISLAND_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.BIG_SURF_ISLAND_MEGA_JUMPS,
    },
}

def get_locations_for_breakable_option(breakable: BreakableType, area: AreaType, count, lock_option = 0) -> list[GeneratedLocationData]:
    from ...options import BreakableLocks
    locs: list[GeneratedLocationData] = []
    count = count if count <= breakable_count_lookup[area.value][breakable] else breakable_count_lookup[area.value][breakable]
    for num in range(count):
        name = f"{area.value} {'Mega Jump' if area == AreaType.BIG_SURF_ISLAND and breakable == BreakableType.SUPER_JUMP else name_lookup[breakable]} {num+1}"
        region = type_region_lookup[area][breakable] if lock_option == BreakableLocks.option_locked_by_area_and_type else region_lookup[area]
        locs.append(GeneratedLocationData(
            name = name,
            location_id=LOCATIONS_OFFSET_BREAKABLES + (1000 * area.index) + (100 * breakable.value) + num,
            region=region))
    return locs


# Duplicate to not cause import chains based on importing options
def get_locations_for_breakable(breakable: BreakableType, area: AreaType, count) -> list[GeneratedLocationData]:
    locs: list[GeneratedLocationData] = []
    count = count if count <= breakable_count_lookup[area.value][breakable] else breakable_count_lookup[area.value][breakable]
    for num in range(count):
        name = f"{area.value} {'Mega Jump' if area == AreaType.BIG_SURF_ISLAND and breakable == BreakableType.SUPER_JUMP else name_lookup[breakable]} {num+1}"
        region = region_lookup[area]
        locs.append(GeneratedLocationData(
            name = name,
            location_id=LOCATIONS_OFFSET_BREAKABLES + (1000 * area.index) + (100 * breakable.value) + num,
            region=region))
    return locs
