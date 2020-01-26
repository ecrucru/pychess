import os
import sys
from collections import namedtuple
from pychess.System.cpu import get_cpu


# Constants
AUTO_DETECT = True
NO_AUTO_DETECT = False

# CPUID
cpu = get_cpu()

# List of known interpreters
PYTHONBIN = sys.executable.split("/")[-1]
VM = namedtuple('VM', 'name, ext, args')
VM_LIST = [
    VM("node", ".js", None),
    VM("java", ".jar", ["-jar"]),
    VM(PYTHONBIN, ".py", ["-u"])
]

# Needed by shutil.which() on Windows to find .py engines
if cpu['windows']:
    for vm in VM_LIST:
        if vm.ext.upper() not in os.getenv("PATHEXT"):
            os.environ["PATHEXT"] += ";%s" % vm.ext.upper()

# List of engines later sorted by descending length of name
# The comments provides known conflicts with Linux packages
# Weak engines (<2700) should be added manually unless a package exists already
if cpu['windows']:
    stockfish_name = "stockfish_11_x%s.exe" % cpu['bitness']
    sjaakii_name = "sjaakii_win%s_ms.exe" % cpu['bitness']
else:
    stockfish_name = "stockfish"
    sjaakii_name = "sjaakii"

ENGINE = namedtuple('ENGINE', 'name, protocol, country, elo, autoDetect, defaultLevel')
ENGINES_LIST = [
    # -- Full names for internal processing
    ENGINE("PyChess.py", "xboard", "dk", 0, AUTO_DETECT, 5),
    ENGINE("pychess-engine", "xboard", "dk", 0, AUTO_DETECT, 5),
    ENGINE(stockfish_name, "uci", "no", 3554, AUTO_DETECT, None),
    ENGINE(sjaakii_name, "xboard", "nl", 2194, AUTO_DETECT, None),
    ENGINE("Houdini.exe", "uci", "be", 3526, AUTO_DETECT, None),
    ENGINE("Rybka.exe", "uci", "cz", 3207, AUTO_DETECT, None),

    # -- Engines from CCRL 40/4
    ENGINE("leelenstein", "uci", "unknown", 3622, NO_AUTO_DETECT, None),
    ENGINE("leela", "uci", "us", 3617, NO_AUTO_DETECT, None),
    ENGINE("lczero", "uci", "us", 3617, NO_AUTO_DETECT, None),
    ENGINE("lc0", "uci", "us", 3617, NO_AUTO_DETECT, None),
    ENGINE("fatfritz", "uci", "nl", 3607, NO_AUTO_DETECT, None),
    ENGINE("stockfish", "uci", "no", 3606, AUTO_DETECT, None),
    ENGINE("allie", "uci", "unknown", 3561, NO_AUTO_DETECT, None),
    ENGINE("stoofvlees", "", "be", 3554, NO_AUTO_DETECT, None),
    ENGINE("komodo", "uci", "us", 3524, AUTO_DETECT, None),
    ENGINE("houdini", "uci", "be", 3517, AUTO_DETECT, None),
    ENGINE("xiphos", "uci", "us", 3429, NO_AUTO_DETECT, None),  # xiphos - environment for Bible reading, study, and research
    ENGINE("fire", "uci", "us", 3427, NO_AUTO_DETECT, None),  # fire in mesa-demos https://www.archlinux.org/packages/extra/x86_64/mesa-demos/files/
    ENGINE("ethereal", "uci", "us", 3426, AUTO_DETECT, None),
    ENGINE("fritz", "uci", "nl", 3385, AUTO_DETECT, None),
    ENGINE("laser", "uci", "us", 3366, AUTO_DETECT, None),
    ENGINE("defenchess", "uci", "tr", 3355, AUTO_DETECT, None),
    ENGINE("rofchade", "uci", "nl", 3348, AUTO_DETECT, None),
    ENGINE("fizbo", "uci", "us", 3346, AUTO_DETECT, None),
    ENGINE("andscacs", "uci", "ad", 3336, AUTO_DETECT, None),
    ENGINE("booot", "uci", "ua", 3326, AUTO_DETECT, None),  # Formerly XB
    ENGINE("shredder", "uci", "de", 3323, AUTO_DETECT, None),
    ENGINE("schooner", "xboard", "ca", 3289, AUTO_DETECT, None),
    ENGINE("arasan", "uci", "us", 3273, AUTO_DETECT, None),
    ENGINE("rubichess", "uci", "de", 3264, AUTO_DETECT, None),
    ENGINE("gull", "uci", "ru", 3260, AUTO_DETECT, None),
    ENGINE("equinox", "uci", "it", 3252, AUTO_DETECT, None),
    ENGINE("pedone", "uci", "it", 3247, AUTO_DETECT, None),
    ENGINE("chiron", "uci", "it", 3241, AUTO_DETECT, None),  # Allows XB
    ENGINE("critter", "uci", "sk", 3233, AUTO_DETECT, None),
    ENGINE("vajolet", "uci", "it", 3231, AUTO_DETECT, None),
    ENGINE("hannibal", "uci", "us", 3227, AUTO_DETECT, None),
    ENGINE("nirvana", "uci", "us", 3222, AUTO_DETECT, None),
    ENGINE("rybka", "uci", "cz", 3206, AUTO_DETECT, None),
    ENGINE("texel", "xboard", "se", 3203, AUTO_DETECT, None),  # UCI is an option in the command line
    ENGINE("blackmamba", "uci", "it", 3196, AUTO_DETECT, None),
    ENGINE("wasp", "uci", "us", 3189, AUTO_DETECT, None),
    ENGINE("nemorino", "uci", "de", 3176, AUTO_DETECT, None),  # Allows XB
    ENGINE("senpai", "uci", "fr", 3176, AUTO_DETECT, None),
    # ivanhoe, robbolito, panchess, bouquet, elektro
    # ice (name too short)
    ENGINE("naum", "uci", "rs", 3153, AUTO_DETECT, None),
    ENGINE("strelka", "uci", "ru", 3141, AUTO_DETECT, None),
    ENGINE("protector", "uci", "de", 3128, AUTO_DETECT, None),
    ENGINE("chessbrain", "uci", "de", 3126, AUTO_DETECT, None),  # Allows XB
    ENGINE("hiarcs", "uci", "gb", 3107, AUTO_DETECT, None),
    ENGINE("demolito", "uci", "fr", 3103, AUTO_DETECT, None),
    ENGINE("rodent", "uci", "pl", 3091, AUTO_DETECT, None),
    ENGINE("pesto", "uci", "nl", 3087, NO_AUTO_DETECT, None),
    ENGINE("chess22k", "uci", "nl", 3086, AUTO_DETECT, None),
    ENGINE("pirarucu", "uci", "br", 3085, AUTO_DETECT, None),
    ENGINE("winter", "uci", "ch", 3083, NO_AUTO_DETECT, None),
    ENGINE("cheng", "uci", "cz", 3061, AUTO_DETECT, None),
    ENGINE("crafty", "xboard", "us", 3054, AUTO_DETECT, None),
    ENGINE("marvin", "uci", "se", 3051, AUTO_DETECT, None),  # Allows XB
    ENGINE("bobcat", "uci", "nl", 3050, AUTO_DETECT, None),
    ENGINE("amoeba", "uci", "fr", 3049, AUTO_DETECT, None),
    ENGINE("smarthink", "uci", "ru", 3041, AUTO_DETECT, None),  # Allows XB
    ENGINE("spike", "uci", "de", 3038, AUTO_DETECT, None),  # Allows XB
    ENGINE("alfil", "uci", "es", 3031, AUTO_DETECT, None),
    ENGINE("igel", "uci", "ch", 3030, NO_AUTO_DETECT, None),
    ENGINE("minic", "xboard", "fr", 3028, NO_AUTO_DETECT, None),
    ENGINE("spark", "uci", "nl", 3027, NO_AUTO_DETECT, None),  # spark - Apache tool
    ENGINE("junior", "uci", "il", 3025, AUTO_DETECT, None),
    ENGINE("schess", "uci", "us", 3024, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("sblitz", "uci", "us", 3024, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("deuterium", "uci", "ph", 3019, AUTO_DETECT, None),
    ENGINE("hakkapeliitta", "uci", "fi", 3019, AUTO_DETECT, None),
    ENGINE("exchess", "xboard", "us", 3013, AUTO_DETECT, None),
    ENGINE("gogobello", "uci", "it", 3011, AUTO_DETECT, None),
    ENGINE("invictus", "uci", "ph", 3005, NO_AUTO_DETECT, None),
    ENGINE("topple", "uci", "unknown", 3005, NO_AUTO_DETECT, None),
    ENGINE("tucano", "xboard", "br", 2995, AUTO_DETECT, None),
    ENGINE("scorpio", "xboard", "et", 2994, AUTO_DETECT, None),
    ENGINE("baron", "xboard", "nl", 2991, AUTO_DETECT, None),
    ENGINE("asymptote", "uci", "de", 2987, NO_AUTO_DETECT, None),
    ENGINE("gaviota", "xboard", "ar", 2978, AUTO_DETECT, None),
    ENGINE("zappa", "uci", "us", 2971, AUTO_DETECT, None),
    ENGINE("fabchess", "uci", "de", 2962, NO_AUTO_DETECT, None),
    ENGINE("togaii", "uci", "de", 2962, AUTO_DETECT, None),
    ENGINE("toga2", "uci", "de", 2962, AUTO_DETECT, None),
    ENGINE("counter", "uci", "ru", 2960, NO_AUTO_DETECT, None),
    ENGINE("onno", "uci", "de", 2955, AUTO_DETECT, None),
    ENGINE("thinker", "uci", "ca", 2952, AUTO_DETECT, None),
    ENGINE("bagatur", "uci", "bg", 2947, NO_AUTO_DETECT, None),
    ENGINE("godel", "uci", "es", 2947, AUTO_DETECT, None),  # May allow XB
    ENGINE("sjeng", "xboard", "be", 2940, AUTO_DETECT, None),
    ENGINE("disasterarea", "uci", "de", 2931, AUTO_DETECT, None),
    ENGINE("atlas", "uci", "es", 2925, NO_AUTO_DETECT, None),
    ENGINE("dirty", "xboard", "es", 2925, AUTO_DETECT, None),
    ENGINE("discocheck", "uci", "fr", 2915, AUTO_DETECT, None),
    ENGINE("monolith", "uci", "it", 2913, NO_AUTO_DETECT, None),
    ENGINE("bright", "uci", "nl", 2910, AUTO_DETECT, None),
    ENGINE("minko", "uci", "sv", 2908, AUTO_DETECT, None),
    ENGINE("quazar", "uci", "ru", 2900, AUTO_DETECT, None),
    ENGINE("zurichess", "uci", "ro", 2900, AUTO_DETECT, None),
    ENGINE("daydreamer", "uci", "us", 2891, AUTO_DETECT, None),
    ENGINE("cheese", "uci", "fr", 2888, NO_AUTO_DETECT, None),  # Allows XB; cheese - tool to take pictures and videos from your webcam
    ENGINE("murka", "uci", "by", 2882, AUTO_DETECT, None),
    ENGINE("loop", "uci", "de", 2881, NO_AUTO_DETECT, None),
    ENGINE("tornado", "uci", "de", 2866, AUTO_DETECT, None),
    ENGINE("francesca", "xboard", "gb", 2865, NO_AUTO_DETECT, None),
    ENGINE("nemo", "uci", "de", 2856, NO_AUTO_DETECT, None),  # nemo - File manager and graphical shell for Cinnamon
    ENGINE("bugchess", "xboard", "fr", 2842, AUTO_DETECT, None),
    ENGINE("octochess", "uci", "de", 2824, AUTO_DETECT, None),  # Allows XB
    ENGINE("gnuchessu", "uci", "us", 2808, NO_AUTO_DETECT, None),
    ENGINE("gnuchess", "xboard", "us", 2808, AUTO_DETECT, None),
    ENGINE("ruydos", "uci", "es", 2807, AUTO_DETECT, None),
    ENGINE("rhetoric", "uci", "es", 2805, AUTO_DETECT, None),
    ENGINE("shield", "uci", "it", 2799, NO_AUTO_DETECT, None),
    ENGINE("fridolin", "uci", "de", 2791, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("ktulu", "uci", "ir", 2781, AUTO_DETECT, None),  # Allows XB
    ENGINE("prodeo", "uci", "nl", 2770, AUTO_DETECT, None),  # Allows XB
    ENGINE("twisted-logic", "uci", "ph", 2770, AUTO_DETECT, None),
    ENGINE("frenzee", "xboard", "dk", 2769, AUTO_DETECT, None),
    ENGINE("pawny", "uci", "bg", 2767, AUTO_DETECT, None),
    ENGINE("tomitank", "uci", "hu", 2765, NO_AUTO_DETECT, None),
    ENGINE("jonny", "uci", "de", 2762, AUTO_DETECT, None),  # Formerly XB
    ENGINE("bison", "uci", "ru", 2761, NO_AUTO_DETECT, None),  # bison - YACC-compatible parser generator
    ENGINE("chessmaster", "xboard", "nl", 2757, AUTO_DETECT, None),
    ENGINE("arminius", "xboard", "de", 2752, NO_AUTO_DETECT, None),
    ENGINE("chronos", "uci", "ar", 2739, AUTO_DETECT, None),
    ENGINE("karballo", "uci", "es", 2730, AUTO_DETECT, None),
    ENGINE("tiger", "uci", "gp", 2713, AUTO_DETECT, None),
    ENGINE("devel", "uci", "no", 2712, NO_AUTO_DETECT, None),
    ENGINE("greko", "uci", "ru", 2709, AUTO_DETECT, None),
    ENGINE("ece-x3", "uci", "it", 2700, NO_AUTO_DETECT, None),
    ENGINE("donna", "uci", "us", 2697, NO_AUTO_DETECT, None),
    ENGINE("danasah", "uci", "es", 2690, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("redqueen", "uci", "br", 2689, NO_AUTO_DETECT, None),
    ENGINE("delfi", "uci", "it", 2683, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("djinn", "xboard", "us", 2676, NO_AUTO_DETECT, None),
    ENGINE("pharaon", "uci", "fr", 2674, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("alaric", "uci", "se", 2663, NO_AUTO_DETECT, None),  # Allows XB
    # k2 (name to short)
    ENGINE("gandalf", "uci", "dk", 2661, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("dorky", "xboard", "us", 2653, NO_AUTO_DETECT, None),
    ENGINE("naraku", "uci", "it", 2653, NO_AUTO_DETECT, None),
    ENGINE("nebula", "uci", "rs", 2653, NO_AUTO_DETECT, None),
    ENGINE("phalanx", "xboard1", "cz", 2653, NO_AUTO_DETECT, None),
    ENGINE("colossus", "uci", "gb", 2641, NO_AUTO_DETECT, None),
    ENGINE("cyrano", "uci", "no", 2641, NO_AUTO_DETECT, None),
    ENGINE("sjakk", "uci", "no", 2638, NO_AUTO_DETECT, None),
    ENGINE("rodin", "xboard", "es", 2636, NO_AUTO_DETECT, None),
    ENGINE("et_chess", "xboard2", "fr", 2634, NO_AUTO_DETECT, None),
    ENGINE("wyldchess", "uci", "in", 2630, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("detroid", "uci", "at", 2626, NO_AUTO_DETECT, None),
    ENGINE("weiss", "uci", "no", 2623, NO_AUTO_DETECT, None),
    ENGINE("wildcat", "uci", "by", 2623, NO_AUTO_DETECT, None),  # Formerly XB
    ENGINE("movei", "uci", "il", 2622, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("orion", "uci", "fr", 2621, NO_AUTO_DETECT, None),
    ENGINE("philou", "uci", "fr", 2620, NO_AUTO_DETECT, None),
    ENGINE("rotor", "uci", "nl", 2618, NO_AUTO_DETECT, None),
    ENGINE("zarkov", "xboard", "us", 2617, NO_AUTO_DETECT, None),
    ENGINE("sloppy", "xboard", "fi", 2616, NO_AUTO_DETECT, None),
    ENGINE("coiled", "uci", "es", 2611, NO_AUTO_DETECT, None),
    ENGINE("delocto", "uci", "at", 2611, NO_AUTO_DETECT, None),
    ENGINE("glass", "uci", "pl", 2611, NO_AUTO_DETECT, None),
    ENGINE("jellyfish", "uci", "unknown", 2611, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("noragrace", "xboard", "us", 2610, NO_AUTO_DETECT, None),
    ENGINE("ruffian", "uci", "se", 2608, NO_AUTO_DETECT, None),
    ENGINE("caligula", "uci", "es", 2606, NO_AUTO_DETECT, None),
    ENGINE("garbochess", "uci", "us", 2606, NO_AUTO_DETECT, None),
    ENGINE("amyan", "uci", "cl", 2604, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("lemming", "xboard", "us", 2599, NO_AUTO_DETECT, None),
    # n2 (name to short)
    ENGINE("nawito", "uci", "cu", 2588, NO_AUTO_DETECT, None),
    ENGINE("floyd", "uci", "nl", 2584, NO_AUTO_DETECT, None),
    ENGINE("cuckoo", "xboard", "se", 2583, NO_AUTO_DETECT, None),  # UCI is an option in the command line
    ENGINE("muse", "xboard", "ch", 2581, NO_AUTO_DETECT, None),  # May support UCI as well
    ENGINE("hamsters", "uci", "it", 2578, NO_AUTO_DETECT, None),
    ENGINE("pseudo", "xboard", "cz", 2576, NO_AUTO_DETECT, None),
    ENGINE("galjoen", "uci", "be", 2572, NO_AUTO_DETECT, None),  # Allows XB
    # sos (name too short)
    ENGINE("maverick", "uci", "gb", 2569, NO_AUTO_DETECT, None),
    ENGINE("aristarch", "uci", "de", 2566, NO_AUTO_DETECT, None),
    ENGINE("petir", "xboard", "id", 2566, NO_AUTO_DETECT, None),
    ENGINE("capivara", "uci", "br", 2565, NO_AUTO_DETECT, None),
    ENGINE("nanoszachy", "xboard", "pl", 2559, NO_AUTO_DETECT, None),
    ENGINE("brutus", "xboard", "nl", 2557, NO_AUTO_DETECT, None),
    ENGINE("dimitri", "uci", "it", 2557, NO_AUTO_DETECT, None),  # May allow XB
    ENGINE("ghost", "xboard", "de", 2553, NO_AUTO_DETECT, None),
    ENGINE("jumbo", "xboard", "de", 2547, NO_AUTO_DETECT, None),
    ENGINE("anaconda", "uci", "de", 2545, NO_AUTO_DETECT, None),
    ENGINE("frank-walter", "xboard", "nl", 2544, NO_AUTO_DETECT, None),
    ENGINE("rebel", "uci", "nl", 2543, NO_AUTO_DETECT, None),
    ENGINE("betsabe", "xboard", "es", 2542, NO_AUTO_DETECT, None),
    ENGINE("hermann", "uci", "de", 2540, NO_AUTO_DETECT, None),
    ENGINE("ufim", "uci", "ru", 2540, NO_AUTO_DETECT, None),  # Formerly XB
    ENGINE("anmon", "uci", "fr", 2538, NO_AUTO_DETECT, None),
    ENGINE("pupsi", "uci", "se", 2536, NO_AUTO_DETECT, None),
    ENGINE("jikchess", "xboard2", "fi", 2522, NO_AUTO_DETECT, None),
    ENGINE("pepito", "xboard", "es", 2521, NO_AUTO_DETECT, None),
    ENGINE("axolotl", "uci", "de", 2508, NO_AUTO_DETECT, None),
    ENGINE("danchess", "xboard", "et", 2506, NO_AUTO_DETECT, None),
    ENGINE("greenlight", "xboard", "gb", 2505, NO_AUTO_DETECT, None),
    ENGINE("goliath", "uci", "de", 2505, NO_AUTO_DETECT, None),
    ENGINE("yace", "uci", "de", 2503, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("trace", "xboard", "au", 2502, NO_AUTO_DETECT, None),
    ENGINE("cyberpagno", "xboard", "it", 2491, NO_AUTO_DETECT, None),
    ENGINE("bruja", "xboard", "us", 2490, NO_AUTO_DETECT, None),
    ENGINE("magnum", "uci", "ca", 2490, NO_AUTO_DETECT, None),
    ENGINE("nemeton", "xboard", "nl", 2490, NO_AUTO_DETECT, None),
    # tao (name too short)
    ENGINE("gothmog", "uci", "no", 2482, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("bbchess", "uci", "si", 2479, NO_AUTO_DETECT, None),
    ENGINE("drosophila", "xboard", "se", 2479, NO_AUTO_DETECT, None),
    ENGINE("delphil", "uci", "fr", 2477, NO_AUTO_DETECT, None),
    ENGINE("mephisto", "uci", "gb", 2474, NO_AUTO_DETECT, None),
    ENGINE("cerebro", "xboard", "it", 2471, NO_AUTO_DETECT, None),
    ENGINE("kiwi", "xboard", "it", 2469, NO_AUTO_DETECT, None),
    ENGINE("xpdnt", "xboard", "us", 2468, NO_AUTO_DETECT, None),
    ENGINE("myrddin", "xboard", "us", 2458, NO_AUTO_DETECT, None),
    ENGINE("pikoszachy", "xboard", "pl", 2456, NO_AUTO_DETECT, None),
    ENGINE("anatoli", "xboard", "nl", 2454, NO_AUTO_DETECT, None),
    ENGINE("littlethought", "uci", "au", 2452, NO_AUTO_DETECT, None),
    ENGINE("matacz", "xboard", "pl", 2446, NO_AUTO_DETECT, None),
    ENGINE("tunguska", "uci", "br", 2445, NO_AUTO_DETECT, None),
    ENGINE("lozza", "uci", "gb", 2444, NO_AUTO_DETECT, None),
    ENGINE("ares", "uci", "us", 2441, NO_AUTO_DETECT, None),
    ENGINE("bumblebee", "uci", "us", 2440, NO_AUTO_DETECT, None),
    ENGINE("soldat", "xboard", "it", 2440, NO_AUTO_DETECT, None),
    ENGINE("spider", "xboard", "nl", 2439, NO_AUTO_DETECT, None),
    ENGINE("madchess", "uci", "us", 2436, NO_AUTO_DETECT, None),
    ENGINE("abrok", "uci", "de", 2435, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("lambchop", "uci", "nz", 2434, NO_AUTO_DETECT, None),  # Formerly XB
    ENGINE("kingofkings", "uci", "ca", 2433, NO_AUTO_DETECT, None),
    ENGINE("flux", "uci", "ch", 2428, NO_AUTO_DETECT, None),
    ENGINE("shallow", "uci", "unknown", 2428, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("eeyore", "uci", "ru", 2427, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("zevra", "uci", "ru", 2427, NO_AUTO_DETECT, None),
    ENGINE("gaia", "uci", "fr", 2425, NO_AUTO_DETECT, None),
    ENGINE("gromit", "uci", "de", 2425, NO_AUTO_DETECT, None),
    ENGINE("nejmet", "uci", "fr", 2425, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("quark", "xboard", "de", 2423, NO_AUTO_DETECT, None),
    ENGINE("hussar", "uci", "hu", 2420, NO_AUTO_DETECT, None),
    ENGINE("snitch", "xboard", "de", 2418, NO_AUTO_DETECT, None),
    ENGINE("dragon", "xboard", "fr", 2417, NO_AUTO_DETECT, None),  # Video player
    ENGINE("olithink", "xboard", "de", 2416, NO_AUTO_DETECT, None),
    ENGINE("romichess", "xboard", "us", 2415, NO_AUTO_DETECT, None),
    ENGINE("typhoon", "xboard", "us", 2414, NO_AUTO_DETECT, None),
    ENGINE("giraffe", "xboard", "gb", 2410, NO_AUTO_DETECT, None),
    ENGINE("simplex", "uci", "es", 2409, NO_AUTO_DETECT, None),
    ENGINE("teki", "uci", "in", 2406, NO_AUTO_DETECT, None),
    ENGINE("taltos", "uci", "hu", 2405, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("ifrit", "uci", "ru", 2403, NO_AUTO_DETECT, None),
    ENGINE("tjchess", "uci", "us", 2398, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("knightdreamer", "xboard", "se", 2392, NO_AUTO_DETECT, None),
    ENGINE("bearded", "xboard", "pl", 2391, NO_AUTO_DETECT, None),
    ENGINE("starthinker", "uci", "de", 2391, NO_AUTO_DETECT, None),
    ENGINE("postmodernist", "xboard", "gb", 2389, NO_AUTO_DETECT, None),
    ENGINE("comet", "xboard", "de", 2387, NO_AUTO_DETECT, None),
    ENGINE("leila", "xboard", "it", 2387, NO_AUTO_DETECT, None),
    # amy (name too short)
    ENGINE("diablo", "uci", "us", 2385, NO_AUTO_DETECT, None),
    ENGINE("capture", "xboard", "fr", 2383, NO_AUTO_DETECT, None),
    ENGINE("gosu", "xboard", "pl", 2382, NO_AUTO_DETECT, None),
    ENGINE("barbarossa", "uci", "at", 2381, NO_AUTO_DETECT, None),
    ENGINE("cmcchess", "uci", "zh", 2377, NO_AUTO_DETECT, None),
    ENGINE("knightx", "xboard2", "fr", 2375, NO_AUTO_DETECT, None),
    ENGINE("bringer", "xboard", "de", 2374, NO_AUTO_DETECT, None),
    ENGINE("jazz", "xboard", "nl", 2374, NO_AUTO_DETECT, None),
    ENGINE("patzer", "xboard", "de", 2374, NO_AUTO_DETECT, None),
    ENGINE("terra", "uci", "se", 2368, NO_AUTO_DETECT, None),
    ENGINE("wchess", "xboard", "us", 2366, NO_AUTO_DETECT, None),  # Unsure protocol
    ENGINE("crazybishop", "xboard", "fr", 2363, NO_AUTO_DETECT, None),  # Named as tcb
    ENGINE("dumb", "uci", "fr", 2358, NO_AUTO_DETECT, None),
    ENGINE("homer", "uci", "de", 2357, NO_AUTO_DETECT, None),
    ENGINE("betsy", "xboard", "us", 2356, NO_AUTO_DETECT, None),
    ENGINE("jonesy", "xboard", "es", 2353, NO_AUTO_DETECT, None),  # popochin
    ENGINE("amateur", "xboard", "us", 2351, NO_AUTO_DETECT, None),
    ENGINE("alex", "uci", "us", 2347, NO_AUTO_DETECT, None),
    ENGINE("tigran", "uci", "es", 2346, NO_AUTO_DETECT, None),
    ENGINE("popochin", "xboard", "es", 2345, NO_AUTO_DETECT, None),
    ENGINE("plisk", "uci", "us", 2343, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("horizon", "xboard", "us", 2341, NO_AUTO_DETECT, None),
    ENGINE("queen", "uci", "nl", 2337, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("arion", "uci", "fr", 2332, NO_AUTO_DETECT, None),
    ENGINE("gibbon", "uci", "fr", 2332, NO_AUTO_DETECT, None),
    ENGINE("waxman", "xboard", "us", 2331, NO_AUTO_DETECT, None),
    ENGINE("thor", "xboard", "hr", 2330, NO_AUTO_DETECT, None),
    ENGINE("amundsen", "xboard", "se", 2329, NO_AUTO_DETECT, None),
    ENGINE("sorgenkind", "xboard", "dk", 2329, NO_AUTO_DETECT, None),
    ENGINE("eveann", "xboard", "es", 2328, NO_AUTO_DETECT, None),
    ENGINE("sage", "xboard", "unknown", 2325, NO_AUTO_DETECT, None),
    ENGINE("chezzz", "xboard", "dk", 2323, NO_AUTO_DETECT, None),
    ENGINE("mediocre", "uci", "se", 2320, NO_AUTO_DETECT, None),
    # isa (name too short)
    ENGINE("absolute-zero", "uci", "zh", 2316, NO_AUTO_DETECT, None),
    ENGINE("aice", "xboard", "gr", 2314, NO_AUTO_DETECT, None),
    ENGINE("sungorus", "uci", "es", 2313, NO_AUTO_DETECT, None),
    ENGINE("nebiyu", "xboard", "et", 2310, NO_AUTO_DETECT, None),  # wine crash on Ubuntu 1804 with NebiyuAlien.exe
    ENGINE("asterisk", "uci", "hu", 2307, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("averno", "xboard", "es", 2306, NO_AUTO_DETECT, None),
    ENGINE("joker", "xboard", "nl", 2306, NO_AUTO_DETECT, None),
    ENGINE("kingfisher", "uci", "hk", 2304, NO_AUTO_DETECT, None),
    ENGINE("tytan", "xboard", "pl", 2304, NO_AUTO_DETECT, None),
    ENGINE("resp", "xboard", "de", 2295, NO_AUTO_DETECT, None),
    ENGINE("ayito", "uci", "es", 2286, NO_AUTO_DETECT, None),  # Formerly XB
    ENGINE("chaturanga", "xboard", "it", 2285, NO_AUTO_DETECT, None),
    ENGINE("matilde", "xboard", "it", 2281, NO_AUTO_DETECT, None),
    ENGINE("fischerle", "uci", "de", 2280, NO_AUTO_DETECT, None),
    ENGINE("rival", "uci", "gb", 2273, NO_AUTO_DETECT, None),
    ENGINE("ct800", "uci", "de", 2272, NO_AUTO_DETECT, None),
    ENGINE("paladin", "uci", "in", 2272, NO_AUTO_DETECT, None),
    # esc (name too short)
    ENGINE("scidlet", "xboard", "nz", 2266, NO_AUTO_DETECT, None),
    ENGINE("butcher", "xboard", "pl", 2264, NO_AUTO_DETECT, None),
    ENGINE("zeus", "xboard", "ru", 2262, NO_AUTO_DETECT, None),
    ENGINE("natwarlal", "xboard", "in", 2261, NO_AUTO_DETECT, None),
    # doctor (unknown protocol)
    ENGINE("kmtchess", "xboard", "es", 2260, NO_AUTO_DETECT, None),
    ENGINE("firefly", "uci", "hk", 2252, NO_AUTO_DETECT, None),
    ENGINE("robocide", "uci", "gb", 2252, NO_AUTO_DETECT, None),
    ENGINE("napoleon", "uci", "it", 2250, NO_AUTO_DETECT, None),
    ENGINE("spacedog", "uci", "uk", 2242, NO_AUTO_DETECT, None),  # Allows XB
    # ant (name too short)
    ENGINE("anechka", "uci", "ru", 2234, NO_AUTO_DETECT, None),
    ENGINE("gopher_check", "uci", "us", 2234, NO_AUTO_DETECT, None),
    ENGINE("dorpsgek", "xboard", "en", 2231, NO_AUTO_DETECT, None),
    ENGINE("alichess", "uci", "de", 2229, NO_AUTO_DETECT, None),
    ENGINE("obender", "xboard", "ru", 2224, NO_AUTO_DETECT, None),
    ENGINE("joker2", "uci", "it", 2222, NO_AUTO_DETECT, None),
    ENGINE("adam", "xboard", "fr", 2220, NO_AUTO_DETECT, None),
    ENGINE("ramjet", "uci", "it", 2219, NO_AUTO_DETECT, None),
    ENGINE("exacto", "xboard", "us", 2216, NO_AUTO_DETECT, None),
    ENGINE("buzz", "xboard", "us", 2215, NO_AUTO_DETECT, None),
    ENGINE("chessalex", "uci", "ru", 2207, NO_AUTO_DETECT, None),
    ENGINE("chispa", "uci", "ar", 2206, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("beowulf", "xboard", "gb", 2203, NO_AUTO_DETECT, None),
    ENGINE("weini", "xboard", "fr", 2201, NO_AUTO_DETECT, None),  # Allows UCI
    ENGINE("rattate", "xboard", "it", 2199, NO_AUTO_DETECT, None),
    ENGINE("latista", "xboard", "us", 2195, NO_AUTO_DETECT, None),
    ENGINE("sinobyl", "xboard", "us", 2195, NO_AUTO_DETECT, None),
    ENGINE("ng-play", "xboard", "gr", 2194, NO_AUTO_DETECT, None),
    ENGINE("feuerstein", "uci", "de", 2192, NO_AUTO_DETECT, None),
    ENGINE("neurosis", "xboard", "nl", 2188, NO_AUTO_DETECT, None),
    # uralochka (blacklisted)
    ENGINE("mango", "xboard", "ve", 2184, NO_AUTO_DETECT, None),
    ENGINE("atak", "xboard", "pl", 2183, NO_AUTO_DETECT, None),
    ENGINE("madeleine", "uci", "it", 2182, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("mora", "uci", "ar", 2182, NO_AUTO_DETECT, None),
    ENGINE("sjaakii", "xboard", "nl", 2176, NO_AUTO_DETECT, None),
    ENGINE("protej", "uci", "it", 2175, NO_AUTO_DETECT, None),
    ENGINE("baislicka", "uci", "unknown", 2174, NO_AUTO_DETECT, None),
    ENGINE("achillees", "uci", "es", 2172, NO_AUTO_DETECT, None),
    ENGINE("genesis", "xboard", "il", 2170, NO_AUTO_DETECT, None),
    ENGINE("blackbishop", "uci", "de", 2163, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("inmichess", "xboard", "at", 2162, NO_AUTO_DETECT, None),
    ENGINE("kurt", "xboard", "de", 2162, NO_AUTO_DETECT, None),
    ENGINE("blitzkrieg", "uci", "in", 2159, NO_AUTO_DETECT, None),
    ENGINE("nagaskaki", "xboard", "za", 2156, NO_AUTO_DETECT, None),
    ENGINE("raven", "uci", "gb", 2152, NO_AUTO_DETECT, None),
    ENGINE("chesley", "xboard", "us", 2147, NO_AUTO_DETECT, None),
    ENGINE("alarm", "xboard", "se", 2145, NO_AUTO_DETECT, None),
    ENGINE("lime", "uci", "gb", 2144, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("hedgehog", "uci", "ru", 2142, NO_AUTO_DETECT, None),
    ENGINE("sunsetter", "xboard", "de", 2141, NO_AUTO_DETECT, None),
    ENGINE("chesskiss", "xboard", "unknown", 2137, NO_AUTO_DETECT, None),
    ENGINE("fortress", "xboard", "it", 2136, NO_AUTO_DETECT, None),
    ENGINE("tinychess", "uci", "unknown", 2136, NO_AUTO_DETECT, None),
    ENGINE("nesik", "xboard", "pl", 2133, NO_AUTO_DETECT, None),
    ENGINE("wjchess", "uci", "fr", 2132, NO_AUTO_DETECT, None),
    ENGINE("prophet", "xboard", "us", 2124, NO_AUTO_DETECT, None),
    ENGINE("uragano", "xboard", "it", 2122, NO_AUTO_DETECT, None),
    ENGINE("clever-girl", "uci", "us", 2117, NO_AUTO_DETECT, None),
    # merlin (no information)
    ENGINE("embla", "uci", "nl", 2114, NO_AUTO_DETECT, None),
    ENGINE("little-wing", "uci", "fr", 2114, NO_AUTO_DETECT, None),  # Allows XB
    # gk (name too short)
    ENGINE("knockout", "xboard", "de", 2107, NO_AUTO_DETECT, None),
    # alf (name too short)
    ENGINE("bikjump", "uci", "nl", 2103, NO_AUTO_DETECT, None),
    ENGINE("micah", "", "nl", 2102, NO_AUTO_DETECT, None),
    ENGINE("wing", "xboard", "nl", 2100, NO_AUTO_DETECT, None),
    ENGINE("clarabit", "uci", "es", 2098, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("adroitchess", "uci", "gb", 2079, NO_AUTO_DETECT, None),
    ENGINE("parrot", "xboard", "us", 2078, NO_AUTO_DETECT, None),
    ENGINE("abbess", "xboard", "us", 2069, NO_AUTO_DETECT, None),
    ENGINE("crabby", "uci", "us", 2068, NO_AUTO_DETECT, None),
    ENGINE("gunborg", "uci", "unknown", 2068, NO_AUTO_DETECT, None),
    ENGINE("alcibiades", "uci", "bg", 2065, NO_AUTO_DETECT, None),
    ENGINE("cinnamon", "uci", "it", 2064, NO_AUTO_DETECT, None),
    ENGINE("smash", "uci", "it", 2060, NO_AUTO_DETECT, None),
    ENGINE("chessmind", "uci", "de", 2058, NO_AUTO_DETECT, None),
    ENGINE("matheus", "uci", "br", 2058, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("potato", "xboard", "at", 2057, NO_AUTO_DETECT, None),
    ENGINE("honzovy", "uci", "cz", 2056, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("monarch", "uci", "gb", 2056, NO_AUTO_DETECT, None),
    ENGINE("dolphin", "xboard", "vn", 2055, NO_AUTO_DETECT, None),  # File manager
    ENGINE("kingsout", "xboard", "de", 2055, NO_AUTO_DETECT, None),
    ENGINE("bodo", "uci", "au", 2049, NO_AUTO_DETECT, None),
    ENGINE("rdchess", "xboard", "at", 2046, NO_AUTO_DETECT, None),
    ENGINE("gerbil", "xboard", "us", 2043, NO_AUTO_DETECT, None),
    ENGINE("vice", "uci", "unknown", 2043, NO_AUTO_DETECT, None),  # Both UCI/XBoard
    # ax (name too short)
    ENGINE("jabba", "uci", "gb", 2036, NO_AUTO_DETECT, None),
    # plp (name too short)
    ENGINE("prochess", "uci", "it", 2029, NO_AUTO_DETECT, None),
    # zct (name too short)
    ENGINE("zetadva", "xboard", "de", 2023, NO_AUTO_DETECT, None),
    ENGINE("bestia", "xboard", "ua", 2020, NO_AUTO_DETECT, None),
    ENGINE("bismark", "uci", "il", 2020, NO_AUTO_DETECT, None),
    ENGINE("plywood", "xboard", "unknown", 2019, NO_AUTO_DETECT, None),
    ENGINE("ecce", "uci", "ru", 2017, NO_AUTO_DETECT, None),
    ENGINE("cupcake", "xboard", "us", 2016, NO_AUTO_DETECT, None),
    ENGINE("delphimax", "uci", "de", 2013, NO_AUTO_DETECT, None),
    ENGINE("oberon", "xboard", "pl", 2013, NO_AUTO_DETECT, None),
    # schola (no information)
    ENGINE("freyr", "xboard", "ro", 2008, NO_AUTO_DETECT, None),
    ENGINE("ceibo", "uci", "ar", 2005, NO_AUTO_DETECT, None),
    ENGINE("leonidas", "xboard", "nl", 2005, NO_AUTO_DETECT, None),
    ENGINE("requiem", "xboard", "fi", 2004, NO_AUTO_DETECT, None),
    ENGINE("chess4j", "xboard", "us", 1996, NO_AUTO_DETECT, None),
    ENGINE("squared-chess", "uci", "de", 1996, NO_AUTO_DETECT, None),
    ENGINE("wowl", "uci", "de", 1995, NO_AUTO_DETECT, None),
    ENGINE("gullydeckel", "xboard", "de", 1993, NO_AUTO_DETECT, None),
    ENGINE("goldfish", "uci", "no", 1992, NO_AUTO_DETECT, None),
    ENGINE("elephant", "xboard", "de", 1989, NO_AUTO_DETECT, None),
    ENGINE("arabian-knight", "xboard", "pl", 1987, NO_AUTO_DETECT, None),
    ENGINE("biglion", "uci", "cm", 1987, NO_AUTO_DETECT, None),
    ENGINE("armageddon", "xboard", "pl", 1986, NO_AUTO_DETECT, None),
    ENGINE("bubble", "uci", "br", 1986, NO_AUTO_DETECT, None),
    ENGINE("snowy", "uci", "us", 1985, NO_AUTO_DETECT, None),
    ENGINE("faile", "xboard1", "ca", 1978, NO_AUTO_DETECT, None),
    ENGINE("slibo", "xboard", "de", 1976, NO_AUTO_DETECT, None),
    ENGINE("matant", "xboard", "pl", 1969, NO_AUTO_DETECT, None),
    ENGINE("ladameblanche", "xboard", "fr", 1968, NO_AUTO_DETECT, None),
    ENGINE("monik", "xboard", "unknown", 1968, NO_AUTO_DETECT, None),
    ENGINE("sissa", "uci", "fr", 1967, NO_AUTO_DETECT, None),
    ENGINE("ssechess", "xboard", "us", 1967, NO_AUTO_DETECT, None),
    ENGINE("jacksprat", "xboard", "unknown", 1965, NO_AUTO_DETECT, None),
    ENGINE("alchess", "uci", "ru", 1961, NO_AUTO_DETECT, None),
    # eia (name too short)
    # bsc (name too short)
    ENGINE("cilian", "xboard", "ch", 1960, NO_AUTO_DETECT, None),
    # franky (no information)
    ENGINE("mustang", "xboard", "by", 1957, NO_AUTO_DETECT, None),
    ENGINE("adachess", "xboard", "it", 1955, NO_AUTO_DETECT, None),
    ENGINE("micromax", "xboard", "nl", 1954, NO_AUTO_DETECT, None),
    ENGINE("umax", "xboard", "nl", 1954, NO_AUTO_DETECT, None),
    ENGINE("etude", "uci", "us", 1953, NO_AUTO_DETECT, None),
    ENGINE("wuttang", "uci", "in", 1951, NO_AUTO_DETECT, None),
    ENGINE("janwillem", "xboard", "nl", 1950, NO_AUTO_DETECT, None),
    ENGINE("pleco", "uci", "us", 1948, NO_AUTO_DETECT, None),
    ENGINE("sharper", "xboard", "se", 1940, NO_AUTO_DETECT, None),
    ENGINE("sapeli", "uci", "fi", 1939, NO_AUTO_DETECT, None),
    ENGINE("bell", "xboard", "fr", 1937, NO_AUTO_DETECT, None),
    ENGINE("bibichess", "uci", "fr", 1927, NO_AUTO_DETECT, None),
    ENGINE("smirf", "xboard", "de", 1925, NO_AUTO_DETECT, None),
    ENGINE("heracles", "uci", "fr", 1923, NO_AUTO_DETECT, None),
    ENGINE("samchess", "xboard", "us", 1918, NO_AUTO_DETECT, None),
    ENGINE("iach", "xboard", "unknown", 1917, NO_AUTO_DETECT, None),
    ENGINE("bambam", "xboard", "at", 1913, NO_AUTO_DETECT, None),
    ENGINE("tony", "xboard", "ca", 1912, NO_AUTO_DETECT, None),
    ENGINE("eagle", "uci", "uci", 1911, NO_AUTO_DETECT, None),
    ENGINE("reger", "xboard", "nl", 1911, NO_AUTO_DETECT, None),
    ENGINE("claudia", "uci", "es", 1908, NO_AUTO_DETECT, None),
    ENGINE("dabbaba", "xboard", "dk", 1908, NO_AUTO_DETECT, None),
    ENGINE("warrior", "xboard", "lv", 1907, NO_AUTO_DETECT, None),
    ENGINE("clueless", "uci", "de", 1905, NO_AUTO_DETECT, None),
    ENGINE("morphy", "xboard", "us", 1902, NO_AUTO_DETECT, None),
    ENGINE("zeta", "xboard", "me", 1896, NO_AUTO_DETECT, None),
    ENGINE("snailchess", "xboard", "sg", 1895, NO_AUTO_DETECT, None),
    ENGINE("surprise", "xboard", "de", 1888, NO_AUTO_DETECT, None),
    ENGINE("tyrell", "uci", "us", 1886, NO_AUTO_DETECT, None),
    ENGINE("matmoi", "xboard", "ca", 1884, NO_AUTO_DETECT, None),
    ENGINE("purplehaze", "xboard", "fr", 1884, NO_AUTO_DETECT, None),
    ENGINE("mrchess", "xboard", "sg", 1883, NO_AUTO_DETECT, None),
    # freechess (blacklisted)
    ENGINE("presbyter", "uci", "unknown", 1872, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("simontacchi", "uci", "us", 1861, NO_AUTO_DETECT, None),
    ENGINE("butter", "uci", "unknown", 1860, NO_AUTO_DETECT, None),
    ENGINE("roce", "uci", "ch", 1853, NO_AUTO_DETECT, None),
    ENGINE("deepov", "uci", "fr", 1851, NO_AUTO_DETECT, None),
    ENGINE("ranita", "uci", "fr", 1842, NO_AUTO_DETECT, None),
    ENGINE("sayuri", "uci", "jp", 1838, NO_AUTO_DETECT, None),
    ENGINE("milady", "xboard", "fr", 1835, NO_AUTO_DETECT, None),
    ENGINE("skiull", "uci", "ve", 1835, NO_AUTO_DETECT, None),
    ENGINE("halogen", "uci", "au", 1834, NO_AUTO_DETECT, None),
    ENGINE("heavychess", "uci", "ar", 1833, NO_AUTO_DETECT, None),
    ENGINE("ajedreztactico", "xboard", "mx", 1831, NO_AUTO_DETECT, None),
    ENGINE("celes", "uci", "nl", 1824, NO_AUTO_DETECT, None),
    ENGINE("jars", "xboard", "fr", 1823, NO_AUTO_DETECT, None),
    ENGINE("ziggurat", "uci", "us", 1819, NO_AUTO_DETECT, None),
    ENGINE("rataaeroespacial", "xboard", "ar", 1818, NO_AUTO_DETECT, None),
    ENGINE("noonian", "uci", "us", 1814, NO_AUTO_DETECT, None),
    ENGINE("predateur", "uci", "fr", 1811, NO_AUTO_DETECT, None),
    ENGINE("chenard", "xboard", "us", 1810, NO_AUTO_DETECT, None),
    ENGINE("morphychess", "xboard", "us", 1804, NO_AUTO_DETECT, None),
    ENGINE("beaches", "xboard", "us", 1802, NO_AUTO_DETECT, None),
    ENGINE("macromix", "uci", "ua", 1802, NO_AUTO_DETECT, None),
    ENGINE("pigeon", "uci", "ca", 1800, NO_AUTO_DETECT, None),
    ENGINE("chessterfield", "xboard", "ch", 1799, NO_AUTO_DETECT, None),
    ENGINE("cdrill", "uci", "unknown", 1793, NO_AUTO_DETECT, None),
    ENGINE("hoichess", "xboard", "de", 1792, NO_AUTO_DETECT, None),
    ENGINE("bremboce", "xboard", "it", 1791, NO_AUTO_DETECT, None),
    ENGINE("enigma", "xboard", "pl", 1791, NO_AUTO_DETECT, None),
    ENGINE("mobmat", "uci", "us", 1790, NO_AUTO_DETECT, None),
    ENGINE("grizzly", "xboard", "de", 1786, NO_AUTO_DETECT, None),
    ENGINE("embracer", "xboard", "se", 1784, NO_AUTO_DETECT, None),
    ENGINE("cecir", "xboard", "uy", 1782, NO_AUTO_DETECT, None),
    ENGINE("fauce", "xboard", "it", 1781, NO_AUTO_DETECT, None),
    ENGINE("berochess", "uci", "de", 1774, NO_AUTO_DETECT, None),
    ENGINE("apollo", "uci", "us", 1773, NO_AUTO_DETECT, None),
    ENGINE("pulsar", "xboard", "us", 1773, NO_AUTO_DETECT, None),
    ENGINE("mint", "xboard", "se", 1764, NO_AUTO_DETECT, None),
    ENGINE("robin", "xboard", "pl", 1764, NO_AUTO_DETECT, None),
    ENGINE("lodocase", "xboard", "be", 1760, NO_AUTO_DETECT, None),
    ENGINE("laurifer", "xboard", "pl", 1752, NO_AUTO_DETECT, None),
    ENGINE("rocinante", "uci", "es", 1745, NO_AUTO_DETECT, None),
    ENGINE("ziggy", "uci", "is", 1745, NO_AUTO_DETECT, None),
    ENGINE("vicki", "xboard", "za", 1744, NO_AUTO_DETECT, None),
    # elf (name too short)
    ENGINE("shallowblue", "uci", "ca", 1736, NO_AUTO_DETECT, None),
    ENGINE("kanguruh", "xboard", "at", 1735, NO_AUTO_DETECT, None),
    ENGINE("adamant", "xboard", "ru", 1734, NO_AUTO_DETECT, None),
    ENGINE("foxsee", "uci", "cn", 1733, NO_AUTO_DETECT, None),
    ENGINE("gchess", "xboard", "it", 1733, NO_AUTO_DETECT, None),
    ENGINE("zzzzzz", "xboard", "nl", 1730, NO_AUTO_DETECT, None),
    ENGINE("jaksah", "uci", "rs", 1727, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("kitteneitor", "xboard", "es", 1724, NO_AUTO_DETECT, None),
    ENGINE("tscp", "xboard", "us", 1724, NO_AUTO_DETECT, None),
    ENGINE("zoidberg", "xboard", "es", 1724, NO_AUTO_DETECT, None),
    # see (name too short)
    ENGINE("tristram", "xboard", "us", 1718, NO_AUTO_DETECT, None),
    ENGINE("enkochess", "uci", "unknown", 1717, NO_AUTO_DETECT, None),
    ENGINE("aldebaran", "xboard", "it", 1710, NO_AUTO_DETECT, None),
    ENGINE("testina", "uci", "it", 1698, NO_AUTO_DETECT, None),
    ENGINE("celestial", "uci", "au", 1695, NO_AUTO_DETECT, None),
    ENGINE("jester", "xboard", "us", 1694, NO_AUTO_DETECT, None),
    # chess (name too generic)
    ENGINE("sharpchess", "xboard", "unknown", 1691, NO_AUTO_DETECT, None),
    ENGINE("gargamella", "xboard", "it", 1687, NO_AUTO_DETECT, None),
    ENGINE("chengine", "xboard", "jp", 1683, NO_AUTO_DETECT, None),
    ENGINE("mizar", "xboard", "it", 1683, NO_AUTO_DETECT, None),
    ENGINE("polarchess", "xboard", "no", 1676, NO_AUTO_DETECT, None),
    ENGINE("bace", "xboard", "us", 1675, NO_AUTO_DETECT, None),
    ENGINE("golem", "xboard", "it", 1672, NO_AUTO_DETECT, None),
    ENGINE("tom-thumb", "uci", "nl", 1664, NO_AUTO_DETECT, None),
    ENGINE("belzebub", "xboard", "pl", 1662, NO_AUTO_DETECT, None),
    ENGINE("pooky", "uci", "us", 1656, NO_AUTO_DETECT, None),
    ENGINE("koedem", "uci", "de", 1655, NO_AUTO_DETECT, None),
    ENGINE("dchess", "xboard", "us", 1651, NO_AUTO_DETECT, None),
    ENGINE("simon", "xboard", "us", 1647, NO_AUTO_DETECT, None),
    ENGINE("spartan", "uci", "unknown", 1643, NO_AUTO_DETECT, None),
    ENGINE("vapor", "uci", "us", 1643, NO_AUTO_DETECT, None),
    ENGINE("iq23", "uci", "de", 1642, NO_AUTO_DETECT, None),
    ENGINE("pulse", "uci", "ch", 1638, NO_AUTO_DETECT, None),
    ENGINE("chessrikus", "xboard", "us", 1633, NO_AUTO_DETECT, None),
    ENGINE("mscp", "xboard", "nl", 1632, NO_AUTO_DETECT, None),
    ENGINE("storm", "xboard", "us", 1627, NO_AUTO_DETECT, None),
    ENGINE("monochrome", "uci", "unknown", 1624, NO_AUTO_DETECT, None),
    ENGINE("jsbam", "xboard", "nl", 1621, NO_AUTO_DETECT, None),
    ENGINE("saruman", "uci", "unknown", 1620, NO_AUTO_DETECT, None),
    ENGINE("revati", "uci", "de", 1619, NO_AUTO_DETECT, None),
    ENGINE("kasparov", "uci", "ca", 1618, NO_AUTO_DETECT, None),
    ENGINE("philemon", "uci", "ch", 1614, NO_AUTO_DETECT, None),
    ENGINE("bullitchess", "uci", "unknown", 1611, NO_AUTO_DETECT, None),
    ENGINE("rainman", "xboard", "se", 1609, NO_AUTO_DETECT, None),
    ENGINE("marginal", "uci", "ru", 1599, NO_AUTO_DETECT, None),
    ENGINE("zotron", "xboard", "us", 1592, NO_AUTO_DETECT, None),
    ENGINE("violet", "uci", "unknown", 1591, NO_AUTO_DETECT, None),
    ENGINE("casper", "uci", "gb", 1589, NO_AUTO_DETECT, None),
    ENGINE("darky", "uci", "mx", 1589, NO_AUTO_DETECT, None),
    ENGINE("dreamer", "xboard", "nl", 1581, NO_AUTO_DETECT, None),
    ENGINE("needle", "xboard", "fi", 1581, NO_AUTO_DETECT, None),
    ENGINE("damas", "xboard", "br", 1580, NO_AUTO_DETECT, None),
    ENGINE("sdbc", "xboard", "de", 1577, NO_AUTO_DETECT, None),
    ENGINE("vanilla", "xboard", "au", 1576, NO_AUTO_DETECT, None),
    ENGINE("cicada", "uci", "us", 1573, NO_AUTO_DETECT, None),
    ENGINE("hokus", "xboard", "pl", 1552, NO_AUTO_DETECT, None),
    ENGINE("mace", "uci", "de", 1546, NO_AUTO_DETECT, None),
    ENGINE("larsen", "xboard", "it", 1543, NO_AUTO_DETECT, None),
    ENGINE("trappist", "uci", "unknown", 1536, NO_AUTO_DETECT, None),
    ENGINE("yawce", "xboard", "dk", 1517, NO_AUTO_DETECT, None),
    ENGINE("supra", "uci", "pt", 1507, NO_AUTO_DETECT, None),
    ENGINE("piranha", "uci", "de", 1501, NO_AUTO_DETECT, None),
    ENGINE("alibaba", "uci", "nl", 1500, NO_AUTO_DETECT, None),
    ENGINE("apep", "xboard", "us", 1494, NO_AUTO_DETECT, None),
    ENGINE("tarrasch", "uci", "us", 1492, NO_AUTO_DETECT, None),
    ENGINE("andersen", "xboard", "se", 1489, NO_AUTO_DETECT, None),
    ENGINE("pwned", "uci", "us", 1484, NO_AUTO_DETECT, None),
    ENGINE("apil", "xboard", "de", 1482, NO_AUTO_DETECT, None),
    ENGINE("pentagon", "xboard", "it", 1479, NO_AUTO_DETECT, None),
    ENGINE("gedeone", "xboard", "unknown", 1476, NO_AUTO_DETECT, None),
    ENGINE("roque", "xboard", "es", 1471, NO_AUTO_DETECT, None),
    ENGINE("numpty", "xboard", "gb", 1470, NO_AUTO_DETECT, None),
    ENGINE("blikskottel", "xboard", "za", 1461, NO_AUTO_DETECT, None),
    ENGINE("hactar", "uci", "de", 1448, NO_AUTO_DETECT, None),
    ENGINE("nero", "xboard", "de", 1447, NO_AUTO_DETECT, None),
    ENGINE("suff", "uci", "at", 1422, NO_AUTO_DETECT, None),
    ENGINE("sabrina", "xboard", "it", 1414, NO_AUTO_DETECT, None),
    ENGINE("quokka", "uci", "us", 1411, NO_AUTO_DETECT, None),
    ENGINE("minimardi", "xboard", "unknown", 1410, NO_AUTO_DETECT, None),
    ENGINE("satana", "xboard", "it", 1407, NO_AUTO_DETECT, None),
    ENGINE("eden", "uci", "de", 1406, NO_AUTO_DETECT, None),
    ENGINE("goyaz", "xboard", "br", 1405, NO_AUTO_DETECT, None),
    ENGINE("jchess", "xboard", "pl", 1405, NO_AUTO_DETECT, None),
    ENGINE("nanook", "uci", "fr", 1388, NO_AUTO_DETECT, None),
    ENGINE("skaki", "xboard", "us", 1372, NO_AUTO_DETECT, None),
    ENGINE("virutor", "uci", "cz", 1366, NO_AUTO_DETECT, None),
    ENGINE("minichessai", "xboard", "pl", 1364, NO_AUTO_DETECT, None),
    ENGINE("joanna", "xboard", "pl", 1344, NO_AUTO_DETECT, None),
    ENGINE("gladiator", "xboard", "es", 1337, NO_AUTO_DETECT, None),
    ENGINE("ozwald", "xboard", "fi", 1332, NO_AUTO_DETECT, None),
    ENGINE("fimbulwinter", "xboard", "us", 1318, NO_AUTO_DETECT, None),
    ENGINE("cerulean", "xboard", "ca", 1296, NO_AUTO_DETECT, None),
    ENGINE("killerqueen", "uci", "it", 1290, NO_AUTO_DETECT, None),
    ENGINE("trex", "uci", "fr", 1288, NO_AUTO_DETECT, None),
    # chess (name too generic)
    ENGINE("qutechess", "uci", "si", 1275, NO_AUTO_DETECT, None),
    ENGINE("ronja", "xboard", "se", 1271, NO_AUTO_DETECT, None),
    ENGINE("tikov", "uci", "gb", 1244, NO_AUTO_DETECT, None),
    ENGINE("raffaela", "xboard", "it", 1233, NO_AUTO_DETECT, None),
    ENGINE("dragontooth", "uci", "us", 1231, NO_AUTO_DETECT, None),
    ENGINE("gringo", "xboard", "at", 1231, NO_AUTO_DETECT, None),  # gringo - grounding tools for (disjunctive) logic programs
    ENGINE("pierre", "xboard", "ca", 1230, NO_AUTO_DETECT, None),
    ENGINE("toledo-uci", "uci", "mx", 1225, NO_AUTO_DETECT, 5),
    ENGINE("toledo", "xboard", "mx", 1225, NO_AUTO_DETECT, None),
    ENGINE("neurone", "xboard", "it", 1217, NO_AUTO_DETECT, None),
    ENGINE("gray-matter", "xboard", "unknown", 1215, NO_AUTO_DETECT, None),
    ENGINE("enxadrista", "xboard", "br", 1211, NO_AUTO_DETECT, None),
    ENGINE("darkfusch", "uci", "de", 1185, NO_AUTO_DETECT, None),
    ENGINE("project-invincible", "xboard", "fi", 1181, NO_AUTO_DETECT, None),
    ENGINE("cassandre", "uci", "fr", 1157, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("jchecs", "xboard", "fr", 1141, NO_AUTO_DETECT, None),
    ENGINE("brama", "xboard", "it", 1139, NO_AUTO_DETECT, None),
    ENGINE("soberango", "xboard", "ar", 1134, NO_AUTO_DETECT, None),
    ENGINE("usurpator", "xboard", "nl", 1132, NO_AUTO_DETECT, None),
    ENGINE("blitzter", "xboard", "de", 1078, NO_AUTO_DETECT, None),
    ENGINE("strategicdeep", "xboard", "pl", 1074, NO_AUTO_DETECT, None),
    ENGINE("frank", "xboard", "it", 1072, NO_AUTO_DETECT, None),
    ENGINE("talvmenni", "xboard", "fo", 1064, NO_AUTO_DETECT, None),
    ENGINE("minnow", "uci", "unknown", 1043, NO_AUTO_DETECT, None),
    ENGINE("xadreco", "xboard", "br", 1025, NO_AUTO_DETECT, None),
    ENGINE("safrad", "uci", "cz", 1024, NO_AUTO_DETECT, None),
    ENGINE("iota", "uci", "gb", 1018, NO_AUTO_DETECT, None),
    ENGINE("giuchess", "xboard", "it", 1001, NO_AUTO_DETECT, None),
    ENGINE("belofte", "uci", "be", 989, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("kace", "xboard", "us", 982, NO_AUTO_DETECT, None),
    ENGINE("feeks", "uci", "nl", 967, NO_AUTO_DETECT, None),
    ENGINE("youk", "xboard", "fr", 963, NO_AUTO_DETECT, None),
    ENGINE("nsvchess", "uci", "fr", 944, NO_AUTO_DETECT, None),
    # zoe (name too short)
    ENGINE("chad", "uci", "xb", 940, NO_AUTO_DETECT, None),
    ENGINE("luzhin", "xboard", "unknown", 926, NO_AUTO_DETECT, None),
    ENGINE("hippocampe", "xboard", "fr", 870, NO_AUTO_DETECT, None),
    ENGINE("pyotr", "xboard", "gr", 867, NO_AUTO_DETECT, None),
    ENGINE("dika", "xboard", "fr", 859, NO_AUTO_DETECT, None),
    ENGINE("chessputer", "uci", "unknown", 846, NO_AUTO_DETECT, None),
    ENGINE("alouette", "uci", "fr", 699, NO_AUTO_DETECT, None),
    # easypeasy (no information)
    ENGINE("acquad", "uci", "it", 637, NO_AUTO_DETECT, None),
    ENGINE("acqua", "uci", "it", 612, NO_AUTO_DETECT, None),
    # neg (name too short)
    # ram (name too short)
    ENGINE("cpp1", "xboard", "nl", 458, NO_AUTO_DETECT, None),
    # pos (name too short)
    ENGINE("lamosca", "xboard", "it", 364, NO_AUTO_DETECT, None),
    # ace (name too short)
    ENGINE("sxrandom", "uci", "cz", 204, NO_AUTO_DETECT, None),  # Allows XB

    # -- Other (parent engine, derivative work, unlisted, variant engine...)
    ENGINE("s_pro", "uci", "it", 3540, NO_AUTO_DETECT, None),
    ENGINE("asmfish", "uci", "bg", 3531, NO_AUTO_DETECT, None),
    ENGINE("glaurung", "uci", "no", 2915, AUTO_DETECT, None),
    ENGINE("amundsen", "xboard", "se", 0, NO_AUTO_DETECT, None),
    ENGINE("anticrux", "uci", "fr", 0, NO_AUTO_DETECT, 10),
    ENGINE("fairymax", "xboard", "nl", 0, AUTO_DETECT, None),
    ENGINE("fruit", "uci", "fr", 2783, AUTO_DETECT, None),
    ENGINE("sunfish", "xboard", "dk", 0, NO_AUTO_DETECT, None),
    ENGINE("democracy", "uci", "fr", 0, NO_AUTO_DETECT, None),
    ENGINE("worse-chess", "uci", "fr", 0, NO_AUTO_DETECT, None)
]


# Bubble sort by descending length of the name
for i in range(len(ENGINES_LIST) - 1, 1, - 1):
    for j in range(0, i - 1):
        if len(ENGINES_LIST[i].name) > len(ENGINES_LIST[j].name):
            tmp = ENGINES_LIST[i]
            ENGINES_LIST[i] = ENGINES_LIST[j]
            ENGINES_LIST[j] = tmp


# Mass detection of the engines (no recursion if maxDepth=0)
def listEnginesFromPath(defaultPath, maxDepth=3, withSymLink=False):
    # Base folders
    if defaultPath is None or defaultPath == "":
        base = os.getenv("PATH")
        maxDepth = 1
    else:
        base = defaultPath
    base = [os.path.join(p, "") for p in base.split(";")]

    # List the executable files
    found_engines = []
    depth_current = 1
    depth_next = len(base)
    for depth_loop, dir in enumerate(base):
        files = os.listdir(dir)
        for file in files:
            file_ci = file.lower()
            fullname = os.path.join(dir, file)

            # Recurse the folders by appending to the scanned list
            if os.path.isdir(fullname):
                if not withSymLink and os.path.islink(fullname):
                    continue
                if maxDepth > 0:
                    if depth_loop == depth_next:
                        depth_current += 1
                        depth_next = len(base)
                    if depth_current <= maxDepth:
                        base.append(os.path.join(dir, file, ""))
                continue

            # Blacklisted keywords
            blacklisted = False
            for kw in ["install", "setup", "reset", "remove", "delete", "clean", "purge", "config", "register", "editor", "book"]:
                if kw in file_ci:
                    blacklisted = True
                    break
            if blacklisted:
                continue

            # Check if the file is a supported scripting language, or an executable file
            executable = False
            for vm in VM_LIST:
                if file_ci.endswith(vm.ext):
                    executable = True
                    break
            if not executable:
                if cpu['windows']:
                    executable = file_ci.endswith(cpu['binext'])
                else:
                    executable = os.access(fullname, os.X_OK)
            if not executable:
                continue

            # Check the filename against the known list of engines
            found = False
            for engine in ENGINES_LIST:
                if engine.name in file_ci:
                    found = True
                    break
            if not found:
                continue

            # Check the bitness because x64 does not run on x32
            if cpu['bitness'] == "32" and "64" in file_ci:
                continue

            # Check the support for POPCNT
            if not cpu['popcnt'] and "popcnt" in file_ci:
                continue

            # Check the support for BMI2
            if not cpu['bmi2'] and "bmi2" in file_ci:
                continue

            # Great, this is an engine !
            found_engines.append(fullname)

    # Return the found engines as an array of full file names
    return found_engines
