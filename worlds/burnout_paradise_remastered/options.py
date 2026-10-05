from itertools import accumulate
from functools import cached_property
from dataclasses import dataclass

from Options import OptionGroup, Toggle, PerGameCommonOptions, Choice, OptionCounter, ItemDict, StartInventoryPool, Range, Accessibility, ProgressionBalancing
from .constants import AreaType, WinType
from .data.items.filler import get_default_dict


class LicenseGoal(Choice):
    """
    What license do you require to goal?
    This is in addition to the other goal settings.

    **C Class** - 9 Event Wins
    **B Class** - 24 Event Wins
    **A Class** - 50 Event Wins
    **Burnout** - 90 Event Wins
    **Burnout Elite** - 210 Event Wins
    """
    display_name = "License Goal Class"
    option_c_class = 0
    option_b_class = 1
    option_a_class = 2
    option_burnout = 3
    option_burnout_elite = 4
    default = 1

class CarCollectionGoal(Range):
    """
    How many base game cars do you need to goal?
    This is in addition to the other goal settings.
    """
    display_name = "Car Goal Amount"
    range_start = 0
    range_end = 76
    default = 0

unique_wins_default = {
    WinType.BURNING_ROUTE_WINS.value : 0,
    WinType.RACE_WINS.value : 0,
    WinType.STUNT_RUN_WINS.value : 0,
    WinType.ROAD_RAGE_WINS.value : 0,
    WinType.MARKED_MAN_WINS.value : 0,
}

class UniqueEventWinGoals(OptionCounter):
    """
    How many unique wins per event type do you need to acquire to goal?
    This is in addition to the other goal settings.

    Valid Options:
        - **Unique Burning Route Wins** Must be in Range 0 to 35
        - **Unique Race Wins** Must be in Range 0 to 41
        - **Unique Stunt Run Wins** Must be in Range 0 to 14
        - **Unique Road Rage Wins** Must be in Range 0 to 16
        - **Unique Marked Man Wins* Must be in Range 0 to 14
    """
    display_name = "Unique Event Wins Goal Amount"
    default = unique_wins_default
    min = 0
    max = 41
    valid_keys = unique_wins_default.keys()

class BreakableLocks(Choice):
    """
    Lock each area's Sanity checks behind an item?

    This reduces sphere 1 down to a small amount of checks, which can help progression balancing.

    Recommended if you have sanity options turned up.

    **All Unlocked From The Start** - All Smashes, Billboards and Super/Mega Jumps are available from the Start
    **Locked By Area** - Smashes, Billboards, Super/Mega Jumps and Road Rules are locked behind regional items, all types becoming available all at once per area
    **Locked By Area And Type** - Smashes, Billboards, Super/Mega Jumps and Road Rules are locked behind individual regional items, becoming available per area per type
    """
    option_all_unlocked_from_the_start = 0
    option_locked_by_area = 1
    option_locked_by_area_and_type = 2
    default = 0
    display_name = "Lock Breakables"
    rich_text_doc = True

class StarterCar(Choice):
    """
    With what car are you starting with?
    """
    option_hunter_cavalry = 0
    option_hunter_mesquite = 1
    option_nakamura_si_7 = 2
    option_hunter_vegas = 3
    option_krieger_pioneer = 4
    option_nakamura_ikusa_gt = 5
    option_kitano_hydros_custom = 6
    option_hunter_reliable_custom = 7
    option_watson_r_turbo_roadster = 8
    option_rossolini_lm_classic = 9
    option_hunter_manhattan = 10
    option_carson_fastback = 11
    option_carson_grand_marais = 12
    option_montgomery_hyperion = 13
    option_krieger_616_sport = 14
    option_hunter_spur = 15
    option_montgomery_gt_2400 = 16
    option_jansen_p12 = 17
    option_carson_inferno_van = 18
    option_rossolini_tempesta = 19
    option_carson_opus = 20
    option_carson_annihilator = 21
    option_jansen_x12 = 22
    option_kitano_touge_sport = 23
    option_hunter_takedown_4x4 = 24
    option_carson_500_gt = 25
    option_hunter_racing_oval_champ = 26
    option_carson_gt_concept = 27
    option_hunter_citizen = 28
    option_watson_25_v16_revenge = 29
    option_montgomery_hawker = 30
    option_krieger_uberschall_8 = 31
    option_carson_thunder_custom = 32
    option_carson_hot_rod_coupe = 33
    option_krieger_racing_wtr = 34

    default = 0
    display_name = "Starter Car"
    rich_text_doc = True

