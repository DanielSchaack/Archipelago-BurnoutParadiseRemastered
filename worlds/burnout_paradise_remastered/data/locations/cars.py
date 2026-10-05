from rule_builder.rules import Has
from ...constants import LOCATIONS_OFFSET_UNIQUE_WINS
from .. import LocationTypeEnum
from ..items.cars import BurningCars, Cars, CarbonCars, ParadiseBikes, BigSurfIslandCars, CopCars, LegendaryCars, BoostSpecialCars, ToyCars, OnlineCars
from ..regions.regions import Regions
from ..rules.state_rules import HasEventWins


class CarLocations(LocationTypeEnum):
    OVAL_CHAMP_69 = ("Burning Route Car Unlock - Hunter Oval Champ 69", 0xD676FB5119E20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.HUNTER_CAVALRY.value))
    MESQUITE = ("License Gift - Hunter Mesquite", 0xA7E5D4F26592D, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=2))
    MESQUITE_CUSTOM = ("Burning Route Car Unlock - Hunter Mesquite Custom", 0xD676F97EFEC34, Regions.DOWNTOWN_PARADISE, Has(BurningCars.HUNTER_MESQUITE.value))
    SI_7 = ("Car Takedown Unlock - Nakamura SI-7", 0xA4FCC11A5567C, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=3))
    RACING_SI_7 = ("Burning Route Car Unlock - Nakamura Racing SI-7", 0xD38DAEEA988B4, Regions.DOWNTOWN_PARADISE, Has(BurningCars.NAKAMURA_SI_7.value))
    VEGAS = ("Car Takedown Unlock - Hunter Vegas", 0xA7E5D37F70360, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=5))
    VEGAS_CARNIVALE = ("Burning Route Car Unlock - Hunter Vegas Carnivale", 0xD676C159EDC20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.HUNTER_VEGAS.value))
    PIONEER = ("Car Takedown Unlock - Krieger Pioneer", 0xA59406A49B160, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=7))
    PIONEER_SUPER_GATOR = ("Burning Route Car Unlock - Krieger Pioneer Super Gator", 0xD424F47F18A20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.KRIEGER_PIONEER.value))
    IKUSA_GT = ("License Gift - Nakamura Ikusa GT", 0xA4FCC10EE9360, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=9))
    IKUSA_SAMURAI = ("Burning Route Car Unlock - Nakamura Ikusa Samurai", 0xD38DAEE966C20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.NAKAMURA_IKUSA_GT.value))
    HYDROS_CUSTOM = ("Car Takedown Unlock - Kitano Hydros Custom", 0xA4FCBEB7FB67C, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=10))
    HYDROS_TECHNO = ("Burning Route Car Unlock - Kitano Hydros Techno", 0xD38DAC870CC20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.KITANO_HYDROS_CUSTOM.value))
    RELIABLE_CUSTOM = ("Car Takedown Unlock - Hunter Reliable Custom", 0xA7E5D607EFD60, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=13))
    RELIABLE_SPECIAL = ("Burning Route Car Unlock - Hunter Reliable Special", 0xD676C3D7F1F8E, Regions.DOWNTOWN_PARADISE, Has(BurningCars.HUNTER_RELIABLE_CUSTOM.value))
    R_TURBO_ROADSTER = ("Car Takedown Unlock - Watson Burnout Roadster", 0xA593A0B813960, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=16))
    BURNOUT_ROADSTER = ("Burning Route Car Unlock - Watson R-Turbo Roadster", 0xD4248E9278B80, Regions.DOWNTOWN_PARADISE, Has(BurningCars.WATSON_R_TURBO_ROADSTER.value))
    LM_CLASSIC = ("Car Takedown Unlock - Rossolini LM Classic", 0xA593DB9421760, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=19))
    LM_TRACK_PACKAGE = ("Burning Route Car Unlock - Rossolini LM Track Package", 0xD424C965533F4, Regions.DOWNTOWN_PARADISE, Has(BurningCars.ROSSOLINI_LM_CLASSIC.value))
    MANHATTAN = ("Car Takedown Unlock - Hunter Manhattan", 0xA7E5CD898F360, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=22))
    MANHATTAN_CUSTOM = ("Burning Route Car Unlock - Hunter Manhattan Custom", 0xD676BB640CC20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.HUNTER_MANHATTAN.value))
    FASTBACK = ("License Gift - Carson Fastback", 0xA7E60D533AB80, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=24))
    FASTBACK_SPECIAL = ("Burning Route Car Unlock - Carson Fastback Special", 0xD676FF9BF8EB0, Regions.DOWNTOWN_PARADISE, Has(BurningCars.CARSON_FASTBACK.value))
    GRAND_MARAIS = ("Car Takedown Unlock - Carson Grand Marais", 0xA7E5EB0AA8F60, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=26))
    GRAND_SICILIAN = ("Burning Route Car Unlock - Carson Grand Sicilian", 0xA7E5EB1526820, Regions.DOWNTOWN_PARADISE, Has(BurningCars.CARSON_GRAND_MARAIS.value))
    HYPERION = ("Car Takedown Unlock - Montgomery Hyperion", 0xA594060C04960, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=30))
    HYPERION_RATTLER = ("Burning Route Car Unlock - Montgomery Hyperion Rattler", 0xD424F3E682220, Regions.DOWNTOWN_PARADISE, Has(BurningCars.MONTGOMERY_HYPERION.value))
    _616_SPORT = ("Car Takedown Unlock - Krieger 616 Sport", 0xA59403CFDC6B0, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=34))
    _616_ARACHNO_SPORT = ("Burning Route Car Unlock - Krieger 616 Arachno Sport", 0xD424F1A2EA474, Regions.DOWNTOWN_PARADISE, Has(BurningCars.KRIEGER_616_SPORT.value))
    SPUR = ("Car Takedown Unlock - Hunter Spur", 0xA7E60F6685760, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=38))
    HOTSPUR = ("Burning Route Car Unlock - Hunter Hotspur", 0xD676FD4103020, Regions.DOWNTOWN_PARADISE, Has(BurningCars.HUNTER_SPUR.value))
    GT_2400 = ("Car Takedown Unlock - Montgomery GT 2400", 0xA593FDD9FB6B0, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=42))
    SABOTAGE_GT_2400 = ("Burning Route Car Unlock - Montgomery Sabotage GT 2400", 0xD424EBAD09474, Regions.DOWNTOWN_PARADISE, Has(BurningCars.MONTGOMERY_GT_2400.value))
    P12 = ("Car Takedown Unlock - Jansen P12", 0xA7E632DD80360, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=46))
    P12_TRACK_PACKAGE = ("Burning Route Car Unlock - Jansen P12 Track Package", 0xD67720B7FDC20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.JANSEN_P12.value))
    INFERNO_VAN = ("Car Takedown Unlock - Carson Inferno Van", 0xA7E5D6543B160, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=41))
    INFERNO_BRT_VAN = ("Burning Route Car Unlock - Carson Inferno BRT Van", 0xD676C4256CDF4, Regions.DOWNTOWN_PARADISE, Has(BurningCars.CARSON_INFERNO_VAN.value))
    TEMPESTA = ("License Gift - Rossolini Tempesta", 0xA59403CFD6508, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=50))
    TEMPESTA_GT = ("Burning Route Car Unlock - Rossolini Tempesta GT", 0xD424F1A1F5870, Regions.DOWNTOWN_PARADISE, Has(BurningCars.ROSSOLINI_TEMPESTA.value))
    OPUS = ("Car Takedown Unlock - Carson Opus", 0xA7E60B608D960, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=56))
    OPUS_XS = ("Burning Route Car Unlock - Carson Opus XS", 0xD676F93B0B220, Regions.DOWNTOWN_PARADISE, Has(BurningCars.CARSON_OPUS.value))
    ANNIHILATOR = ("Car Takedown Unlock - Carson Annihilator", 0xA7E60F1A40508, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=61))
    ANNIHILATOR_PHOENIX = ("Burning Route Car Unlock - Carson Annihilator Phoenix", 0xD676FB773F820, Regions.DOWNTOWN_PARADISE, Has(BurningCars.CARSON_ANNIHILATOR.value))
    X12 = ("Car Takedown Unlock - Jansen X12", 0xA59403CFE2858, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=66))
    XS12 = ("Burning Route Car Unlock - Jansen XS12", 0xA59402A920C20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.JANSEN_X12.value))
    TOUGE_SPORT = ("Car Takedown Unlock - Kitano Touge Sport", 0xA4FCC2D988700, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=71))
    TOUGE_CRITERION = ("Burning Route Car Unlock - Kitano Touge Criterion", 0xD38DB0D94FE20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.KITANO_TOUGE_SPORT.value))
    TAKEDOWN_4X4 = ("Car Takedown Unlock - Hunter Takedown 4x4", 0xA7E6222D0A360, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=77))
    TAKEDOWN_DIRT_RACER = ("Burning Route Car Unlock - Hunter Takedown Dirt Racer", 0xD677100787C20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.HUNTER_TAKEDOWN_4X4.value))
    _500_GT = ("Car Takedown Unlock - Carson 500 GT", 0xA7E62CE79F360, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=83))
    RACING_500_GT = ("Burning Route Car Unlock - Carson Racing 500 GT", 0xD6771AC21CC20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.CARSON_500_GT.value))
    RACING_OVAL_CHAMP = ("Car Takedown Unlock - Hunter Racing Oval Champ", 0xA7E62E8B3D160, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=89))
    BRT_OVAL_CHAMP = ("Burning Route Car Unlock - Hunter BRT Oval Champ", 0xD6771C65BAA20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.HUNTER_RACING_OVAL_CHAMP.value))
    GT_CONCEPT = ("License Gift - Carson GT Concept", 0xA7E60F1A4C858, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=90))
    GT_FLAME = ("Burning Route Car Unlock - Carson GT Flame", 0xD676FBC38AC20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.CARSON_GT_CONCEPT.value))
    CITIZEN = ("Car Takedown Unlock - Hunter Citizen", 0xA7E5D3964E17C, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=98))
    CIVILIAN = ("Burning Route Car Unlock - Hunter Civilian", 0xD676C166913B4, Regions.DOWNTOWN_PARADISE, Has(BurningCars.HUNTER_CITIZEN.value))
    _25_V16_REVENGE = ("Car Takedown Unlock - Watson 25 v16 Revenge", 0xA594001623960, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=107))
    REVENGE_RACER = ("Burning Route Car Unlock - Watson Revenge Racer", 0xD424EDF0A1220, Regions.DOWNTOWN_PARADISE, Has(BurningCars.WATSON_25_V16_REVENGE.value))
    HAWKER = ("Car Takedown Unlock - Montgomery Hawker", 0xA5940206E8700, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=116))
    HAWKER_SOLO = ("Burning Route Car Unlock - Montgomery Hawker Solo", 0xD424F17A86500, Regions.DOWNTOWN_PARADISE, Has(BurningCars.MONTGOMERY_HAWKER.value))
    UBERSCHALL_8 = ("Car Takedown Unlock - Krieger Überschall 8", 0xA593FE7285B60, Regions.DOWNTOWN_PARADISE,HasEventWins(wins=128))
    KRIEGER_UBERSCHALL_CLEAR_VIEW = ("Burning Route Car Unlock - Krieger Überschall Clear-View", 0xD424EC43B9C93, Regions.DOWNTOWN_PARADISE, Has(BurningCars.KRIEGER_UBERSCHALL_8.value))
    THUNDER_CUSTOM = ("Car Takedown Unlock - Carson Thunder Custom", 0xA7E5D4D6C2D60, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=140))
    CARSON_THUNDER_SHADOW = ("Burning Route Car Unlock - Carson Thunder Shadow", 0xD676C2A7F49F4, Regions.DOWNTOWN_PARADISE, Has(BurningCars.CARSON_THUNDER_CUSTOM.value))
    HOT_ROD_COUPE = ("Car Takedown Unlock - Carson Hot Rod Coupe", 0xA7E5CE484B560, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=154))
    TRIBAL_SPECIAL = ("Burning Route Car Unlock - Carson Tribal Special", 0xD676BC22C8E20, Regions.DOWNTOWN_PARADISE, Has(BurningCars.CARSON_HOT_ROD_COUPE.value))
    RACING_WTR = ("Car Takedown Unlock - Krieger Racing WTR", 0xA7E62DCC80F60, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=168))
    PCPD_SPECIAL = ("Burning Route Car Unlock - Krieger PCPD Special", 0xA7E5D5809C480, Regions.DOWNTOWN_PARADISE, Has(BurningCars.KRIEGER_RACING_WTR.value))

