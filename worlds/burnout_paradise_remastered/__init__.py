import logging
from itertools import chain
import json
import os
from importlib.resources import files
from typing import ClassVar, Any, Mapping

from BaseClasses import Tutorial, Item
from Utils import visualize_regions
from worlds.AutoWorld import WebWorld
from rule_builder.rules import HasGroupUnique
from . import locations, items
from .constants import BURNOUT_PARADISE_REMASTERED, BURNOUT_WINS, BURNOUT_ELITE_WINS, A_CLASS_WINS, B_CLASS_WINS, C_CLASS_WINS, AreaType, BreakableType, WinType, wintype_to_item_group, event_type_to_wintype, BURNOUT_ELITE_EVENTS, BURNOUT_EVENTS, A_CLASS_EVENTS, B_CLASS_EVENTS, D_CLASS_WINS, C_CLASS_EVENTS
from .data import BoostType, ItemTypeEnum, CarItemTypeEnum
from .data.items import all_items, Blockers, Discoverables, RaceEvents, StuntRunEvents, RoadRageEvents, MarkedManEvents
from .data.items.events import BurningRideEvents, MidnightRideEvents, BigSurfIslandEvents
from .data.items.cars import BurningRouteRewardCars, BurningCars, CarbonCars, ToyCars, LegendaryCars, BoostSpecialCars, CopCars, BigSurfIslandCars, ParadiseBikes, OnlineCars, _BURNING_CARS_IN_ORDER
from .data.items.liveries import ParadiseCarsLivery
from .data.locations import all_generated_locations, all_enum_locations, breakable_count_lookup, MarkedManLocations, BurningRouteLocations, RaceLocations, StuntRunLocations, RoadRageLocations, BigSurfIslandLocations
from .data.rules.state_rules import HasEventWins
from .options import burnout_paradise_remastered_option_groups, LicenseGoal, amount_events_default, mode_base_difficulty_default
from .world_base import BurnoutParadiseRemasteredBase
from .items import BurnoutParadiseRemasteredItem


NON_PARADISE_CITY_EVENT_NAMES = ("Big Surf Island Event", "Burning Ride Event", "Midnight Ride Event")
BIKE_EVENT_NAMES = ("Burning Ride Event", "Midnight Ride Event")

class BurnoutParadiseRemasteredWeb(WebWorld):
    theme = "partyTime"
    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Burnout Paradise Remastered Randomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["FyreDay", "Schaackii"],
    )
    option_groups = burnout_paradise_remastered_option_groups
    tutorials = [setup_en]


def load_manifest():
    return json.loads(
        files(__package__).joinpath("archipelago.json").read_text("utf-8")
    )