class StartingEventAmount(Range):
    """
    With how many random events do you want to start with?
    """
    display_name = "Starting Event Amount"
    range_start = 0
    range_end = 85
    default = 5

class AddLiveryItems(Toggle):
    """
    If enabled, adds cars' additional liveries as items. Otherwise they are unlocked upon receiving the car.
    """
    display_name = "Add Car Liveries As Items"

class AddDriveThruAsJumpPointItems(Toggle):
    """
    Use F4 to open a quick travel menu.

    If enabled, adds each drive-thru (Junkyards, Gas Stations, Auto Repairs) as an item. If received, allows you to teleport to said drive-thru.
    If disabled, these jump points become available as soon as you discover them by driving near them.
    """
    display_name = "Add Drive-Thrus As Jump Points"

class AddLegendaryCars(Toggle):
    """
    If enabled, adds all Legendary cars as unlockable items
    """
    display_name = "Add Legendary Cars"

class AddOnlineCars(Toggle):
    """
    If enabled, adds all Online cars as unlockable items
    """
    display_name = "Add Online Cars"

class AddBoostSpecialCars(Toggle):
    """
    If enabled, adds all Boost Special cars as unlockable items
    """
    display_name = "Add Boost Special Cars"

class AddToyCars(Toggle):
    """
    If enabled, adds all Toy cars as unlockable items
    """
    display_name = "Add Toy Cars"

class AddParadiseBikes(Toggle):
    """
    If enabled, adds all Paradise bikes as unlockable items
    """
    display_name = "Add Paradise Bikes"

class AddBigSurfIslandCars(Toggle):
    """
    If enabled, adds all Big Surf Island cars as unlockable items
    """
    display_name = "Add Big Surf Island Cars"

class AddPCPDCars(Toggle):
    """
    If enabled, adds all PCPD police cars as unlockable items
    """
    display_name = "Add PCPD Cars"

class UniqueCarWins(Choice):
    """
    Enable locations for wins with each vehicle available.

    **NOTE:** Including more cars will expand these locations for each car added.

    **None** - No car wins are included as locations.
    **Each Car Its Own** - Every vehicle has its own location for winning.
    **Grouped By Boost Type** - Each unique car win now increments its boost type category instead. There are for groups: Speed, Crash, Stunt and Special.
    """
    option_none = 0
    option_each_car_its_own = 1
    option_grouped_by_boost_type = 2
    default = 0
    display_name = "Add Unique Vehicle Wins as Locations"
    rich_text_doc = True

smash_sanity_default = {
    AreaType.PALM_BAY_HEIGHTS.value : 10,
    AreaType.SILVER_LAKE.value : 10,
    AreaType.WHITE_MOUNTAIN.value : 10,
    AreaType.HARBOR_TOWN.value : 10,
    AreaType.DOWNTOWN_PARADISE.value : 10,
    AreaType.BIG_SURF_ISLAND.value : 10,
}

class SmashSanityCounts(OptionCounter):
    """
    Change how many Smash checks there are for each area

    Valid Options:
        - **Palm Bay Heights** Must be in Range 0 to 50
        - **Silver Lake** Must be in Range 0 to 90
        - **White Mountain** Must be in Range 0 to 90
        - **Harbor Town** Must be in Range 0 to 90
        - **Downtown Paradise** Must be in Range 0 to 80
        - **Big Surf Island** Must be in Range 0 to 75
    """
    display_name = "Smash Sanity"
    default = smash_sanity_default
    min = 0
    max = 90
    valid_keys = smash_sanity_default.keys()

billboard_sanity_default = {
    AreaType.PALM_BAY_HEIGHTS.value : 4,
    AreaType.SILVER_LAKE.value : 4,
    AreaType.WHITE_MOUNTAIN.value : 4,
    AreaType.HARBOR_TOWN.value : 4,
    AreaType.DOWNTOWN_PARADISE.value : 4,
    AreaType.BIG_SURF_ISLAND.value : 4,
}

