from rule_builder.rules import Has, HasGroup
from itertools import chain
import json
import os
from importlib.resources import files
from typing import ClassVar, Any, Mapping

from BaseClasses import Tutorial, Item
from Utils import visualize_regions
from worlds.AutoWorld import WebWorld
from . import locations, items
from .constants import BURNOUT_PARADISE_REMASTERED, BURNOUT_WINS, BURNOUT_ELITE_WINS, A_CLASS_WINS, B_CLASS_WINS, C_CLASS_WINS, AreaType, BreakableType, WinType
from .data import BoostType
from .data.items import all_items, Events, Blockers, Discoverables, DriveThrus
from .data.items.cars import Cars, BurningCars, CarbonCars, ToyCars, LegendaryCars, BoostSpecialCars, CopCars, BigSurfIslandCars, ParadiseBikes, OnlineCars
from .data.items.liveries import ParadiseCarsLivery
from .data.locations import all_generated_locations, all_enum_locations, breakable_count_lookup, EventLocations
from .data.rules.state_rules import HasEventWins
from .options import burnout_paradise_remastered_option_groups, LicenseGoal
from .world_base import BurnoutParadiseRemasteredBase
from .items import BurnoutParadiseRemasteredItem


class BurnoutParadiseRemasteredWeb(WebWorld):
    theme = "partyTime"
    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Burnout Paradise Remasteredrandomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["FyreDay"],
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
        "Car": {car.value for car in chain(Cars, BurningCars, CarbonCars, ToyCars, LegendaryCars, BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars)},
        "Bike": {bike.value for bike in chain(ParadiseBikes, [ToyCars.NAKAMURA_TOY_FIREHAWK_GP]) },
        "Paradise Car": {car.value for car in chain(Cars, BurningCars, CarbonCars)},
        "Toy Car": {car.value for car in ToyCars},
        "Legendary Car": {car.value for car in LegendaryCars},
        "Boost Special Car": {car.value for car in BoostSpecialCars},
        "Cop Car": {car.value for car in CopCars},
        "Big Surf Island Car": {car.value for car in BigSurfIslandCars},
        "Online Car": {car.value for car in OnlineCars},
        "Speed Car": {
            car.value for car in chain(
                Cars, BurningCars, CarbonCars, ToyCars, LegendaryCars,
                BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars
            ) if car.boosttype == BoostType.SPEED
        },
        "Crash Car": {
            car.value for car in chain(
                Cars, BurningCars, CarbonCars, ToyCars, LegendaryCars,
                BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars
            ) if car.boosttype == BoostType.CRASH
        },
        "Stunt Car": {
            car.value for car in chain(
                Cars, BurningCars, CarbonCars, ToyCars, LegendaryCars,
                BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars
            ) if car.boosttype == BoostType.STUNT
        },
        "Special Car": {
            car.value for car in chain(
                Cars, BurningCars, CarbonCars, ToyCars, LegendaryCars,
                BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars, ParadiseBikes
            ) if car.boosttype == BoostType.SPECIAL
        },
        "Livery": {livery.value for livery in ParadiseCarsLivery},
        "Regular Event": {event.value for event in Events},
        "Burning Route Event": {car.value for car in BurningCars},
        "Race Event": { loc.value.split(" - ", 1)[1] for loc in EventLocations if loc.value.startswith("Win the Race - ") },
        "Stunt Run Event": { loc.value.split(" - ", 1)[1] for loc in EventLocations if loc.value.startswith("Win the Stunt Run - ") },
        "Road Rage Event": { loc.value.split(" - ", 1)[1] for loc in EventLocations if loc.value.startswith("Win the Road Rage - ") },
        "Marked Man Event": { loc.value.split(" - ", 1)[1] for loc in EventLocations if loc.value.startswith("Win the Marked Man - ") },
        f"{AreaType.PALM_BAY_HEIGHTS.value} Event": { loc.value.split(" - ", 1)[1] for loc in EventLocations if loc.region.value == AreaType.PALM_BAY_HEIGHTS.value },
        f"{AreaType.HARBOR_TOWN.value} Event": { loc.value.split(" - ", 1)[1] for loc in EventLocations if loc.region.value == AreaType.HARBOR_TOWN.value },
        f"{AreaType.SILVER_LAKE.value} Event": { loc.value.split(" - ", 1)[1] for loc in EventLocations if loc.region.value == AreaType.SILVER_LAKE.value },
        f"{AreaType.WHITE_MOUNTAIN.value} Event": { loc.value.split(" - ", 1)[1] for loc in EventLocations if loc.region.value == AreaType.WHITE_MOUNTAIN.value },
        f"{AreaType.DOWNTOWN_PARADISE.value} Event": { loc.value.split(" - ", 1)[1] for loc in EventLocations if loc.region.value == AreaType.DOWNTOWN_PARADISE.value },
        "Any Event": {e.value for e in chain(Events, BurningCars)},
        "Area Breakable": {area.value for area in Blockers},
        "Area Discoverable": {discoverable.value for discoverable in Discoverables},
        "Any Jump Point": {drivethru.value for drivethru in DriveThrus},
    }

    item_lookup = {item.value: item for item in all_items}

    ut_can_gen_without_yaml = True

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
        match self.options.license_goal:
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

        for missing in sorted({area.value for area in AreaType} - self.options.smash_counts.value.keys()):
            self.options.smash_counts.value[missing] = 0

        for area_name, value in self.options.smash_counts.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.SMASH]:
                self.options.smash_counts.value[area_name] = breakable_count_lookup[area_name][BreakableType.SMASH]


        for missing in sorted({area.value for area in AreaType} - self.options.billboard_counts.value.keys()):
            self.options.billboard_counts.value[missing] = 0

        for area_name, value in self.options.billboard_counts.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.BILLBOARD]:
                self.options.billboard_counts.value[area_name] = breakable_count_lookup[area_name][BreakableType.BILLBOARD]


        for missing in sorted({area.value for area in AreaType} - self.options.super_jump_counts.value.keys()):
            self.options.super_jump_counts.value[missing] = 0

        for area_name, value in self.options.super_jump_counts.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.SUPER_JUMP]:
                self.options.super_jump_counts.value[area_name] = breakable_count_lookup[area_name][BreakableType.SUPER_JUMP]


        for missing in sorted({area.value for area in AreaType} - self.options.drive_thru_counts.value.keys()):
            self.options.drive_thru_counts.value[missing] = 0

        for area_name, value in self.options.drive_thru_counts.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.DRIVETHRU]:
                self.options.drive_thru_counts.value[area_name] = breakable_count_lookup[area_name][BreakableType.DRIVETHRU]


        for missing in sorted({area.value for area in AreaType} - self.options.road_rule_time_count.value.keys()):
            self.options.road_rule_time_count.value[missing] = 0

        for area_name, value in self.options.road_rule_time_count.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.ROADRULE_TIME]:
                self.options.road_rule_time_count.value[area_name] = breakable_count_lookup[area_name][BreakableType.ROADRULE_TIME]


        for missing in sorted({area.value for area in AreaType} - self.options.road_rule_showtime_count.value.keys()):
            self.options.road_rule_showtime_count.value[missing] = 0

        for area_name, value in self.options.road_rule_showtime_count.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.ROADRULE_SHOWTIME]:
                self.options.road_rule_showtime_count.value[area_name] = breakable_count_lookup[area_name][BreakableType.ROADRULE_SHOWTIME]


        for missing in sorted({area.value for area in AreaType} - self.options.road_rule_bike_day_count.value.keys()):
            self.options.road_rule_bike_day_count.value[missing] = 0

        for area_name, value in self.options.road_rule_bike_day_count.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_DAY]:
                self.options.road_rule_bike_day_count.value[area_name] = breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_DAY]


        for missing in sorted({area.value for area in AreaType} - self.options.road_rule_bike_night_count.value.keys()):
            self.options.road_rule_bike_night_count.value[missing] = 0

        for area_name, value in self.options.road_rule_bike_night_count.value.items():
            if value > breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_NIGHT]:
                self.options.road_rule_bike_night_count.value[area_name] = breakable_count_lookup[area_name][BreakableType.ROADRULE_BIKES_NIGHT]


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
        goal &= HasGroup("Paradise Car", count=self.options.car_goal.value)
        uw = self.options.unique_event_win_goals
        event_map = {
            WinType.BURNING_ROUTE_WINS.value: "Burning Route Event",
            WinType.RACE_WINS.value:          "Race Event",
            WinType.STUNT_RUN_WINS.value:     "Stunt Run Event",
            WinType.ROAD_RAGE_WINS.value:     "Road Rage Event",
            WinType.MARKED_MAN_WINS.value:    "Marked Man Event",
        }
        for win_type in WinType:
            name = event_map[win_type.value]
            count = min(uw.get(win_type.value, 0), win_type.maximum)
            goal &= HasGroup(name, count=count)
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
            "unique_event_win_goals": self.options.unique_event_win_goals.value,
            "breakable_locks" : self.options.breakable_locks.value,
            "starter_car" : self.options.starter_car.value,
            "starting_event_amount" : self.options.starting_event_amount.value,
            "add_livery_items" : self.options.add_livery_items.value,
            "unique_car_wins": self.options.unique_car_wins.value,
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
            "add_legendary_cars": self.options.add_legendary_cars.value,
            "add_online_cars": self.options.add_online_cars.value,
            "add_boost_special_cars": self.options.add_boost_special_cars.value,
            "add_toy_cars": self.options.add_toy_cars.value,
            "add_pcpd_cars": self.options.add_pcpd_cars.value,
            "add_big_surf_island_cars": self.options.add_big_surf_island_cars.value,
            "add_paradise_bikes": self.options.add_paradise_bikes.value,
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
        self.options.unique_event_win_goals.value = slot_data["unique_event_win_goals"]
        self.options.breakable_locks.value = slot_data["breakable_locks"]
        self.options.unique_car_wins.value = slot_data["unique_car_wins"]
        self.options.smash_counts.value = slot_data["smash_sanity"]
        self.options.billboard_counts.value = slot_data["billboard_sanity"]
        self.options.super_jump_counts.value = slot_data["super_jump_sanity"]
        self.options.drive_thru_counts.value = slot_data["drive_thru_counts"]
        self.options.road_rule_time_count.value = slot_data["road_rule_time_count"]
        self.options.road_rule_showtime_count.value = slot_data["road_rule_showtime_count"]
        self.options.road_rule_bike_day_count.value = slot_data["road_rule_bike_day_count"]
        self.options.road_rule_bike_night_count.value = slot_data["road_rule_bike_night_count"]
        self.options.add_legendary_cars.value = slot_data["add_legendary_cars"]
        self.options.add_online_cars.value = slot_data["add_online_cars"]
        self.options.add_boost_special_cars.value = slot_data["add_boost_special_cars"]
        self.options.add_toy_cars.value = slot_data["add_toy_cars"]
        self.options.add_pcpd_cars.value = slot_data["add_pcpd_cars"]
        self.options.add_big_surf_island_cars.value = slot_data["add_big_surf_island_cars"]
        self.options.add_paradise_bikes.value = slot_data["add_paradise_bikes"]
        self.options.add_drive_thru_jump_points.value = slot_data["add_drive_thru_jump_points"]

        return slot_data
