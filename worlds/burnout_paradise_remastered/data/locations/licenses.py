from .. import LocationTypeEnum
from ..regions.regions import Regions
from ..rules.state_rules import HasEventWins
from ...constants import LOCATIONS_OFFSET_LICENSES, D_CLASS_WINS, C_CLASS_WINS, B_CLASS_WINS, A_CLASS_WINS, BURNOUT_WINS, BURNOUT_ELITE_WINS


class LicenseLocations(LocationTypeEnum):
    CLASS_D_LICENSE = ("License Acquired - Class D", LOCATIONS_OFFSET_LICENSES + 1, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=D_CLASS_WINS))
    CLASS_C_LICENSE = ("License Acquired - Class C", LOCATIONS_OFFSET_LICENSES + 2, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=C_CLASS_WINS))
    CLASS_B_LICENSE = ("License Acquired - Class B", LOCATIONS_OFFSET_LICENSES + 3, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=B_CLASS_WINS))
    CLASS_A_LICENSE = ("License Acquired - Class A", LOCATIONS_OFFSET_LICENSES + 4, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=A_CLASS_WINS))
    BURNOUT_LICENSE = ("License Acquired - Burnout", LOCATIONS_OFFSET_LICENSES + 5, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=BURNOUT_WINS))
    BURNOUT_ELITE_LICENSE = ("License Acquired - Burnout Elite", LOCATIONS_OFFSET_LICENSES + 6, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=BURNOUT_ELITE_WINS))
