from collections import Counter
from BaseClasses import ItemClassification
from worlds.burnout_paradise_remastered.data import CarItemTypeEnum, BoostType

class Cars(CarItemTypeEnum):
    HUNTER_OVAL_CHAMP_69 = ("Hunter Oval Champ 69", 0xD676FB5119E20, ItemClassification.useful, BoostType.CRASH)
    HUNTER_MESQUITE_CUSTOM = ("Hunter Mesquite Custom", 0xD676F97EFEC34, ItemClassification.useful, BoostType.CRASH)
    NAKAMURA_RACING_SI_7 = ("Nakamura Racing SI-7", 0xD38DAEEA988B4, ItemClassification.useful, BoostType.SPEED)
    HUNTER_VEGAS_CARNIVALE = ("Hunter Vegas Carnivale", 0xD676C159EDC20, ItemClassification.useful, BoostType.STUNT)
    KRIEGER_PIONEER_SUPER_GATOR = ("Krieger Pioneer Super Gator", 0xD424F47F18A20, ItemClassification.useful, BoostType.CRASH)
    NAKAMURA_IKUSA_SAMURAI = ("Nakamura Ikusa Samurai", 0xD38DAEE966C20, ItemClassification.useful, BoostType.STUNT)
    KITANO_HYDROS_TECHNO = ("Kitano Hydros Techno", 0xD38DAC870CC20, ItemClassification.useful, BoostType.SPEED)
    HUNTER_RELIABLE_SPECIAL = ("Hunter Reliable Special", 0xD676C3D7F1F8E, ItemClassification.useful, BoostType.CRASH)
    WATSON_BURNOUT_ROADSTER = ("Watson Burnout Roadster", 0xD4248E9278B80, ItemClassification.useful, BoostType.STUNT)
    ROSSOLINI_LM_TRACK_PACKAGE = ("Rossolini LM Track Package", 0xD424C965533F4, ItemClassification.useful, BoostType.SPEED)
    HUNTER_MANHATTAN_CUSTOM = ("Hunter Manhattan Custom", 0xD676BB640CC20, ItemClassification.useful, BoostType.STUNT)
    CARSON_FASTBACK_SPECIAL = ("Carson Fastback Special", 0xD676FF9BF8EB0, ItemClassification.useful, BoostType.SPEED)
    CARSON_GRAND_SICILIAN = ("Carson Grand Sicilian", 0xA7E5EB1526820, ItemClassification.useful, BoostType.CRASH)
    MONTGOMERY_HYPERION_RATTLER = ("Montgomery Hyperion Rattler", 0xD424F3E682220, ItemClassification.useful, BoostType.STUNT)
    KRIEGER_616_ARACHNO_SPORT = ("Krieger 616 Arachno Sport", 0xD424F1A2EA474, ItemClassification.useful, BoostType.SPEED)
    HUNTER_HOTSPUR = ("Hunter Hotspur", 0xD676FD4103020, ItemClassification.useful, BoostType.CRASH)
    MONTGOMERY_SABOTAGE_GT_2400 = ("Montgomery Sabotage GT 2400", 0xD424EBAD09474, ItemClassification.useful, BoostType.SPEED)
    JANSEN_P12_TRACK_PACKAGE = ("Jansen P12 Track Package", 0xD67720B7FDC20, ItemClassification.useful, BoostType.STUNT)
    CARSON_INFERNO_BRT_VAN = ("Carson Inferno BRT Van", 0xD676C4256CDF4, ItemClassification.useful, BoostType.CRASH)
    ROSSOLINI_TEMPESTA_GT = ("Rossolini Tempesta GT", 0xD424F1A1F5870, ItemClassification.useful, BoostType.SPEED)
    CARSON_OPUS_XS = ("Carson Opus XS", 0xD676F93B0B220, ItemClassification.useful, BoostType.STUNT)
    CARSON_ANNIHILATOR_PHOENIX = ("Carson Annihilator Phoenix", 0xD676FB773F820, ItemClassification.useful, BoostType.CRASH)
    JANSEN_XS12 = ("Jansen XS12", 0xA59402A920C20, ItemClassification.useful, BoostType.SPEED)
    KITANO_TOUGE_CRITERION = ("Kitano Touge Criterion", 0xD38DB0D94FE20, ItemClassification.useful, BoostType.STUNT)
    HUNTER_TAKEDOWN_DIRT_RACER = ("Hunter Takedown Dirt Racer", 0xD677100787C20, ItemClassification.useful, BoostType.CRASH)
    CARSON_RACING_500_GT = ("Carson Racing 500 GT", 0xD6771AC21CC20, ItemClassification.useful, BoostType.SPEED)
    HUNTER_BRT_OVAL_CHAMP = ("Hunter BRT Oval Champ", 0xD6771C65BAA20, ItemClassification.useful, BoostType.CRASH)
    CARSON_GT_FLAME = ("Carson GT Flame", 0xD676FBC38AC20, ItemClassification.useful, BoostType.STUNT)
    HUNTER_CIVILIAN = ("Hunter Civilian", 0xD676C166913B4, ItemClassification.useful, BoostType.CRASH)
    WATSON_REVENGE_RACER = ("Watson Revenge Racer", 0xD424EDF0A1220, ItemClassification.useful, BoostType.SPEED)
    MONTGOMERY_HAWKER_SOLO = ("Montgomery Hawker Solo", 0xD424F17A86500, ItemClassification.useful, BoostType.STUNT)
    KRIEGER_UBERSCHALL_CLEAR_VIEW = ("Krieger Überschall Clear-View", 0xD424EC43B9C93, ItemClassification.useful, BoostType.SPEED)
    CARSON_THUNDER_SHADOW = ("Carson Thunder Shadow", 0xD676C2A7F49F4, ItemClassification.useful, BoostType.CRASH)
    CARSON_TRIBAL_SPECIAL = ("Carson Tribal Special", 0xD676BC22C8E20, ItemClassification.useful, BoostType.STUNT)
    KRIEGER_PCPD_SPECIAL = ("Krieger PCPD Special", 0xA7E5D5809C480, ItemClassification.useful, BoostType.SPEED)

    # NAKAMURA_IKUSA_GT_BZ = ("Nakamura B'Z Ikusa GT ", 0xA798843603C00, ItemClassification.useful)  # added
    # KITANO_HYDROS_MICROMANIA_CUSTOM = ("Kitano Hydros Micromania Custom", 0xA798C34D34570, ItemClassification.useful)  # sponsor
    # KITANO_GAMESTOP_SPORT = ("Kitano Gamespot Sport", 0xA7989E674C7C0, ItemClassification.useful)  # sponsor
    # OVAL_STEEL_RACER = ("Oval Steel Racer", 0xA566038412870, ItemClassification.useful)  # sponsor
    # TIGER_GT = ("Tiger GT", 0xA5235AA8AE1CF, ItemClassification.useful) - livery for GT Concept
    # TEMPESTA_DREAM = ("Tempesta Dream", 0xA5234FBC86D60, ItemClassification.useful) - livery for Tempesta
    # HIPPY_VAN = ("Hippy Van", 0xA566020D0000D, ItemClassification.useful)