class CarWinLocations(LocationTypeEnum):
    HUNTER_OVAL_CHAMP_69 = (
        "First Car Win - Hunter Oval Champ 69",
        LOCATIONS_OFFSET_UNIQUE_WINS + 0,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.HUNTER_OVAL_CHAMP_69.value)
    )
    HUNTER_MESQUITE_CUSTOM = (
        "First Car Win - Hunter Mesquite Custom",
        LOCATIONS_OFFSET_UNIQUE_WINS + 1,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.HUNTER_MESQUITE_CUSTOM.value)
    )
    NAKAMURA_RACING_SI_7 = (
        "First Car Win - Nakamura Racing SI-7",
        LOCATIONS_OFFSET_UNIQUE_WINS + 2,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.NAKAMURA_RACING_SI_7.value)
    )
    HUNTER_VEGAS_CARNIVALE = (
        "First Car Win - Hunter Vegas Carnivale",
        LOCATIONS_OFFSET_UNIQUE_WINS + 3,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.HUNTER_VEGAS_CARNIVALE.value)
    )
    KRIEGER_PIONEER_SUPER_GATOR = (
        "First Car Win - Krieger Pioneer Super Gator",
        LOCATIONS_OFFSET_UNIQUE_WINS + 4,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.KRIEGER_PIONEER_SUPER_GATOR.value)
    )
    NAKAMURA_IKUSA_SAMURAI = (
        "First Car Win - Nakamura Ikusa Samurai",
        LOCATIONS_OFFSET_UNIQUE_WINS + 5,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.NAKAMURA_IKUSA_SAMURAI.value)
    )
    KITANO_HYDROS_TECHNO = (
        "First Car Win - Kitano Hydros Techno",
        LOCATIONS_OFFSET_UNIQUE_WINS + 6,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.KITANO_HYDROS_TECHNO.value)
    )
    HUNTER_RELIABLE_SPECIAL = (
        "First Car Win - Hunter Reliable Special",
        LOCATIONS_OFFSET_UNIQUE_WINS + 7,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.HUNTER_RELIABLE_SPECIAL.value)
    )
    WATSON_BURNOUT_ROADSTER = (
        "First Car Win - Watson Burnout Roadster",
        LOCATIONS_OFFSET_UNIQUE_WINS + 8,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.WATSON_BURNOUT_ROADSTER.value)
    )
    ROSSOLINI_LM_TRACK_PACKAGE = (
        "First Car Win - Rossolini LM Track Package",
        LOCATIONS_OFFSET_UNIQUE_WINS + 9,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.ROSSOLINI_LM_TRACK_PACKAGE.value)
    )
    HUNTER_MANHATTAN_CUSTOM = (
        "First Car Win - Hunter Manhattan Custom",
        LOCATIONS_OFFSET_UNIQUE_WINS + 10,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.HUNTER_MANHATTAN_CUSTOM.value)
    )
    CARSON_FASTBACK_SPECIAL = (
        "First Car Win - Carson Fastback Special",
        LOCATIONS_OFFSET_UNIQUE_WINS + 11,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.CARSON_FASTBACK_SPECIAL.value)
    )
    CARSON_GRAND_SICILIAN = (
        "First Car Win - Carson Grand Sicilian",
        LOCATIONS_OFFSET_UNIQUE_WINS + 12,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.CARSON_GRAND_SICILIAN.value)
    )
    MONTGOMERY_HYPERION_RATTLER = (
        "First Car Win - Montgomery Hyperion Rattler",
        LOCATIONS_OFFSET_UNIQUE_WINS + 13,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.MONTGOMERY_HYPERION_RATTLER.value)
    )
    KRIEGER_616_ARACHNO_SPORT = (
        "First Car Win - Krieger 616 Arachno Sport",
        LOCATIONS_OFFSET_UNIQUE_WINS + 14,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.KRIEGER_616_ARACHNO_SPORT.value)
    )
    HUNTER_HOTSPUR = (
        "First Car Win - Hunter Hotspur",
        LOCATIONS_OFFSET_UNIQUE_WINS + 15,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.HUNTER_HOTSPUR.value)
    )
    MONTGOMERY_SABOTAGE_GT_2400 = (
        "First Car Win - Montgomery Sabotage GT 2400",
        LOCATIONS_OFFSET_UNIQUE_WINS + 16,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.MONTGOMERY_SABOTAGE_GT_2400.value)
    )
    JANSEN_P12_TRACK_PACKAGE = (
        "First Car Win - Jansen P12 Track Package",
        LOCATIONS_OFFSET_UNIQUE_WINS + 17,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.JANSEN_P12_TRACK_PACKAGE.value)
    )
    CARSON_INFERNO_BRT_VAN = (
        "First Car Win - Carson Inferno BRT Van",
        LOCATIONS_OFFSET_UNIQUE_WINS + 18,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.CARSON_INFERNO_BRT_VAN.value)
    )
    ROSSOLINI_TEMPESTA_GT = (
        "First Car Win - Rossolini Tempesta GT",
        LOCATIONS_OFFSET_UNIQUE_WINS + 19,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.ROSSOLINI_TEMPESTA_GT.value)
    )
    CARSON_OPUS_XS = (
        "First Car Win - Carson Opus XS",
        LOCATIONS_OFFSET_UNIQUE_WINS + 20,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.CARSON_OPUS_XS.value)
    )
    CARSON_ANNIHILATOR_PHOENIX = (
        "First Car Win - Carson Annihilator Phoenix",
        LOCATIONS_OFFSET_UNIQUE_WINS + 21,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.CARSON_ANNIHILATOR_PHOENIX.value)
    )
    JANSEN_XS12 = (
        "First Car Win - Jansen XS12",
        LOCATIONS_OFFSET_UNIQUE_WINS + 22,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.JANSEN_XS12.value)
    )
    KITANO_TOUGE_CRITERION = (
        "First Car Win - Kitano Touge Criterion",
        LOCATIONS_OFFSET_UNIQUE_WINS + 23,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.KITANO_TOUGE_CRITERION.value)
    )
    HUNTER_TAKEDOWN_DIRT_RACER = (
        "First Car Win - Hunter Takedown Dirt Racer",
        LOCATIONS_OFFSET_UNIQUE_WINS + 24,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.HUNTER_TAKEDOWN_DIRT_RACER.value)
    )
    CARSON_RACING_500_GT = (
        "First Car Win - Carson Racing 500 GT",
        LOCATIONS_OFFSET_UNIQUE_WINS + 25,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.CARSON_RACING_500_GT.value)
    )
    HUNTER_BRT_OVAL_CHAMP = (
        "First Car Win - Hunter BRT Oval Champ",
        LOCATIONS_OFFSET_UNIQUE_WINS + 26,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.HUNTER_BRT_OVAL_CHAMP.value)
    )
    CARSON_GT_FLAME = (
        "First Car Win - Carson GT Flame",
        LOCATIONS_OFFSET_UNIQUE_WINS + 27,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.CARSON_GT_FLAME.value)
    )
    HUNTER_CIVILIAN = (
        "First Car Win - Hunter Civilian",
        LOCATIONS_OFFSET_UNIQUE_WINS + 28,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.HUNTER_CIVILIAN.value)
    )
    WATSON_REVENGE_RACER = (
        "First Car Win - Watson Revenge Racer",
        LOCATIONS_OFFSET_UNIQUE_WINS + 29,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.WATSON_REVENGE_RACER.value)
    )
    MONTGOMERY_HAWKER_SOLO = (
        "First Car Win - Montgomery Hawker Solo",
        LOCATIONS_OFFSET_UNIQUE_WINS + 30,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.MONTGOMERY_HAWKER_SOLO.value)
    )
    KRIEGER_UBERSCHALL_CLEAR_VIEW = (
        "First Car Win - Krieger Überschall Clear-View",
        LOCATIONS_OFFSET_UNIQUE_WINS + 31,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.KRIEGER_UBERSCHALL_CLEAR_VIEW.value)
    )
    CARSON_THUNDER_SHADOW = (
        "First Car Win - Carson Thunder Shadow",
        LOCATIONS_OFFSET_UNIQUE_WINS + 32,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.CARSON_THUNDER_SHADOW.value)
    )
    CARSON_TRIBAL_SPECIAL = (
        "First Car Win - Carson Tribal Special",
        LOCATIONS_OFFSET_UNIQUE_WINS + 33,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.CARSON_TRIBAL_SPECIAL.value)
    )
    KRIEGER_PCPD_SPECIAL = (
        "First Car Win - Krieger PCPD Special",
        LOCATIONS_OFFSET_UNIQUE_WINS + 34,
        Regions.DOWNTOWN_PARADISE,
        Has(Cars.KRIEGER_PCPD_SPECIAL.value)
    )

