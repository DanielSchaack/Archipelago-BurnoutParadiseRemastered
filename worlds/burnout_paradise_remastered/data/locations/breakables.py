from rule_builder.rules import True_, HasGroup
from .. import GeneratedLocationData, BoostType, RegionTypeEnum
from ..rules.state_rules import HasEventWins
from ..regions.regions import Regions
from ...constants import AreaType, BreakableType, LOCATIONS_OFFSET_BREAKABLES

breakable_count_lookup = {
    AreaType.DOWNTOWN_PARADISE.value : {
        BreakableType.SMASH: 80,
        BreakableType.BILLBOARD: 30,
        BreakableType.SUPER_JUMP: 10,
        BreakableType.DRIVETHRU: 12,
        BreakableType.ROADRULE_TIME: 13,
        BreakableType.ROADRULE_SHOWTIME: 13,
        BreakableType.ROADRULE_BIKES_DAY: 13,
        BreakableType.ROADRULE_BIKES_NIGHT: 13,
    },
    AreaType.HARBOR_TOWN.value: {
        BreakableType.SMASH: 90,
        BreakableType.BILLBOARD: 25,
        BreakableType.SUPER_JUMP: 10,
        BreakableType.DRIVETHRU: 10,
        BreakableType.ROADRULE_TIME: 14,
        BreakableType.ROADRULE_SHOWTIME: 14,
        BreakableType.ROADRULE_BIKES_DAY: 14,
        BreakableType.ROADRULE_BIKES_NIGHT: 14,
    },
    AreaType.WHITE_MOUNTAIN.value: {
        BreakableType.SMASH: 90,
        BreakableType.BILLBOARD: 25,
        BreakableType.SUPER_JUMP: 10,
        BreakableType.DRIVETHRU: 7,
        BreakableType.ROADRULE_TIME: 10,
        BreakableType.ROADRULE_SHOWTIME: 10,
        BreakableType.ROADRULE_BIKES_DAY: 10,
        BreakableType.ROADRULE_BIKES_NIGHT: 10,
    },
    AreaType.SILVER_LAKE.value: {
        BreakableType.SMASH: 90,
        BreakableType.BILLBOARD: 20,
        BreakableType.SUPER_JUMP: 10,
        BreakableType.DRIVETHRU: 7,
        BreakableType.ROADRULE_TIME: 9,
        BreakableType.ROADRULE_SHOWTIME: 9,
        BreakableType.ROADRULE_BIKES_DAY: 9,
        BreakableType.ROADRULE_BIKES_NIGHT: 9,
    },
    AreaType.PALM_BAY_HEIGHTS.value: {
        BreakableType.SMASH: 50,
        BreakableType.BILLBOARD: 20,
        BreakableType.SUPER_JUMP: 10,
        BreakableType.DRIVETHRU: 10,
        BreakableType.ROADRULE_TIME: 18,
        BreakableType.ROADRULE_SHOWTIME: 18,
        BreakableType.ROADRULE_BIKES_DAY: 18,
        BreakableType.ROADRULE_BIKES_NIGHT: 18,
    },
    AreaType.BIG_SURF_ISLAND.value: {
        BreakableType.SMASH: 75,
        BreakableType.BILLBOARD: 45,
        BreakableType.SUPER_JUMP: 15,
        BreakableType.DRIVETHRU: 5,
        BreakableType.ROADRULE_TIME: 12,
        BreakableType.ROADRULE_SHOWTIME: 12,
        BreakableType.ROADRULE_BIKES_DAY: 12,
        BreakableType.ROADRULE_BIKES_NIGHT: 12,
    }
}