class BurningCars(CarItemTypeEnum):
    HUNTER_CAVALRY = ("Hunter Cavalry", 0xA7E60F1A3A360, ItemClassification.progression, BoostType.STUNT)
    HUNTER_MESQUITE = ("Hunter Mesquite", 0xA7E5D4F26592D, ItemClassification.progression, BoostType.CRASH)
    NAKAMURA_SI_7 = ("Nakamura SI-7", 0xA4FCC11A5567C, ItemClassification.progression, BoostType.SPEED)
    HUNTER_VEGAS = ("Hunter Vegas", 0xA7E5D37F70360, ItemClassification.progression, BoostType.STUNT)
    KRIEGER_PIONEER = ("Krieger Pioneer", 0xA59406A49B160, ItemClassification.progression, BoostType.CRASH)
    NAKAMURA_IKUSA_GT = ("Nakamura Ikusa GT", 0xA4FCC10EE9360, ItemClassification.progression, BoostType.STUNT)
    KITANO_HYDROS_CUSTOM = ("Kitano Hydros Custom", 0xA4FCBEB7FB67C, ItemClassification.progression, BoostType.SPEED)
    HUNTER_RELIABLE_CUSTOM = ("Hunter Reliable Custom", 0xA7E5D607EFD60, ItemClassification.progression, BoostType.CRASH)
    WATSON_R_TURBO_ROADSTER = ("Watson R-Turbo Roadster", 0xA593A0B813960, ItemClassification.progression, BoostType.STUNT)
    ROSSOLINI_LM_CLASSIC = ("Rossolini LM Classic", 0xA593DB9421760, ItemClassification.progression, BoostType.SPEED)
    HUNTER_MANHATTAN = ("Hunter Manhattan", 0xA7E5CD898F360, ItemClassification.progression, BoostType.STUNT)
    CARSON_FASTBACK = ("Carson Fastback", 0xA7E60D533AB80, ItemClassification.progression, BoostType.SPEED)
    CARSON_GRAND_MARAIS = ("Carson Grand Marais", 0xA7E5EB0AA8F60, ItemClassification.progression, BoostType.CRASH)
    MONTGOMERY_HYPERION = ("Montgomery Hyperion", 0xA594060C04960, ItemClassification.progression, BoostType.STUNT)
    KRIEGER_616_SPORT = ("Krieger 616 Sport", 0xA59403CFDC6B0, ItemClassification.progression, BoostType.SPEED)
    HUNTER_SPUR = ("Hunter Spur", 0xA7E60F6685760, ItemClassification.progression, BoostType.CRASH)
    MONTGOMERY_GT_2400 = ("Montgomery GT 2400", 0xA593FDD9FB6B0, ItemClassification.progression, BoostType.SPEED)
    JANSEN_P12 = ("Jansen P12", 0xA7E632DD80360, ItemClassification.progression, BoostType.STUNT)
    CARSON_INFERNO_VAN = ("Carson Inferno Van", 0xA7E5D6543B160, ItemClassification.progression, BoostType.CRASH)
    ROSSOLINI_TEMPESTA = ("Rossolini Tempesta", 0xA59403CFD6508, ItemClassification.progression, BoostType.SPEED)
    CARSON_OPUS = ("Carson Opus", 0xA7E60B608D960, ItemClassification.progression, BoostType.STUNT)
    CARSON_ANNIHILATOR = ("Carson Annihilator", 0xA7E60F1A40508, ItemClassification.progression, BoostType.CRASH)
    JANSEN_X12 = ("Jansen X12", 0xA59403CFE2858, ItemClassification.progression, BoostType.SPEED)
    KITANO_TOUGE_SPORT = ("Kitano Touge Sport", 0xA4FCC2D988700, ItemClassification.progression, BoostType.STUNT)
    HUNTER_TAKEDOWN_4X4 = ("Hunter Takedown 4x4", 0xA7E6222D0A360, ItemClassification.progression, BoostType.CRASH)
    CARSON_500_GT = ("Carson 500 GT", 0xA7E62CE79F360, ItemClassification.progression, BoostType.SPEED)
    HUNTER_RACING_OVAL_CHAMP = ("Hunter Racing Oval Champ", 0xA7E62E8B3D160, ItemClassification.progression, BoostType.CRASH)
    CARSON_GT_CONCEPT = ("Carson GT Concept", 0xA7E60F1A4C858, ItemClassification.progression, BoostType.STUNT)
    HUNTER_CITIZEN = ("Hunter Citizen", 0xA7E5D3964E17C, ItemClassification.progression, BoostType.CRASH)
    WATSON_25_V16_REVENGE = ("Watson 25 V16 Revenge", 0xA594001623960, ItemClassification.progression, BoostType.SPEED)
    MONTGOMERY_HAWKER = ("Montgomery Hawker", 0xA5940206E8700, ItemClassification.progression, BoostType.STUNT)
    KRIEGER_UBERSCHALL_8 = ("Krieger Überschall 8", 0xA593FE7285B60, ItemClassification.progression, BoostType.SPEED)
    CARSON_THUNDER_CUSTOM = ("Carson Thunder Custom", 0xA7E5D4D6C2D60, ItemClassification.progression, BoostType.CRASH)
    CARSON_HOT_ROD_COUPE = ("Carson Hot Rod Coupe", 0xA7E5CE484B560, ItemClassification.progression, BoostType.STUNT)
    KRIEGER_RACING_WTR = ("Krieger Racing WTR", 0xA7E62DCC80F60, ItemClassification.progression, BoostType.SPEED)