class BurningCarWinLocations(LocationTypeEnum):
    HUNTER_CAVALRY = (
        "First Car Win - Hunter Cavalry",
        LOCATIONS_OFFSET_UNIQUE_WINS + 35,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.HUNTER_CAVALRY.value)
    )
    HUNTER_MESQUITE = (
        "First Car Win - Hunter Mesquite",
        LOCATIONS_OFFSET_UNIQUE_WINS + 36,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.HUNTER_MESQUITE.value)
    )
    NAKAMURA_SI_7 = (
        "First Car Win - Nakamura SI-7",
        LOCATIONS_OFFSET_UNIQUE_WINS + 37,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.NAKAMURA_SI_7.value)
    )
    HUNTER_VEGAS = (
        "First Car Win - Hunter Vegas",
        LOCATIONS_OFFSET_UNIQUE_WINS + 38,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.HUNTER_VEGAS.value)
    )
    KRIEGER_PIONEER = (
        "First Car Win - Krieger Pioneer",
        LOCATIONS_OFFSET_UNIQUE_WINS + 39,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.KRIEGER_PIONEER.value)
    )
    NAKAMURA_IKUSA_GT = (
        "First Car Win - Nakamura Ikusa GT",
        LOCATIONS_OFFSET_UNIQUE_WINS + 40,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.NAKAMURA_IKUSA_GT.value)
    )
    KITANO_HYDROS_CUSTOM = (
        "First Car Win - Kitano Hydros Custom",
        LOCATIONS_OFFSET_UNIQUE_WINS + 41,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.KITANO_HYDROS_CUSTOM.value)
    )
    HUNTER_RELIABLE_CUSTOM = (
        "First Car Win - Hunter Reliable Custom",
        LOCATIONS_OFFSET_UNIQUE_WINS + 42,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.HUNTER_RELIABLE_CUSTOM.value)
    )
    WATSON_R_TURBO_ROADSTER = (
        "First Car Win - Watson R-Turbo Roadster",
        LOCATIONS_OFFSET_UNIQUE_WINS + 43,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.WATSON_R_TURBO_ROADSTER.value)
    )
    ROSSOLINI_LM_CLASSIC = (
        "First Car Win - Rossolini LM Classic",
        LOCATIONS_OFFSET_UNIQUE_WINS + 44,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.ROSSOLINI_LM_CLASSIC.value)
    )
    HUNTER_MANHATTAN = (
        "First Car Win - Hunter Manhattan",
        LOCATIONS_OFFSET_UNIQUE_WINS + 45,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.HUNTER_MANHATTAN.value)
    )
    CARSON_FASTBACK = (
        "First Car Win - Carson Fastback",
        LOCATIONS_OFFSET_UNIQUE_WINS + 46,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.CARSON_FASTBACK.value)
    )
    CARSON_GRAND_MARAIS = (
        "First Car Win - Carson Grand Marais",
        LOCATIONS_OFFSET_UNIQUE_WINS + 47,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.CARSON_GRAND_MARAIS.value)
    )
    MONTGOMERY_HYPERION = (
        "First Car Win - Montgomery Hyperion",
        LOCATIONS_OFFSET_UNIQUE_WINS + 48,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.MONTGOMERY_HYPERION.value)
    )
    KRIEGER_616_SPORT = (
        "First Car Win - Krieger 616 Sport",
        LOCATIONS_OFFSET_UNIQUE_WINS + 49,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.KRIEGER_616_SPORT.value)
    )
    HUNTER_SPUR = (
        "First Car Win - Hunter Spur",
        LOCATIONS_OFFSET_UNIQUE_WINS + 50,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.HUNTER_SPUR.value)
    )
    MONTGOMERY_GT_2400 = (
        "First Car Win - Montgomery GT 2400",
        LOCATIONS_OFFSET_UNIQUE_WINS + 51,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.MONTGOMERY_GT_2400.value)
    )
    JANSEN_P12 = (
        "First Car Win - Jansen P12",
        LOCATIONS_OFFSET_UNIQUE_WINS + 52,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.JANSEN_P12.value)
    )
    CARSON_INFERNO_VAN = (
        "First Car Win - Carson Inferno Van",
        LOCATIONS_OFFSET_UNIQUE_WINS + 53,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.CARSON_INFERNO_VAN.value)
    )
    ROSSOLINI_TEMPESTA = (
        "First Car Win - Rossolini Tempesta",
        LOCATIONS_OFFSET_UNIQUE_WINS + 54,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.ROSSOLINI_TEMPESTA.value)
    )
    CARSON_OPUS = (
        "First Car Win - Carson Opus",
        LOCATIONS_OFFSET_UNIQUE_WINS + 55,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.CARSON_OPUS.value)
    )
    CARSON_ANNIHILATOR = (
        "First Car Win - Carson Annihilator",
        LOCATIONS_OFFSET_UNIQUE_WINS + 56,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.CARSON_ANNIHILATOR.value)
    )
    JANSEN_X12 = (
        "First Car Win - Jansen X12",
        LOCATIONS_OFFSET_UNIQUE_WINS + 57,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.JANSEN_X12.value)
    )
    KITANO_TOUGE_SPORT = (
        "First Car Win - Kitano Touge Sport",
        LOCATIONS_OFFSET_UNIQUE_WINS + 58,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.KITANO_TOUGE_SPORT.value)
    )
    HUNTER_TAKEDOWN_4X4 = (
        "First Car Win - Hunter Takedown 4x4",
        LOCATIONS_OFFSET_UNIQUE_WINS + 59,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.HUNTER_TAKEDOWN_4X4.value)
    )
    CARSON_500_GT = (
        "First Car Win - Carson 500 GT",
        LOCATIONS_OFFSET_UNIQUE_WINS + 60,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.CARSON_500_GT.value)
    )
    HUNTER_RACING_OVAL_CHAMP = (
        "First Car Win - Hunter Racing Oval Champ",
        LOCATIONS_OFFSET_UNIQUE_WINS + 61,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.HUNTER_RACING_OVAL_CHAMP.value)
    )
    CARSON_GT_CONCEPT = (
        "First Car Win - Carson GT Concept",
        LOCATIONS_OFFSET_UNIQUE_WINS + 62,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.CARSON_GT_CONCEPT.value)
    )
    HUNTER_CITIZEN = (
        "First Car Win - Hunter Citizen",
        LOCATIONS_OFFSET_UNIQUE_WINS + 63,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.HUNTER_CITIZEN.value)
    )
    WATSON_25_V16_REVENGE = (
        "First Car Win - Watson 25 V16 Revenge",
        LOCATIONS_OFFSET_UNIQUE_WINS + 64,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.WATSON_25_V16_REVENGE.value)
    )
    MONTGOMERY_HAWKER = (
        "First Car Win - Montgomery Hawker",
        LOCATIONS_OFFSET_UNIQUE_WINS + 65,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.MONTGOMERY_HAWKER.value)
    )
    KRIEGER_UBERSCHALL_8 = (
        "First Car Win - Krieger Uberschall 8",
        LOCATIONS_OFFSET_UNIQUE_WINS + 66,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.KRIEGER_UBERSCHALL_8.value)
    )
    CARSON_THUNDER_CUSTOM = (
        "First Car Win - Carson Thunder Custom",
        LOCATIONS_OFFSET_UNIQUE_WINS + 67,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.CARSON_THUNDER_CUSTOM.value)
    )
    CARSON_HOT_ROD_COUPE = (
        "First Car Win - Carson Hot Rod Coupe",
        LOCATIONS_OFFSET_UNIQUE_WINS + 68,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.CARSON_HOT_ROD_COUPE.value)
    )
    KRIEGER_RACING_WTR = (
        "First Car Win - Krieger Racing WTR",
        LOCATIONS_OFFSET_UNIQUE_WINS + 69,
        Regions.DOWNTOWN_PARADISE,
        Has(BurningCars.KRIEGER_RACING_WTR.value)
    )

