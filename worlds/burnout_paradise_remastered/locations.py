from worlds.burnout_paradise_remastered.data.items.cars import BigSurfIslandCars
from itertools import chain
from rule_builder.rules import HasGroup, True_
from collections import defaultdict, Counter
from typing import TYPE_CHECKING

from BaseClasses import Location, Region, EntranceType
from .options import BreakableLocks, UniqueCarWins, UniqueEventWins
from .data import RegionTypeEnum, GeneratedLocationData, BoostType
from .data.locations import LicenseLocations
from .data.locations.events import RaceLocations, StuntRunLocations, RoadRageLocations, MarkedManLocations, BurningRouteLocations, BikeEventLocations, BigSurfIslandLocations
from .data.locations.cars import CarLocations, CarWinLocations, BurningCarWinLocations, CarbonCarWinLocations, ToyCarWinLocations, LegendaryCarWinLocations, CopCarWinLocations, BigSurfIslandCarWinLocations, OnlineCarWinLocations, ParadiseBikesWinLocations, BoostSpecialCarWinLocations, BURNING_ROUTE_UNLOCK_TO_BURNING_CAR
from .data.locations.breakables import get_locations_for_breakable_option, get_car_wins_locations_by_boost, get_event_wins_locations_by_type
from .data.regions.entrances import base_entrances, smash_entrances, billboard_entrances, jump_entrances, breakable_entrances, drivethru_entrances, roadrules_time_entrances, roadrules_showtime_entrances, roadrules_bikes_day_entrances, roadrules_bikes_night_entrances
from .data.regions.regions import Regions, smash_regions, billboard_regions, jump_regions, areas, breakable_regions, drivethru_regions, roadrules_time_regions, roadrules_bikes_day_regions, roadrules_bikes_night_regions, roadrules_showtime_regions
from .constants import BreakableType, AreaType, LOCATIONS_OFFSET_SPEED_CAR_WINS, LOCATIONS_OFFSET_CRASH_CAR_WINS, LOCATIONS_OFFSET_STUNT_CAR_WINS, LOCATIONS_OFFSET_SPECIAL_CAR_WINS, WinType, LOCATIONS_OFFSET_BURNING_ROUTE_WINS, LOCATIONS_OFFSET_RACE_WINS, LOCATIONS_OFFSET_STUNT_RUN_WINS, LOCATIONS_OFFSET_ROAD_RAGE_WINS, LOCATIONS_OFFSET_MARKED_MAN_WINS, LOCATIONS_OFFSET_BURNING_RIDE_WINS, LOCATIONS_OFFSET_MIDNIGHT_RIDE_WINS, LOCATIONS_OFFSET_BIKE_WINS, LOCATIONS_OFFSET_BIG_SURF_ISLAND_WINS

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
            car_suffixes = tuple(car.value for car in world.added_cars)

            for _location in chain(
                CarWinLocations,
                BurningCarWinLocations,
                CarbonCarWinLocations,
                ToyCarWinLocations,
                LegendaryCarWinLocations,
                BoostSpecialCarWinLocations,
                CopCarWinLocations,
                BigSurfIslandCarWinLocations,
                OnlineCarWinLocations,
                ParadiseBikesWinLocations,
            ):
                if not _location.value.endswith(car_suffixes):
                    continue
                event_rule = True_()
                if _location in chain(ParadiseBikesWinLocations, [ToyCarWinLocations.NAKAMURA_TOY_FIREHAWK_GP]):
                    event_rule &= HasGroup("Bike Event")
                else:
                    event_rule &= HasGroup("Car Event")

                locations_by_region[_location.region].append(GeneratedLocationData(
                    name=_location.value,
                    region=_location.region,
                    rule=_location.rule & event_rule,
                    location_id=_location.location_id
                ))
        case UniqueCarWins.option_grouped_by_boost_type:
            boost_counter = Counter()
            for car in world.added_cars:
                boost_counter[car.boosttype] += 1

            speed_count   = boost_counter.get(BoostType.SPEED, 0)
            crash_count   = boost_counter.get(BoostType.CRASH, 0)
            stunt_count   = boost_counter.get(BoostType.STUNT, 0)
            special_count = boost_counter.get(BoostType.SPECIAL, 0)
            bike_count = boost_counter.get(BoostType.BIKE, 0)
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
            if any(("Burning Ride" in event.value) or ("Midnight Ride" in event.value) for event in world.event_items):
                locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                    get_car_wins_locations_by_boost(
                        BoostType.BIKE, bike_count, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_BIKE_WINS
                    )
                )

    for _location in CarLocations:
        if (
            (
                _location.min_events > 0
                and world.options.finished_events_stay_finished.value
                and world.total_amount_car_events >= _location.amount_events
            )
            or (
                _location.min_events > 0
                and not world.options.finished_events_stay_finished.value
                and world.total_amount_car_events >= _location.min_events
            )
            or (
                _location in BURNING_ROUTE_UNLOCK_TO_BURNING_CAR
                and BURNING_ROUTE_UNLOCK_TO_BURNING_CAR[_location] in chain(world.event_items, world.added_cars)
            )
        ):
            locations_by_region[_location.region].append(GeneratedLocationData(
                name=_location.value,
                region=_location.region,
                rule=_location.rule,
                location_id=_location.location_id
            ))

    match world.options.unique_event_wins:
        case UniqueEventWins.option_each_event_its_own:
            event_suffixes = tuple(item.value for item in world.event_items)

            for _location in chain(RaceLocations, StuntRunLocations, RoadRageLocations, MarkedManLocations, BurningRouteLocations, BikeEventLocations, BigSurfIslandLocations):
                if _location.value.endswith(event_suffixes):
                    locations_by_region[_location.region].append(GeneratedLocationData(
                        name=_location.value,
                        region=_location.region,
                        rule=_location.rule,
                        location_id=_location.location_id
                    ))
        case UniqueEventWins.option_grouped_by_event_type:
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_event_wins_locations_by_type(
                    WinType.BURNING_ROUTE_WINS, world.options.amount_events.value["Burning Route Event"], Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_BURNING_ROUTE_WINS
                )
            )
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_event_wins_locations_by_type(
                    WinType.RACE_WINS, world.options.amount_events.value["Race Event"],Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_RACE_WINS
                )
            )
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_event_wins_locations_by_type(
                    WinType.STUNT_RUN_WINS, world.options.amount_events.value["Stunt Run Event"], Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_STUNT_RUN_WINS
                )
            )
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_event_wins_locations_by_type(
                    WinType.ROAD_RAGE_WINS, world.options.amount_events.value["Road Rage Event"], Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_ROAD_RAGE_WINS
                )
            )
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_event_wins_locations_by_type(
                    WinType.MARKED_MAN_WINS, world.options.amount_events.value["Marked Man Event"], Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_MARKED_MAN_WINS
                )
            )
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_event_wins_locations_by_type(
                    WinType.BIG_SURF_ISLAND_WINS, world.options.amount_events.value["Big Surf Island Event"], Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_BIG_SURF_ISLAND_WINS
                )
            )
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_event_wins_locations_by_type(
                    WinType.BURNING_RIDE_WINS, world.options.amount_events.value["Burning Ride Event"], Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_BURNING_RIDE_WINS
                )
            )
            locations_by_region[Regions.DOWNTOWN_PARADISE].extend(
                get_event_wins_locations_by_type(
                    WinType.MIDNIGHT_RIDE_WINS, world.options.amount_events.value["Midnight Ride Event"], Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_MIDNIGHT_RIDE_WINS
                )
            )

    for _location in LicenseLocations:
        if (
            world.options.finished_events_stay_finished.value and world.total_amount_car_events >= _location.amount_events
        ) or (
            not world.options.finished_events_stay_finished.value and world.total_amount_car_events >= _location.min_events
        ):
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

        if any(car.boosttype == BoostType.BIKE for car in world.added_cars):
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
        if any(car.boosttype == BoostType.BIKE for car in world.added_cars):
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
