from worlds.burnout_paradise_remastered.data.items.cars import BoostSpecialCars, BurningCars, ParadiseBikes, OnlineCars, BigSurfIslandCars, CopCars, LegendaryCars, ToyCars, Cars, CarbonCars
from collections import defaultdict, Counter
from typing import TYPE_CHECKING

from BaseClasses import Location, Region, EntranceType
from .options import BreakableLocks, UniqueCarWins
from .data import RegionTypeEnum, GeneratedLocationData, BoostType
from .data.locations import EventLocations, LicenseLocations
from .data.locations.cars import CarLocations, CarWinLocations, BurningCarWinLocations, CarbonCarWinLocations, ToyCarWinLocations, LegendaryCarWinLocations, CopCarWinLocations, BigSurfIslandCarWinLocations, OnlineCarWinLocations, ParadiseBikesWinLocations, BoostSpecialCarWinLocations
from .data.locations.breakables import get_locations_for_breakable_option, get_car_wins_locations_by_boost
from .data.regions.entrances import base_entrances, smash_entrances, billboard_entrances, jump_entrances, breakable_entrances, drivethru_entrances, roadrules_time_entrances, roadrules_showtime_entrances, roadrules_bikes_day_entrances, roadrules_bikes_night_entrances
from .data.regions.regions import Regions, smash_regions, billboard_regions, jump_regions, areas, breakable_regions, drivethru_regions, roadrules_time_regions, roadrules_bikes_day_regions, roadrules_bikes_night_regions, roadrules_showtime_regions
from .constants import BreakableType, AreaType, LOCATIONS_OFFSET_SPEED_CAR_WINS, LOCATIONS_OFFSET_CRASH_CAR_WINS, LOCATIONS_OFFSET_STUNT_CAR_WINS, LOCATIONS_OFFSET_SPECIAL_CAR_WINS

if TYPE_CHECKING:
    from . import BurnoutParadiseRemasteredWorld


class DefaultRegions(RegionTypeEnum):
    MENU = "Menu"


def create_location(world, data: GeneratedLocationData):
    region = world.get_region(data.region.value)
    location = Location(world.player, data.name, data.location_id, region)
    location.progress_type = data.progress_type
    # location.item_rule = data.item_rule
    region.locations.append(location)
    world.set_rule(location, data.rule)

def create_region(world: "BurnoutParadiseRemasteredWorld", region_type: RegionTypeEnum, locations_by_region: dict[RegionTypeEnum, list[GeneratedLocationData]] | None = None):
    region = Region(region_type.value, world.player, world.multiworld)
    world.multiworld.regions.append(region)

    if locations_by_region is None:
        return region

    for data in locations_by_region[region_type]:
        location = Location(world.player, data.name, data.location_id, region)
        location.progress_type = data.progress_type
        # location.item_rule = data.item_rule
        region.locations.append(location)
        world.set_rule(location, data.rule)

    return region

