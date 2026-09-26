from BaseClasses import ItemClassification
from worlds.burnout_paradise_remastered.constants import ITEMS_OFFSET_FILLER
from worlds.burnout_paradise_remastered.data import ItemTypeEnum


class Filler(ItemTypeEnum):
    BOOST = ("Boost", ITEMS_OFFSET_FILLER + 0, ItemClassification.filler)

def get_default_dict():
    return {filler.value: 50 for filler in Filler}
