from worlds.burnout_paradise_remastered.data.rules.state_rules import HasEventWins
from BaseClasses import EntranceType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasGroup
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

    PALM_BAY_HEIGHTS_TO_DRIVETHRUS = (
        "Palm Bay Heights To Palm Bay Heights Drivethrus",
        Regions.PALM_BAY_HEIGHTS,
        Regions.PALM_BAY_HEIGHTS_DRIVETHRUS,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.PALM_BAY_HEIGHTS_DRIVETHRUS.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        ),
    )
    SILVER_LAKE_TO_DRIVETHRUS = (
        "Silver Lake To Silver Lake Drivethrus",
        Regions.SILVER_LAKE,
        Regions.SILVER_LAKE_DRIVETHRUS,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.SILVER_LAKE_DRIVETHRUS.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        ),
    )
    WHITE_MOUNTAIN_TO_DRIVETHRUS = (
        "White Mountain To White Mountain Drivethrus",
        Regions.WHITE_MOUNTAIN,
        Regions.WHITE_MOUNTAIN_DRIVETHRUS,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.WHITE_MOUNTAIN_DRIVETHRUS.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        ),
    )
    HARBOR_TOWN_TO_DRIVETHRUS = (
        "Harbor Town To Harbor Town Drivethrus",
        Regions.HARBOR_TOWN,
        Regions.HARBOR_TOWN_DRIVETHRUS,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.HARBOR_TOWN_DRIVETHRUS.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        ),
    )
    DOWNTOWN_PARADISE_TO_DRIVETHRUS = (
        "Downtown Paradise To Downtown Paradise Drivethrus",
        Regions.DOWNTOWN_PARADISE,
        Regions.DOWNTOWN_PARADISE_DRIVETHRUS,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.DOWNTOWN_PARADISE_DRIVETHRUS.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        ),
    )
    BIG_SURF_ISLAND_TO_DRIVETHRUS = (
        "Big Surf Island To Big Surf Island Drivethrus",
        Regions.BIG_SURF_ISLAND,
        Regions.BIG_SURF_ISLAND_DRIVETHRUS,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.BIG_SURF_ISLAND_DRIVETHRUS.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        ),
    )

    PALM_BAY_HEIGHTS_TO_ROADRULE_TIME = (
        "Palm Bay Heights To Palm Bay Heights Road Rule Time",
        Regions.PALM_BAY_HEIGHTS,
        Regions.PALM_BAY_HEIGHTS_ROADRULE_TIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.PALM_BAY_HEIGHTS_ROADRULE_TIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )
    SILVER_LAKE_TO_ROADRULE_TIME = (
        "Silver Lake To Silver Lake Road Rule Time",
        Regions.SILVER_LAKE,
        Regions.SILVER_LAKE_ROADRULE_TIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.SILVER_LAKE_ROADRULE_TIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )
    WHITE_MOUNTAIN_TO_ROADRULE_TIME = (
        "White Mountain To White Mountain Road Rule Time",
        Regions.WHITE_MOUNTAIN,
        Regions.WHITE_MOUNTAIN_ROADRULE_TIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.WHITE_MOUNTAIN_ROADRULE_TIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )
    HARBOR_TOWN_TO_ROADRULE_TIME = (
        "Harbor Town To Harbor Town Road Rule Time",
        Regions.HARBOR_TOWN,
        Regions.HARBOR_TOWN_ROADRULE_TIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.HARBOR_TOWN_ROADRULE_TIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )
    DOWNTOWN_PARADISE_TO_ROADRULE_TIME = (
        "Downtown Paradise To Downtown Paradise Road Rule Time",
        Regions.DOWNTOWN_PARADISE,
        Regions.DOWNTOWN_PARADISE_ROADRULE_TIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.DOWNTOWN_PARADISE_ROADRULE_TIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )
    BIG_SURF_ISLAND_TO_ROADRULE_TIME = (
        "Big Surf Island To Big Surf Island Road Rule Time",
        Regions.BIG_SURF_ISLAND,
        Regions.BIG_SURF_ISLAND_ROADRULE_TIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.BIG_SURF_ISLAND_ROADRULE_TIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )

    PALM_BAY_HEIGHTS_TO_ROADRULE_SHOWTIME = (
        "Palm Bay Heights To Palm Bay Heights Road Rule Showtime",
        Regions.PALM_BAY_HEIGHTS,
        Regions.PALM_BAY_HEIGHTS_ROADRULE_SHOWTIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.PALM_BAY_HEIGHTS_ROADRULE_SHOWTIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )
    SILVER_LAKE_TO_ROADRULE_SHOWTIME = (
        "Silver Lake To Silver Lake Road Rule Showtime",
        Regions.SILVER_LAKE,
        Regions.SILVER_LAKE_ROADRULE_SHOWTIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.SILVER_LAKE_ROADRULE_SHOWTIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )
    WHITE_MOUNTAIN_TO_ROADRULE_SHOWTIME = (
        "White Mountain To White Mountain Road Rule Showtime",
        Regions.WHITE_MOUNTAIN,
        Regions.WHITE_MOUNTAIN_ROADRULE_SHOWTIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.WHITE_MOUNTAIN_ROADRULE_SHOWTIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )
    HARBOR_TOWN_TO_ROADRULE_SHOWTIME = (
        "Harbor Town To Harbor Town Road Rule Showtime",
        Regions.HARBOR_TOWN,
        Regions.HARBOR_TOWN_ROADRULE_SHOWTIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.HARBOR_TOWN_ROADRULE_SHOWTIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )
    DOWNTOWN_PARADISE_TO_ROADRULE_SHOWTIME = (
        "Downtown Paradise To Downtown Paradise Road Rule Showtime",
        Regions.DOWNTOWN_PARADISE,
        Regions.DOWNTOWN_PARADISE_ROADRULE_SHOWTIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.DOWNTOWN_PARADISE_ROADRULE_SHOWTIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )
    BIG_SURF_ISLAND_TO_ROADRULE_SHOWTIME = (
        "Big Surf Island To Big Surf Island Road Rule Showtime",
        Regions.BIG_SURF_ISLAND,
        Regions.BIG_SURF_ISLAND_ROADRULE_SHOWTIME,
        EntranceType.TWO_WAY,
        Has(Discoverables.BIG_SURF_ISLAND_ROADRULE_SHOWTIME.value, options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)], filtered_resolution=True)
        & HasEventWins(wins=4)
    )

    PALM_BAY_HEIGHTS_TO_ROADRULE_BIKES_DAY = (
        "Palm Bay Heights To Palm Bay Heights Road Rule Bikes Day",
        Regions.PALM_BAY_HEIGHTS,
        Regions.PALM_BAY_HEIGHTS_ROADRULE_BIKES_DAY,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.PALM_BAY_HEIGHTS_ROADRULE_BIKES_DAY.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )
    SILVER_LAKE_TO_ROADRULE_BIKES_DAY = (
        "Silver Lake To Silver Lake Road Rule Bikes Day",
        Regions.SILVER_LAKE,
        Regions.SILVER_LAKE_ROADRULE_BIKES_DAY,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.SILVER_LAKE_ROADRULE_BIKES_DAY.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )
    WHITE_MOUNTAIN_TO_ROADRULE_BIKES_DAY = (
        "White Mountain To White Mountain Road Rule Bikes Day",
        Regions.WHITE_MOUNTAIN,
        Regions.WHITE_MOUNTAIN_ROADRULE_BIKES_DAY,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.WHITE_MOUNTAIN_ROADRULE_BIKES_DAY.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )
    HARBOR_TOWN_TO_ROADRULE_BIKES_DAY = (
        "Harbor Town To Harbor Town Road Rule Bikes Day",
        Regions.HARBOR_TOWN,
        Regions.HARBOR_TOWN_ROADRULE_BIKES_DAY,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.HARBOR_TOWN_ROADRULE_BIKES_DAY.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )
    DOWNTOWN_PARADISE_TO_ROADRULE_BIKES_DAY = (
        "Downtown Paradise To Downtown Paradise Road Rule Bikes Day",
        Regions.DOWNTOWN_PARADISE,
        Regions.DOWNTOWN_PARADISE_ROADRULE_BIKES_DAY,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.DOWNTOWN_PARADISE_ROADRULE_BIKES_DAY.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )
    BIG_SURF_ISLAND_TO_ROADRULE_BIKES_DAY = (
        "Big Surf Island To Big Surf Island Road Rule Bikes Day",
        Regions.BIG_SURF_ISLAND,
        Regions.BIG_SURF_ISLAND_ROADRULE_BIKES_DAY,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.BIG_SURF_ISLAND_ROADRULE_BIKES_DAY.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )

    PALM_BAY_HEIGHTS_TO_ROADRULE_BIKES_NIGHT = (
        "Palm Bay Heights To Palm Bay Heights Road Rule Bikes Night",
        Regions.PALM_BAY_HEIGHTS,
        Regions.PALM_BAY_HEIGHTS_ROADRULE_BIKES_NIGHT,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.PALM_BAY_HEIGHTS_ROADRULE_BIKES_NIGHT.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )
    SILVER_LAKE_TO_ROADRULE_BIKES_NIGHT = (
        "Silver Lake To Silver Lake Road Rule Bikes Night",
        Regions.SILVER_LAKE,
        Regions.SILVER_LAKE_ROADRULE_BIKES_NIGHT,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.SILVER_LAKE_ROADRULE_BIKES_NIGHT.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )
    WHITE_MOUNTAIN_TO_ROADRULE_BIKES_NIGHT = (
        "White Mountain To White Mountain Road Rule Bikes Night",
        Regions.WHITE_MOUNTAIN,
        Regions.WHITE_MOUNTAIN_ROADRULE_BIKES_NIGHT,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.WHITE_MOUNTAIN_ROADRULE_BIKES_NIGHT.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )
    HARBOR_TOWN_TO_ROADRULE_BIKES_NIGHT = (
        "Harbor Town To Harbor Town Road Rule Bikes Night",
        Regions.HARBOR_TOWN,
        Regions.HARBOR_TOWN_ROADRULE_BIKES_NIGHT,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.HARBOR_TOWN_ROADRULE_BIKES_NIGHT.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )
    DOWNTOWN_PARADISE_TO_ROADRULE_BIKES_NIGHT = (
        "Downtown Paradise To Downtown Paradise Road Rule Bikes Night",
        Regions.DOWNTOWN_PARADISE,
        Regions.DOWNTOWN_PARADISE_ROADRULE_BIKES_NIGHT,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.DOWNTOWN_PARADISE_ROADRULE_BIKES_NIGHT.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
    )
    BIG_SURF_ISLAND_TO_ROADRULE_BIKES_NIGHT = (
        "Big Surf Island To Big Surf Island Road Rule Bikes Night",
        Regions.BIG_SURF_ISLAND,
        Regions.BIG_SURF_ISLAND_ROADRULE_BIKES_NIGHT,
        EntranceType.TWO_WAY,
        Has(
            Discoverables.BIG_SURF_ISLAND_ROADRULE_BIKES_NIGHT.value,
            options=[OptionFilter(BreakableLocks, BreakableLocks.option_locked_by_area_and_type)],
            filtered_resolution=True,
        )
        & HasGroup("Bike"),
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

drivethru_entrances = [
    Entrances.PALM_BAY_HEIGHTS_TO_DRIVETHRUS,
    Entrances.SILVER_LAKE_TO_DRIVETHRUS,
    Entrances.WHITE_MOUNTAIN_TO_DRIVETHRUS,
    Entrances.HARBOR_TOWN_TO_DRIVETHRUS,
    Entrances.DOWNTOWN_PARADISE_TO_DRIVETHRUS,
    Entrances.BIG_SURF_ISLAND_TO_DRIVETHRUS,
]

roadrules_time_entrances = [
    Entrances.PALM_BAY_HEIGHTS_TO_ROADRULE_TIME,
    Entrances.SILVER_LAKE_TO_ROADRULE_TIME,
    Entrances.WHITE_MOUNTAIN_TO_ROADRULE_TIME,
    Entrances.HARBOR_TOWN_TO_ROADRULE_TIME,
    Entrances.DOWNTOWN_PARADISE_TO_ROADRULE_TIME,
    Entrances.BIG_SURF_ISLAND_TO_ROADRULE_TIME,
]

roadrules_showtime_entrances = [
    Entrances.PALM_BAY_HEIGHTS_TO_ROADRULE_SHOWTIME,
    Entrances.SILVER_LAKE_TO_ROADRULE_SHOWTIME,
    Entrances.WHITE_MOUNTAIN_TO_ROADRULE_SHOWTIME,
    Entrances.HARBOR_TOWN_TO_ROADRULE_SHOWTIME,
    Entrances.DOWNTOWN_PARADISE_TO_ROADRULE_SHOWTIME,
    Entrances.BIG_SURF_ISLAND_TO_ROADRULE_SHOWTIME,
]

roadrules_bikes_day_entrances = [
    Entrances.PALM_BAY_HEIGHTS_TO_ROADRULE_BIKES_DAY,
    Entrances.SILVER_LAKE_TO_ROADRULE_BIKES_DAY,
    Entrances.WHITE_MOUNTAIN_TO_ROADRULE_BIKES_DAY,
    Entrances.HARBOR_TOWN_TO_ROADRULE_BIKES_DAY,
    Entrances.DOWNTOWN_PARADISE_TO_ROADRULE_BIKES_DAY,
    Entrances.BIG_SURF_ISLAND_TO_ROADRULE_BIKES_DAY,
]

roadrules_bikes_night_entrances = [
    Entrances.PALM_BAY_HEIGHTS_TO_ROADRULE_BIKES_NIGHT,
    Entrances.SILVER_LAKE_TO_ROADRULE_BIKES_NIGHT,
    Entrances.WHITE_MOUNTAIN_TO_ROADRULE_BIKES_NIGHT,
    Entrances.HARBOR_TOWN_TO_ROADRULE_BIKES_NIGHT,
    Entrances.DOWNTOWN_PARADISE_TO_ROADRULE_BIKES_NIGHT,
    Entrances.BIG_SURF_ISLAND_TO_ROADRULE_BIKES_NIGHT,
]

