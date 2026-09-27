from itertools import accumulate
from functools import cached_property
from dataclasses import dataclass

from Options import OptionGroup, Toggle, PerGameCommonOptions, Choice, OptionCounter, ItemDict, StartInventoryPool
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
        FillerItemsDistribution
    ]),
    OptionGroup("Goal Options", [
        Goal,
        LicenseGoal,
        # CarCollectionGoal,
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
    goal: Goal
    license_goal: LicenseGoal
    # car_goal: CarCollectionGoal
    breakable_locks: BreakableLocks
    smash_counts: SmashSanityCounts
    billboard_counts: BillboardSanityCounts
    super_jump_counts: SuperJumpSanityCounts
    filler_items_distribution: FillerItemsDistribution
