import os
import platform
import sys
from collections import namedtuple


# Constants
AUTO_DETECT = True
NO_AUTO_DETECT = False

# CPUID
BITNESS = "64" if platform.machine().endswith('64') else "32"
POPCOUNT = True  # TODO Auto-detect
BMI2 = True  # TODO Auto-detect

# List of known interpreters
PYTHONBIN = sys.executable.split("/")[-1]
VM = namedtuple('VM', 'name, ext, args')
VM_LIST = [
    VM("node", ".js", None),
    VM("java", ".jar", ["-jar"]),
    VM(PYTHONBIN, ".py", ["-u"])
]

# Needed by shutil.which() on Windows to find .py engines
if sys.platform == "win32":
    for vm in VM_LIST:
        if vm.ext.upper() not in os.getenv("PATHEXT"):
            os.environ["PATHEXT"] += ";%s" % vm.ext.upper()

# List of engines later sorted by descending length of name
# The comments provides known conflicts with Linux packages
# Weak engines (<2700) should be added manually unless a package exists already
if sys.platform == "win32":
    stockfish_name = "stockfish_10_x%s.exe" % BITNESS
    sjaakii_name = "sjaakii_win%s_ms.exe" % BITNESS
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
    ENGINE("stockfish", "uci", "no", 3546, AUTO_DETECT, None),
    ENGINE("houdini", "uci", "be", 3520, AUTO_DETECT, None),
    ENGINE("komodo", "uci", "us", 3502, AUTO_DETECT, None),
    ENGINE("leela", "uci", "us", 3473, NO_AUTO_DETECT, None),
    ENGINE("lczero", "uci", "us", 3473, NO_AUTO_DETECT, None),
    ENGINE("lc0", "uci", "us", 3473, NO_AUTO_DETECT, None),
    ENGINE("fire", "uci", "us", 3422, NO_AUTO_DETECT, None),  # fire in mesa-demos https://www.archlinux.org/packages/extra/x86_64/mesa-demos/files/
    ENGINE("xiphos", "uci", "us", 3403, NO_AUTO_DETECT, None),  # xiphos - environment for Bible reading, study, and research
    ENGINE("ethereal", "uci", "us", 3389, AUTO_DETECT, None),
    ENGINE("laser", "uci", "us", 3367, AUTO_DETECT, None),
    ENGINE("fizbo", "uci", "us", 3339, AUTO_DETECT, None),
    ENGINE("andscacs", "uci", "ad", 3335, AUTO_DETECT, None),
    ENGINE("booot", "uci", "ua", 3324, AUTO_DETECT, None),  # Formerly XB
    ENGINE("shredder", "uci", "de", 3322, AUTO_DETECT, None),
    ENGINE("schooner", "xboard", "ca", 3274, AUTO_DETECT, None),
    ENGINE("gull", "uci", "ru", 3259, AUTO_DETECT, None),
    ENGINE("equinox", "uci", "it", 3251, AUTO_DETECT, None),
    ENGINE("arasan", "uci", "us", 3248, AUTO_DETECT, None),
    ENGINE("chiron", "uci", "it", 3240, AUTO_DETECT, None),  # Allows XB
    ENGINE("rofchade", "uci", "nl", 3233, AUTO_DETECT, None),
    ENGINE("critter", "uci", "sk", 3231, AUTO_DETECT, None),
    ENGINE("hannibal", "uci", "us", 3228, AUTO_DETECT, None),
    ENGINE("fritz", "uci", "nl", 3226, AUTO_DETECT, None),
    ENGINE("nirvana", "uci", "us", 3224, AUTO_DETECT, None),
    ENGINE("texel", "xboard", "se", 3205, AUTO_DETECT, None),  # UCI is an option in the command line
    ENGINE("rybka", "uci", "cz", 3204, AUTO_DETECT, None),
    ENGINE("blackmamba", "uci", "it", 3196, AUTO_DETECT, None),
    ENGINE("pedone", "uci", "it", 3193, AUTO_DETECT, None),
    ENGINE("vajolet", "uci", "it", 3180, AUTO_DETECT, None),
    ENGINE("senpai", "uci", "fr", 3176, AUTO_DETECT, None),
    # ivanhoe, robbolito, panchess, bouquet, elektro
    ENGINE("nemorino", "uci", "de", 3170, AUTO_DETECT, None),  # Allows XB
    ENGINE("wasp", "uci", "us", 3155, AUTO_DETECT, None),
    ENGINE("naum", "uci", "rs", 3150, AUTO_DETECT, None),
    ENGINE("strelka", "uci", "ru", 3140, AUTO_DETECT, None),
    ENGINE("chessbrain", "uci", "de", 3129, AUTO_DETECT, None),  # Allows XB
    ENGINE("protector", "uci", "de", 3127, AUTO_DETECT, None),
    ENGINE("defenchess", "uci", "tr", 3118, AUTO_DETECT, None),
    ENGINE("hiarcs", "uci", "gb", 3107, AUTO_DETECT, None),
    ENGINE("rubichess", "uci", "de", 3104, AUTO_DETECT, None),
    ENGINE("demolito", "uci", "fr", 3103, AUTO_DETECT, None),
    ENGINE("rodent", "uci", "pl", 3092, AUTO_DETECT, None),
    ENGINE("chess22k", "uci", "nl", 3083, AUTO_DETECT, None),
    ENGINE("pirarucu", "uci", "br", 3082, AUTO_DETECT, None),
    # ice (name too short)
    ENGINE("cheng", "uci", "cz", 3065, AUTO_DETECT, None),
    ENGINE("bobcat", "uci", "nl", 3056, AUTO_DETECT, None),
    ENGINE("crafty", "xboard", "us", 3056, AUTO_DETECT, None),
    ENGINE("smarthink", "uci", "ru", 3037, AUTO_DETECT, None),  # Allows XB
    ENGINE("spike", "uci", "de", 3036, AUTO_DETECT, None),  # Allows XB
    ENGINE("alfil", "uci", "es", 3030, AUTO_DETECT, None),
    ENGINE("spark", "uci", "nl", 3028, NO_AUTO_DETECT, None),  # spark - Apache tool
    ENGINE("junior", "uci", "il", 3025, AUTO_DETECT, None),
    ENGINE("hakkapeliitta", "uci", "fi", 3022, AUTO_DETECT, None),
    ENGINE("gogobello", "uci", "it", 3015, AUTO_DETECT, None),
    ENGINE("exchess", "xboard", "us", 3012, AUTO_DETECT, None),
    ENGINE("deuterium", "uci", "ph", 2999, AUTO_DETECT, None),
    ENGINE("baron", "xboard", "nl", 2996, AUTO_DETECT, None),
    ENGINE("tucano", "xboard", "br", 2994, AUTO_DETECT, None),
    ENGINE("scorpio", "xboard", "et", 2993, AUTO_DETECT, None),
    ENGINE("gaviota", "xboard", "ar", 2971, AUTO_DETECT, None),
    ENGINE("zappa", "uci", "us", 2970, AUTO_DETECT, None),
    ENGINE("togaii", "uci", "de", 2962, AUTO_DETECT, None),
    ENGINE("toga2", "uci", "de", 2962, AUTO_DETECT, None),
    ENGINE("onno", "uci", "de", 2954, AUTO_DETECT, None),
    ENGINE("amoeba", "uci", "fr", 2951, AUTO_DETECT, None),
    ENGINE("thinker", "uci", "ca", 2951, AUTO_DETECT, None),
    ENGINE("winter", "uci", "ch", 2946, NO_AUTO_DETECT, None),
    ENGINE("sjeng", "xboard", "be", 2939, AUTO_DETECT, None),
    ENGINE("marvin", "uci", "se", 2935, AUTO_DETECT, None),  # Allows XB
    ENGINE("disasterarea", "uci", "de", 2932, AUTO_DETECT, None),
    ENGINE("dirty", "xboard", "es", 2929, AUTO_DETECT, None),
    ENGINE("atlas", "uci", "es", 2926, NO_AUTO_DETECT, None),
    ENGINE("minko", "uci", "sv", 2922, AUTO_DETECT, None),
    ENGINE("discocheck", "uci", "fr", 2913, AUTO_DETECT, None),
    ENGINE("bright", "uci", "nl", 2909, AUTO_DETECT, None),
    ENGINE("monolith", "uci", "it", 2904, NO_AUTO_DETECT, None),
    ENGINE("zurichess", "uci", "ro", 2899, AUTO_DETECT, None),
    ENGINE("quazar", "uci", "ru", 2898, AUTO_DETECT, None),
    ENGINE("daydreamer", "uci", "us", 2896, AUTO_DETECT, None),
    ENGINE("cheese", "uci", "fr", 2887, NO_AUTO_DETECT, None),  # Allows XB; cheese - tool to take pictures and videos from your webcam
    ENGINE("godel", "uci", "es", 2882, AUTO_DETECT, None),  # May allow XB
    ENGINE("murka", "uci", "by", 2881, AUTO_DETECT, None),
    ENGINE("loop", "uci", "de", 2880, NO_AUTO_DETECT, None),
    ENGINE("tornado", "uci", "de", 2866, AUTO_DETECT, None),
    ENGINE("nemo", "uci", "de", 2856, NO_AUTO_DETECT, None),  # nemo - File manager and graphical shell for Cinnamon
    ENGINE("topple", "uci", "unknown", 2845, NO_AUTO_DETECT, None),
    ENGINE("bugchess", "xboard", "fr", 2842, AUTO_DETECT, None),
    ENGINE("counter", "uci", "ru", 2837, NO_AUTO_DETECT, None),
    ENGINE("shield", "uci", "it", 2832, NO_AUTO_DETECT, None),
    ENGINE("octochess", "uci", "de", 2822, AUTO_DETECT, None),  # Allows XB
    ENGINE("gnuchessu", "uci", "us", 2807, NO_AUTO_DETECT, None),
    ENGINE("gnuchess", "xboard", "us", 2807, AUTO_DETECT, None),
    ENGINE("rhetoric", "uci", "es", 2801, AUTO_DETECT, None),
    ENGINE("ruydos", "uci", "es", 2799, AUTO_DETECT, None),
    ENGINE("fridolin", "uci", "de", 2794, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("ktulu", "uci", "ir", 2782, AUTO_DETECT, None),  # Allows XB
    ENGINE("tomitank", "uci", "hu", 2777, NO_AUTO_DETECT, None),
    ENGINE("twisted-logic", "uci", "ph", 2769, AUTO_DETECT, None),
    ENGINE("frenzee", "xboard", "dk", 2768, AUTO_DETECT, None),
    ENGINE("prodeo", "uci", "nl", 2768, AUTO_DETECT, None),  # Allows XB
    ENGINE("pawny", "uci", "bg", 2767, AUTO_DETECT, None),
    ENGINE("bison", "uci", "ru", 2761, NO_AUTO_DETECT, None),  # bison - YACC-compatible parser generator
    ENGINE("arminius", "xboard", "de", 2760, NO_AUTO_DETECT, None),
    ENGINE("chessmaster", "xboard", "nl", 2757, AUTO_DETECT, None),
    ENGINE("karballo", "uci", "es", 2754, AUTO_DETECT, None),
    ENGINE("jonny", "uci", "de", 2749, AUTO_DETECT, None),  # Formerly XB
    ENGINE("chronos", "uci", "ar", 2739, AUTO_DETECT, None),
    ENGINE("francesca", "xboard", "gb", 2727, NO_AUTO_DETECT, None),
    ENGINE("devel", "uci", "no", 2718, NO_AUTO_DETECT, None),
    ENGINE("greko", "uci", "ru", 2716, AUTO_DETECT, None),
    ENGINE("tiger", "uci", "gp", 2714, AUTO_DETECT, None),
    ENGINE("donna", "uci", "us", 2703, NO_AUTO_DETECT, None),
    ENGINE("minic", "xboard", "fr", 2694, NO_AUTO_DETECT, None),
    ENGINE("redqueen", "uci", "br", 2689, NO_AUTO_DETECT, None),
    ENGINE("delfi", "uci", "it", 2683, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("djinn", "xboard", "us", 2678, NO_AUTO_DETECT, None),
    ENGINE("pharaon", "uci", "fr", 2676, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("ece-x3", "uci", "it", 2674, NO_AUTO_DETECT, None),
    ENGINE("gandalf", "uci", "dk", 2669, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("alaric", "uci", "se", 2664, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("nebula", "uci", "rs", 2656, NO_AUTO_DETECT, None),
    ENGINE("phalanx", "xboard1", "cz", 2655, NO_AUTO_DETECT, None),
    ENGINE("asymptote", "uci", "de", 2653, NO_AUTO_DETECT, None),
    ENGINE("dorky", "xboard", "us", 2653, NO_AUTO_DETECT, None),
    ENGINE("naraku", "uci", "it", 2652, NO_AUTO_DETECT, None),
    ENGINE("colossus", "uci", "gb", 2642, NO_AUTO_DETECT, None),
    ENGINE("cyrano", "uci", "no", 2641, NO_AUTO_DETECT, None),
    ENGINE("sjakk", "uci", "no", 2640, NO_AUTO_DETECT, None),
    ENGINE("rodin", "xboard", "es", 2636, NO_AUTO_DETECT, None),
    ENGINE("et_chess", "xboard2", "fr", 2634, NO_AUTO_DETECT, None),
    ENGINE("igel", "uci", "ch", 2634, NO_AUTO_DETECT, None),
    ENGINE("wyldchess", "uci", "in", 2630, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("wildcat", "uci", "by", 2623, NO_AUTO_DETECT, None),  # Formerly XB
    ENGINE("movei", "uci", "il", 2622, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("danasah", "uci", "es", 2621, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("philou", "uci", "fr", 2620, NO_AUTO_DETECT, None),
    ENGINE("zarkov", "xboard", "us", 2619, NO_AUTO_DETECT, None),
    ENGINE("rotor", "uci", "nl", 2618, NO_AUTO_DETECT, None),
    ENGINE("sloppy", "xboard", "fi", 2617, NO_AUTO_DETECT, None),
    ENGINE("schess", "uci", "us", 2614, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("sblitz", "uci", "us", 2614, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("coiled", "uci", "es", 2611, NO_AUTO_DETECT, None),
    ENGINE("delocto", "uci", "at", 2610, NO_AUTO_DETECT, None),
    ENGINE("glass", "uci", "pl", 2609, NO_AUTO_DETECT, None),
    ENGINE("ruffian", "uci", "se", 2609, NO_AUTO_DETECT, None),
    ENGINE("noragrace", "xboard", "us", 2607, NO_AUTO_DETECT, None),
    ENGINE("garbochess", "uci", "us", 2606, NO_AUTO_DETECT, None),
    ENGINE("jellyfish", "uci", "unknown", 2606, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("amyan", "uci", "cl", 2604, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("lemming", "xboard", "us", 2599, NO_AUTO_DETECT, None),
    ENGINE("caligula", "uci", "es", 2597, NO_AUTO_DETECT, None),
    # k2 (name to short)
    # n2 (name to short)
    ENGINE("nawito", "uci", "cu", 2586, NO_AUTO_DETECT, None),
    ENGINE("floyd", "uci", "nl", 2584, NO_AUTO_DETECT, None),
    ENGINE("muse", "xboard", "ch", 2583, NO_AUTO_DETECT, None),  # May support UCI as well
    ENGINE("cuckoo", "xboard", "se", 2582, NO_AUTO_DETECT, None),  # UCI is an option in the command line
    ENGINE("hamsters", "uci", "it", 2578, NO_AUTO_DETECT, None),
    ENGINE("pseudo", "xboard", "cz", 2575, NO_AUTO_DETECT, None),
    # sos (name too short)
    ENGINE("maverick", "uci", "gb", 2566, NO_AUTO_DETECT, None),
    ENGINE("petir", "xboard", "id", 2566, NO_AUTO_DETECT, None),
    ENGINE("aristarch", "uci", "de", 2565, NO_AUTO_DETECT, None),
    ENGINE("capivara", "uci", "br", 2565, NO_AUTO_DETECT, None),
    ENGINE("dimitri", "uci", "it", 2561, NO_AUTO_DETECT, None),  # May allow XB
    ENGINE("nanoszachy", "xboard", "pl", 2557, NO_AUTO_DETECT, None),
    ENGINE("brutus", "xboard", "nl", 2555, NO_AUTO_DETECT, None),
    ENGINE("ghost", "xboard", "de", 2552, NO_AUTO_DETECT, None),
    ENGINE("rebel", "uci", "nl", 2547, NO_AUTO_DETECT, None),
    ENGINE("anaconda", "uci", "de", 2545, NO_AUTO_DETECT, None),
    ENGINE("hermann", "uci", "de", 2540, NO_AUTO_DETECT, None),
    ENGINE("anmon", "uci", "fr", 2539, NO_AUTO_DETECT, None),
    ENGINE("betsabe", "xboard", "es", 2539, NO_AUTO_DETECT, None),
    ENGINE("ufim", "uci", "ru", 2539, NO_AUTO_DETECT, None),  # Formerly XB
    ENGINE("pupsi", "uci", "se", 2537, NO_AUTO_DETECT, None),
    ENGINE("jikchess", "xboard2", "fi", 2523, NO_AUTO_DETECT, None),
    ENGINE("pepito", "xboard", "es", 2520, NO_AUTO_DETECT, None),
    ENGINE("orion", "uci", "fr", 2514, NO_AUTO_DETECT, None),
    ENGINE("danchess", "xboard", "et", 2507, NO_AUTO_DETECT, None),
    ENGINE("greenlight", "xboard", "gb", 2505, NO_AUTO_DETECT, None),
    ENGINE("goliath", "uci", "de", 2504, NO_AUTO_DETECT, None),
    ENGINE("yace", "uci", "de", 2503, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("trace", "xboard", "au", 2502, NO_AUTO_DETECT, None),
    ENGINE("bagatur", "uci", "bg", 2494, NO_AUTO_DETECT, None),
    ENGINE("cyberpagno", "xboard", "it", 2492, NO_AUTO_DETECT, None),
    ENGINE("magnum", "uci", "ca", 2492, NO_AUTO_DETECT, None),
    ENGINE("jumbo", "xboard", "de", 2490, NO_AUTO_DETECT, None),
    ENGINE("bruja", "xboard", "us", 2489, NO_AUTO_DETECT, None),
    # tao (name too short)
    ENGINE("delphil", "uci", "fr", 2481, NO_AUTO_DETECT, None),
    ENGINE("drosophila", "xboard", "se", 2481, NO_AUTO_DETECT, None),
    ENGINE("gothmog", "uci", "no", 2478, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("bbchess", "uci", "si", 2475, NO_AUTO_DETECT, None),
    ENGINE("mephisto", "uci", "gb", 2475, NO_AUTO_DETECT, None),
    ENGINE("nemeton", "xboard", "nl", 2472, NO_AUTO_DETECT, None),
    ENGINE("cerebro", "xboard", "it", 2470, NO_AUTO_DETECT, None),
    ENGINE("kiwi", "xboard", "it", 2469, NO_AUTO_DETECT, None),
    ENGINE("xpdnt", "xboard", "us", 2467, NO_AUTO_DETECT, None),
    ENGINE("myrddin", "xboard", "us", 2464, NO_AUTO_DETECT, None),
    ENGINE("frank-walter", "xboard", "nl", 2463, NO_AUTO_DETECT, None),
    ENGINE("pikoszachy", "xboard", "pl", 2456, NO_AUTO_DETECT, None),
    ENGINE("anatoli", "xboard", "nl", 2454, NO_AUTO_DETECT, None),
    ENGINE("littlethought", "uci", "au", 2454, NO_AUTO_DETECT, None),
    ENGINE("matacz", "xboard", "pl", 2445, NO_AUTO_DETECT, None),
    ENGINE("lozza", "uci", "gb", 2441, NO_AUTO_DETECT, None),
    ENGINE("ares", "uci", "us", 2439, NO_AUTO_DETECT, None),
    ENGINE("bumblebee", "uci", "us", 2439, NO_AUTO_DETECT, None),
    ENGINE("soldat", "xboard", "it", 2439, NO_AUTO_DETECT, None),
    ENGINE("spider", "xboard", "nl", 2439, NO_AUTO_DETECT, None),
    ENGINE("madchess", "uci", "us", 2436, NO_AUTO_DETECT, None),
    ENGINE("abrok", "uci", "de", 2434, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("lambchop", "uci", "nz", 2434, NO_AUTO_DETECT, None),  # Formerly XB
    ENGINE("kingofkings", "uci", "ca", 2432, NO_AUTO_DETECT, None),
    ENGINE("shallow", "uci", "unknown", 2429, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("eeyore", "uci", "ru", 2426, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("gaia", "uci", "fr", 2425, NO_AUTO_DETECT, None),
    ENGINE("nejmet", "uci", "fr", 2425, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("gromit", "uci", "de", 2422, NO_AUTO_DETECT, None),
    ENGINE("quark", "xboard", "de", 2422, NO_AUTO_DETECT, None),
    ENGINE("snitch", "xboard", "de", 2419, NO_AUTO_DETECT, None),
    ENGINE("dragon", "xboard", "fr", 2418, NO_AUTO_DETECT, None),
    ENGINE("hussar", "uci", "hu", 2418, NO_AUTO_DETECT, None),
    ENGINE("flux", "uci", "ch", 2416, NO_AUTO_DETECT, None),
    ENGINE("olithink", "xboard", "de", 2416, NO_AUTO_DETECT, None),
    ENGINE("romichess", "xboard", "us", 2413, NO_AUTO_DETECT, None),
    ENGINE("typhoon", "xboard", "us", 2413, NO_AUTO_DETECT, None),
    ENGINE("simplex", "uci", "es", 2410, NO_AUTO_DETECT, None),
    ENGINE("giraffe", "xboard", "gb", 2409, NO_AUTO_DETECT, None),
    ENGINE("zevra", "uci", "ru", 2407, NO_AUTO_DETECT, None),
    ENGINE("taltos", "uci", "hu", 2406, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("teki", "uci", "in", 2406, NO_AUTO_DETECT, None),
    ENGINE("ifrit", "uci", "ru", 2401, NO_AUTO_DETECT, None),
    ENGINE("tjchess", "uci", "us", 2398, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("knightdreamer", "xboard", "se", 2394, NO_AUTO_DETECT, None),
    ENGINE("galjoen", "uci", "be", 2393, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("bearded", "xboard", "pl", 2391, NO_AUTO_DETECT, None),
    ENGINE("postmodernist", "xboard", "gb", 2389, NO_AUTO_DETECT, None),
    ENGINE("comet", "xboard", "de", 2388, NO_AUTO_DETECT, None),
    ENGINE("leila", "xboard", "it", 2386, NO_AUTO_DETECT, None),
    # amy (name too short)
    ENGINE("capture", "xboard", "fr", 2385, NO_AUTO_DETECT, None),
    ENGINE("diablo", "uci", "us", 2385, NO_AUTO_DETECT, None),
    ENGINE("barbarossa", "uci", "at", 2384, NO_AUTO_DETECT, None),
    ENGINE("gosu", "xboard", "pl", 2381, NO_AUTO_DETECT, None),
    ENGINE("invictus", "uci", "ph", 2376, NO_AUTO_DETECT, None),
    ENGINE("cmcchess", "uci", "zh", 2375, NO_AUTO_DETECT, None),
    ENGINE("jazz", "xboard", "nl", 2374, NO_AUTO_DETECT, None),
    ENGINE("patzer", "xboard", "de", 2374, NO_AUTO_DETECT, None),
    ENGINE("bringer", "xboard", "de", 2373, NO_AUTO_DETECT, None),
    ENGINE("wchess", "xboard", "us", 2369, NO_AUTO_DETECT, None),  # Unsure protocol
    ENGINE("terra", "uci", "se", 2368, NO_AUTO_DETECT, None),
    ENGINE("crazybishop", "xboard", "fr", 2363, NO_AUTO_DETECT, None),  # Named as tcb
    ENGINE("betsy", "xboard", "us", 2356, NO_AUTO_DETECT, None),
    ENGINE("homer", "uci", "de", 2356, NO_AUTO_DETECT, None),
    ENGINE("jonesy", "xboard", "es", 2353, NO_AUTO_DETECT, None),  # popochin
    ENGINE("amateur", "xboard", "us", 2351, NO_AUTO_DETECT, None),
    ENGINE("alex", "uci", "us", 2347, NO_AUTO_DETECT, None),
    ENGINE("tigran", "uci", "es", 2345, NO_AUTO_DETECT, None),
    ENGINE("popochin", "xboard", "es", 2342, NO_AUTO_DETECT, None),
    ENGINE("horizon", "xboard", "us", 2341, NO_AUTO_DETECT, None),
    ENGINE("plisk", "uci", "us", 2339, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("queen", "uci", "nl", 2337, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("arion", "uci", "fr", 2333, NO_AUTO_DETECT, None),
    ENGINE("eveann", "xboard", "es", 2332, NO_AUTO_DETECT, None),
    ENGINE("gibbon", "uci", "fr", 2332, NO_AUTO_DETECT, None),
    ENGINE("waxman", "xboard", "us", 2331, NO_AUTO_DETECT, None),
    ENGINE("sorgenkind", "xboard", "dk", 2330, NO_AUTO_DETECT, None),
    ENGINE("thor", "xboard", "hr", 2330, NO_AUTO_DETECT, None),
    ENGINE("amundsen", "xboard", "se", 2329, NO_AUTO_DETECT, None),
    ENGINE("sage", "xboard", "unknown", 2325, NO_AUTO_DETECT, None),
    ENGINE("chezzz", "xboard", "dk", 2324, NO_AUTO_DETECT, None),
    # isa (name too short)
    ENGINE("knightx", "xboard2", "fr", 2320, NO_AUTO_DETECT, None),
    ENGINE("mediocre", "uci", "se", 2316, NO_AUTO_DETECT, None),
    ENGINE("absolute-zero", "uci", "zh", 2315, NO_AUTO_DETECT, None),
    ENGINE("aice", "xboard", "gr", 2315, NO_AUTO_DETECT, None),
    ENGINE("sungorus", "uci", "es", 2313, NO_AUTO_DETECT, None),
    ENGINE("nebiyu", "xboard", "et", 2310, NO_AUTO_DETECT, None),  # wine crash on Ubuntu 1804 with NebiyuAlien.exe
    ENGINE("asterisk", "uci", "hu", 2307, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("averno", "xboard", "es", 2307, NO_AUTO_DETECT, None),
    ENGINE("joker", "xboard", "nl", 2307, NO_AUTO_DETECT, None),
    ENGINE("kingfisher", "uci", "hk", 2304, NO_AUTO_DETECT, None),
    ENGINE("tytan", "xboard", "pl", 2304, NO_AUTO_DETECT, None),
    ENGINE("starthinker", "uci", "de", 2295, NO_AUTO_DETECT, None),
    ENGINE("resp", "xboard", "de", 2295, NO_AUTO_DETECT, None),
    ENGINE("ayito", "uci", "es", 2287, NO_AUTO_DETECT, None),  # Formerly XB
    ENGINE("chaturanga", "xboard", "it", 2285, NO_AUTO_DETECT, None),
    ENGINE("matilde", "xboard", "it", 2281, NO_AUTO_DETECT, None),
    ENGINE("fischerle", "uci", "de", 2280, NO_AUTO_DETECT, None),
    ENGINE("dumb", "uci", "fr", 2274, NO_AUTO_DETECT, None),
    ENGINE("rival", "uci", "gb", 2274, NO_AUTO_DETECT, None),
    ENGINE("ct800", "uci", "de", 2272, NO_AUTO_DETECT, None),
    ENGINE("paladin", "uci", "in", 2272, NO_AUTO_DETECT, None),
    # esc (name too short)
    ENGINE("butcher", "xboard", "pl", 2266, NO_AUTO_DETECT, None),
    ENGINE("scidlet", "xboard", "nz", 2266, NO_AUTO_DETECT, None),
    ENGINE("zeus", "xboard", "ru", 2262, NO_AUTO_DETECT, None),
    ENGINE("natwarlal", "xboard", "in", 2261, NO_AUTO_DETECT, None),
    # doctor (unknown protocol)
    ENGINE("kmtchess", "xboard", "es", 2260, NO_AUTO_DETECT, None),
    ENGINE("robocide", "uci", "gb", 2255, NO_AUTO_DETECT, None),
    ENGINE("firefly", "uci", "hk", 2253, NO_AUTO_DETECT, None),
    ENGINE("napoleon", "uci", "it", 2251, NO_AUTO_DETECT, None),
    ENGINE("dorpsgek", "xboard", "en", 2237, NO_AUTO_DETECT, None),
    ENGINE("gopher_check", "uci", "us", 2237, NO_AUTO_DETECT, None),
    # ant (name too short)
    ENGINE("anechka", "uci", "ru", 2235, NO_AUTO_DETECT, None),
    ENGINE("alichess", "uci", "de", 2229, NO_AUTO_DETECT, None),
    ENGINE("joker2", "uci", "it", 2228, NO_AUTO_DETECT, None),
    ENGINE("obender", "xboard", "ru", 2224, NO_AUTO_DETECT, None),
    ENGINE("adam", "xboard", "fr", 2221, NO_AUTO_DETECT, None),
    ENGINE("ramjet", "uci", "it", 2220, NO_AUTO_DETECT, None),
    ENGINE("exacto", "xboard", "us", 2217, NO_AUTO_DETECT, None),
    ENGINE("buzz", "xboard", "us", 2215, NO_AUTO_DETECT, None),
    ENGINE("chispa", "uci", "ar", 2207, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("chessalex", "uci", "ru", 2206, NO_AUTO_DETECT, None),
    ENGINE("beowulf", "xboard", "gb", 2203, NO_AUTO_DETECT, None),
    ENGINE("weini", "xboard", "fr", 2201, NO_AUTO_DETECT, None),  # Allows UCI
    ENGINE("rattate", "xboard", "it", 2199, NO_AUTO_DETECT, None),
    ENGINE("latista", "xboard", "us", 2195, NO_AUTO_DETECT, None),
    ENGINE("sinobyl", "xboard", "us", 2195, NO_AUTO_DETECT, None),
    ENGINE("ng-play", "xboard", "gr", 2195, NO_AUTO_DETECT, None),
    ENGINE("feuerstein", "uci", "de", 2192, NO_AUTO_DETECT, None),
    # uralochka (blacklisted)
    ENGINE("neurosis", "xboard", "nl", 2188, NO_AUTO_DETECT, None),
    ENGINE("atak", "xboard", "pl", 2184, NO_AUTO_DETECT, None),
    ENGINE("madeleine", "uci", "it", 2183, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("mango", "xboard", "ve", 2182, NO_AUTO_DETECT, None),
    ENGINE("protej", "uci", "it", 2178, NO_AUTO_DETECT, None),
    ENGINE("sjaakii", "xboard", "nl", 2177, NO_AUTO_DETECT, None),
    ENGINE("baislicka", "uci", "unknown", 2172, NO_AUTO_DETECT, None),
    ENGINE("genesis", "xboard", "il", 2171, NO_AUTO_DETECT, None),
    ENGINE("blackbishop", "uci", "de", 2163, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("inmichess", "xboard", "at", 2162, NO_AUTO_DETECT, None),
    ENGINE("kurt", "xboard", "de", 2162, NO_AUTO_DETECT, None),
    ENGINE("blitzkrieg", "uci", "in", 2157, NO_AUTO_DETECT, None),
    ENGINE("nagaskaki", "xboard", "za", 2154, NO_AUTO_DETECT, None),
    ENGINE("chesley", "xboard", "us", 2147, NO_AUTO_DETECT, None),
    ENGINE("alarm", "xboard", "se", 2145, NO_AUTO_DETECT, None),
    ENGINE("tunguska", "uci", "br", 2145, NO_AUTO_DETECT, None),
    ENGINE("hedgehog", "uci", "ru", 2143, NO_AUTO_DETECT, None),
    ENGINE("lime", "uci", "gb", 2143, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("axolotl", "uci", "de", 2140, NO_AUTO_DETECT, None),
    ENGINE("sunsetter", "xboard", "de", 2139, NO_AUTO_DETECT, None),
    ENGINE("tinychess", "uci", "unknown", 2137, NO_AUTO_DETECT, None),
    ENGINE("chesskiss", "xboard", "unknown", 2136, NO_AUTO_DETECT, None),
    ENGINE("fortress", "xboard", "it", 2134, NO_AUTO_DETECT, None),
    ENGINE("nesik", "xboard", "pl", 2134, NO_AUTO_DETECT, None),
    ENGINE("wjchess", "uci", "fr", 2131, NO_AUTO_DETECT, None),
    # merlin (no information)
    ENGINE("prophet", "xboard", "us", 2124, NO_AUTO_DETECT, None),
    ENGINE("uragano", "xboard", "it", 2123, NO_AUTO_DETECT, None),
    ENGINE("clever-girl", "uci", "us", 2117, NO_AUTO_DETECT, None),
    ENGINE("embla", "uci", "nl", 2115, NO_AUTO_DETECT, None),
    ENGINE("spacedog", "uci", "uk", 2113, NO_AUTO_DETECT, None),  # Allows XB
    # gk (name too short)
    # alf (name too short)
    ENGINE("knockout", "xboard", "de", 2107, NO_AUTO_DETECT, None),
    ENGINE("bikjump", "uci", "nl", 2104, NO_AUTO_DETECT, None),
    ENGINE("wing", "xboard", "nl", 2101, NO_AUTO_DETECT, None),
    ENGINE("clarabit", "uci", "es", 2098, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("adroitchess", "uci", "gb", 2082, NO_AUTO_DETECT, None),
    ENGINE("parrot", "xboard", "us", 2079, NO_AUTO_DETECT, None),
    ENGINE("abbess", "xboard", "us", 2069, NO_AUTO_DETECT, None),
    ENGINE("gunborg", "uci", "unknown", 2069, NO_AUTO_DETECT, None),
    ENGINE("crabby", "uci", "us", 2068, NO_AUTO_DETECT, None),
    ENGINE("alcibiades", "uci", "bg", 2065, NO_AUTO_DETECT, None),
    ENGINE("cinnamon", "uci", "it", 2065, NO_AUTO_DETECT, None),
    ENGINE("little-wing", "uci", "fr", 2062, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("matheus", "uci", "br", 2059, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("potato", "xboard", "at", 2059, NO_AUTO_DETECT, None),
    ENGINE("chessmind", "uci", "de", 2057, NO_AUTO_DETECT, None),
    ENGINE("monarch", "uci", "gb", 2057, NO_AUTO_DETECT, None),
    ENGINE("dolphin", "xboard", "vn", 2055, NO_AUTO_DETECT, None),
    ENGINE("kingsout", "xboard", "de", 2055, NO_AUTO_DETECT, None),
    ENGINE("smash", "uci", "it", 2053, NO_AUTO_DETECT, None),
    ENGINE("bodo", "uci", "au", 2049, NO_AUTO_DETECT, None),
    ENGINE("rdchess", "xboard", "at", 2046, NO_AUTO_DETECT, None),
    ENGINE("gerbil", "xboard", "us", 2043, NO_AUTO_DETECT, None),
    ENGINE("vice", "uci", "unknown", 2041, NO_AUTO_DETECT, None),  # Both UCI/XBoard
    # ax (name too short)
    ENGINE("detroid", "uci", "at", 2038, NO_AUTO_DETECT, None),
    ENGINE("jabba", "uci", "gb", 2035, NO_AUTO_DETECT, None),
    # plp (name too short)
    ENGINE("prochess", "uci", "it", 2029, NO_AUTO_DETECT, None),
    ENGINE("plywood", "xboard", "unknown", 2023, NO_AUTO_DETECT, None),
    # zct (name too short)
    ENGINE("zetadva", "xboard", "de", 2023, NO_AUTO_DETECT, None),
    ENGINE("bestia", "xboard", "ua", 2021, NO_AUTO_DETECT, None),
    ENGINE("bismark", "uci", "il", 2020, NO_AUTO_DETECT, None),
    ENGINE("ecce", "uci", "ru", 2015, NO_AUTO_DETECT, None),
    # schola (no information)
    ENGINE("delphimax", "uci", "de", 2013, NO_AUTO_DETECT, None),
    ENGINE("oberon", "xboard", "pl", 2012, NO_AUTO_DETECT, None),
    ENGINE("cupcake", "xboard", "us", 2011, NO_AUTO_DETECT, None),
    ENGINE("freyr", "xboard", "ro", 2009, NO_AUTO_DETECT, None),
    ENGINE("leonidas", "xboard", "nl", 2004, NO_AUTO_DETECT, None),
    ENGINE("requiem", "xboard", "fi", 2004, NO_AUTO_DETECT, None),
    ENGINE("ceibo", "uci", "ar", 1999, NO_AUTO_DETECT, None),
    ENGINE("goldfish", "uci", "no", 1997, NO_AUTO_DETECT, None),
    ENGINE("squared-chess", "uci", "de", 1996, NO_AUTO_DETECT, None),
    ENGINE("wowl", "uci", "de", 1995, NO_AUTO_DETECT, None),
    ENGINE("snowy", "uci", "us", 1992, NO_AUTO_DETECT, None),
    ENGINE("chess4j", "xboard", "us", 1991, NO_AUTO_DETECT, None),
    ENGINE("gullydeckel", "xboard", "de", 1991, NO_AUTO_DETECT, None),
    ENGINE("elephant", "xboard", "de", 1989, NO_AUTO_DETECT, None),
    ENGINE("biglion", "uci", "cm", 1988, NO_AUTO_DETECT, None),
    ENGINE("arabian-knight", "xboard", "pl", 1987, NO_AUTO_DETECT, None),
    ENGINE("armageddon", "xboard", "pl", 1985, NO_AUTO_DETECT, None),
    ENGINE("bubble", "uci", "br", 1985, NO_AUTO_DETECT, None),
    ENGINE("faile", "xboard1", "ca", 1977, NO_AUTO_DETECT, None),
    ENGINE("slibo", "xboard", "de", 1975, NO_AUTO_DETECT, None),
    ENGINE("matant", "xboard", "pl", 1967, NO_AUTO_DETECT, None),
    ENGINE("monik", "xboard", "unknown", 1967, NO_AUTO_DETECT, None),
    ENGINE("ssechess", "xboard", "us", 1967, NO_AUTO_DETECT, None),
    ENGINE("ladameblanche", "xboard", "fr", 1966, NO_AUTO_DETECT, None),
    ENGINE("sissa", "uci", "fr", 1961, NO_AUTO_DETECT, None),
    # bsc (name too short)
    ENGINE("cilian", "xboard", "ch", 1960, NO_AUTO_DETECT, None),
    # eia (name too short)
    ENGINE("alchess", "uci", "ru", 1958, NO_AUTO_DETECT, None),
    ENGINE("mustang", "xboard", "by", 1957, NO_AUTO_DETECT, None),
    ENGINE("etude", "uci", "us", 1954, NO_AUTO_DETECT, None),
    # franky (no information)
    ENGINE("micromax", "xboard", "nl", 1953, NO_AUTO_DETECT, None),
    ENGINE("umax", "xboard", "nl", 1953, NO_AUTO_DETECT, None),
    ENGINE("janwillem", "xboard", "nl", 1951, NO_AUTO_DETECT, None),
    ENGINE("wuttang", "uci", "in", 1949, NO_AUTO_DETECT, None),
    ENGINE("pleco", "uci", "us", 1948, NO_AUTO_DETECT, None),
    ENGINE("sharper", "xboard", "se", 1940, NO_AUTO_DETECT, None),
    ENGINE("bell", "xboard", "fr", 1937, NO_AUTO_DETECT, None),
    ENGINE("bibichess", "uci", "fr", 1927, NO_AUTO_DETECT, None),
    ENGINE("smirf", "xboard", "de", 1925, NO_AUTO_DETECT, None),
    ENGINE("heracles", "uci", "fr", 1921, NO_AUTO_DETECT, None),
    ENGINE("samchess", "xboard", "us", 1918, NO_AUTO_DETECT, None),
    ENGINE("iach", "xboard", "unknown", 1916, NO_AUTO_DETECT, None),
    ENGINE("eagle", "uci", "uci", 1913, NO_AUTO_DETECT, None),
    ENGINE("bambam", "xboard", "at", 1912, NO_AUTO_DETECT, None),
    ENGINE("reger", "xboard", "nl", 1911, NO_AUTO_DETECT, None),
    ENGINE("dabbaba", "xboard", "dk", 1906, NO_AUTO_DETECT, None),
    ENGINE("warrior", "xboard", "lv", 1906, NO_AUTO_DETECT, None),
    ENGINE("clueless", "uci", "de", 1904, NO_AUTO_DETECT, None),
    ENGINE("morphy", "xboard", "us", 1903, NO_AUTO_DETECT, None),
    ENGINE("claudia", "uci", "es", 1897, NO_AUTO_DETECT, None),
    ENGINE("snailchess", "xboard", "sg", 1897, NO_AUTO_DETECT, None),
    ENGINE("surprise", "xboard", "de", 1888, NO_AUTO_DETECT, None),
    ENGINE("matmoi", "xboard", "ca", 1887, NO_AUTO_DETECT, None),
    ENGINE("mrchess", "xboard", "sg", 1886, NO_AUTO_DETECT, None),
    ENGINE("tyrell", "uci", "us", 1886, NO_AUTO_DETECT, None),
    ENGINE("purplehaze", "xboard", "fr", 1884, NO_AUTO_DETECT, None),
    # freechess (blacklisted)
    ENGINE("butter", "uci", "unknown", 1865, NO_AUTO_DETECT, None),
    ENGINE("presbyter", "uci", "unknown", 1864, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("simontacchi", "uci", "us", 1862, NO_AUTO_DETECT, None),
    ENGINE("roce", "uci", "ch", 1854, NO_AUTO_DETECT, None),
    ENGINE("deepov", "uci", "fr", 1848, NO_AUTO_DETECT, None),
    ENGINE("ranita", "uci", "fr", 1843, NO_AUTO_DETECT, None),
    ENGINE("sayuri", "uci", "jp", 1836, NO_AUTO_DETECT, None),
    ENGINE("milady", "xboard", "fr", 1835, NO_AUTO_DETECT, None),
    ENGINE("heavychess", "uci", "ar", 1834, NO_AUTO_DETECT, None),
    ENGINE("ajedreztactico", "xboard", "mx", 1832, NO_AUTO_DETECT, None),
    ENGINE("skiull", "uci", "ve", 1831, NO_AUTO_DETECT, None),
    ENGINE("celes", "uci", "nl", 1826, NO_AUTO_DETECT, None),
    ENGINE("jars", "xboard", "fr", 1824, NO_AUTO_DETECT, None),
    ENGINE("rataaeroespacial", "xboard", "ar", 1819, NO_AUTO_DETECT, None),
    ENGINE("ziggurat", "uci", "us", 1818, NO_AUTO_DETECT, None),
    ENGINE("noonian", "uci", "us", 1814, NO_AUTO_DETECT, None),
    ENGINE("predateur", "uci", "fr", 1811, NO_AUTO_DETECT, None),
    ENGINE("chenard", "xboard", "us", 1810, NO_AUTO_DETECT, None),
    ENGINE("morphychess", "xboard", "us", 1805, NO_AUTO_DETECT, None),
    ENGINE("hoichess", "xboard", "de", 1804, NO_AUTO_DETECT, None),
    ENGINE("beaches", "xboard", "us", 1803, NO_AUTO_DETECT, None),
    ENGINE("sapeli", "uci", "fi", 1803, NO_AUTO_DETECT, None),
    ENGINE("macromix", "uci", "ua", 1800, NO_AUTO_DETECT, None),
    ENGINE("pigeon", "uci", "ca", 1799, NO_AUTO_DETECT, None),
    ENGINE("chessterfield", "xboard", "ch", 1797, NO_AUTO_DETECT, None),
    ENGINE("mobmat", "uci", "us", 1794, NO_AUTO_DETECT, None),
    ENGINE("enigma", "xboard", "pl", 1793, NO_AUTO_DETECT, None),
    ENGINE("bremboce", "xboard", "it", 1792, NO_AUTO_DETECT, None),
    ENGINE("adachess", "xboard", "it", 1791, NO_AUTO_DETECT, None),
    ENGINE("grizzly", "xboard", "de", 1787, NO_AUTO_DETECT, None),
    ENGINE("cecir", "xboard", "uy", 1786, NO_AUTO_DETECT, None),
    ENGINE("embracer", "xboard", "se", 1785, NO_AUTO_DETECT, None),
    ENGINE("cdrill", "uci", "unknown", 1784, NO_AUTO_DETECT, None),
    ENGINE("fauce", "xboard", "it", 1782, NO_AUTO_DETECT, None),
    ENGINE("berochess", "uci", "de", 1775, NO_AUTO_DETECT, None),
    ENGINE("pulsar", "xboard", "us", 1769, NO_AUTO_DETECT, None),
    ENGINE("apollo", "uci", "us", 1766, NO_AUTO_DETECT, None),
    ENGINE("mint", "xboard", "se", 1765, NO_AUTO_DETECT, None),
    ENGINE("robin", "xboard", "pl", 1763, NO_AUTO_DETECT, None),
    ENGINE("lodocase", "xboard", "be", 1761, NO_AUTO_DETECT, None),
    ENGINE("laurifer", "xboard", "pl", 1750, NO_AUTO_DETECT, None),
    ENGINE("ziggy", "uci", "is", 1745, NO_AUTO_DETECT, None),
    ENGINE("rocinante", "uci", "es", 1744, NO_AUTO_DETECT, None),
    ENGINE("vicki", "xboard", "za", 1744, NO_AUTO_DETECT, None),
    # elf (name too short)
    ENGINE("kanguruh", "xboard", "at", 1738, NO_AUTO_DETECT, None),
    ENGINE("shallowblue", "uci", "ca", 1734, NO_AUTO_DETECT, None),
    ENGINE("adamant", "xboard", "ru", 1733, NO_AUTO_DETECT, None),
    ENGINE("gchess", "xboard", "it", 1731, NO_AUTO_DETECT, None),
    ENGINE("zzzzzz", "xboard", "nl", 1730, NO_AUTO_DETECT, None),
    ENGINE("jaksah", "uci", "rs", 1726, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("kitteneitor", "xboard", "es", 1725, NO_AUTO_DETECT, None),
    ENGINE("zoidberg", "xboard", "es", 1724, NO_AUTO_DETECT, None),
    # see (name too short)
    ENGINE("tscp", "xboard", "us", 1721, NO_AUTO_DETECT, None),
    ENGINE("enkochess", "uci", "unknown", 1717, NO_AUTO_DETECT, None),
    ENGINE("aldebaran", "xboard", "it", 1713, NO_AUTO_DETECT, None),
    ENGINE("tristram", "xboard", "us", 1711, NO_AUTO_DETECT, None),
    ENGINE("testina", "uci", "it", 1699, NO_AUTO_DETECT, None),
    ENGINE("jester", "xboard", "us", 1695, NO_AUTO_DETECT, None),
    # chess (name too generic)
    ENGINE("sharpchess", "xboard", "unknown", 1692, NO_AUTO_DETECT, None),
    ENGINE("chengine", "xboard", "jp", 1683, NO_AUTO_DETECT, None),
    ENGINE("gargamella", "xboard", "it", 1683, NO_AUTO_DETECT, None),
    ENGINE("mizar", "xboard", "it", 1683, NO_AUTO_DETECT, None),
    ENGINE("bace", "xboard", "us", 1678, NO_AUTO_DETECT, None),
    ENGINE("polarchess", "xboard", "no", 1677, NO_AUTO_DETECT, None),
    ENGINE("golem", "xboard", "it", 1672, NO_AUTO_DETECT, None),
    ENGINE("tom-thumb", "uci", "nl", 1664, NO_AUTO_DETECT, None),
    ENGINE("belzebub", "xboard", "pl", 1662, NO_AUTO_DETECT, None),
    ENGINE("pooky", "uci", "us", 1657, NO_AUTO_DETECT, None),
    ENGINE("dchess", "xboard", "us", 1651, NO_AUTO_DETECT, None),
    ENGINE("simon", "xboard", "us", 1647, NO_AUTO_DETECT, None),
    ENGINE("iq23", "uci", "de", 1644, NO_AUTO_DETECT, None),
    ENGINE("spartan", "uci", "unknown", 1644, NO_AUTO_DETECT, None),
    ENGINE("vapor", "uci", "us", 1641, NO_AUTO_DETECT, None),
    ENGINE("chessrikus", "xboard", "us", 1635, NO_AUTO_DETECT, None),
    ENGINE("mscp", "xboard", "nl", 1633, NO_AUTO_DETECT, None),
    ENGINE("storm", "xboard", "us", 1630, NO_AUTO_DETECT, None),
    ENGINE("monochrome", "uci", "unknown", 1624, NO_AUTO_DETECT, None),
    ENGINE("saruman", "uci", "unknown", 1622, NO_AUTO_DETECT, None),
    ENGINE("jsbam", "xboard", "nl", 1621, NO_AUTO_DETECT, None),
    ENGINE("revati", "uci", "de", 1620, NO_AUTO_DETECT, None),
    ENGINE("kasparov", "uci", "ca", 1618, NO_AUTO_DETECT, None),
    ENGINE("philemon", "uci", "ch", 1616, NO_AUTO_DETECT, None),
    ENGINE("rainman", "xboard", "se", 1614, NO_AUTO_DETECT, None),
    ENGINE("bullitchess", "uci", "unknown", 1610, NO_AUTO_DETECT, None),
    ENGINE("pulse", "uci", "ch", 1606, NO_AUTO_DETECT, None),
    ENGINE("violet", "uci", "unknown", 1601, NO_AUTO_DETECT, None),
    ENGINE("marginal", "uci", "ru", 1600, NO_AUTO_DETECT, None),
    ENGINE("zotron", "xboard", "us", 1593, NO_AUTO_DETECT, None),
    ENGINE("darky", "uci", "mx", 1592, NO_AUTO_DETECT, None),
    ENGINE("casper", "uci", "gb", 1589, NO_AUTO_DETECT, None),
    ENGINE("dreamer", "xboard", "nl", 1581, NO_AUTO_DETECT, None),
    ENGINE("needle", "xboard", "fi", 1580, NO_AUTO_DETECT, None),
    ENGINE("damas", "xboard", "br", 1579, NO_AUTO_DETECT, None),
    ENGINE("vanilla", "xboard", "au", 1579, NO_AUTO_DETECT, None),
    ENGINE("sdbc", "xboard", "de", 1578, NO_AUTO_DETECT, None),
    ENGINE("cicada", "uci", "us", 1576, NO_AUTO_DETECT, None),
    ENGINE("hokus", "xboard", "pl", 1555, NO_AUTO_DETECT, None),
    ENGINE("mace", "uci", "de", 1546, NO_AUTO_DETECT, None),
    ENGINE("larsen", "xboard", "it", 1543, NO_AUTO_DETECT, None),
    ENGINE("trappist", "uci", "unknown", 1535, NO_AUTO_DETECT, None),
    ENGINE("yawce", "xboard", "dk", 1518, NO_AUTO_DETECT, None),
    ENGINE("supra", "uci", "pt", 1508, NO_AUTO_DETECT, None),
    ENGINE("piranha", "uci", "de", 1502, NO_AUTO_DETECT, None),
    ENGINE("alibaba", "uci", "nl", 1500, NO_AUTO_DETECT, None),
    ENGINE("koedem", "uci", "de", 1495, NO_AUTO_DETECT, None),
    ENGINE("apep", "xboard", "us", 1493, NO_AUTO_DETECT, None),
    ENGINE("tarrasch", "uci", "us", 1493, NO_AUTO_DETECT, None),
    ENGINE("andersen", "xboard", "se", 1491, NO_AUTO_DETECT, None),
    ENGINE("gedeone", "xboard", "unknown", 1486, NO_AUTO_DETECT, None),
    ENGINE("pwned", "uci", "us", 1484, NO_AUTO_DETECT, None),
    ENGINE("apil", "xboard", "de", 1482, NO_AUTO_DETECT, None),
    ENGINE("pentagon", "xboard", "it", 1480, NO_AUTO_DETECT, None),
    ENGINE("roque", "xboard", "es", 1471, NO_AUTO_DETECT, None),
    ENGINE("numpty", "xboard", "gb", 1467, NO_AUTO_DETECT, None),
    ENGINE("blikskottel", "xboard", "za", 1456, NO_AUTO_DETECT, None),
    ENGINE("hactar", "uci", "de", 1449, NO_AUTO_DETECT, None),
    ENGINE("nero", "xboard", "de", 1448, NO_AUTO_DETECT, None),
    ENGINE("suff", "uci", "at", 1423, NO_AUTO_DETECT, None),
    ENGINE("sabrina", "xboard", "it", 1416, NO_AUTO_DETECT, None),
    ENGINE("tony", "xboard", "ca", 1410, NO_AUTO_DETECT, None),
    ENGINE("goyaz", "xboard", "br", 1409, NO_AUTO_DETECT, None),
    ENGINE("quokka", "uci", "us", 1408, NO_AUTO_DETECT, None),
    ENGINE("minimardi", "xboard", "unknown", 1407, NO_AUTO_DETECT, None),
    ENGINE("satana", "xboard", "it", 1407, NO_AUTO_DETECT, None),
    ENGINE("eden", "uci", "de", 1406, NO_AUTO_DETECT, None),
    ENGINE("jchess", "xboard", "pl", 1405, NO_AUTO_DETECT, None),
    ENGINE("nanook", "uci", "fr", 1390, NO_AUTO_DETECT, None),
    ENGINE("skaki", "xboard", "us", 1373, NO_AUTO_DETECT, None),
    ENGINE("virutor", "uci", "cz", 1371, NO_AUTO_DETECT, None),
    ENGINE("minichessai", "xboard", "pl", 1362, NO_AUTO_DETECT, None),
    ENGINE("joanna", "xboard", "pl", 1345, NO_AUTO_DETECT, None),
    ENGINE("gladiator", "xboard", "es", 1336, NO_AUTO_DETECT, None),
    ENGINE("ozwald", "xboard", "fi", 1335, NO_AUTO_DETECT, None),
    ENGINE("fimbulwinter", "xboard", "us", 1319, NO_AUTO_DETECT, None),
    ENGINE("cerulean", "xboard", "ca", 1294, NO_AUTO_DETECT, None),
    ENGINE("killerqueen", "uci", "it", 1291, NO_AUTO_DETECT, None),
    ENGINE("trex", "uci", "fr", 1289, NO_AUTO_DETECT, None),
    # chess (name too generic)
    ENGINE("qutechess", "uci", "si", 1277, NO_AUTO_DETECT, None),
    ENGINE("ronja", "xboard", "se", 1274, NO_AUTO_DETECT, None),
    ENGINE("tikov", "uci", "gb", 1246, NO_AUTO_DETECT, None),
    ENGINE("raffaela", "xboard", "it", 1234, NO_AUTO_DETECT, None),
    ENGINE("gringo", "xboard", "at", 1232, NO_AUTO_DETECT, None),  # gringo - grounding tools for (disjunctive) logic programs
    ENGINE("pierre", "xboard", "ca", 1232, NO_AUTO_DETECT, None),
    ENGINE("toledo-uci", "uci", "mx", 1230, NO_AUTO_DETECT, 5),
    ENGINE("toledo", "xboard", "mx", 1230, NO_AUTO_DETECT, None),
    ENGINE("dragontooth", "uci", "us", 1229, NO_AUTO_DETECT, None),
    ENGINE("neurone", "xboard", "it", 1217, NO_AUTO_DETECT, None),
    ENGINE("gray-matter", "xboard", "unknown", 1215, NO_AUTO_DETECT, None),
    ENGINE("darkfusch", "uci", "de", 1186, NO_AUTO_DETECT, None),
    ENGINE("project-invincible", "xboard", "fi", 1182, NO_AUTO_DETECT, None),
    ENGINE("cassandre", "uci", "fr", 1158, NO_AUTO_DETECT, None),  # Allows XB
    ENGINE("jchecs", "xboard", "fr", 1143, NO_AUTO_DETECT, None),
    ENGINE("brama", "xboard", "it", 1141, NO_AUTO_DETECT, None),
    ENGINE("soberango", "xboard", "ar", 1136, NO_AUTO_DETECT, None),
    ENGINE("usurpator", "xboard", "nl", 1133, NO_AUTO_DETECT, None),
    ENGINE("blitzter", "xboard", "de", 1079, NO_AUTO_DETECT, None),
    ENGINE("strategicdeep", "xboard", "pl", 1074, NO_AUTO_DETECT, None),
    ENGINE("frank", "xboard", "it", 1073, NO_AUTO_DETECT, None),
    ENGINE("talvmenni", "xboard", "fo", 1064, NO_AUTO_DETECT, None),
    ENGINE("minnow", "uci", "unknown", 1045, NO_AUTO_DETECT, None),
    ENGINE("safrad", "uci", "cz", 1026, NO_AUTO_DETECT, None),
    ENGINE("xadreco", "xboard", "br", 1025, NO_AUTO_DETECT, None),
    ENGINE("iota", "uci", "gb", 1019, NO_AUTO_DETECT, None),
    ENGINE("giuchess", "xboard", "it", 1004, NO_AUTO_DETECT, None),
    ENGINE("kace", "xboard", "us", 980, NO_AUTO_DETECT, None),
    ENGINE("feeks", "uci", "nl", 967, NO_AUTO_DETECT, None),
    ENGINE("youk", "xboard", "fr", 963, NO_AUTO_DETECT, None),
    # zoe (name too short)
    ENGINE("nsvchess", "uci", "fr", 945, NO_AUTO_DETECT, None),
    ENGINE("chad", "uci", "xb", 943, NO_AUTO_DETECT, None),
    ENGINE("luzhin", "xboard", "unknown", 920, NO_AUTO_DETECT, None),
    ENGINE("dika", "xboard", "fr", 882, NO_AUTO_DETECT, None),
    ENGINE("hippocampe", "xboard", "fr", 876, NO_AUTO_DETECT, None),
    ENGINE("pyotr", "xboard", "gr", 843, NO_AUTO_DETECT, None),
    ENGINE("chessputer", "uci", "unknown", 799, NO_AUTO_DETECT, None),
    ENGINE("belofte", "uci", "be", 725, NO_AUTO_DETECT, None),  # Allows XB
    # easypeasy (no information)
    ENGINE("acqua", "uci", "it", 607, NO_AUTO_DETECT, None),
    # neg (name too short)
    # ram (name too short)
    ENGINE("cpp1", "xboard", "nl", 489, NO_AUTO_DETECT, None),
    ENGINE("lamosca", "xboard", "it", 443, NO_AUTO_DETECT, None),
    ENGINE("alouette", "uci", "fr", 430, NO_AUTO_DETECT, None),
    # ace (name too short)
    # pos (name too short)

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
                if sys.platform == "win32":
                    executable = file_ci.endswith(".exe")
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
            if BITNESS == "32" and "64" in file_ci:
                continue

            # Check the support for POPCNT
            if not POPCOUNT and "popcnt" in file_ci:
                continue

            # Check the support for BMI2
            if not BMI2 and "bmi2" in file_ci:
                continue

            # Great, this is an engine !
            found_engines.append(fullname)

    # Return the found engines as an array of full file names
    return found_engines
