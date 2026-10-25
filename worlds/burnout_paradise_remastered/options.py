from itertools import accumulate
from functools import cached_property
from dataclasses import dataclass

from Options import OptionGroup, Toggle, PerGameCommonOptions, Choice, OptionCounter, ItemDict, StartInventoryPool, Range, Accessibility, ProgressionBalancing, DefaultOnToggle
from .constants import AreaType, WinType


amount_events_default = {
    "Burning Route Event" : 9,
    "Race Event" : 10,
    "Stunt Run Event" : 10,
    "Road Rage Event" : 10,
    "Marked Man Event" : 10,
    "Big Surf Island Event" : 5,
    "Burning Ride Event" : 5,
    "Midnight Ride Event" : 5,
}

class AmountOfEventsIncluded(OptionCounter):
    """
    How many events per event type do you want to include?
    Burning Routes also control how many of the base 34 Cars you can receive, in addition to your starting car.
    Atleast 1 Paradise City Car Event is expected of you to add, otherwise a random Race Event will be added.
    Atleast 4 Paradise City Car Event are expected of you to add if you want to enable any Road Rule for Time or Showtime (excluding Bike's Road Rules).

    Valid Options:
        - **Burning Route Events** Must be in Range 0 to 34
        - **Race Events** Must be in Range 0 to 40
        - **Stunt Run Events** Must be in Range 0 to 14
        - **Road Rage Events** Must be in Range 0 to 16
        - **Marked Man Events** Must be in Range 0 to 15
        - **Big Surf Island Events** Must be in Range 0 to 15
        - **Burning Ride Events** Must be in Range 0 to 19
        - **Midnight Ride Events** Must be in Range 0 to 19
    """
    display_name = "Amount of Included Events"
    default = amount_events_default
    min = 0
    max = 40
    valid_keys = amount_events_default.keys()


class LicenseGoal(Choice):
    """
    What license do you require to goal?
    If you do not include enough events for your required class, the goal license will be lowered to the highest possible one.
    If you do not include a Paradise City Car Event for D Class, then one Race Event will be added automatically.
    This is in addition to the other goal settings.

    **D Class** - 2 Event Wins = 2 Unique Events
    **C Class** - 9 Event Wins = 7 Unique Events
    **B Class** - 24 Event Wins = 15 Unique Events
    **A Class** - 50 Event Wins = 26 Unique Events
    **Burnout** - 90 Event Wins = 40 Unique Events
    **Burnout Elite** - 210 Event Wins = All 120 Events
    """
    display_name = "License Goal Class"
    option_d_class = 0
    option_c_class = 1
    option_b_class = 2
    option_a_class = 3
    option_burnout = 4
    option_burnout_elite = 5
    default = 3

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
    WinType.BIG_SURF_ISLAND_WINS.value : 0,
    WinType.BURNING_RIDE_WINS.value : 0,
    WinType.MIDNIGHT_RIDE_WINS.value : 0,
}

class UniqueEventWinGoals(OptionCounter):
    """
    How many unique wins per event type do you need to acquire to goal?
    'Amount of Included Events' will automatically be the limit for each option.
    This is in addition to the other goal settings.

    Valid Options:
        - **Unique Burning Route Wins** Must be in Range 0 to 35
        - **Unique Race Wins** Must be in Range 0 to 40
        - **Unique Stunt Run Wins** Must be in Range 0 to 14
        - **Unique Road Rage Wins** Must be in Range 0 to 16
        - **Unique Marked Man Wins** Must be in Range 0 to 15
        - **Unique Big Surf Island Wins** Must be in Range 0 to 15
        - **Unique Burning Ride Wins** Must be in Range 0 to 19
        - **Unique Midnight Ride Wins** Must be in Range 0 to 19
    """
    display_name = "Unique Event Wins Goal Amount"
    default = unique_wins_default
    min = 0
    max = 40
    valid_keys = unique_wins_default.keys()

mode_base_difficulty_default = {
    "Race": 0,
    "Stunt Run": 0,
    "Road Rage": 0,
    "Marked Man": 0,
}

class ModeBaseDifficulty(OptionCounter):
    """
    Base difficulty per event mode. The game expects you to win any event with any car. Must be in Range of 0 to 6.
    0 is the difficulty of a new game, 6 is the maximum difficulty.

    **NOTE**: Be careful! You are always expected to beat any event with any car.

    Valid Options:
        - **Race** - Increases CPU strength + rubberbanding, traffic density
        - **Stunt Run** - Increases points required, traffic density
        - **Road Rage** - Increases takedowns required, traffic density, amount of large vehicles
        - **Marked Man** - Increases Hunter Car strength, traffic density
    """
    display_name = "Mode Base Difficulty"
    default = mode_base_difficulty_default
    min = 0
    max = 6
    valid_keys = mode_base_difficulty_default.keys()

class BreakableLocks(Choice):
    """
    Lock each area's Sanity checks behind an item?
    Recommended if you have sanity options turned up.

    This reduces the amount of locations you can do right at the start down to a small amount of checks, which can help progression balancing.

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
    With how many random Paradise City Car Events do you want to start with? (Excluding your starter car)
    """
    display_name = "Starting Event Amount"
    range_start = 0
    range_end = 119
    default = 5