class CarbonCarWinLocations(LocationTypeEnum):
    NAKAMURA_CARBON_IKUSA_GT = (
        "First Car Win - Nakamura Carbon Ikusa GT",
        LOCATIONS_OFFSET_UNIQUE_WINS + 70,
        Regions.DOWNTOWN_PARADISE,
        Has(CarbonCars.NAKAMURA_CARBON_IKUSA_GT.value)
    )
    KITANO_CARBON_HYDROS_CUSTOM = (
        "First Car Win - Kitano Carbon Hydros Custom",
        LOCATIONS_OFFSET_UNIQUE_WINS + 71,
        Regions.DOWNTOWN_PARADISE,
        Has(CarbonCars.KITANO_CARBON_HYDROS_CUSTOM.value)
    )
    JANSEN_CARBON_X12 = (
        "First Car Win - Jansen Carbon X12",
        LOCATIONS_OFFSET_UNIQUE_WINS + 72,
        Regions.DOWNTOWN_PARADISE,
        Has(CarbonCars.JANSEN_CARBON_X12.value)
    )
    CARSON_CARBON_GT_CONCEPT = (
        "First Car Win - Carson Carbon GT Concept",
        LOCATIONS_OFFSET_UNIQUE_WINS + 73,
        Regions.DOWNTOWN_PARADISE,
        Has(CarbonCars.CARSON_CARBON_GT_CONCEPT.value)
    )
    MONTGOMERY_CARBON_HAWKER = (
        "First Car Win - Montgomery Carbon Hawker",
        LOCATIONS_OFFSET_UNIQUE_WINS + 74,
        Regions.DOWNTOWN_PARADISE,
        Has(CarbonCars.MONTGOMERY_CARBON_HAWKER.value)
    )
    KRIEGER_CARBON_UBERSCHALL_8 = (
        "First Car Win - Krieger Carbon Uberschall 8",
        LOCATIONS_OFFSET_UNIQUE_WINS + 75,
        Regions.DOWNTOWN_PARADISE,
        Has(CarbonCars.KRIEGER_CARBON_UBERSCHALL_8.value)
    )

