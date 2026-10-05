from BaseClasses import ItemClassification
from worlds.burnout_paradise_remastered.constants import ITEMS_OFFSET_FILLER
from worlds.burnout_paradise_remastered.data import ItemTypeEnum


class Filler(ItemTypeEnum):
    BOOST_REFILL = ("Boost Refill", ITEMS_OFFSET_FILLER + 0, ItemClassification.filler)
    BOOST_SWAP = ("Boost Swap", ITEMS_OFFSET_FILLER + 1, ItemClassification.trap)
    CAR_SWAP = ("Car Swap", ITEMS_OFFSET_FILLER + 2, ItemClassification.trap)

def get_default_dict():
    return {
        Filler.BOOST_REFILL.value: 50,
        Filler.BOOST_SWAP.value: 25,
        Filler.CAR_SWAP.value: 5,
    }
