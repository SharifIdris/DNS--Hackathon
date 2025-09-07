# 🧘 Cyber Monk DNSSEC Validator & Visualizer

A CLI tool built for the **DNS Uganda Hackathon 2025** to validate DNSSEC configurations across `.ug` domains and beyond. It blends cryptographic rigor with creative flair — featuring rotating ASCII banners, graphical trust chain visualization, and exportable reports. Designed by **Angole Sharif Abubakar**, this tool empowers African digital infrastructure with clarity, style, and security.

---

## 🔐 Features

- ✅ DNSSEC record detection using `dig`
- ✅ SERVFAIL and delegation error reporting
- ✅ Rotating ASCII splash screens (Cyber Monk, Falcon, Owl, Zen Firewall, etc.)
- ✅ JSON report export for audit and sharing
- ✅ Graphical trust chain visualization (Root → TLD → Domain)
- ✅ `--help` flag for usage instructions
- ✅ `--about` flag to display author bio and project story

---

## ⚙️ Installation
# Clone the repo
git clone https://github.com/SharifIdris/DNS--Hackathon.git
cd DNS--Hackathon

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

##Usage
python cli.py [domain] [options]

##Options:
--help Show usage instructions

--export Save validation report as JSON

--visualize Display trust chain graph

--about Show author bio and project background

##Example
python cli.py gov.ug
python cli.py gov.ug --export
python cli.py gov.ug --visualize
python cli.py gov.ug --export --visualize
python cli.py --about

##Sample Output 
🔒 Cyber Monk DNSSEC Validator

DNSSEC Status: Insecure ⚠️  
Details: No DNSSEC records found  
Report saved to gov_ug_dnssec_report.json


##Screenshots


##👤 About the Author
Angole Sharif Abubakar is a Certified Virtual Assistant, AI Tools Expert, and early-stage Developer with a passion for building efficient, tech-driven solutions. He helps individuals, startups, and small businesses work smarter by combining digital organization, automation, and fast MVP development.

Sharif blends administrative precision with technical curiosity — actively building his foundation in cybersecurity and data science while studying Computer Science at Busitema University. He’s also enrolled in professional tracks with ALX Africa (Cybersecurity & Data Science) and CISCO’s Ethical Hacking program.

His long-term vision is to evolve into a Data Scientist enriched with cybersecurity expertise — someone who can protect digital systems, analyze complex data, and drive intelligent, secure decision-making across industries.

Currently, Sharif lives out his mission through Sharif Digital Hub, where he delivers impactful CLI tools, branding systems, and automation workflows.

“I combine digital organization, AI fluency, and development skills to deliver solutions that matter.” — Angole Sharif Abubakar

Portfolio: sharifabubakar.netlify.app



##Built with GitHub Copilot
This project was developed in close collaboration with GitHub Copilot, which served as a creative and technical companion throughout the build. From debugging Python logic to refining CLI workflows, Copilot helped shape the tool’s structure, banner rotation, and DNSSEC validation logic — turning raw ideas into a polished, demo-ready solution.

“Copilot wasn’t just a code assistant — it was a thinking partner. Every banner, every validation rule, every visual element was sharpened through that collaboration.” — Angole Sharif Abubakar


##🌍 Vision & Impact
This tool is part of a broader mission to:

Strengthen DNSSEC adoption across African ccTLDs

Make cybersecurity accessible through visual storytelling

Empower registries, developers, and communities with open-source tools