class OnlineCarWinLocations(LocationTypeEnum):
    HUNTER_OLYMPUS = (
        "First Car Win - Hunter Olympus",
        LOCATIONS_OFFSET_UNIQUE_WINS + 76,
        Regions.DOWNTOWN_PARADISE,
        Has(OnlineCars.HUNTER_OLYMPUS.value)
    )
    NAKAMURA_RAI_JIN_TURBO = (
        "First Car Win - Nakamura Rai-Jin Turbo",
        LOCATIONS_OFFSET_UNIQUE_WINS + 77,
        Regions.DOWNTOWN_PARADISE,
        Has(OnlineCars.NAKAMURA_RAI_JIN_TURBO.value)
    )

class ToyCarWinLocations(LocationTypeEnum):
    HUNTER_TOY_CAVALRY = (
        "First Car Win - Hunter Toy Cavalry",
        LOCATIONS_OFFSET_UNIQUE_WINS + 78,
        Regions.DOWNTOWN_PARADISE,
        Has(ToyCars.HUNTER_TOY_CAVALRY.value)
    )
    CARSON_TOY_GT_CONCEPT = (
        "First Car Win - Carson Toy GT Concept",
        LOCATIONS_OFFSET_UNIQUE_WINS + 79,
        Regions.DOWNTOWN_PARADISE,
        Has(ToyCars.CARSON_TOY_GT_CONCEPT.value)
    )
    KRIEGER_TOY_WTR = (
        "First Car Win - Krieger Toy WTR",
        LOCATIONS_OFFSET_UNIQUE_WINS + 80,
        Regions.DOWNTOWN_PARADISE,
        Has(ToyCars.KRIEGER_TOY_WTR.value)
    )
    JANSEN_TOY_P12 = (
        "First Car Win - Jansen Toy P12",
        LOCATIONS_OFFSET_UNIQUE_WINS + 81,
        Regions.DOWNTOWN_PARADISE,
        Has(ToyCars.JANSEN_TOY_P12.value)
    )
    HUNTER_TOY_MANHATTAN = (
        "First Car Win - Hunter Toy Manhattan",
        LOCATIONS_OFFSET_UNIQUE_WINS + 82,
        Regions.DOWNTOWN_PARADISE,
        Has(ToyCars.HUNTER_TOY_MANHATTAN.value)
    )
    HUNTER_TOY_TAKEDOWN_4X4 = (
        "First Car Win - Hunter Toy Takedown 4x4",
        LOCATIONS_OFFSET_UNIQUE_WINS + 83,
        Regions.DOWNTOWN_PARADISE,
        Has(ToyCars.HUNTER_TOY_TAKEDOWN_4X4.value)
    )
    HUNTER_TOY_CITIZEN = (
        "First Car Win - Hunter Toy Citizen",
        LOCATIONS_OFFSET_UNIQUE_WINS + 84,
        Regions.DOWNTOWN_PARADISE,
        Has(ToyCars.HUNTER_TOY_CITIZEN.value)
    )
    CARSON_TOY_INFERNO = (
        "First Car Win - Carson Toy Inferno",
        LOCATIONS_OFFSET_UNIQUE_WINS + 85,
        Regions.DOWNTOWN_PARADISE,
        Has(ToyCars.CARSON_TOY_INFERNO.value)
    )
    NAKAMURA_TOY_FIREHAWK_GP = (
        "First Car Win - Nakamura Toy Firehawk GP",
        LOCATIONS_OFFSET_UNIQUE_WINS + 86,
        Regions.DOWNTOWN_PARADISE,
        Has(ToyCars.NAKAMURA_TOY_FIREHAWK_GP.value)
    )