class CarbonCars(CarItemTypeEnum):
    NAKAMURA_CARBON_IKUSA_GT = ("Nakamura Carbon Ikusa GT", 0x59504DAA96298, ItemClassification.useful, BoostType.CRASH)
    KITANO_CARBON_HYDROS_CUSTOM = ("Kitano Carbon Hydros Custom", 0x59504DAB6F4B7, ItemClassification.useful, BoostType.STUNT)
    JANSEN_CARBON_X12 = ("Jansen Carbon X12", 0x5950503D2DDCF, ItemClassification.useful, BoostType.STUNT)
    CARSON_CARBON_GT_CONCEPT = ("Carson Carbon GT Concept", 0x59504F584C1CF, ItemClassification.useful, BoostType.SPEED)
    MONTGOMERY_CARBON_HAWKER = ("Montgomery Carbon Hawker", 0x5950502A6E0EF, ItemClassification.useful, BoostType.SPEED)
    KRIEGER_CARBON_UBERSCHALL_8 = ("Krieger Carbon Uberschall 8", 0x59504E259C4D8, ItemClassification.useful, BoostType.STUNT)

class OnlineCars(CarItemTypeEnum):
    HUNTER_OLYMPUS = ("Hunter Olympus", 0xA5235611C067C, ItemClassification.useful, BoostType.SPECIAL)
    NAKAMURA_RAI_JIN_TURBO = ("Nakamura Rai-Jin Turbo", 0xA56C12301BD60, ItemClassification.useful, BoostType.SPECIAL)