class BurnoutParadiseRemasteredWorld(BurnoutParadiseRemasteredBase):

    manifest = load_manifest()

    game = BURNOUT_PARADISE_REMASTERED
    web = BurnoutParadiseRemasteredWeb()

    item_name_to_id: ClassVar[dict[str, int]] = {
        item.value: item.item_id for item in all_items
    }
    location_name_to_id: ClassVar[dict[str, int]] = {
        **{
            loc.value: loc.location_id
            for loc in all_enum_locations
        },
        **{
            gen_loc.name: gen_loc.location_id
            for gen_loc in all_generated_locations
        },
    }

    item_name_groups: ClassVar[dict[str, set[str]]] = {
        "Car": {car.value for car in chain(BurningRouteRewardCars, BurningCars, CarbonCars, ToyCars, LegendaryCars, BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars)},
        "Bike": {bike.value for bike in chain(ParadiseBikes, [ToyCars.NAKAMURA_TOY_FIREHAWK_GP]) },
        "Paradise Car": {car.value for car in chain(BurningRouteRewardCars, BurningCars, CarbonCars)},
        "Toy Car": {car.value for car in ToyCars},
        "Legendary Car": {car.value for car in LegendaryCars},
        "Boost Special Car": {car.value for car in BoostSpecialCars},
        "Cop Car": {car.value for car in CopCars},
        "Big Surf Island Car": {car.value for car in BigSurfIslandCars},
        "Online Car": {car.value for car in OnlineCars},
        "Speed Car": {
            car.value for car in chain(
                BurningRouteRewardCars, BurningCars, CarbonCars, ToyCars, LegendaryCars,
                BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars
            ) if car.boosttype == BoostType.SPEED
        },
        "Crash Car": {
            car.value for car in chain(
                BurningRouteRewardCars, BurningCars, CarbonCars, ToyCars, LegendaryCars,
                BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars
            ) if car.boosttype == BoostType.CRASH
        },
        "Stunt Car": {
            car.value for car in chain(
                BurningRouteRewardCars, BurningCars, CarbonCars, ToyCars, LegendaryCars,
                BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars
            ) if car.boosttype == BoostType.STUNT
        },
        "Special Car": {
            car.value for car in chain(
                BurningRouteRewardCars, BurningCars, CarbonCars, ToyCars, LegendaryCars,
                BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars, ParadiseBikes
            ) if car.boosttype == BoostType.SPECIAL
        },
        "Livery": {livery.value for livery in ParadiseCarsLivery},
        "Car Event": {event.value for event in chain(RaceEvents, StuntRunEvents, RoadRageEvents, MarkedManEvents)},
        "Bike Event": {event.value for event in chain(BurningRideEvents, MidnightRideEvents)},
        "Big Surf Island Event": {event.value for event in chain(BigSurfIslandEvents, [BigSurfIslandCars.CARSON_DUST_STORM])},
        "Burning Ride Event": {event.value for event in BurningRideEvents},
        "Midnight Ride Event": {event.value for event in MidnightRideEvents},
        "Burning Route Event": {car.value for car in BurningCars},
        "Burning Car": {car.value for car in BurningCars},
        "Race Event": { event.value for event in RaceEvents },
        "Stunt Run Event": { event.value for event in StuntRunEvents },
        "Road Rage Event": { event.value for event in RoadRageEvents },
        "Marked Man Event": { event.value for event in MarkedManEvents },
        f"{AreaType.PALM_BAY_HEIGHTS.value} Event": { loc.value.split(" - ", 1)[1] for loc in chain(BurningRouteLocations, RaceLocations, StuntRunLocations, RoadRageLocations, MarkedManLocations) if loc.region.value == AreaType.PALM_BAY_HEIGHTS.value },
        f"{AreaType.HARBOR_TOWN.value} Event": { loc.value.split(" - ", 1)[1] for loc in chain(BurningRouteLocations, RaceLocations, StuntRunLocations, RoadRageLocations, MarkedManLocations) if loc.region.value == AreaType.HARBOR_TOWN.value },
        f"{AreaType.SILVER_LAKE.value} Event": { loc.value.split(" - ", 1)[1] for loc in chain(BurningRouteLocations, RaceLocations, StuntRunLocations, RoadRageLocations, MarkedManLocations) if loc.region.value == AreaType.SILVER_LAKE.value },
        f"{AreaType.WHITE_MOUNTAIN.value} Event": { loc.value.split(" - ", 1)[1] for loc in chain(BurningRouteLocations, RaceLocations, StuntRunLocations, RoadRageLocations, MarkedManLocations) if loc.region.value == AreaType.WHITE_MOUNTAIN.value },
        f"{AreaType.DOWNTOWN_PARADISE.value} Event": { loc.value.split(" - ", 1)[1] for loc in chain(BurningRouteLocations, RaceLocations, StuntRunLocations, RoadRageLocations, MarkedManLocations) if loc.region.value == AreaType.DOWNTOWN_PARADISE.value },
        f"{AreaType.BIG_SURF_ISLAND.value} Event": { loc.value.split(" - ", 1)[1] for loc in BigSurfIslandLocations},
        "Any Event": {e.value for e in chain(RaceEvents, StuntRunEvents, RoadRageEvents, MarkedManEvents, BurningCars)},
        "Area Breakable": {area.value for area in Blockers},
        "Area Discoverable": {discoverable.value for discoverable in Discoverables},
    }

    item_lookup = {item.value: item for item in all_items}

    glitches_item_name = "Out of Logic"
    ut_can_gen_without_yaml = True

    CAR_BY_NAME = {car.value: car for car_enum in CarItemTypeEnum.__subclasses__() for car in car_enum}
    EVENT_BY_NAME = {
        event.value: event
        for event_enum in (BurningCars, RaceEvents, StuntRunEvents, RoadRageEvents, MarkedManEvents, BigSurfIslandEvents, BurningRideEvents, MidnightRideEvents, [BigSurfIslandCars.CARSON_DUST_STORM])
        for event in event_enum
    }

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    def __init__(self, multiworld, player):
        self.debug_regions = False

        self.regions: set[str] = set()
        self.itempool: list[Item] = []
        self.starting_items:list[Item] = []

        self.goal_event_wins = 0

        self.smash_sanity_data: dict[AreaType, int] = {}

        self.is_ut = False
        super().__init__(multiworld, player)

    def generate_early(self) -> None:

        for missing in sorted(set(amount_events_default.keys()) - self.options.amount_events.value.keys()):
            self.options.amount_events.value[missing] = 0

        total_amount_car_events = sum(
            amount
            for event_name, amount in self.options.amount_events.value.items()
            if event_name not in NON_PARADISE_CITY_EVENT_NAMES
        )

        if total_amount_car_events < 1:
            self.options.amount_events.value["Race Event"] = 1
            logging.warning(
                f"{self.game}: {self.player_name} has no added events. "
                f"Including one Race Event"
            )

        for event_name, value in self.options.amount_events.value.items():
            win_type = event_type_to_wintype[event_name]
            if value > win_type.maximum:
                logging.warning(
                    f"{self.game}: {self.player_name} requested {value} {event_name}s, but only "
                    f"{win_type.maximum} exist. Adjusting to {win_type.maximum}"
                )
                self.options.amount_events.value[event_name] = win_type.maximum
            if event_name == "Burning Route Event":
                new_value = min(34, self.options.amount_events.value[event_name])
                if new_value != self.options.amount_events.value[event_name]:
                    logging.warning(
                        f"{self.game}: {self.player_name} requested {self.options.amount_events.value[event_name]} "
                        f"Burning Route Events, but at most 34 can be included (the starter car takes one of the 35). "
                        f"Adjusting to {new_value}"
                    )
                self.options.amount_events.value[event_name] = new_value

        self.total_amount_car_events = (
            sum(
                amount
                for event_name, amount in self.options.amount_events.value.items()
                if event_name not in NON_PARADISE_CITY_EVENT_NAMES
            )
            + 1 # for starter car
        )

        self.total_amount_big_surf_events = sum(
            amount
            for event_name, amount in self.options.amount_events.value.items()
            if event_name == "Big Surf Island Event"
        )

        self.total_amount_bike_events = sum(
            amount
            for event_name, amount in self.options.amount_events.value.items()
            if event_name in BIKE_EVENT_NAMES
        )

        self.total_amount_events = self.total_amount_car_events + self.total_amount_bike_events + self.total_amount_big_surf_events

        goal = self.options.license_goal.value
        if goal == LicenseGoal.option_burnout_elite and self.total_amount_car_events < BURNOUT_ELITE_EVENTS:
            goal = LicenseGoal.option_burnout
        if goal == LicenseGoal.option_burnout and self.total_amount_car_events < BURNOUT_EVENTS:
            goal = LicenseGoal.option_a_class
        if goal == LicenseGoal.option_a_class and self.total_amount_car_events < A_CLASS_EVENTS:
            goal = LicenseGoal.option_b_class
        if goal == LicenseGoal.option_b_class and self.total_amount_car_events < B_CLASS_EVENTS:
            goal = LicenseGoal.option_c_class
        if goal == LicenseGoal.option_c_class and self.total_amount_car_events < C_CLASS_EVENTS:
            goal = LicenseGoal.option_d_class

        if goal != self.options.license_goal.value:
            logging.warning(
                f"{self.game}: {self.player_name} chose the {LicenseGoal.get_option_name(self.options.license_goal.value)} "
                f"license goal, but only {self.total_amount_car_events} events are included, which is not enough to earn it. "
                f"Adjusting the license goal to {LicenseGoal.get_option_name(goal)}"
            )
        self.options.license_goal.value = goal

        match self.options.license_goal:
            case LicenseGoal.option_d_class:
                self.goal_event_wins = D_CLASS_WINS
            case LicenseGoal.option_c_class:
                self.goal_event_wins = C_CLASS_WINS
            case LicenseGoal.option_b_class:
                self.goal_event_wins = B_CLASS_WINS
            case LicenseGoal.option_a_class:
                self.goal_event_wins = A_CLASS_WINS
            case LicenseGoal.option_burnout:
                self.goal_event_wins = BURNOUT_WINS
            case LicenseGoal.option_burnout_elite:
                self.goal_event_wins = BURNOUT_ELITE_WINS

        starter_car = _BURNING_CARS_IN_ORDER[self.options.starter_car.value]
        other_burning_cars = [car for car in BurningCars if car != starter_car]
        burning_cars = self.random.sample(other_burning_cars, self.options.amount_events.value["Burning Route Event"])

        self.event_items: list[ItemTypeEnum] = [starter_car]
        self.event_items += burning_cars
        self.event_items += self.random.sample(list(RaceEvents), self.options.amount_events.value["Race Event"])
        self.event_items += self.random.sample(list(StuntRunEvents), self.options.amount_events.value["Stunt Run Event"])
        self.event_items += self.random.sample(list(RoadRageEvents), self.options.amount_events.value["Road Rage Event"])
        self.event_items += self.random.sample(list(MarkedManEvents), self.options.amount_events.value["Marked Man Event"])
        self.event_items += self.random.sample(list(BurningRideEvents), self.options.amount_events.value["Burning Ride Event"])
        self.event_items += self.random.sample(list(MidnightRideEvents), self.options.amount_events.value["Midnight Ride Event"])
        self.event_items += self.random.sample(list(BigSurfIslandEvents), self.options.amount_events.value["Big Surf Island Event"])

        if self.options.unique_car_wins.value and not sum(
            [
                self.options.amount_events.value["Race Event"],
                self.options.amount_events.value["Stunt Run Event"],
                self.options.amount_events.value["Road Rage Event"],
                self.options.amount_events.value["Marked Man Event"],
            ]
        ):
            self.event_items += self.random.sample(list(chain(RaceEvents, StuntRunEvents, RoadRageEvents, MarkedManEvents)), 1)
            logging.warning(
                f"{self.game}: {self.player_name} wants to enable unique car wins, but did not include any generic events. "
                f"Adding a random event to allow for these locations."
                # f"Disabling unique car wins"
            )
            # self.options.unique_car_wins.value = 0

        # -1 for the following to exclude starter car
        if self.options.starting_event_amount.value > self.total_amount_car_events - 1:
            logging.warning(
                f"{self.game}: {self.player_name} wants to start with {self.options.starting_event_amount.value} events, "
                f"but only {self.total_amount_car_events - 1} events are included. "
                f"Adjusting starting events to {self.total_amount_car_events - 1}"
            )
            self.options.starting_event_amount.value = self.total_amount_car_events - 1

        self.added_cars: list[CarItemTypeEnum] = []
        self.added_cars += self.random.sample(list(BurningRouteRewardCars), self.options.add_burning_route_reward_cars.value)
        self.added_cars += self.random.sample(list(CarbonCars), self.options.add_carbon_cars.value)
        self.added_cars += self.random.sample(list(OnlineCars), self.options.add_online_cars.value)
        self.added_cars += self.random.sample(list(ToyCars), self.options.add_toy_cars.value)
        self.added_cars += self.random.sample(list(LegendaryCars), self.options.add_legendary_cars.value)
        self.added_cars += self.random.sample(list(BoostSpecialCars), self.options.add_boost_special_cars.value)
        self.added_cars += self.random.sample(list(CopCars), self.options.add_pcpd_cars.value)
        self.added_cars += self.random.sample(list(BigSurfIslandCars), self.options.add_big_surf_island_cars.value)
        self.added_cars += self.random.sample(list(ParadiseBikes), self.options.add_paradise_bikes.value)

        if BigSurfIslandEvents.CARSON_DUST_STORM_BURNING_ROUTE in self.event_items and BigSurfIslandCars.CARSON_DUST_STORM not in self.added_cars:
            if BigSurfIslandCars.CARSON_DUST_STORM not in self.added_cars:
                self.event_items.append(BigSurfIslandCars.CARSON_DUST_STORM)
            self.event_items.remove(BigSurfIslandEvents.CARSON_DUST_STORM_BURNING_ROUTE)

        added_paradise_cars = self.options.amount_events.value["Burning Route Event"] + 1 + self.options.add_burning_route_reward_cars.value + self.options.add_carbon_cars.value
        if self.options.car_goal.value > added_paradise_cars:
            logging.warning(
                f"{self.game}: {self.player_name} has a car goal of {self.options.car_goal.value}, but only "
                f"{added_paradise_cars} Paradise cars are included. Adjusting the car goal to {added_paradise_cars}"
            )
            self.options.car_goal.value = min(added_paradise_cars, self.options.car_goal.value)


        for missing in sorted({area.value for area in WinType} - self.options.unique_event_win_goals.value.keys()):
            self.options.unique_event_win_goals.value[missing] = 0

        self.required_wins: [str, int] = {}
        for event_name, value in self.options.unique_event_win_goals.value.items():
            limit = self.options.amount_events.value[wintype_to_item_group[event_name]]
            if event_name == "Unique Burning Route Wins":
                limit += 1
            if value > limit:
                logging.warning(
                    f"{self.game}: {self.player_name} wants {value} {event_name}, but only {limit} "
                    f"{wintype_to_item_group[event_name]}s are included. Adjusting to {limit}"
                )
            self.required_wins[event_name] = min(value, limit)

        for missing in sorted({area.value for area in AreaType} - self.options.smash_counts.value.keys()):
            self.options.smash_counts.value[missing] = 0

        for area_name, value in self.options.smash_counts.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.SMASH]:
                logging.warning(
                    f"{self.game}: {self.player_name} wants {value} Smashes in {area_name}, but there are only "
                    f"{breakable_count_lookup[area_name][BreakableType.SMASH]} in that area. "
                    f"Adjusting to {breakable_count_lookup[area_name][BreakableType.SMASH]}"
                )
                self.options.smash_counts.value[area_name] = breakable_count_lookup[area_name][BreakableType.SMASH]


        for missing in sorted({area.value for area in AreaType} - self.options.billboard_counts.value.keys()):
            self.options.billboard_counts.value[missing] = 0

        for area_name, value in self.options.billboard_counts.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.BILLBOARD]:
                logging.warning(
                    f"{self.game}: {self.player_name} wants {value} Billboards in {area_name}, but there are only "
                    f"{breakable_count_lookup[area_name][BreakableType.BILLBOARD]} in that area. "
                    f"Adjusting to {breakable_count_lookup[area_name][BreakableType.BILLBOARD]}"
                )
                self.options.billboard_counts.value[area_name] = breakable_count_lookup[area_name][BreakableType.BILLBOARD]


        for missing in sorted({area.value for area in AreaType} - self.options.super_jump_counts.value.keys()):
            self.options.super_jump_counts.value[missing] = 0

        for area_name, value in self.options.super_jump_counts.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.SUPER_JUMP]:
                logging.warning(
                    f"{self.game}: {self.player_name} wants {value} Super Jumps in {area_name}, but there are only "
                    f"{breakable_count_lookup[area_name][BreakableType.SUPER_JUMP]} in that area. "
                    f"Adjusting to {breakable_count_lookup[area_name][BreakableType.SUPER_JUMP]}"
                )
                self.options.super_jump_counts.value[area_name] = breakable_count_lookup[area_name][BreakableType.SUPER_JUMP]


        for missing in sorted({area.value for area in AreaType} - self.options.drive_thru_counts.value.keys()):
            self.options.drive_thru_counts.value[missing] = 0

        for area_name, value in self.options.drive_thru_counts.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.DRIVETHRU]:
                logging.warning(
                    f"{self.game}: {self.player_name} wants {value} Drive-Thrus in {area_name}, but there are only "
                    f"{breakable_count_lookup[area_name][BreakableType.DRIVETHRU]} in that area. "
                    f"Adjusting to {breakable_count_lookup[area_name][BreakableType.DRIVETHRU]}"
                )
                self.options.drive_thru_counts.value[area_name] = breakable_count_lookup[area_name][BreakableType.DRIVETHRU]


        for missing in sorted({area.value for area in AreaType} - self.options.road_rule_time_count.value.keys()):
            self.options.road_rule_time_count.value[missing] = 0

        if self.total_amount_car_events < 4:
            logging.warning(
                f"{self.game}: {self.player_name} does not include enough Paradise City Car Events to enable Road Rules for Time or Showtime, "
                f"disabling any wanted Road Rules for Time or Showtime"
            )

        for area_name, value in self.options.road_rule_time_count.value.items():
            if self.total_amount_car_events < 4:
                self.options.road_rule_time_count.value[area_name] = 0
            elif value > breakable_count_lookup[area_name][BreakableType.ROADRULE_TIME]:
                logging.warning(
                    f"{self.game}: {self.player_name} wants {value} Road Rule Time in {area_name}, but there are only "
                    f"{breakable_count_lookup[area_name][BreakableType.ROADRULE_TIME]} in that area. "
                    f"Adjusting to {breakable_count_lookup[area_name][BreakableType.ROADRULE_TIME]}"
                )
                self.options.road_rule_time_count.value[area_name] = breakable_count_lookup[area_name][BreakableType.ROADRULE_TIME]


        for missing in sorted({area.value for area in AreaType} - self.options.road_rule_showtime_count.value.keys()):
            self.options.road_rule_showtime_count.value[missing] = 0

        for area_name, value in self.options.road_rule_showtime_count.value.items():
            if self.total_amount_car_events < 4:
                self.options.road_rule_showtime_count.value[area_name] = 0
            elif value > breakable_count_lookup[area_name][BreakableType.ROADRULE_SHOWTIME]:
                logging.warning(
                    f"{self.game}: {self.player_name} wants {value} Road Rule Showtime in {area_name}, but there are only "
                    f"{breakable_count_lookup[area_name][BreakableType.ROADRULE_SHOWTIME]} in that area. "
                    f"Adjusting to {breakable_count_lookup[area_name][BreakableType.ROADRULE_SHOWTIME]}"
                )
                self.options.road_rule_showtime_count.value[area_name] = breakable_count_lookup[area_name][BreakableType.ROADRULE_SHOWTIME]


        for missing in sorted({area.value for area in AreaType} - self.options.road_rule_bike_day_count.value.keys()):
            self.options.road_rule_bike_day_count.value[missing] = 0

        for area_name, value in self.options.road_rule_bike_day_count.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_DAY]:
                logging.warning(
                    f"{self.game}: {self.player_name} wants {value} Road Rule Bike Day in {area_name}, but there are only "
                    f"{breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_DAY]} in that area. "
                    f"Adjusting to {breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_DAY]}"
                )
                self.options.road_rule_bike_day_count.value[area_name] = breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_DAY]


        for missing in sorted({area.value for area in AreaType} - self.options.road_rule_bike_night_count.value.keys()):
            self.options.road_rule_bike_night_count.value[missing] = 0

        for area_name, value in self.options.road_rule_bike_night_count.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_NIGHT]:
                logging.warning(
                    f"{self.game}: {self.player_name} wants {value} Road Rule Bike Night in {area_name}, but there are only "
                    f"{breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_NIGHT]} in that area. "
                    f"Adjusting to {breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_NIGHT]}"
                )
                self.options.road_rule_bike_night_count.value[area_name] = breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_NIGHT]

        bike_locations = (
            sum(self.options.road_rule_bike_day_count.value.values())
            + sum(self.options.road_rule_bike_night_count.value.values())
            + self.options.amount_events.value["Burning Ride Event"]
            + self.options.amount_events.value["Midnight Ride Event"]
        )
        if bike_locations and not self.options.add_paradise_bikes.value:
            self.added_cars += self.random.sample(list(ParadiseBikes), 1)
            logging.warning(
                f"{self.game}: {self.player_name} wants {bike_locations} Locations requiring a Bike, but did not include any Paradise Bikes. "
                f"Randomly adding one bike to make these guaranteed to be available."
            )

        if (
            self.options.unique_car_wins.value
            and not self.total_amount_bike_events
            and any(car in {*ParadiseBikes, ToyCars.NAKAMURA_TOY_FIREHAWK_GP} for car in self.added_cars)
        ):
            self.event_items += self.random.sample(list(chain(BurningRideEvents, MidnightRideEvents)), 1)
            self.total_amount_bike_events = 1

        for missing in sorted(mode_base_difficulty_default.keys() - self.options.mode_base_difficulty.value.keys()):
            self.options.mode_base_difficulty.value[missing] = mode_base_difficulty_default[missing]

        self.is_ut = (hasattr(self.multiworld, "re_gen_passthrough")
                    and isinstance(self.multiworld.re_gen_passthrough, dict)
                    and self.game in self.multiworld.re_gen_passthrough)
        self.handle_ut_yamless(None)

    def create_regions(self):
        locations.create_regions(self)
        locations.create_entrances(self)

    def connect_entrances(self) -> None:
        pass

    def create_item(self, name: str) -> BurnoutParadiseRemasteredItem:
        item_enum = self.item_lookup[name]
        return items.create_item(self, item_enum)

    def create_items(self):
        self.starting_items = items.create_items(self)
        for item in self.starting_items:
            self.push_precollected(item)

    def get_filler_item_name(self) -> str:
        if self.options.filler_items_distribution.weights_pair:
            return items.create_random_items( self, self.options.filler_items_distribution.weights_pair, 1)[0]
        return items.create_random_items( self, self.options.filler_items_distribution.default, 1)[0]

    def set_rules(self):
        goal = HasEventWins(wins=self.goal_event_wins)
        goal &= HasGroupUnique("Paradise Car", count=self.options.car_goal.value)
        uw = self.required_wins
        for win_type in WinType:
            name = wintype_to_item_group[win_type.value]
            count = min(uw.get(win_type.value, 0), win_type.maximum)
            goal &= HasGroupUnique(name, count=count)

        self.set_completion_rule(goal)


    def generate_output(self, output_directory: str):
        if self.debug_regions:
            print("Generating Output")
            visualize_regions(
                self.multiworld.get_region("Menu", self.player),
                file_name=os.path.join(output_directory, f"Player{self.player}_output.puml"),
                show_entrance_names=True,
                regions_to_highlight=self.multiworld.get_all_state().reachable_regions[self.player],
            )

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "sem_ver": self.manifest["mod_version"],
            "license_goal": self.options.license_goal.value,
            "car_goal_count": self.options.car_goal.value,
            "amount_events": self.options.amount_events.value,
            "unique_event_win_goals": self.options.unique_event_win_goals.value,
            "cache_breakable_locations": self.options.cache_breakable_locations.value,
            "finished_events_stay_finished": self.options.finished_events_stay_finished.value,
            "breakable_locks" : self.options.breakable_locks.value,
            "starter_car" : self.options.starter_car.value,
            "starting_event_amount" : self.options.starting_event_amount.value,
            "add_livery_items" : self.options.add_livery_items.value,
            "unique_car_wins": self.options.unique_car_wins.value,
            "unique_event_wins": self.options.unique_event_wins.value,
            "smash_sanity": self.options.smash_counts.value,
            "billboard_sanity": self.options.billboard_counts.value,
            "super_jump_sanity": self.options.super_jump_counts.value,
            "drive_thru_counts": self.options.drive_thru_counts.value,
            "road_rule_time_count": self.options.road_rule_time_count.value,
            "road_rule_showtime_count": self.options.road_rule_showtime_count.value,
            "road_rule_bike_day_count": self.options.road_rule_bike_day_count.value,
            "road_rule_bike_night_count": self.options.road_rule_bike_night_count.value,
            "death_link": self.options.deathlink.value,
            "death_link_amnesty": self.options.deathlink_amnesty.value,
            "use_what_you_get": self.options.use_what_you_get.value,
            "add_burning_route_reward_cars": self.options.add_burning_route_reward_cars.value,
            "add_carbon_cars": self.options.add_carbon_cars.value,
            "add_legendary_cars": self.options.add_legendary_cars.value,
            "add_online_cars": self.options.add_online_cars.value,
            "add_boost_special_cars": self.options.add_boost_special_cars.value,
            "add_toy_cars": self.options.add_toy_cars.value,
            "add_pcpd_cars": self.options.add_pcpd_cars.value,
            "add_big_surf_island_cars": self.options.add_big_surf_island_cars.value,
            "add_paradise_bikes": self.options.add_paradise_bikes.value,
            "mode_base_difficulty": self.options.mode_base_difficulty.value,
            "added_cars": [car.value for car in self.added_cars],
            "event_items": [event.value for event in self.event_items],
            "goal_event_wins": self.goal_event_wins,
            "required_wins": self.required_wins,
            "add_drive_thru_jump_points": self.options.add_drive_thru_jump_points.value,
        }


    def handle_ut_yamless(
        self, slot_data: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        if self.is_ut and not slot_data:
            slot_data = self.multiworld.re_gen_passthrough[self.game]
        if not slot_data:
            return None

        self.options.deathlink.value = slot_data["death_link"]

        self.options.license_goal.value = slot_data["license_goal"]
        self.options.car_goal.value = slot_data["car_goal_count"]
        self.options.starter_car.value = slot_data["starter_car"]
        self.options.starting_event_amount.value = slot_data["starting_event_amount"]
        self.options.add_livery_items.value = slot_data["add_livery_items"]
        self.options.unique_event_win_goals.value = slot_data["unique_event_win_goals"]
        self.options.breakable_locks.value = slot_data["breakable_locks"]
        self.options.amount_events.value = slot_data["amount_events"]
        self.options.unique_event_wins.value = slot_data["unique_event_wins"]
        self.options.unique_car_wins.value = slot_data["unique_car_wins"]
        self.options.finished_events_stay_finished.value = slot_data["finished_events_stay_finished"]
        self.options.smash_counts.value = slot_data["smash_sanity"]
        self.options.billboard_counts.value = slot_data["billboard_sanity"]
        self.options.super_jump_counts.value = slot_data["super_jump_sanity"]
        self.options.drive_thru_counts.value = slot_data["drive_thru_counts"]
        self.options.road_rule_time_count.value = slot_data["road_rule_time_count"]
        self.options.road_rule_showtime_count.value = slot_data["road_rule_showtime_count"]
        self.options.road_rule_bike_day_count.value = slot_data["road_rule_bike_day_count"]
        self.options.road_rule_bike_night_count.value = slot_data["road_rule_bike_night_count"]
        self.options.add_burning_route_reward_cars.value = slot_data["add_burning_route_reward_cars"]
        self.options.add_carbon_cars.value = slot_data["add_carbon_cars"]
        self.options.add_legendary_cars.value = slot_data["add_legendary_cars"]
        self.options.add_online_cars.value = slot_data["add_online_cars"]
        self.options.add_boost_special_cars.value = slot_data["add_boost_special_cars"]
        self.options.add_toy_cars.value = slot_data["add_toy_cars"]
        self.options.add_pcpd_cars.value = slot_data["add_pcpd_cars"]
        self.options.add_big_surf_island_cars.value = slot_data["add_big_surf_island_cars"]
        self.options.add_paradise_bikes.value = slot_data["add_paradise_bikes"]
        self.options.add_drive_thru_jump_points.value = slot_data["add_drive_thru_jump_points"]

        self.added_cars = [self.CAR_BY_NAME[name] for name in slot_data["added_cars"]]
        self.event_items = [self.EVENT_BY_NAME[name] for name in slot_data["event_items"]]
        self.total_amount_car_events = (
            sum(
                amount
                for event_name, amount in self.options.amount_events.value.items()
                if event_name not in NON_PARADISE_CITY_EVENT_NAMES
            )
            + 1
        )
        self.total_amount_bike_events = sum(
            amount
            for event_name, amount in self.options.amount_events.value.items()
            if event_name in BIKE_EVENT_NAMES
        )
        if (
            self.options.unique_car_wins.value
            and not self.total_amount_bike_events
            and any(car in {*ParadiseBikes, ToyCars.NAKAMURA_TOY_FIREHAWK_GP} for car in self.added_cars)
        ):
            self.total_amount_bike_events = 1

        self.total_amount_big_surf_events = sum(
            amount
            for event_name, amount in self.options.amount_events.value.items()
            if event_name == "Big Surf Island Event"
        )
        self.total_amount_events = self.total_amount_car_events + self.total_amount_bike_events + self.total_amount_big_surf_events
        self.goal_event_wins = slot_data["goal_event_wins"]
        self.required_wins = slot_data["required_wins"]

        return slot_data

    # def custom_ut_sort(self, region_label: str, location_label: str) -> str:
    #     loc_id = self.location_name_to_id.get(location_label, 99999999)
    #     return f"{region_label}_{loc_id}"