class LegendaryCarWinLocations(LocationTypeEnum):
    JANSEN_P12_88_SPECIAL = (
        "First Car Win - Jansen P12 88 Special",
        LOCATIONS_OFFSET_UNIQUE_WINS + 87,
        Regions.DOWNTOWN_PARADISE,
        Has(LegendaryCars.JANSEN_P12_88_SPECIAL.value)
    )
    HUNTER_MANHATTAN_SPIRIT = (
        "First Car Win - Hunter Manhattan Spirit",
        LOCATIONS_OFFSET_UNIQUE_WINS + 88,
        Regions.DOWNTOWN_PARADISE,
        Has(LegendaryCars.HUNTER_MANHATTAN_SPIRIT.value)
    )
    CARSON_GT_NIGHTHAWK = (
        "First Car Win - Carson GT Nighthawk",
        LOCATIONS_OFFSET_UNIQUE_WINS + 89,
        Regions.DOWNTOWN_PARADISE,
        Has(LegendaryCars.CARSON_GT_NIGHTHAWK.value)
    )
    HUNTER_CAVALRY_BOOTLEGGER = (
        "First Car Win - Hunter Cavalry Bootlegger",
        LOCATIONS_OFFSET_UNIQUE_WINS + 90,
        Regions.DOWNTOWN_PARADISE,
        Has(LegendaryCars.HUNTER_CAVALRY_BOOTLEGGER.value)
    )

class BoostSpecialCarWinLocations(LocationTypeEnum):
    CARSON_EXTREME_HOT_ROD = (
        "First Car Win - Carson Extreme Hot Rod",
        LOCATIONS_OFFSET_UNIQUE_WINS + 91,
        Regions.DOWNTOWN_PARADISE,
        Has(BoostSpecialCars.CARSON_EXTREME_HOT_ROD.value)
    )
    MONTGOMERY_HAWKER_MECH = (
        "First Car Win - Montgomery Hawker Mech",
        LOCATIONS_OFFSET_UNIQUE_WINS + 92,
        Regions.DOWNTOWN_PARADISE,
        Has(BoostSpecialCars.MONTGOMERY_HAWKER_MECH.value)
    )

