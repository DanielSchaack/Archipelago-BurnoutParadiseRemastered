from itertools import accumulate
from functools import cached_property
from dataclasses import dataclass

from Options import OptionGroup, Toggle, PerGameCommonOptions, Choice, OptionCounter, ItemDict, StartInventoryPool, Range
from .constants import AreaType
from .data.items.filler import get_default_dict


class Goal(Choice):
    """
    Goal

    License Level: Reach the Specified License
    """
    #Collect Cars: Collect the specified amount of cars. This is a mc-guffin hunt
    display_name = "Goal"
    option_license_level = 0
    # option_collect_cars = 1
    default = 0

class LicenseGoal(Choice):
    """
    If on License Level Goal, What license is your goal?

    **C Class** - 9 Event Wins
    **B Class** - 24 Event Wins
    **A Class** - 50 Event Wins
    **Burnout** - 90 Event Wins
    **Burnout Elite** - 210 Event Wins
    """
    display_name = "License Goal"
    option_c_class = 0
    option_b_class = 1
    option_a_class = 2
    option_burnout = 3
    option_burnout_elite = 4
    default = 1

# class CarCollectionGoal(Range):
#     """
#     If on Car Collection Goal, how many cars do you need to goal?
#     """
#     display_name = "Car Goal Amount"
#     range_start = 10
#     range_end = 75
#     default = 0

class BreakableLocks(Choice):
    """
    Lock each area's Sanity checks behind an item?

    This reduces sphere 1 down to a small amount of checks, which can help progression balancing.

    Recommended if you have sanity options turned up.

    **All Unlocked From The Start** - All Smashes, Billboards and Super/Mega Jumps are available from the Start
    **Locked By Area** - Smashes, Billboards and Super/Mega Jumps are locked behind regional items, all 3 types becoming available all at once per area
    **Locked By Area And Type** - Smashes, Billboards and Super/Mega Jumps are locked behind individual regional items, becoming available per area per type
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


class FillerItemsDistribution(ItemDict):
    """
    Change the weights of each filler

    Valid Options:
        - **Boost** - Refills your Boost bar
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
        DeathLink,
        DeathLinkAmnesty,
    ]),
    OptionGroup("Goal Options", [
        Goal,
        LicenseGoal,
        # CarCollectionGoal,
    ]),
    OptionGroup("Item Options", [
        StarterCar,
        StartingEventAmount,
        AddLiveryItems,
        FillerItemsDistribution
    ]),
    OptionGroup("Sanity Options", [
        BreakableLocks,
        SmashSanityCounts,
        BillboardSanityCounts,
        SuperJumpSanityCounts,
    ])
]

@dataclass
class BurnoutParadiseRemasteredOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    deathlink: DeathLink
    deathlink_amnesty: DeathLinkAmnesty
    goal: Goal
    license_goal: LicenseGoal
    # car_goal: CarCollectionGoal
    breakable_locks: BreakableLocks
    starter_car: StarterCar
    starting_event_amount: StartingEventAmount
    add_livery_items: AddLiveryItems
    smash_counts: SmashSanityCounts
    billboard_counts: BillboardSanityCounts
    super_jump_counts: SuperJumpSanityCounts
    filler_items_distribution: FillerItemsDistribution
