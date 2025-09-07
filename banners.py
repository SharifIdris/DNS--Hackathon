from termcolor import cprint
import random

def show_random_banner():
    banners = [
        # 🧘 Cyber Monk DNSSEC Validator
        """
   _____      _                __  __             _    
  / ____|    | |              |  \/  |           | |   
 | |     ___ | |__   ___ _ __ | \  / | ___  _ __ | |_  
 | |    / _ \| '_ \ / _ \ '_ \| |\/| |/ _ \| '_ \| __| 
 | |___| (_) | |_) |  __/ | | | |  | | (_) | | | | |_  
  \_____\___/|_.__/ \___|_| |_|_|  |_|\___/|_| |_|\__| 
        🧘 Cyber Monk DNSSEC Validator
        """,

        # 🔒 Cyber Monk DNSSEC Validator
        """
   ____      _               __  __             _    
  / ___| ___| |_ _   _ _ __ |  \/  | ___  _ __ | |_  
 | |  _ / _ \ __| | | | '_ \| |\/| |/ _ \| '_ \| __| 
 | |_| |  __/ |_| |_| | |_) | |  | | (_) | | | | |_  
  \____|\___|\__|\__,_| .__/|_|  |_|\___/|_| |_|\__| 
                      |_|                           
        🔒 Cyber Monk DNSSEC Validator
        """,

        # 🦅 Falcon Banner
        """
     __
    /__\\
   (o_o )  🦅 Falcon Scan Mode
   /|_|\\  DNSSEC Dive Activated
    / \\   Trust Chain Tracker
        """,

        # 🦉 Owl Banner
        """
     ___
    (o,o)  🦉 Owl Audit Mode
    { "`"}  DNSSEC Wisdom Engaged
    -"-"-  Cryptographic Insight
        """,

        # 🧘 Digital Monk Glyph
        """
     ( )
    /|_|\\   🔐
   /_|_|_\\  Cyber Monk Glyph
    /   \\   DNSSEC Guardian
        """,

        # 🔥 Zen Firewall
        """
🔥🔥🔥🔥🔥🔥🔥
🧘 Zen Firewall Activated
🔐 DNSSEC Validator
        """,

        # 📜 DNSSEC Scroll
        """
╔══════════════════════╗
║ 🔐 DNSSEC Scroll     ║
║ 🧘 Cyber Monk Reads  ║
║ 🔍 Trust Chain Found ║
╚══════════════════════╝
        """
    ]

    banner = random.choice(banners)
    cprint(banner, "green", attrs=["bold"])