class CopCarWinLocations(LocationTypeEnum):
    HUNTER_PCPD_CAVALRY = (
        "First Car Win - Hunter PCPD Cavalry",
        LOCATIONS_OFFSET_UNIQUE_WINS + 93,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.HUNTER_PCPD_CAVALRY.value)
    )
    HUNTER_PCPD_MESQUITE = (
        "First Car Win - Hunter PCPD Mesquite",
        LOCATIONS_OFFSET_UNIQUE_WINS + 94,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.HUNTER_PCPD_MESQUITE.value)
    )
    NAKAMURA_PCPD_SI_7 = (
        "First Car Win - Nakamura PCPD SI-7",
        LOCATIONS_OFFSET_UNIQUE_WINS + 95,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.NAKAMURA_PCPD_SI_7.value)
    )
    HUNTER_PCPD_VEGAS = (
        "First Car Win - Hunter PCPD Vegas",
        LOCATIONS_OFFSET_UNIQUE_WINS + 96,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.HUNTER_PCPD_VEGAS.value)
    )
    KRIEGER_PCPD_PIONEER = (
        "First Car Win - Krieger PCPD Pioneer",
        LOCATIONS_OFFSET_UNIQUE_WINS + 97,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.KRIEGER_PCPD_PIONEER.value)
    )
    NAKAMURA_PCPD_IKUSA_GT = (
        "First Car Win - Nakamura PCPD Ikusa GT",
        LOCATIONS_OFFSET_UNIQUE_WINS + 98,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.NAKAMURA_PCPD_IKUSA_GT.value)
    )
    KITANO_PCPD_HYDROS_CUSTOM = (
        "First Car Win - Kitano PCPD Hydros Custom",
        LOCATIONS_OFFSET_UNIQUE_WINS + 99,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.KITANO_PCPD_HYDROS_CUSTOM.value)
    )
    HUNTER_PCPD_RELIABLE_CUSTOM = (
        "First Car Win - Hunter PCPD Reliable Custom",
        LOCATIONS_OFFSET_UNIQUE_WINS + 100,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.HUNTER_PCPD_RELIABLE_CUSTOM.value)
    )
    WATSON_PCPD_R_TURBO_ROADSTER = (
        "First Car Win - Watson PCPD R-Turbo Roadster",
        LOCATIONS_OFFSET_UNIQUE_WINS + 101,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.WATSON_PCPD_R_TURBO_ROADSTER.value)
    )
    ROSSOLINI_PCPD_LM_CLASSIC = (
        "First Car Win - Rossolini PCPD LM Classic",
        LOCATIONS_OFFSET_UNIQUE_WINS + 102,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.ROSSOLINI_PCPD_LM_CLASSIC.value)
    )
    HUNTER_PCPD_MANHATTAN = (
        "First Car Win - Hunter PCPD Manhattan",
        LOCATIONS_OFFSET_UNIQUE_WINS + 103,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.HUNTER_PCPD_MANHATTAN.value)
    )
    CARSON_PCPD_FASTBACK = (
        "First Car Win - Carson PCPD Fastback",
        LOCATIONS_OFFSET_UNIQUE_WINS + 104,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.CARSON_PCPD_FASTBACK.value)
    )
    CARSON_PCPD_GRAND_MARAIS = (
        "First Car Win - Carson PCPD Grand Marais",
        LOCATIONS_OFFSET_UNIQUE_WINS + 105,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.CARSON_PCPD_GRAND_MARAIS.value)
    )
    MONTGOMERY_PCPD_HYPERION = (
        "First Car Win - Montgomery PCPD Hyperion",
        LOCATIONS_OFFSET_UNIQUE_WINS + 106,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.MONTGOMERY_PCPD_HYPERION.value)
    )
    KRIEGER_PCPD_616_SPORT = (
        "First Car Win - Krieger PCPD 616 Sport",
        LOCATIONS_OFFSET_UNIQUE_WINS + 107,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.KRIEGER_PCPD_616_SPORT.value)
    )
    HUNTER_PCPD_SPUR = (
        "First Car Win - Hunter PCPD Spur",
        LOCATIONS_OFFSET_UNIQUE_WINS + 108,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.HUNTER_PCPD_SPUR.value)
    )
    MONTGOMERY_PCPD_GT_2400 = (
        "First Car Win - Montgomery PCPD GT 2400",
        LOCATIONS_OFFSET_UNIQUE_WINS + 109,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.MONTGOMERY_PCPD_GT_2400.value)
    )
    JANSEN_PCPD_P12 = (
        "First Car Win - Jansen PCPD P12",
        LOCATIONS_OFFSET_UNIQUE_WINS + 110,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.JANSEN_PCPD_P12.value)
    )
    CARSON_PCPD_INFERNO_VAN = (
        "First Car Win - Carson PCPD Inferno Van",
        LOCATIONS_OFFSET_UNIQUE_WINS + 111,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.CARSON_PCPD_INFERNO_VAN.value)
    )
    ROSSOLINI_PCPD_TEMPESTA = (
        "First Car Win - Rossolini PCPD Tempesta",
        LOCATIONS_OFFSET_UNIQUE_WINS + 112,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.ROSSOLINI_PCPD_TEMPESTA.value)
    )
    CARSON_PCPD_OPUS = (
        "First Car Win - Carson PCPD Opus",
        LOCATIONS_OFFSET_UNIQUE_WINS + 113,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.CARSON_PCPD_OPUS.value)
    )
    CARSON_PCPD_ANNIHILATOR = (
        "First Car Win - Carson PCPD Annihilator",
        LOCATIONS_OFFSET_UNIQUE_WINS + 114,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.CARSON_PCPD_ANNIHILATOR.value)
    )
    JANSEN_PCPD_X12 = (
        "First Car Win - Jansen PCPD X12",
        LOCATIONS_OFFSET_UNIQUE_WINS + 115,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.JANSEN_PCPD_X12.value)
    )
    KITANO_PCPD_TOUGE_SPORT = (
        "First Car Win - Kitano PCPD Touge Sport",
        LOCATIONS_OFFSET_UNIQUE_WINS + 116,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.KITANO_PCPD_TOUGE_SPORT.value)
    )
    HUNTER_PCPD_TAKEDOWN_4X4 = (
        "First Car Win - Hunter PCPD Takedown 4x4",
        LOCATIONS_OFFSET_UNIQUE_WINS + 117,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.HUNTER_PCPD_TAKEDOWN_4X4.value)
    )
    CARSON_PCPD_500_GT = (
        "First Car Win - Carson PCPD 500 GT",
        LOCATIONS_OFFSET_UNIQUE_WINS + 118,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.CARSON_PCPD_500_GT.value)
    )
    HUNTER_PCPD_RACING_OVAL_CHAMP = (
        "First Car Win - Hunter PCPD Racing Oval Champ",
        LOCATIONS_OFFSET_UNIQUE_WINS + 119,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.HUNTER_PCPD_RACING_OVAL_CHAMP.value)
    )
    CARSON_PCPD_GT_CONCEPT = (
        "First Car Win - Carson PCPD GT Concept",
        LOCATIONS_OFFSET_UNIQUE_WINS + 120,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.CARSON_PCPD_GT_CONCEPT.value)
    )
    MONTGOMERY_PCPD_HAWKER = (
        "First Car Win - Montgomery PCPD Hawker",
        LOCATIONS_OFFSET_UNIQUE_WINS + 121,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.MONTGOMERY_PCPD_HAWKER.value)
    )
    KRIEGER_PCPD_UBERSCHALL_8 = (
        "First Car Win - Krieger PCPD Uberschall 8",
        LOCATIONS_OFFSET_UNIQUE_WINS + 122,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.KRIEGER_PCPD_UBERSCHALL_8.value)
    )
    CARSON_PCPD_THUNDER_CUSTOM = (
        "First Car Win - Carson PCPD Thunder Custom",
        LOCATIONS_OFFSET_UNIQUE_WINS + 123,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.CARSON_PCPD_THUNDER_CUSTOM.value)
    )
    CARSON_PCPD_HOT_ROD_COUPE = (
        "First Car Win - Carson PCPD Hot Rod Coupe",
        LOCATIONS_OFFSET_UNIQUE_WINS + 124,
        Regions.DOWNTOWN_PARADISE,
        Has(CopCars.CARSON_PCPD_HOT_ROD_COUPE.value)
    )