class BillboardSanityCounts(OptionCounter):
    """
    Change how many Billboard checks there are for each area

    Valid Options:
        - **Palm Bay Heights** Must be in Range 0 to 20
        - **Silver Lake** Must be in Range 0 to 20
        - **White Mountain** Must be in Range 0 to 25
        - **Harbor Town** Must be in Range 0 to 25
        - **Downtown Paradise** Must be in Range 0 to 30
        - **Big Surf Island** Must be in Range 0 to 45
    """
    display_name = "Billboard Sanity"
    default = billboard_sanity_default
    min = 0
    max = 45
    valid_keys = billboard_sanity_default.keys()

super_jump_sanity_default = {
    AreaType.PALM_BAY_HEIGHTS.value : 1,
    AreaType.SILVER_LAKE.value : 1,
    AreaType.WHITE_MOUNTAIN.value : 1,
    AreaType.HARBOR_TOWN.value : 1,
    AreaType.DOWNTOWN_PARADISE.value : 1,
    AreaType.BIG_SURF_ISLAND.value : 1,
}

class SuperJumpSanityCounts(OptionCounter):
    """
    Change how many Super Jump checks there are for each area

    Valid Options:
        - **Palm Bay Heights** Must be in Range 0 to 10
        - **Silver Lake** Must be in Range 0 to 10
        - **White Mountain** Must be in Range 0 to 10
        - **Harbor Town** Must be in Range 0 to 10
        - **Downtown Paradise** Must be in Range 0 to 10
        - **Big Surf Island** Must be in Range 0 to 15
    """
    display_name = "Super Jump Sanity"
    default = super_jump_sanity_default
    min = 0
    max = 15
    cull_zeroes = False
    valid_keys = super_jump_sanity_default.keys()

drivethru_sanity_default = {
    AreaType.PALM_BAY_HEIGHTS.value : 5,
    AreaType.SILVER_LAKE.value : 5,
    AreaType.WHITE_MOUNTAIN.value : 5,
    AreaType.HARBOR_TOWN.value : 5,
    AreaType.DOWNTOWN_PARADISE.value : 5,
    AreaType.BIG_SURF_ISLAND.value : 5,
}

class DriveThruSanityCounts(OptionCounter):
    """
    Change how many Drive-Thru (Junkyards, Gas Stations, Auto Repairs, Paint Shops, Parking Garages) checks there are for each area

    Valid Options:
        - **Palm Bay Heights** Must be in Range 0 to 10
        - **Silver Lake** Must be in Range 0 to 7
        - **White Mountain** Must be in Range 0 to 7
        - **Harbor Town** Must be in Range 0 to 10
        - **Downtown Paradise** Must be in Range 0 to 12
        - **Big Surf Island** Must be in Range 0 to 5
    """
    display_name = "Drive-Thru Sanity"
    default = drivethru_sanity_default
    min = 0
    max = 12
    cull_zeroes = False
    valid_keys = drivethru_sanity_default.keys()

road_rule_time_sanity_default = {
    AreaType.PALM_BAY_HEIGHTS.value : 5,
    AreaType.SILVER_LAKE.value : 5,
    AreaType.WHITE_MOUNTAIN.value : 5,
    AreaType.HARBOR_TOWN.value : 5,
    AreaType.DOWNTOWN_PARADISE.value : 5,
    AreaType.BIG_SURF_ISLAND.value : 5,
}

class RoadRuleTimeSanityCounts(OptionCounter):
    """
    Change how many Road Rules for Time checks there are for each area. (The count goes by the placement of pins on the ingame map)

    Valid Options:
        - **Palm Bay Heights** Must be in Range 0 to 18
        - **Silver Lake** Must be in Range 0 to 9
        - **White Mountain** Must be in Range 0 to 10
        - **Harbor Town** Must be in Range 0 to 14
        - **Downtown Paradise** Must be in Range 0 to 13
        - **Big Surf Island** Must be in Range 0 to 12
    """
    display_name = "Road Rule for Time Sanity"
    default = road_rule_time_sanity_default
    min = 0
    max = 18
    cull_zeroes = False
    valid_keys = road_rule_time_sanity_default.keys()