name_lookup = {
    BreakableType.SMASH: "Smash",
    BreakableType.BILLBOARD: "Billboard",
    BreakableType.SUPER_JUMP: "Super Jump",
    BreakableType.DRIVETHRU: "Drive-Thru",
    BreakableType.ROADRULE_TIME: "Road Rules for Time",
    BreakableType.ROADRULE_SHOWTIME: "Road Rules for Showtime",
    BreakableType.ROADRULE_BIKES_DAY: "Road Rules for Bikes at Day",
    BreakableType.ROADRULE_BIKES_NIGHT: "Road Rules for Bikes at Night",
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
        BreakableType.DRIVETHRU:  Regions.PALM_BAY_HEIGHTS_DRIVETHRUS,
        BreakableType.ROADRULE_TIME:      Regions.PALM_BAY_HEIGHTS_ROADRULE_TIME,
        BreakableType.ROADRULE_SHOWTIME:  Regions.PALM_BAY_HEIGHTS_ROADRULE_SHOWTIME,
        BreakableType.ROADRULE_BIKES_DAY: Regions.PALM_BAY_HEIGHTS_ROADRULE_BIKES_DAY,
        BreakableType.ROADRULE_BIKES_NIGHT: Regions.PALM_BAY_HEIGHTS_ROADRULE_BIKES_NIGHT,
    },
    AreaType.SILVER_LAKE: {
        BreakableType.SMASH:      Regions.SILVER_LAKE_SMASHES,
        BreakableType.BILLBOARD:  Regions.SILVER_LAKE_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.SILVER_LAKE_SUPER_JUMPS,
        BreakableType.DRIVETHRU:  Regions.SILVER_LAKE_DRIVETHRUS,
        BreakableType.ROADRULE_TIME:      Regions.SILVER_LAKE_ROADRULE_TIME,
        BreakableType.ROADRULE_SHOWTIME:  Regions.SILVER_LAKE_ROADRULE_SHOWTIME,
        BreakableType.ROADRULE_BIKES_DAY: Regions.SILVER_LAKE_ROADRULE_BIKES_DAY,
        BreakableType.ROADRULE_BIKES_NIGHT: Regions.SILVER_LAKE_ROADRULE_BIKES_NIGHT,
    },
    AreaType.WHITE_MOUNTAIN: {
        BreakableType.SMASH:      Regions.WHITE_MOUNTAIN_SMASHES,
        BreakableType.BILLBOARD:  Regions.WHITE_MOUNTAIN_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.WHITE_MOUNTAIN_SUPER_JUMPS,
        BreakableType.DRIVETHRU:  Regions.WHITE_MOUNTAIN_DRIVETHRUS,
        BreakableType.ROADRULE_TIME:      Regions.WHITE_MOUNTAIN_ROADRULE_TIME,
        BreakableType.ROADRULE_SHOWTIME:  Regions.WHITE_MOUNTAIN_ROADRULE_SHOWTIME,
        BreakableType.ROADRULE_BIKES_DAY: Regions.WHITE_MOUNTAIN_ROADRULE_BIKES_DAY,
        BreakableType.ROADRULE_BIKES_NIGHT: Regions.WHITE_MOUNTAIN_ROADRULE_BIKES_NIGHT,
    },
    AreaType.HARBOR_TOWN: {
        BreakableType.SMASH:      Regions.HARBOR_TOWN_SMASHES,
        BreakableType.BILLBOARD:  Regions.HARBOR_TOWN_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.HARBOR_TOWN_SUPER_JUMPS,
        BreakableType.DRIVETHRU:  Regions.HARBOR_TOWN_DRIVETHRUS,
        BreakableType.ROADRULE_TIME:      Regions.HARBOR_TOWN_ROADRULE_TIME,
        BreakableType.ROADRULE_SHOWTIME:  Regions.HARBOR_TOWN_ROADRULE_SHOWTIME,
        BreakableType.ROADRULE_BIKES_DAY: Regions.HARBOR_TOWN_ROADRULE_BIKES_DAY,
        BreakableType.ROADRULE_BIKES_NIGHT: Regions.HARBOR_TOWN_ROADRULE_BIKES_NIGHT,
    },
    AreaType.DOWNTOWN_PARADISE: {
        BreakableType.SMASH:      Regions.DOWNTOWN_PARADISE_SMASHES,
        BreakableType.BILLBOARD:  Regions.DOWNTOWN_PARADISE_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.DOWNTOWN_PARADISE_SUPER_JUMPS,
        BreakableType.DRIVETHRU:  Regions.DOWNTOWN_PARADISE_DRIVETHRUS,
        BreakableType.ROADRULE_TIME:      Regions.DOWNTOWN_PARADISE_ROADRULE_TIME,
        BreakableType.ROADRULE_SHOWTIME:  Regions.DOWNTOWN_PARADISE_ROADRULE_SHOWTIME,
        BreakableType.ROADRULE_BIKES_DAY: Regions.DOWNTOWN_PARADISE_ROADRULE_BIKES_DAY,
        BreakableType.ROADRULE_BIKES_NIGHT: Regions.DOWNTOWN_PARADISE_ROADRULE_BIKES_NIGHT,
    },
    AreaType.BIG_SURF_ISLAND: {
        BreakableType.SMASH:      Regions.BIG_SURF_ISLAND_SMASHES,
        BreakableType.BILLBOARD:  Regions.BIG_SURF_ISLAND_BILLBOARDS,
        BreakableType.SUPER_JUMP: Regions.BIG_SURF_ISLAND_MEGA_JUMPS,
        BreakableType.DRIVETHRU:  Regions.BIG_SURF_ISLAND_DRIVETHRUS,
        BreakableType.ROADRULE_TIME:      Regions.BIG_SURF_ISLAND_ROADRULE_TIME,
        BreakableType.ROADRULE_SHOWTIME:  Regions.BIG_SURF_ISLAND_ROADRULE_SHOWTIME,
        BreakableType.ROADRULE_BIKES_DAY: Regions.BIG_SURF_ISLAND_ROADRULE_BIKES_DAY,
        BreakableType.ROADRULE_BIKES_NIGHT: Regions.BIG_SURF_ISLAND_ROADRULE_BIKES_NIGHT,
    },
}