class AddLiveryItems(Toggle):
    """
    If enabled, adds cars' additional liveries as items. Otherwise they are unlocked upon receiving the car.
    """
    display_name = "Add Car Liveries As Items"

class AddDriveThruAsJumpPointItems(Toggle):
    """
    Use F4 to open a quick travel menu.

    If enabled, adds each Junkyard as an item. If received, allows you to teleport to said Junkyard.
    If disabled, these jump points become available as soon as you discover them by driving near them.
    """
    display_name = "Add Junkyards As Jump Points"

class AddBurningRouteRewardsCars(Range):
    """
    How many Burning Route Reward cars to add as unlockable items?
    **Note:** This will also affect how many Paradise Cars there are in the item pool for the goal of collecting cars.
    """
    display_name = "Add Burning Route Reward Cars"
    range_start = 0
    range_end = 35
    default = 10

class AddCarbonCars(Range):
    """
    How many Carbon cars to add as unlockable items?
    **Note:** This will also affect how many Paradise Cars there are in the item pool for the goal of collecting cars.
    """
    display_name = "Add Carbon Cars"
    range_start = 0
    range_end = 6
    default = 3

class AddLegendaryCars(Range):
    """
    How many Legendary cars to add as unlockable items?
    """
    display_name = "Add Legendary Cars"
    range_start = 0
    range_end = 4
    default = 2

class AddOnlineCars(Range):
    """
    How many Online cars to add as unlockable items?
    """
    display_name = "Add Online Cars"
    range_start = 0
    range_end = 2
    default = 1

class AddBoostSpecialCars(Range):
    """
    How many Boost Special cars to add as unlockable items?
    """
    display_name = "Add Boost Special Cars"
    range_start = 0
    range_end = 2
    default = 1

class AddToyCars(Range):
    """
    How many Toy cars to add as unlockable items?
    """
    display_name = "Add Toy Cars"
    range_start = 0
    range_end = 9
    default = 5

class AddParadiseBikes(Range):
    """
    How many Paradise bikes to add as unlockable items?
    """
    display_name = "Add Paradise Bikes"
    range_start = 0
    range_end = 4
    default = 2

class AddBigSurfIslandCars(Range):
    """
    How many Big Surf Island cars to add as unlockable items?
    """
    display_name = "Add Big Surf Island Cars"
    range_start = 0
    range_end = 9
    default = 5

class AddPCPDCars(Range):
    """
    How many PCPD police cars to add as unlockable items?
    """
    display_name = "Add PCPD Cars"
    range_start = 0
    range_end = 33
    default = 10

class CacheBreakableLocations(DefaultOnToggle):
    """
    While Areas are locked, the games saves what Breakable you have gotten, releasing them all at once when the area becomes unlocked.
    Disabling this makes Area/Type unlocks feel like real unlocks, but also increases the play length considerably.

    This option applies to Smashes, Billboard, Super/Mega Jumps and Drive-Thrus. Other Sanities are all cached.
    If disabled, Drive-Thrus will still be revealed on the map when discovering for the first time, but need to be revisited for the locations to send.

    **NOTE:** You may want to restart the game to restore the state of smash gates and billboards after you unlock them, otherwise they may either show as missing or as broken.
    """
    display_name = "Cache Breakable Discoveries"

class UniqueEventWins(Choice):
    """
    Control whether each event sends a location specifically for its event, or its event type.
    Grouping allows for a more free choice of events when going for such locations.

    **Each Event Its Own** - Every event has its own location for winning.
    **Grouped By Event Type** - Each unique event win now increments its event type category instead. There are seven groups: Burning Route, Race, Stunt Run, Road Rage, Marked Man, Burning Ride, Midnight Ride
    """
    option_each_event_its_own = 0
    option_grouped_by_event_type = 1
    default = 0
    display_name = "Group Unique Event Wins"
    rich_text_doc = True

