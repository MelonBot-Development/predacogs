from random import choice

# Stuff for the cog
def emoji():
    """Randomize footer emojis."""
    EMOJIS = [
        "\N{AUBERGINE}",
        "\N{SMIRKING FACE}",
        "\N{PEACH}",
        "\N{SPLASHING SWEAT SYMBOL}",
        "\N{BANANA}",
        "\N{KISS MARK}",
    ]
    emoji = choice(EMOJIS)
    return emoji


REDDIT_BASEURL = "https://api.reddit.com/r/{}/random"
IMGUR_LINKS = ("http://imgur.com", "https://m.imgur.com", "https://imgur.com")
GOOD_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif")

# Subreddits
FOUR_K = [
    "HighResNSFW",
    "UHDnsfw",
    "nsfw_hd",
    "NSFW_Wallpapers",
    "closeup",
    "Hegre",
    "HighResASS",
    "SexyWallpapers",
]
AHEGAO = ["AhegaoGirls", "RealAhegao", "EyeRollOrgasm", "MouthWideOpen", "O_Faces"]
ASS = [
    "ass",
    "pawg",
    "AssholeBehindThong",
    "girlsinyogapants",
    "girlsinleggings",
    "bigasses",
    "asshole",
    "AssOnTheGlass",
    "TheUnderbun",
    "asstastic",
    "booty",
    "AssReveal",
    "beautifulbutt",
    "Mooning",
    "BestBooties",
    "brunetteass",
    "assinthong",
    "paag",
    "asstastic",
    "GodBooty",
    "Underbun",
    "datass",
    "ILikeLittleButts",
    "datgap",
    "HungryButts",
    "Upshorts",
    "TwistButt",
    "SnakeButt",
    "ButtsAndBareFeet",
    "HighResASS",
    "hugeass",
]
ASIANPORN = [
    "AmateurAsianGirls",
    "asian_gifs",
    "AsianHotties",
    "AsianCuties",
    "AsianNSFW",
    "AsianPorn",
    "AsiansGoneWild",
    "AmateurAsianGirls",
    "AsianNSFW",
    "bustyasians",
    "juicyasians",
    "AsianPussy",
    "AmateurAsianGirls",
    "AsianAmericanHotties",
    "KoreanHotties",
    "NSFW_Korea",
    "NSFW_Japan",
    "AsiansGoneWild",
]
ANAL = [
    "MasterOfAnal",
    "anal",
    "buttsex",
    "buttsthatgrip",
    "AnalGW",
    "analinsertions",
    "assholegonewild",
    "sodomy",
    "NotInThePussy",
]
BBW = ["BBW", "BBW_Chubby", "BBWVideos", "chubby", "PerkyChubby", "gonewildcurvy", "GoneWildPlus"]
BDSM = ["BDSMGW", "bdsm", "ropeart", "shibari", "Bondage", "Spanking", "BDSM_NoSpam", "kinbaku"]
BLACKCOCK = ["ChurchOfTheBBC", "blackcock", "Blackdick", "bigblackcocks"]
BLOWJOB = [
    "blowjobsandwich",
    "Blowjobs",
    "BlowjobGifs",
    "BlowjobEyeContact",
    "AsianBlowjobs",
    "SuckingItDry",
    "OralCreampie",
    "SwordSwallowers",
    "fellatio",
]
BOOBS = [
    "boobs",
    "TheHangingBoobs",
    "bigboobs",
    "BigBoobsGW",
    "hugeboobs",
    "pokies",
    "ghostnipples",
    "PiercedNSFW",
    "piercedtits",
    "PerfectTits",
    "BestTits",
    "Boobies",
    "tits",
    "naturaltitties",
    "smallboobs",
    "Nipples",
    "homegrowntits",
    "TheUnderboob",
    "BiggerThanYouThought",
    "fortyfivefiftyfive",
    "Stacked",
    "BigBoobsGonewild",
    "AreolasGW",
    "TittyDrop",
    "Titties",
    "Boobies",
    "boobbounce",
    "TinyTits",
    "cleavage",
    "BoobsBetweenArms",
    "BustyNaturals",
    "burstingout",
    "boobgifs",
    "BustyPetite",
]
BOTTOMLESS = ["upskirt", "Bottomless", "nopanties", "Pantiesdown"]
COSPLAY = [
    "nsfwcosplay",
    "cosplayonoff",
    "Cosplayheels",
    "CosplayBoobs",
    "gwcosplay",
    "CosplayLewd",
    "CosplayBeauties",
]
CUNNI = ["cunnilingus", "CunnilingusSelfie", "Hegoesdown"]
CUMSHOTS = [
    "cumfetish",
    "cumontongue",
    "cumshots",
    "CumshotSelfies",
    "facialcumshots",
    "pulsatingcumshots",
    "gwcumsluts",
    "ImpresssedByCum",
    "GirlsFinishingTheJob",
    "amateurcumsluts",
    "unexpectedcum",
    "bodyshots",
    "ContainTheLoad",
]
DEEPTHROAT = [
    "deepthroat_gifs",
    "AmateurDeepthroat",
    "DeepThroatTears",
    "deepthroat",
    "SwordSwallowers",
]
DICK = ["DickPics4Freedom", "MassiveCock", "penis", "cock", "ThickDick", "bulges", "twinks"]
DOUBLE_P = ["doublepenetration", "dp_porn", "Technical_DP"]
EBONY = [
    "Ebony",
    "ebonyamateurs",
    "EbonyGirls",
    "blackchickswhitedicks",
    "bigblackasses",
    "blackporn",
    "DarkAngels",
]
FACIALS = ["facial", "facialcumshots", "FacialFun"]
FEET = [
    "ButtsAndBareFeet",
    "Feet_NSFW",
    "feetish",
    "Feetup",
    "rule34feet",
    "StomachDownFeetUp",
    "FootFetish",
    "legsup",
]
FEMDOM = ["Femdom", "femdom", "FemdomHumiliation", "hentaifemdom"]
FUTA = [
    "FutanariHentai",
    "FutanariPegging",
    "HorsecockFuta",
    "Rule34_Futanari",
    "rule34futanari",
    "hugefutanari",
    "Futadomworld",
]
GAY_P = [
    "gayporn",
    "ladybonersgw",
    "bulges",
    "broslikeus",
    "gaygifs",
    "GayGifs",
    "gayporn",
    "gaybears",
    "CuteGuyButts",
    "gaynsfw",
    "lovegaymale",
    "NSFW_GAY",
    "ManSex",
    "malepornstars",
    "manlove",
    "manass",
    "GayDaddiesPics",
    "gayotters",
    "Singlets",
    "jockstraps",
    "guyskissing",
]
GROUPS = ["GroupOfNudeGirls", "GroupOfNudeMILFs", "groupsex"]
# HENTAI = ["hentai", "thick_hentai", "HQHentai", "AnimeBooty", "thighdeology"]
# HENTAI_GIFS = ["ecchigifs", "nsfwanimegifs", "oppai_gif"]
LESBIANS = [
    "lesbians",
    "HDLesbianGifs",
    "amateurlesbians",
    "Lesbian_gifs",
    "titstouchingtits",
    "dyke",
    "scissoring",
    "StraightGirlsPlaying",
    "mmgirls",
    "girlskissing",
    "Lesbos",
    "Ass_to_ssA",
]
MILF = [
    "amateur_milfs",
    "GroupOfNudeMILFs",
    "milf",
    "Milfie",
    "hairymilfs",
    "HotAsianMilfs",
    "HotMILFs",
    "MILFs",
    "maturemilf",
    "puremilf",
    "amateur_milfs",
    "cougars",
    "AgedBeauty",
]
ORAL = [
    "blowjobsandwich",
    "Blowjobs",
    "BlowjobGifs",
    "BlowjobEyeContact",
    "AsianBlowjobs",
    "SuckingItDry",
    "OralCreampie",
    "cunnilingus",
    "CunnilingusSelfie",
    "Hegoesdown",
    "DeepThroatTears",
    "deepthroat",
    "ballsucking",
    "SwordSwallowers",
]
PUBLIC = [
    "RealPublicNudity",
    "FlashingAndFlaunting",
    "FlashingGirls",
    "PublicFlashing",
    "Unashamed",
    "NudeInPublic",
    "publicplug",
    "casualnudity",
    "bitchinbubba",
    "FlashingTheGoods",
    "Flashing",
    "girlsflashing",
    "holdthemoan",
    "exposedinpublic",
    "ChangingRooms",
    "gwpublic",
    "NotSafeForNature",
    "WoodNymphs",
    "snowgirls",
    "NSFW_Outdoors",
]
PUSSY = [
    "pussy",
    "GodPussy",
    "AsianPussy",
    "rearpussy",
    "PussyFlashing",
    "Innies",
    "pelfie",
    "GirlsWithToys",
    "simps",
    "LabiaGW",
    "grool",
    "MoundofVenus",
    "LipsThatGrip",
    "FireCrotch",
    "HairyPussy",
    "legsup",
    "spreadeagle",
    "PussyMound",
    "PerfectPussies",
    "TheRearPussy",
    "peachlips",
    "AsianPussy",
]
REAL_GIRLS = ["RealGirls", "Nude_Selfie", "selfshots", "CellShots", "ChangingRooms", "selfpix"]
REDHEADS = [
    "redheadxxx",
    "redheads",
    "ginger",
    "FireBush",
    "FreckledRedheads",
    "redhead",
    "RedheadGifs",
    "nsfw_redhead",
    "RedheadsPorn",
    "gingerporn",
    "AlexTanner",
    "FireCrotch",
]
RULE_34 = [
    "rule34",
    "rule34cartoons",
    "Rule_34",
    "Rule34LoL",
    "Overwatch_Porn",
    "Rule34Overwatch",
    "WesternHentai",
    "Naruto_Hentai",
]
SQUIRTS = ["GushingGirls", "squirting_gifs", "squirting"]
THIGHS = [
    "Thighs",
    "ThickThighs",
    "thighhighs",
    "Thigh",
    "leggingsgonewild",
    "legsup",
    "datgap",
    "legs",
    "theratio",
    "legsup",
]
THREESOME = [
    "groupsex",
    "Threesome",
    "amateur_threesomes",
    "Xsome",
    "AirTight",
    "Triplepenetration",
    "RealThreesomes",
    "SpitRoasted",
]
TRAPS = [
    "Transex",
    "DeliciousTraps",
    "traps",
    "trapgifs",
    "GoneWildTrans",
    "SexyShemales",
    "Shemales",
    "shemale_gifs",
    "Shemales",
    "ShemalesParadise",
    "Shemale_Big_Cock",
    "ShemaleGalleries",
]
WILD = [
    "gonewild",
    "GWNerdy",
    "dirtysmall",
    "MyCalvins",
    "AsiansGoneWild",
    "GoneWildSmiles",
    "gonewildcurvy",
    "BigBoobsGonewild",
    "gonewildcouples",
    "gonewildcolor",
    "PetiteGoneWild",
    "GWCouples",
    "BigBoobsGW",
    "altgonewild",
    "LabiaGW",
    "UnderwearGW",
    "JustTheTop",
    "TallGoneWild",
    "LingerieGW",
    "Swingersgw",
    "workgonewild",
    "gonewildcurvy",
    "GWNerdy",
    "gwpublic",
    "ArtGW",
    "bigonewild",
    "GirlsWithBikes",
    "librarygirls",
]
YIFF = ["Yiffbondage", "Hyiff", "femyiff", "yiff", "yiffgif"]

# Other APIs
NEKOBOT_HENTAI = choice(["hentai_anal", "hentai"])
NEKOBOT_URL = "https://nekobot.xyz/api/image?type={}"