class BigSurfIslandCarWinLocations(LocationTypeEnum):
    CARSON_DUST_STORM = (
        "First Car Win - Carson Dust Storm",
        LOCATIONS_OFFSET_UNIQUE_WINS + 125,
        Regions.DOWNTOWN_PARADISE,
        Has(BigSurfIslandCars.CARSON_DUST_STORM.value)
    )
    CARSON_DUST_STORM_SUPERTURBO = (
        "First Car Win - Carson Dust Storm Superturbo",
        LOCATIONS_OFFSET_UNIQUE_WINS + 126,
        Regions.DOWNTOWN_PARADISE,
        Has(BigSurfIslandCars.CARSON_DUST_STORM_SUPERTURBO.value)
    )
    JANSEN_P12_DIAMOND = (
        "First Car Win - Jansen P12 Diamond",
        LOCATIONS_OFFSET_UNIQUE_WINS + 127,
        Regions.DOWNTOWN_PARADISE,
        Has(BigSurfIslandCars.JANSEN_P12_DIAMOND.value)
    )
    HUNTER_OLYMPUS_GOVERNOR = (
        "First Car Win - Hunter Olympus Governor",
        LOCATIONS_OFFSET_UNIQUE_WINS + 128,
        Regions.DOWNTOWN_PARADISE,
        Has(BigSurfIslandCars.HUNTER_OLYMPUS_GOVERNOR.value)
    )
    CARSON_ANNIHILATOR_STREET_ROD = (
        "First Car Win - Carson Annihilator Street Rod",
        LOCATIONS_OFFSET_UNIQUE_WINS + 129,
        Regions.DOWNTOWN_PARADISE,
        Has(BigSurfIslandCars.CARSON_ANNIHILATOR_STREET_ROD.value)
    )
    HUNTER_TOY_BOOTLEGGER = (
        "First Car Win - Hunter Toy Bootlegger",
        LOCATIONS_OFFSET_UNIQUE_WINS + 130,
        Regions.DOWNTOWN_PARADISE,
        Has(BigSurfIslandCars.HUNTER_TOY_BOOTLEGGER.value)
    )
    JANSEN_TOY_88_SPECIAL = (
        "First Car Win - Jansen Toy 88 Special",
        LOCATIONS_OFFSET_UNIQUE_WINS + 131,
        Regions.DOWNTOWN_PARADISE,
        Has(BigSurfIslandCars.JANSEN_TOY_88_SPECIAL.value)
    )
    CARSON_TOY_NIGHTHAWK = (
        "First Car Win - Carson Toy Nighthawk",
        LOCATIONS_OFFSET_UNIQUE_WINS + 132,
        Regions.DOWNTOWN_PARADISE,
        Has(BigSurfIslandCars.CARSON_TOY_NIGHTHAWK.value)
    )
    HUNTER_TOY_SPIRIT = (
        "First Car Win - Hunter Toy Spirit",
        LOCATIONS_OFFSET_UNIQUE_WINS + 133,
        Regions.DOWNTOWN_PARADISE,
        Has(BigSurfIslandCars.HUNTER_TOY_SPIRIT.value)
    )

class ParadiseBikesWinLocations(LocationTypeEnum):
    NAKAMURA_FV1100 = (
        "First Car Win - Nakamura FV1100",
        LOCATIONS_OFFSET_UNIQUE_WINS + 134,
        Regions.DOWNTOWN_PARADISE,
        Has(ParadiseBikes.NAKAMURA_FV1100.value)
    )
    NAKAMURA_FV1100_TI = (
        "First Car Win - Nakamura FV1100-TI",
        LOCATIONS_OFFSET_UNIQUE_WINS + 135,
        Regions.DOWNTOWN_PARADISE,
        Has(ParadiseBikes.NAKAMURA_FV1100_TI.value)
    )
    NAKAMURA_FIREHAWK_V4 = (
        "First Car Win - Nakamura Firehawk V4",
        LOCATIONS_OFFSET_UNIQUE_WINS + 136,
        Regions.DOWNTOWN_PARADISE,
        Has(ParadiseBikes.NAKAMURA_FIREHAWK_V4.value)
    )
    NAKAMURA_FIREHAWK_GP_COMPETITION = (
        "First Car Win - Nakamura Firehawk GP Competition",
        LOCATIONS_OFFSET_UNIQUE_WINS + 137,
        Regions.DOWNTOWN_PARADISE,
        Has(ParadiseBikes.NAKAMURA_FIREHAWK_GP_COMPETITION.value)
    )