class ToyCars(CarItemTypeEnum):
    HUNTER_TOY_CAVALRY = ("Hunter Toy Cavalry", 0xA78D955662360, ItemClassification.useful, BoostType.STUNT)
    CARSON_TOY_GT_CONCEPT = ("Carson Toy GT Concept", 0xA78D955674858, ItemClassification.useful, BoostType.STUNT)
    KRIEGER_TOY_WTR = ("Krieger Toy WTR", 0xA78DB408A8F60, ItemClassification.useful, BoostType.SPEED)
    JANSEN_TOY_P12 = ("Jansen Toy P12", 0xA78DB919A8360, ItemClassification.useful, BoostType.STUNT)
    HUNTER_TOY_MANHATTAN = ("Hunter Toy Manhattan", 0xA78D53C5B7360, ItemClassification.useful, BoostType.STUNT)
    HUNTER_TOY_TAKEDOWN_4X4 = ("Hunter Toy Takedown 4x4", 0xA78DA86932360, ItemClassification.useful, BoostType.CRASH)
    HUNTER_TOY_CITIZEN = ("Hunter Toy Citizen", 0xA78D59D27617C, ItemClassification.useful, BoostType.CRASH)
    CARSON_TOY_INFERNO = ("Carson Toy Inferno", 0xA78D5C9063160, ItemClassification.useful, BoostType.CRASH)
    NAKAMURA_TOY_FIREHAWK_GP = ("Nakamura Toy Firehawk GP", 0xA78D738010800, ItemClassification.progression, BoostType.SPECIAL)