class UniqueCarWins(Choice):
    """
    Enable locations for wins with each included vehicle available. If a car is still missing a win, it will be slightly damaged when initially loading the game and when receiving new cars.
    Grouping allows for more freedom in choosing what car to win with next.

    **None** - No car wins are included as locations.
    **Each Car Its Own** - Every vehicle has its own location for winning.
    **Grouped By Boost Type** - Each unique car win now increments its boost type category instead. There are four groups: Speed, Crash, Stunt and Special.
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
    AreaType.BIG_SURF_ISLAND.value : 3,
}

class DriveThruSanityCounts(OptionCounter):
    """
    Change how many Drive-Thru (Junkyards, Gas Stations, Auto Repairs, Paint Shops, Parking Garages) checks there are for each area.

    **Note:** On Big Surf Island, both the Junkyard and the Auto Repair don't count for this

    Valid Options:
        - **Palm Bay Heights** Must be in Range 0 to 10
        - **Silver Lake** Must be in Range 0 to 7
        - **White Mountain** Must be in Range 0 to 7
        - **Harbor Town** Must be in Range 0 to 10
        - **Downtown Paradise** Must be in Range 0 to 12
        - **Big Surf Island** Must be in Range 0 to 3
    """
    display_name = "Drive-Thru Sanity"
    default = drivethru_sanity_default
    min = 0
    max = 12
    cull_zeroes = False
    valid_keys = drivethru_sanity_default.keys()

road_rule_time_sanity_default = {
    AreaType.PALM_BAY_HEIGHTS.value : 0,
    AreaType.SILVER_LAKE.value : 0,
    AreaType.WHITE_MOUNTAIN.value : 0,
    AreaType.HARBOR_TOWN.value : 0,
    AreaType.DOWNTOWN_PARADISE.value : 0,
    AreaType.BIG_SURF_ISLAND.value : 0,
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
        - **Palm Bay Heights** Must be in Range 0 to 19
        - **Silver Lake** Must be in Range 0 to 9
        - **White Mountain** Must be in Range 0 to 11
        - **Harbor Town** Must be in Range 0 to 13
        - **Downtown Paradise** Must be in Range 0 to 12
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
    """
    When you crash, everyone who enabled death link dies. Of course, the reverse is true too.
    This can be adjusted in the game's F3 config manager. (Slot data takes precedence when logging into an AP World)
    """
    display_name = "Death Link"
    rich_text_doc = True

class DeathLinkAmnesty(Range):
    """
    Number of deaths you require to send a death link. Only applies when deathlink is enabled.
    This can be adjusted in the game's F3 config manager. (Slot data takes precedence when logging into an AP World)

    An amnesty of 1 sends every crash a death, an amnesty of 2 sends every other crash, amnesty of 3 sends every 3rd crash and so on.
    """
    range_start = 1
    range_end = 30
    default = 10
    display_name = "Death Link Amnesty"
    rich_text_doc = True

class UseWhatYouGet(Toggle):
    """
    While outside an event, swaps your current car when you receive a new one. This will only work within Cars or within Bikes.
    This can be adjusted in the game's F3 config manager. (Slot data takes precedence when logging into an AP World)
    """
    display_name = "Use The Car You Receive"
    rich_text_doc = True

class FinishedEventsStayFinished(DefaultOnToggle):
    """
    When you finish an event, its finished state won't reset on upgrading your license. The events keep counting towards the next license.
    Disabling this setting makes the playthrough feel more like the original game, having to beat each event again to progress the license.
    You will also have to keep track of what events you have done as to complete the 'beat each event once' locations.

    This setting is recommended for Syncs and casual play.
    """
    display_name = "Finished Events Stay Finished"
    rich_text_doc = True

filler_default_dict = {
    "Boost Refill": 50,
    "Boost Swap": 25,
    "Car Swap": 10,
    "High Traffic Density": 25,
    "Random Junkyard Teleport": 5,
}
class FillerItemsDistribution(ItemDict):
    """
    Change the weights of each filler

    Valid Options:
        - **Boost Refill** - Refills your Boost bar
        - **Boost Swap** - Randomizes your current Boost type. This lasts until your next car change.
        - **Car Swap** - Randomizes your current car to one you already received. This can only occure outside of an event.
        - **Random Junkyard Teleport** - Teleports you to a random junkyard, regardless of if you are in an event or not.
        - **High Traffic Density** - Drastically increases the amount of cars on the street for the next 60 seconds.
    """

    default = filler_default_dict.copy()
    valid_keys = filler_default_dict.keys()
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
        FinishedEventsStayFinished,
        CacheBreakableLocations,
        ModeBaseDifficulty,
    ]),
    OptionGroup("Goal Options", [
        AmountOfEventsIncluded,
        LicenseGoal,
        CarCollectionGoal,
        UniqueEventWinGoals,
    ]),
    OptionGroup("Sanity Options", [
        # AddBikeEventsAsLocations,
        UniqueEventWins,
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
        AddBurningRouteRewardsCars,
        AddCarbonCars,
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
    amount_events: AmountOfEventsIncluded
    cache_breakable_locations: CacheBreakableLocations
    finished_events_stay_finished: FinishedEventsStayFinished
    license_goal: LicenseGoal
    car_goal: CarCollectionGoal
    unique_event_win_goals: UniqueEventWinGoals
    breakable_locks: BreakableLocks
    mode_base_difficulty: ModeBaseDifficulty
    starter_car: StarterCar
    starting_event_amount: StartingEventAmount
    add_burning_route_reward_cars: AddBurningRouteRewardsCars
    add_carbon_cars: AddCarbonCars
    add_legendary_cars: AddLegendaryCars
    add_online_cars: AddOnlineCars
    add_boost_special_cars: AddBoostSpecialCars
    add_toy_cars: AddToyCars
    add_pcpd_cars: AddPCPDCars
    add_big_surf_island_cars: AddBigSurfIslandCars
    add_paradise_bikes: AddParadiseBikes
    add_livery_items: AddLiveryItems
    add_drive_thru_jump_points: AddDriveThruAsJumpPointItems
    unique_event_wins: UniqueEventWins
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