def get_locations_for_breakable_option(breakable: BreakableType, area: AreaType, count, lock_option = 0) -> list[GeneratedLocationData]:
    from ...options import BreakableLocks
    locs: list[GeneratedLocationData] = []
    count = count if count <= breakable_count_lookup[area.value][breakable] else breakable_count_lookup[area.value][breakable]
    region = type_region_lookup[area][breakable] if lock_option == BreakableLocks.option_locked_by_area_and_type else region_lookup[area]
    rule = True_()
    if lock_option == BreakableLocks.option_locked_by_area and breakable in [BreakableType.ROADRULE_TIME, BreakableType.ROADRULE_SHOWTIME]:
        rule = HasEventWins(wins=4)
    elif lock_option == BreakableLocks.option_locked_by_area and breakable in [BreakableType.ROADRULE_BIKES_DAY, BreakableType.ROADRULE_BIKES_NIGHT]:
        rule = HasGroup("Bike")
    for num in range(count):
        name = f"{area.value} - {'Mega Jump' if area == AreaType.BIG_SURF_ISLAND and breakable == BreakableType.SUPER_JUMP else name_lookup[breakable]} {num+1}"
        locs.append(GeneratedLocationData(
            name = name,
            location_id=LOCATIONS_OFFSET_BREAKABLES + (1000 * area.index) + (100 * breakable.value) + num,
            rule=rule,
            region=region))
    return locs

# Duplicate to not cause import chains based on importing options
def get_locations_for_breakable(breakable: BreakableType, area: AreaType, count) -> list[GeneratedLocationData]:
    locs: list[GeneratedLocationData] = []
    count = count if count <= breakable_count_lookup[area.value][breakable] else breakable_count_lookup[area.value][breakable]
    for num in range(count):
        name = f"{area.value} - {'Mega Jump' if area == AreaType.BIG_SURF_ISLAND and breakable == BreakableType.SUPER_JUMP else name_lookup[breakable]} {num+1}"
        region = region_lookup[area]
        locs.append(GeneratedLocationData(
            name = name,
            location_id=LOCATIONS_OFFSET_BREAKABLES + (1000 * area.index) + (100 * breakable.value) + num,
            region=region))
    return locs

def get_car_wins_locations_by_boost(
    boost_type: BoostType,
    count: int,
    region: RegionTypeEnum,
    base_id: int,
) -> list[GeneratedLocationData]:
    return [
        GeneratedLocationData(
            name=f"Unique {boost_type.value.capitalize()}-Car Wins - Win {i}",
            region=region,
            rule=HasGroup(f"{boost_type.value.capitalize()} Car", count=i),
            location_id=base_id + i - 1,
        )
        for i in range(1, count + 1)
    ]

