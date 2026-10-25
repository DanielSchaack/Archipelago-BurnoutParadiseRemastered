from BaseClasses import ItemClassification
from worlds.burnout_paradise_remastered.constants import ITEMS_OFFSET_FILLER
from worlds.burnout_paradise_remastered.data import ItemTypeEnum


class Filler(ItemTypeEnum):
    BOOST_REFILL = ("Boost Refill", ITEMS_OFFSET_FILLER + 0, ItemClassification.filler)
    BOOST_SWAP = ("Boost Swap", ITEMS_OFFSET_FILLER + 1, ItemClassification.trap)
    CAR_SWAP = ("Car Swap", ITEMS_OFFSET_FILLER + 2, ItemClassification.trap)
    HIGH_TRAFFIC_DENSITY = ("High Traffic Density", ITEMS_OFFSET_FILLER + 3, ItemClassification.trap)
    RANDOM_TELEPORT= ("Random Junkyard Teleport", ITEMS_OFFSET_FILLER + 4, ItemClassification.trap)

