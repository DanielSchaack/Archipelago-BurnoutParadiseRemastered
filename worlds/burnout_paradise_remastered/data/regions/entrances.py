from BaseClasses import EntranceType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has
from .. import EntranceTypeEnum
from ..items.blockers import Blockers
from ..items.discoverables import Discoverables
from ..regions.regions import Regions
from ...options import BreakableLocks


class Entrances(EntranceTypeEnum):
    DOWNTOWN_PARADISE_TO_PALM_BAY_HEIGHTS = (
        "Downtown Paradise To Palm Bay Heights",
        Regions.DOWNTOWN_PARADISE,
        Regions.PALM_BAY_HEIGHTS,
        EntranceType.TWO_WAY,
    )

    DOWNTOWN_PARADISE_TO_HARBOR_TOWN = (
        "Downtown Paradise To Harbor Town",
        Regions.DOWNTOWN_PARADISE,
        Regions.HARBOR_TOWN,
        EntranceType.TWO_WAY,
    )

    DOWNTOWN_PARADISE_TO_BIG_SURF_ISLAND = (
        "Downtown Paradise To Big Surf Island",
        Regions.DOWNTOWN_PARADISE,
        Regions.BIG_SURF_ISLAND,
        EntranceType.TWO_WAY,
    )

    PALM_BAY_HEIGHTS_TO_SILVER_LAKE = (
        "Palm Bay Heights To Silver Lake",
        Regions.PALM_BAY_HEIGHTS,
        Regions.SILVER_LAKE,
        EntranceType.TWO_WAY,
    )


    PALM_BAY_HEIGHTS_TO_HARBOR_TOWN = (
        "Palm Bay Heights To Harbor Town",
        Regions.PALM_BAY_HEIGHTS,
        Regions.HARBOR_TOWN,
        EntranceType.TWO_WAY,
    )

    SILVER_LAKE_TO_WHITE_MOUNTAIN = (
        "Silver Lake To White Mountain",
        Regions.SILVER_LAKE,
        Regions.WHITE_MOUNTAIN,
        EntranceType.TWO_WAY,
    )

    SILVER_LAKE_TO_HARBOR_TOWN = (
        "Silver Lake To Harbor Town",
        Regions.SILVER_LAKE,
        Regions.HARBOR_TOWN,
        EntranceType.TWO_WAY,
    )

    WHITE_MOUNTAIN_TO_HARBOR_TOWN = (
        "White Mountain To Harbor Town",
        Regions.WHITE_MOUNTAIN,
        Regions.HARBOR_TOWN,
        EntranceType.TWO_WAY,
    )

    DOWNTOWN_PARADISE_TO_BREAKABLES = (
        "Downtown Paradise To Downtown Paradise Breakables",
        Regions.DOWNTOWN_PARADISE,
        Regions.DOWNTOWN_PARADISE_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.DOWNTOWN_PARADISE.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area)], filtered_resolution=True),
    )

    PALM_BAY_HEIGHTS_TO_BREAKABLES = (
        "Palm Bay Heights To Palm Bay Heights Breakables",
        Regions.PALM_BAY_HEIGHTS,
        Regions.PALM_BAY_HEIGHTS_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.PALM_BAY_HEIGHTS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area)], filtered_resolution=True),
    )

    SILVER_LAKE_TO_BREAKABLES = (
        "Silver Lake To Silver Lake Breakables",
        Regions.SILVER_LAKE,
        Regions.SILVER_LAKE_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.SILVER_LAKE.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area)], filtered_resolution=True),
    )

    WHITE_MOUNTAIN_TO_BREAKABLES = (
        "White Mountain To White Mountain Breakables",
        Regions.WHITE_MOUNTAIN,
        Regions.WHITE_MOUNTAIN_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.WHITE_MOUNTAIN.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area)], filtered_resolution=True),
    )

    HARBOR_TOWN_TO_BREAKABLES = (
        "Harbor Town To Harbor Town Breakables",
        Regions.HARBOR_TOWN,
        Regions.HARBOR_TOWN_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.HARBOR_TOWN.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area)], filtered_resolution=True),
    )

    BIG_SURF_ISLAND_TO_BREAKABLES = (
        "Big Surf Island To Big Surf Island Breakables",
        Regions.BIG_SURF_ISLAND,
        Regions.BIG_SURF_ISLAND_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.BIG_SURF_ISLAND.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area)], filtered_resolution=True),
    )


    PALM_BAY_HEIGHTS_TO_SMASHES = (
        "Palm Bay Heights To Palm Bay Heights Smashes",
        Regions.PALM_BAY_HEIGHTS,
        Regions.PALM_BAY_HEIGHTS_SMASHES,
        EntranceType.TWO_WAY,
        Has(Discoverables.PALM_BAY_HEIGHTS_SMASHES.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    SILVER_LAKE_TO_SMASHES = (
        "Silver Lake To Silver Lake Smashes",
        Regions.SILVER_LAKE,
        Regions.SILVER_LAKE_SMASHES,
        EntranceType.TWO_WAY,
        Has(Discoverables.SILVER_LAKE_SMASHES.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    WHITE_MOUNTAIN_TO_SMASHES = (
        "White Mountain To White Mountain Smashes",
        Regions.WHITE_MOUNTAIN,
        Regions.WHITE_MOUNTAIN_SMASHES,
        EntranceType.TWO_WAY,
        Has(Discoverables.WHITE_MOUNTAIN_SMASHES.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    HARBOR_TOWN_TO_SMASHES = (
        "Harbor Town To Harbor Town Smashes",
        Regions.HARBOR_TOWN,
        Regions.HARBOR_TOWN_SMASHES,
        EntranceType.TWO_WAY,
        Has(Discoverables.HARBOR_TOWN_SMASHES.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    DOWNTOWN_PARADISE_TO_SMASHES = (
        "Downtown Paradise To Downtown Paradise Smashes",
        Regions.DOWNTOWN_PARADISE,
        Regions.DOWNTOWN_PARADISE_SMASHES,
        EntranceType.TWO_WAY,
        Has(Discoverables.DOWNTOWN_PARADISE_SMASHES.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    BIG_SURF_ISLAND_TO_SMASHES = (
        "Big Surf Island To Big Surf Island Smashes",
        Regions.BIG_SURF_ISLAND,
        Regions.BIG_SURF_ISLAND_SMASHES,
        EntranceType.TWO_WAY,
        Has(Discoverables.BIG_SURF_ISLAND_SMASHES.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )

    PALM_BAY_HEIGHTS_TO_BILLBOARDS = (
        "Palm Bay Heights To Palm Bay Heights Billboards",
        Regions.PALM_BAY_HEIGHTS,
        Regions.PALM_BAY_HEIGHTS_BILLBOARDS,
        EntranceType.TWO_WAY,
        Has(Discoverables.PALM_BAY_HEIGHTS_BILLBOARDS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    SILVER_LAKE_TO_BILLBOARDS = (
        "Silver Lake To Silver Lake Billboards",
        Regions.SILVER_LAKE,
        Regions.SILVER_LAKE_BILLBOARDS,
        EntranceType.TWO_WAY,
        Has(Discoverables.SILVER_LAKE_BILLBOARDS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    WHITE_MOUNTAIN_TO_BILLBOARDS = (
        "White Mountain To White Mountain Billboards",
        Regions.WHITE_MOUNTAIN,
        Regions.WHITE_MOUNTAIN_BILLBOARDS,
        EntranceType.TWO_WAY,
        Has(Discoverables.WHITE_MOUNTAIN_BILLBOARDS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    HARBOR_TOWN_TO_BILLBOARDS = (
        "Harbor Town To Harbor Town Billboards",
        Regions.HARBOR_TOWN,
        Regions.HARBOR_TOWN_BILLBOARDS,
        EntranceType.TWO_WAY,
        Has(Discoverables.HARBOR_TOWN_BILLBOARDS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    DOWNTOWN_PARADISE_TO_BILLBOARDS = (
        "Downtown Paradise To Downtown Paradise Billboards",
        Regions.DOWNTOWN_PARADISE,
        Regions.DOWNTOWN_PARADISE_BILLBOARDS,
        EntranceType.TWO_WAY,
        Has(Discoverables.DOWNTOWN_PARADISE_BILLBOARDS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    BIG_SURF_ISLAND_TO_BILLBOARDS = (
        "Big Surf Island To Big Surf Island Billboards",
        Regions.BIG_SURF_ISLAND,
        Regions.BIG_SURF_ISLAND_BILLBOARDS,
        EntranceType.TWO_WAY,
        Has(Discoverables.BIG_SURF_ISLAND_BILLBOARDS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )

    # --- Jumps ---
    PALM_BAY_HEIGHTS_TO_SUPER_JUMPS = (
        "Palm Bay Heights To Palm Bay Heights Super Jumps",
        Regions.PALM_BAY_HEIGHTS,
        Regions.PALM_BAY_HEIGHTS_SUPER_JUMPS,
        EntranceType.TWO_WAY,
        Has(Discoverables.PALM_BAY_HEIGHTS_SUPER_JUMPS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    SILVER_LAKE_TO_SUPER_JUMPS = (
        "Silver Lake To Silver Lake Super Jumps",
        Regions.SILVER_LAKE,
        Regions.SILVER_LAKE_SUPER_JUMPS,
        EntranceType.TWO_WAY,
        Has(Discoverables.SILVER_LAKE_SUPER_JUMPS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    WHITE_MOUNTAIN_TO_SUPER_JUMPS = (
        "White Mountain To White Mountain Super Jumps",
        Regions.WHITE_MOUNTAIN,
        Regions.WHITE_MOUNTAIN_SUPER_JUMPS,
        EntranceType.TWO_WAY,
        Has(Discoverables.WHITE_MOUNTAIN_SUPER_JUMPS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    HARBOR_TOWN_TO_SUPER_JUMPS = (
        "Harbor Town To Harbor Town Super Jumps",
        Regions.HARBOR_TOWN,
        Regions.HARBOR_TOWN_SUPER_JUMPS,
        EntranceType.TWO_WAY,
        Has(Discoverables.HARBOR_TOWN_SUPER_JUMPS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    DOWNTOWN_PARADISE_TO_SUPER_JUMPS = (
        "Downtown Paradise To Downtown Paradise Super Jumps",
        Regions.DOWNTOWN_PARADISE,
        Regions.DOWNTOWN_PARADISE_SUPER_JUMPS,
        EntranceType.TWO_WAY,
        Has(Discoverables.DOWNTOWN_PARADISE_SUPER_JUMPS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )
    BIG_SURF_ISLAND_TO_MEGA_JUMPS = (
        "Big Surf Island To Big Surf Island Mega Jumps",
        Regions.BIG_SURF_ISLAND,
        Regions.BIG_SURF_ISLAND_MEGA_JUMPS,
        EntranceType.TWO_WAY,
        Has(Discoverables.BIG_SURF_ISLAND_MEGA_JUMPS.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True),
    )

base_entrances = [
    Entrances.DOWNTOWN_PARADISE_TO_PALM_BAY_HEIGHTS,
    Entrances.DOWNTOWN_PARADISE_TO_HARBOR_TOWN,
    Entrances.DOWNTOWN_PARADISE_TO_BIG_SURF_ISLAND,
    Entrances.PALM_BAY_HEIGHTS_TO_SILVER_LAKE,
    Entrances.PALM_BAY_HEIGHTS_TO_HARBOR_TOWN,
    Entrances.SILVER_LAKE_TO_WHITE_MOUNTAIN,
    Entrances.SILVER_LAKE_TO_HARBOR_TOWN,
    Entrances.WHITE_MOUNTAIN_TO_HARBOR_TOWN,
]

breakable_entrances = [
    Entrances.DOWNTOWN_PARADISE_TO_BREAKABLES,
    Entrances.PALM_BAY_HEIGHTS_TO_BREAKABLES,
    Entrances.SILVER_LAKE_TO_BREAKABLES,
    Entrances.WHITE_MOUNTAIN_TO_BREAKABLES,
    Entrances.HARBOR_TOWN_TO_BREAKABLES,
    Entrances.BIG_SURF_ISLAND_TO_BREAKABLES,
]

smash_entrances = [
    Entrances.PALM_BAY_HEIGHTS_TO_SMASHES,
    Entrances.SILVER_LAKE_TO_SMASHES,
    Entrances.WHITE_MOUNTAIN_TO_SMASHES,
    Entrances.HARBOR_TOWN_TO_SMASHES,
    Entrances.DOWNTOWN_PARADISE_TO_SMASHES,
    Entrances.BIG_SURF_ISLAND_TO_SMASHES,
]

billboard_entrances = [
    Entrances.PALM_BAY_HEIGHTS_TO_BILLBOARDS,
    Entrances.SILVER_LAKE_TO_BILLBOARDS,
    Entrances.WHITE_MOUNTAIN_TO_BILLBOARDS,
    Entrances.HARBOR_TOWN_TO_BILLBOARDS,
    Entrances.DOWNTOWN_PARADISE_TO_BILLBOARDS,
    Entrances.BIG_SURF_ISLAND_TO_BILLBOARDS,
]

jump_entrances = [
    Entrances.PALM_BAY_HEIGHTS_TO_SUPER_JUMPS,
    Entrances.SILVER_LAKE_TO_SUPER_JUMPS,
    Entrances.WHITE_MOUNTAIN_TO_SUPER_JUMPS,
    Entrances.HARBOR_TOWN_TO_SUPER_JUMPS,
    Entrances.DOWNTOWN_PARADISE_TO_SUPER_JUMPS,
    Entrances.BIG_SURF_ISLAND_TO_MEGA_JUMPS,
]