class LegendaryCars(CarItemTypeEnum):
    JANSEN_P12_88_SPECIAL = ("Jansen P12 88 Special", 0xA56601CB30510, ItemClassification.useful, BoostType.STUNT)
    HUNTER_MANHATTAN_SPIRIT = ("Hunter Manhattan Spirit", 0xA566029213D80, ItemClassification.useful, BoostType.CRASH)
    CARSON_GT_NIGHTHAWK = ("Carson GT Nighthawk", 0xA56603AC7063C, ItemClassification.useful, BoostType.SPEED)
    HUNTER_CAVALRY_BOOTLEGGER = ("Hunter Cavalry Bootlegger", 0xA566029B9D400, ItemClassification.useful, BoostType.STUNT)

class BoostSpecialCars(CarItemTypeEnum):
    CARSON_EXTREME_HOT_ROD = ("Carson Extreme Hot Rod", 0xA56CA6E6C9960, ItemClassification.useful, BoostType.SPECIAL)
    MONTGOMERY_HAWKER_MECH = ("Montgomery Hawker Mech", 0xA5231316B5760, ItemClassification.useful, BoostType.SPECIAL)

class CopCars(CarItemTypeEnum):
    HUNTER_PCPD_CAVALRY = ("Hunter PCPD Cavalry", 0xA5389B073A360, ItemClassification.useful, BoostType.STUNT)
    HUNTER_PCPD_MESQUITE = ("Hunter PCPD Mesquite", 0xA53860DF71048, ItemClassification.useful, BoostType.CRASH)
    NAKAMURA_PCPD_SI_7 = ("Nakamura PCPD SI-7", 0xA5385BE45567C, ItemClassification.useful, BoostType.SPEED)
    HUNTER_PCPD_VEGAS = ("Hunter PCPD Vegas", 0xA538613633B60, ItemClassification.useful, BoostType.STUNT)
    KRIEGER_PCPD_PIONEER = ("Krieger PCPD Pioneer", 0xA538C19F4B160, ItemClassification.useful, BoostType.CRASH)
    NAKAMURA_PCPD_IKUSA_GT = ("Nakamura PCPD Ikusa GT", 0xA5385BD8E9360, ItemClassification.useful, BoostType.STUNT)
    KITANO_PCPD_HYDROS_CUSTOM = ("Kitano PCPD Hydros Custom", 0xA5385981FB67C, ItemClassification.useful, BoostType.SPEED)
    HUNTER_PCPD_RELIABLE_CUSTOM = ("Hunter PCPD Reliable Custom", 0xA53861F4EFD60, ItemClassification.useful, BoostType.CRASH)
    WATSON_PCPD_R_TURBO_ROADSTER = ("Watson PCPD R-Turbo Roadster", 0xA5385BB2C3960, ItemClassification.useful, BoostType.STUNT)
    ROSSOLINI_PCPD_LM_CLASSIC = ("Rossolini PCPD LM Classic", 0xA538968ED1760, ItemClassification.useful, BoostType.SPEED)
    HUNTER_PCPD_MANHATTAN = ("Hunter PCPD Manhattan", 0xA53859768F360, ItemClassification.useful, BoostType.STUNT)
    CARSON_PCPD_FASTBACK = ("Carson PCPD Fastback", 0xA5389DB8A3780, ItemClassification.useful, BoostType.SPEED)
    CARSON_PCPD_GRAND_MARAIS = ("Carson PCPD Grand Marais", 0xA53876F7A8F60, ItemClassification.useful, BoostType.CRASH)
    MONTGOMERY_PCPD_HYPERION = ("Montgomery PCPD Hyperion", 0xA538C106B4960, ItemClassification.useful, BoostType.STUNT)
    KRIEGER_PCPD_616_SPORT = ("Krieger PCPD 616 Sport", 0xA538BECA8C6B0, ItemClassification.useful, BoostType.SPEED)
    HUNTER_PCPD_SPUR = ("Hunter PCPD Spur", 0xA5389B5385760, ItemClassification.useful, BoostType.CRASH)
    MONTGOMERY_PCPD_GT_2400 = ("Montgomery PCPD GT 2400", 0xA538B8D4AB6B0, ItemClassification.useful, BoostType.SPEED)
    JANSEN_PCPD_P12 = ("Jansen PCPD P12", 0xA538BECA80360, ItemClassification.useful, BoostType.STUNT)
    CARSON_PCPD_INFERNO_VAN = ("Carson PCPD Inferno Van", 0xA53862413B160, ItemClassification.useful, BoostType.CRASH)
    ROSSOLINI_PCPD_TEMPESTA = ("Rossolini PCPD Tempesta", 0xA538BECA86508, ItemClassification.useful, BoostType.SPEED)
    CARSON_PCPD_OPUS = ("Carson PCPD Opus", 0xA538974D8D960, ItemClassification.useful, BoostType.STUNT)
    CARSON_PCPD_ANNIHILATOR = ("Carson PCPD Annihilator", 0xA5389B0740508, ItemClassification.useful, BoostType.CRASH)
    JANSEN_PCPD_X12 = ("Jansen PCPD X12", 0xA538BECA92858, ItemClassification.useful, BoostType.SPEED)
    KITANO_PCPD_TOUGE_SPORT = ("Kitano PCPD Touge Sport", 0xA5385DA388700, ItemClassification.useful, BoostType.STUNT)
    HUNTER_PCPD_TAKEDOWN_4X4 = ("Hunter PCPD Takedown 4x4", 0xA538AE1A0A360, ItemClassification.useful, BoostType.CRASH)
    CARSON_PCPD_500_GT = ("Carson PCPD 500 GT", 0xA538B8D49F360, ItemClassification.useful, BoostType.SPEED)
    HUNTER_PCPD_RACING_OVAL_CHAMP = ("Hunter PCPD Racing Oval Champ", 0xA538BA783D160, ItemClassification.useful, BoostType.CRASH)
    CARSON_PCPD_GT_CONCEPT = ("Carson PCPD GT Concept", 0xA5389B074C858, ItemClassification.useful, BoostType.STUNT)
    MONTGOMERY_PCPD_HAWKER = ("Montgomery PCPD Hawker", 0xA538BD0198700, ItemClassification.useful, BoostType.STUNT)
    KRIEGER_PCPD_UBERSCHALL_8 = ("Krieger PCPD Uberschall 8", 0xA538B96D35B60, ItemClassification.useful, BoostType.SPEED)
    CARSON_PCPD_THUNDER_CUSTOM = ("Carson PCPD Thunder Custom", 0xA5385F6C70360, ItemClassification.useful, BoostType.CRASH)
    CARSON_PCPD_HOT_ROD_COUPE = ("Carson PCPD Hot Rod Coupe", 0xA5385A354B560, ItemClassification.useful, BoostType.STUNT)