def create_regions(world: "BurnoutParadiseRemasteredWorld"):
    menu = create_region(world, DefaultRegions.MENU)
    locations_by_region: dict[RegionTypeEnum, list[GeneratedLocationData]] = defaultdict(list)

    match world.options.unique_car_wins:
        case UniqueCarWins.option_each_car_its_own:
            for _location in CarWinLocations:
                locations_by_region[_location.region].append(GeneratedLocationData(
                    name=_location.value,
                    region=_location.region,
                    rule=_location.rule,
                    location_id=_location.location_id
                ))
            for _location in BurningCarWinLocations:
                locations_by_region[_location.region].append(GeneratedLocationData(
                    name=_location.value,
                    region=_location.region,
                    rule=_location.rule,
                    location_id=_location.location_id
                ))
            for _location in CarbonCarWinLocations:
                locations_by_region[_location.region].append(GeneratedLocationData(
                    name=_location.value,
                    region=_location.region,
                    rule=_location.rule,
                    location_id=_location.location_id
                ))

            if world.options.add_toy_cars.value:
                for _location in ToyCarWinLocations:
                    locations_by_region[_location.region].append(GeneratedLocationData(
                        name=_location.value,
                        region=_location.region,
                        rule=_location.rule,
                        location_id=_location.location_id
                    ))

            if world.options.add_legendary_cars.value:
                for _location in LegendaryCarWinLocations:
                    locations_by_region[_location.region].append(GeneratedLocationData(
                        name=_location.value,
                        region=_location.region,
                        rule=_location.rule,
                        location_id=_location.location_id
                    ))

            if world.options.add_boost_special_cars.value:
                for _location in BoostSpecialCarWinLocations:
                    locations_by_region[_location.region].append(GeneratedLocationData(
                        name=_location.value,
                        region=_location.region,
                        rule=_location.rule,
                        location_id=_location.location_id
                    ))

            if world.options.add_pcpd_cars.value:
                for _location in CopCarWinLocations:
                    locations_by_region[_location.region].append(GeneratedLocationData(
                        name=_location.value,
                        region=_location.region,
                        rule=_location.rule,
                        location_id=_location.location_id
                    ))

            if world.options.add_big_surf_island_cars.value:
                for _location in BigSurfIslandCarWinLocations:
                    locations_by_region[_location.region].append(GeneratedLocationData(
                        name=_location.value,
                        region=_location.region,
                        rule=_location.rule,
                        location_id=_location.location_id
                    ))

            if world.options.add_online_cars.value:
                for _location in OnlineCarWinLocations:
                    locations_by_region[_location.region].append(GeneratedLocationData(
                        name=_location.value,
                        region=_location.region,
                        rule=_location.rule,
                        location_id=_location.location_id
                    ))

            if world.options.add_paradise_bikes.value:
                for _location in ParadiseBikesWinLocations:
                    locations_by_region[_location.region].append(GeneratedLocationData(
                        name=_location.value,
                        region=_location.region,
                        rule=_location.rule,
                        location_id=_location.location_id
                    ))
        case UniqueCarWins.option_grouped_by_boost_type:
            boost_counter = Counter()

            def add_items(enum_iterable):
                for it in enum_iterable:
                    boost_counter[it.boosttype] += 1

            add_items(Cars)
            add_items(BurningCars)
            add_items(CarbonCars)

            if world.options.add_toy_cars.value:
                add_items(ToyCars)
            if world.options.add_legendary_cars.value:
                add_items(LegendaryCars)
            if world.options.add_boost_special_cars.value:
                add_items(BoostSpecialCars)
            if world.options.add_pcpd_cars.value:
                add_items(CopCars)
            if world.options.add_big_surf_island_cars.value:
                add_items(BigSurfIslandCars)
            if world.options.add_online_cars.value:
                add_items(OnlineCars)
            if world.options.add_paradise_bikes.value:
                add_items(ParadiseBikes)

            speed_count   = boost_counter[BoostType.SPEED]
            crash_count   = boost_counter[BoostType.CRASH]
            stunt_count   = boost_counter[BoostType.STUNT]
            special_count = boost_counter.get(BoostType.SPECIAL, 0)
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_car_wins_locations_by_boost(
                    BoostType.SPEED, speed_count, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_SPEED_CAR_WINS
                )
            )
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_car_wins_locations_by_boost(
                    BoostType.CRASH, crash_count, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_CRASH_CAR_WINS
                )
            )
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_car_wins_locations_by_boost(
                    BoostType.STUNT, stunt_count, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_STUNT_CAR_WINS
                )
            )
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_car_wins_locations_by_boost(
                    BoostType.SPECIAL, special_count, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_SPECIAL_CAR_WINS
                )
            )

    for _location in CarLocations:
        locations_by_region[_location.region].append(GeneratedLocationData(
            name=_location.value,
            region=_location.region,
            rule=_location.rule,
            location_id=_location.location_id
        ))

    for _location in EventLocations:
        locations_by_region[_location.region].append(GeneratedLocationData(
             name=_location.value,
             region=_location.region,
             rule=_location.rule,
             location_id=_location.location_id
         ))

    for _location in LicenseLocations:
        locations_by_region[_location.region].append(GeneratedLocationData(
             name=_location.value,
             region=_location.region,
             rule=_location.rule,
             location_id=_location.location_id
         ))

    for area_name, value in world.options.smash_counts.value.items():
        generated_locs = get_locations_for_breakable_option(BreakableType.SMASH, AreaType(area_name), value, world.options.breakable_locks.value)
        for _location in generated_locs:
            locations_by_region[_location.region].append(_location)

    for area_name, value in world.options.billboard_counts.value.items():
        generated_locs = get_locations_for_breakable_option(BreakableType.BILLBOARD, AreaType(area_name), value, world.options.breakable_locks.value)
        for _location in generated_locs:
            locations_by_region[_location.region].append(_location)

    for area_name, value in world.options.super_jump_counts.value.items():
        generated_locs = get_locations_for_breakable_option(BreakableType.SUPER_JUMP, AreaType(area_name), value, world.options.breakable_locks.value)
        for _location in generated_locs:
            locations_by_region[_location.region].append(_location)

    for area_name, value in world.options.drive_thru_counts.value.items():
        generated_locs = get_locations_for_breakable_option(BreakableType.DRIVETHRU, AreaType(area_name), value, world.options.breakable_locks.value)
        for _location in generated_locs:
            locations_by_region[_location.region].append(_location)

    for area_name, value in world.options.road_rule_time_count.value.items():
        generated_locs = get_locations_for_breakable_option(BreakableType.ROADRULE_TIME, AreaType(area_name), value, world.options.breakable_locks.value)
        for _location in generated_locs:
            locations_by_region[_location.region].append(_location)

    for area_name, value in world.options.road_rule_showtime_count.value.items():
        generated_locs = get_locations_for_breakable_option(BreakableType.ROADRULE_SHOWTIME, AreaType(area_name), value, world.options.breakable_locks.value)
        for _location in generated_locs:
            locations_by_region[_location.region].append(_location)

    if world.options.add_toy_cars.value or world.options.add_paradise_bikes.value:
        for area_name, value in world.options.road_rule_bike_day_count.value.items():
            generated_locs = get_locations_for_breakable_option(BreakableType.ROADRULE_BIKES_DAY, AreaType(area_name), value, world.options.breakable_locks.value)
            for _location in generated_locs:
                locations_by_region[_location.region].append(_location)

        for area_name, value in world.options.road_rule_bike_night_count.value.items():
            generated_locs = get_locations_for_breakable_option(BreakableType.ROADRULE_BIKES_NIGHT, AreaType(area_name), value, world.options.breakable_locks.value)
            for _location in generated_locs:
                locations_by_region[_location.region].append(_location)

    regions_to_create = list(areas)
    if world.options.breakable_locks.value == BreakableLocks.option_locked_by_area_and_type:
        regions_to_create += (
            list(smash_regions)
            + list(billboard_regions)
            + list(jump_regions)
            + list(drivethru_regions)
            + list(roadrules_time_regions)
            + list(roadrules_showtime_regions)
        )

        if world.options.add_toy_cars.value or world.options.add_paradise_bikes.value:
            regions_to_create += (
                list(roadrules_bikes_day_regions)
                + list(roadrules_bikes_night_regions)
            )
    else:
        regions_to_create += list(breakable_regions)

    for region in regions_to_create:
        create_region(world, region, locations_by_region)