road_rule_showtime_sanity_default = {
    AreaType.PALM_BAY_HEIGHTS.value : 0,
    AreaType.SILVER_LAKE.value : 0,
    AreaType.WHITE_MOUNTAIN.value : 0,
    AreaType.HARBOR_TOWN.value : 0,
    AreaType.DOWNTOWN_PARADISE.value : 0,
    AreaType.BIG_SURF_ISLAND.value : 0,
}

class RoadRuleShowtimeSanityCounts(OptionCounter):
    """
    Change how many Road Rules for Showtime checks there are for each area. (The count goes by the placement of pins on the ingame map)

    Valid Options:
        - **Palm Bay Heights** Must be in Range 0 to 18
        - **Silver Lake** Must be in Range 0 to 9
        - **White Mountain** Must be in Range 0 to 10
        - **Harbor Town** Must be in Range 0 to 14
        - **Downtown Paradise** Must be in Range 0 to 13
        - **Big Surf Island** Must be in Range 0 to 12
    """
    display_name = "Road Rule for Showtime Sanity"
    default = road_rule_showtime_sanity_default
    min = 0
    max = 18
    cull_zeroes = False
    valid_keys = road_rule_showtime_sanity_default.keys()

road_rule_bike_at_day_sanity_default = {
    AreaType.PALM_BAY_HEIGHTS.value : 0,
    AreaType.SILVER_LAKE.value : 0,
    AreaType.WHITE_MOUNTAIN.value : 0,
    AreaType.HARBOR_TOWN.value : 0,
    AreaType.DOWNTOWN_PARADISE.value : 0,
    AreaType.BIG_SURF_ISLAND.value : 0,
}

class RoadRuleBikeDaySanityCounts(OptionCounter):
    """
    Change how many Road Rules for Bikes at Day checks there are for each area. (The count goes by the placement of pins on the ingame map)
    Requires you to add either Toy Cars or Paradise Bikes to access these locations.

    Valid Options:
        - **Palm Bay Heights** Must be in Range 0 to 18
        - **Silver Lake** Must be in Range 0 to 9
        - **White Mountain** Must be in Range 0 to 10
        - **Harbor Town** Must be in Range 0 to 14
        - **Downtown Paradise** Must be in Range 0 to 13
        - **Big Surf Island** Must be in Range 0 to 12
    """
    display_name = "Road Rule for Bikes at Day Sanity"
    default = road_rule_bike_at_day_sanity_default
    min = 0
    max = 18
    cull_zeroes = False
    valid_keys = road_rule_bike_at_day_sanity_default.keys()

road_rule_bike_at_night_sanity_default = {
    AreaType.PALM_BAY_HEIGHTS.value : 0,
    AreaType.SILVER_LAKE.value : 0,
    AreaType.WHITE_MOUNTAIN.value : 0,
    AreaType.HARBOR_TOWN.value : 0,
    AreaType.DOWNTOWN_PARADISE.value : 0,
    AreaType.BIG_SURF_ISLAND.value : 0,
}

class RoadRuleBikeNightSanityCounts(OptionCounter):
    """
    Change how many Road Rules for Bikes at Night checks there are for each area. (The count goes by the placement of pins on the ingame map)
    Requires you to add either Toy Cars or Paradise Bikes to access these locations.

    Valid Options:
        - **Palm Bay Heights** Must be in Range 0 to 18
        - **Silver Lake** Must be in Range 0 to 9
        - **White Mountain** Must be in Range 0 to 10
        - **Harbor Town** Must be in Range 0 to 14
        - **Downtown Paradise** Must be in Range 0 to 13
        - **Big Surf Island** Must be in Range 0 to 12
    """
    display_name = "Road Rule for Bikes at Night Sanity"
    default = road_rule_bike_at_night_sanity_default
    min = 0
    max = 18
    cull_zeroes = False
    valid_keys = road_rule_bike_at_night_sanity_default.keys()