class BigSurfIslandCars(CarItemTypeEnum):
    CARSON_DUST_STORM = ("Carson Dust Storm", 0xA55EBC7BF8700, ItemClassification.useful, BoostType.STUNT)
    CARSON_DUST_STORM_SUPERTURBO = ("Carson Dust Storm Superturbo", 0xA55EBC7CD8E4F, ItemClassification.useful, BoostType.STUNT)
    JANSEN_P12_DIAMOND = ("Jansen P12 Diamond", 0xA5231F81B5EC8, ItemClassification.useful, BoostType.STUNT)
    HUNTER_OLYMPUS_GOVERNOR = ("Hunter Olympus Governor", 0xA5235611C08ED, ItemClassification.useful, BoostType.STUNT)
    CARSON_ANNIHILATOR_STREET_ROD = ("Carson Annihilator Street Rod", 0xA522FF6B4EF60, ItemClassification.useful, BoostType.SPEED)
    HUNTER_TOY_BOOTLEGGER = ("Hunter Toy Bootlegger", 0xA78D72EA6ED60, ItemClassification.useful, BoostType.STUNT)
    JANSEN_TOY_88_SPECIAL = ("Jansen Toy 88 Special", 0xA78D4166193C0, ItemClassification.useful, BoostType.STUNT)
    CARSON_TOY_NIGHTHAWK = ("Carson Toy Nighthawk", 0xA78D9D8877960, ItemClassification.useful, BoostType.SPEED)
    HUNTER_TOY_SPIRIT = ("Hunter Toy Spirit", 0xA78D716A01C00, ItemClassification.useful, BoostType.CRASH)