def create_entrances(world: "BurnoutParadiseRemasteredWorld"):

    menu = world.get_region("Menu")
    world.create_entrance(menu, world.get_region(Regions.DOWNTOWN_PARADISE.value), name="Menu To Paradise")

    entrances_to_create = list(base_entrances)
    if world.options.breakable_locks.value == BreakableLocks.option_locked_by_area_and_type:
        entrances_to_create += (
            list(smash_entrances)
            + list(billboard_entrances)
            + list(jump_entrances)
            + list(drivethru_entrances)
            + list(roadrules_time_entrances)
            + list(roadrules_showtime_entrances)
        )
        if world.options.add_toy_cars.value or world.options.add_paradise_bikes.value:
            entrances_to_create += (
                list(roadrules_bikes_day_entrances)
                + list(roadrules_bikes_night_entrances)
            )
    else:
        entrances_to_create += list(breakable_entrances)

    for transition_data in entrances_to_create:
        exiting_region = world.get_region(transition_data.exiting_region.value)
        entering_region = world.get_region(transition_data.entering_region.value)

        entrance = world.create_entrance(exiting_region, entering_region, rule=transition_data.rule, name=transition_data.value, force_creation=True)
        if transition_data.two_way == EntranceType.TWO_WAY:
            entrance_other = world.create_entrance(entering_region,exiting_region, rule=transition_data.rule,
                                             name=transition_data.value + "_back", force_creation=True)