class DeathLink(Toggle):
    """When you crash, everyone who enabled death link dies. Of course, the reverse is true too."""
    display_name = "Death Link"
    rich_text_doc = True

class DeathLinkAmnesty(Range):
    """
    Number of deaths you require to send a death link.
    Only applies when deathlink is enabled.

    An amnesty of 1 sends every crash a death, an amnesty of 2 sends every other crash, amnesty of 3 sends every 3rd crash and so on.
    """
    range_start = 1
    range_end = 30
    default = 10
    display_name = "Death Link Amnesty"
    rich_text_doc = True

class UseWhatYouGet(Toggle):
    """When you receive a car, the game will swap to it. This will only work within Cars or within Bikes."""
    display_name = "Use The Car You Receive"
    rich_text_doc = True

class FillerItemsDistribution(ItemDict):
    """
    Change the weights of each filler

    Valid Options:
        - **Boost Refill** - Refills your Boost bar
        - **Boost Swap** - Randomizes your current Boost type. This lasts until your next car change.
        - **Car Swap** - Randomizes your current car to one you already received. Finishing an event counts as for the changed car.
    """

    default = get_default_dict()
    valid_keys = get_default_dict().keys()
    min = 0
    display_name = "Filler Weights"

    @cached_property
    def weights_pair(self) -> dict[str, int]:
        return dict(zip(self.value.keys(), accumulate(self.value.values()), strict=False))


burnout_paradise_remastered_option_groups= [
    OptionGroup("Game Options", [
        Accessibility,
        ProgressionBalancing,
        DeathLink,
        DeathLinkAmnesty,
        UseWhatYouGet,
    ]),
    OptionGroup("Goal Options", [
        LicenseGoal,
        CarCollectionGoal,
        UniqueEventWinGoals,
    ]),
    OptionGroup("Sanity Options", [
        UniqueCarWins,
        BreakableLocks,
        SmashSanityCounts,
        BillboardSanityCounts,
        SuperJumpSanityCounts,
        DriveThruSanityCounts,
        RoadRuleTimeSanityCounts,
        RoadRuleShowtimeSanityCounts,
        RoadRuleBikeDaySanityCounts,
        RoadRuleBikeNightSanityCounts,
    ]),
    OptionGroup("Item Options", [
        StarterCar,
        StartingEventAmount,
        AddLegendaryCars,
        AddOnlineCars,
        AddBoostSpecialCars,
        AddToyCars,
        AddBigSurfIslandCars,
        AddPCPDCars,
        AddParadiseBikes,
        AddLiveryItems,
        AddDriveThruAsJumpPointItems,
        FillerItemsDistribution
    ]),
]

@dataclass
class BurnoutParadiseRemasteredOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    deathlink: DeathLink
    deathlink_amnesty: DeathLinkAmnesty
    use_what_you_get: UseWhatYouGet
    license_goal: LicenseGoal
    car_goal: CarCollectionGoal
    unique_event_win_goals: UniqueEventWinGoals
    breakable_locks: BreakableLocks
    starter_car: StarterCar
    starting_event_amount: StartingEventAmount
    add_legendary_cars: AddLegendaryCars
    add_online_cars: AddOnlineCars
    add_boost_special_cars: AddBoostSpecialCars
    add_toy_cars: AddToyCars
    add_pcpd_cars: AddPCPDCars
    add_big_surf_island_cars: AddBigSurfIslandCars
    add_paradise_bikes: AddParadiseBikes
    add_livery_items: AddLiveryItems
    add_drive_thru_jump_points: AddDriveThruAsJumpPointItems
    unique_car_wins: UniqueCarWins
    smash_counts: SmashSanityCounts
    billboard_counts: BillboardSanityCounts
    super_jump_counts: SuperJumpSanityCounts
    drive_thru_counts: DriveThruSanityCounts
    road_rule_time_count: RoadRuleTimeSanityCounts
    road_rule_showtime_count: RoadRuleShowtimeSanityCounts
    road_rule_bike_day_count: RoadRuleBikeDaySanityCounts
    road_rule_bike_night_count: RoadRuleBikeNightSanityCounts
    filler_items_distribution: FillerItemsDistribution