class ParadiseBikes(CarItemTypeEnum):
    NAKAMURA_FV1100 = ("Nakamura FV1100", 0xA7E60F0F736C0, ItemClassification.progression, BoostType.SPECIAL)
    NAKAMURA_FV1100_TI = ("Nakamura FV1100-TI", 0xA7E60F0F6DEDC, ItemClassification.progression, BoostType.SPECIAL)
    NAKAMURA_FIREHAWK_V4 = ("Nakamura Firehawk V4", 0xA7E60EF414960, ItemClassification.progression, BoostType.SPECIAL)
    NAKAMURA_FIREHAWK_GP_COMPETITION = ("Nakamura Firehawk GP Competition", 0xA7E60F03E9EE4, ItemClassification.progression, BoostType.SPECIAL)

_BURNING_CARS_IN_ORDER = [
    BurningCars.HUNTER_CAVALRY,
    BurningCars.HUNTER_MESQUITE,
    BurningCars.NAKAMURA_SI_7,
    BurningCars.HUNTER_VEGAS,
    BurningCars.KRIEGER_PIONEER,
    BurningCars.NAKAMURA_IKUSA_GT,
    BurningCars.KITANO_HYDROS_CUSTOM,
    BurningCars.HUNTER_RELIABLE_CUSTOM,
    BurningCars.WATSON_R_TURBO_ROADSTER,
    BurningCars.ROSSOLINI_LM_CLASSIC,
    BurningCars.HUNTER_MANHATTAN,
    BurningCars.CARSON_FASTBACK,
    BurningCars.CARSON_GRAND_MARAIS,
    BurningCars.MONTGOMERY_HYPERION,
    BurningCars.KRIEGER_616_SPORT,
    BurningCars.HUNTER_SPUR,
    BurningCars.MONTGOMERY_GT_2400,
    BurningCars.JANSEN_P12,
    BurningCars.CARSON_INFERNO_VAN,
    BurningCars.ROSSOLINI_TEMPESTA,
    BurningCars.CARSON_OPUS,
    BurningCars.CARSON_ANNIHILATOR,
    BurningCars.JANSEN_X12,
    BurningCars.KITANO_TOUGE_SPORT,
    BurningCars.HUNTER_TAKEDOWN_4X4,
    BurningCars.CARSON_500_GT,
    BurningCars.HUNTER_RACING_OVAL_CHAMP,
    BurningCars.CARSON_GT_CONCEPT,
    BurningCars.HUNTER_CITIZEN,
    BurningCars.WATSON_25_V16_REVENGE,
    BurningCars.MONTGOMERY_HAWKER,
    BurningCars.KRIEGER_UBERSCHALL_8,
    BurningCars.CARSON_THUNDER_CUSTOM,
    BurningCars.CARSON_HOT_ROD_COUPE,
    BurningCars.KRIEGER_RACING_WTR,
]

def count_boost_type(boost_type: BoostType) -> int:
    counter = Counter()
    for cls in (Cars, BurningCars, CarbonCars, ToyCars, LegendaryCars,
                BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars,
                ParadiseBikes):
        for item in cls:
            counter[item.boosttype] += 1
    return counter.get(boost_type, 0)

def get_paradise_car_names() -> list[str]:
    names = []
    for cls in (Cars, BurningCars, CarbonCars):
        names.extend([member.value for member in cls])
    return names

def get_car_names() -> list[str]:
    names = []
    for cls in (Cars, BurningCars, CarbonCars, ToyCars, LegendaryCars,
                BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars,
                ParadiseBikes):
        names.extend([member.value for member in cls])
    return names
