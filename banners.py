from termcolor import cprint
import random

def show_random_banner(mode=None):
    banners = {
        "cyber": r"""
   _____      _                __  __             _    
  / ____|    | |              |  \/  |           | |   
 | |     ___ | |__   ___ _ __ | \  / | ___  _ __ | |_  
 | |    / _ \| '_ \ / _ \ '_ \| |\/| |/ _ \| '_ \| __| 
 | |___| (_) | |_) |  __/ | | | |  | | (_) | | | | |_  
  \_____\___/|_.__/ \___|_| |_|_|  |_|\___/|_| |_|\__| 
        🧘 Cyber Monk DNSSEC Validator
        """,

        "lock": r"""
   ____      _               __  __             _    
  / ___| ___| |_ _   _ _ __ |  \/  | ___  _ __ | |_  
 | |  _ / _ \ __| | | | '_ \| |\/| |/ _ \| '_ \| __| 
 | |_| |  __/ |_| |_| | |_) | |  | | (_) | | | | |_  
  \____|\___|\__|\__,_| .__/|_|  |_|\___/|_| |_|\__| 
                      |_|                           
        🔒 Cyber Monk DNSSEC Validator
        """,

        "falcon": r"""
     __
    /__\
   (o_o )  🦅 Falcon Scan Mode
   /|_|\  DNSSEC Dive Activated
    / \   Trust Chain Tracker
        """,

        "owl": r"""
     ___
    (o,o)  🦉 Owl Audit Mode
    { "`"}  DNSSEC Wisdom Engaged
    -"-"-  Cryptographic Insight
        """,

        "glyph": r"""
     ( )
    /|_|\   🔐
   /_|_|_\  Cyber Monk Glyph
    /   \   DNSSEC Guardian
        """,

        "zen": r"""
🔥🔥🔥🔥🔥🔥🔥
🧘 Zen Firewall Activated
🔐 DNSSEC Validator
        """,

        "scroll": r"""
╔══════════════════════╗
║ 🇺🇬Uganda DNSSEC Tool ║
║ 🔍Trust Chain Found  ║
╚══════════════════════╝
        """
    }

    banner = banners.get(mode, random.choice(list(banners.values())))
    cprint(banner, "green", attrs=["bold"])
