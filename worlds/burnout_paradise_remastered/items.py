from typing import TYPE_CHECKING

from BaseClasses import Item
from .options import BreakableLocks
from .constants import BURNOUT_PARADISE_REMASTERED
from .data import ItemTypeEnum, ItemData
from .data.items.blockers import Blockers
from .data.items.discoverables import Discoverables
from .data.items.cars import Cars, StartingCar, BurningCars
from .data.items.events import Events
from .data.items.filler import get_default_dict

if TYPE_CHECKING:
    from . import BurnoutParadiseRemasteredWorld

class BurnoutParadiseRemasteredItem(Item):
    game: str = BURNOUT_PARADISE_REMASTERED

def create_item(world: "BurnoutParadiseRemasteredWorld", item: ItemData):
    for _ in range(item.amount):
        world.itempool.append(world.create_item(item.type.value))


def create_single_item(world: "BurnoutParadiseRemasteredWorld", item_type: ItemTypeEnum):
    world.itempool.append(world.create_item(item_type.value))

def create_item_unchecked(world: "BurnoutParadiseRemasteredWorld", item_value: str):
    world.itempool.append(world.create_item(item_value))

def create_items(world: "BurnoutParadiseRemasteredWorld"):

    starting_items: list[Item] = []

    starting_items.append(world.create_item(StartingCar.HUNTER_CAVALRY.value))

    starting_events = list(world.random.sample(list(Events), 5))
    starting_items.extend(world.create_item(e.value) for e in starting_events)
    remaining_events = [e for e in Events if e not in starting_events]

    match world.options.breakable_locks:
        case BreakableLocks.option_locked_by_area:
            for item_type in Blockers:
                create_single_item(world, item_type)
        case BreakableLocks.option_locked_by_area_and_type:
            for item_type in Discoverables:
                create_single_item(world, item_type)
    for item_type in Cars:
        create_single_item(world, item_type)
    for item_type in BurningCars:
        create_single_item(world, item_type)
    for item_type in remaining_events:
        create_single_item(world, item_type)


    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

    _remaining = total_location_count - len(world.itempool)

    filler_items_distribution = world.options.filler_items_distribution.value.copy()
    if sum(filler_items_distribution.values()) == 0:
        filler_items_distribution = get_default_dict()

    for filler_name in create_random_items(world, filler_items_distribution, _remaining):
        create_item_unchecked(world, filler_name)

    world.multiworld.itempool += world.itempool

    return starting_items

def create_random_items(world: "BurnoutParadiseRemasteredWorld", weights: dict[str, int], count: int) -> list[str]:
    filler_pool = weights.copy()
    return world.random.choices(population=list(filler_pool.keys()),
                                weights=list(filler_pool.values()),
                                k=count)

