import sys
from banners import show_random_banner
from dns_query import fetch_dns_records
from validator import validate_dnssec
from utils import export_report
from visualizer import visualize_trust_chain

def show_help():
    help_text = """
Cyber Monk DNSSEC Validator & Visualizer

Usage:
  python cli.py [domain] [options]

Options:
  --help           Show this help message
  --export         Save validation report as JSON
  --visualize      Display trust chain graph

Examples:
  python cli.py example.ug
  python cli.py example.ug --export
  python cli.py example.ug --visualize
  python cli.py example.ug --export --visualize
"""
    print(help_text)

def main():
    if "--help" in sys.argv or len(sys.argv) < 2:
        show_help()
        return

    show_random_banner()
    domain = sys.argv[1]
    output = fetch_dns_records(domain)
    result = validate_dnssec(output)

    print("\nDNSSEC Status:", result["status"])
    print("Details:", result["details"])

    if "--export" in sys.argv:
        export_report(domain, result)

    if "--visualize" in sys.argv:
        visualize_trust_chain(domain, result)

if __name__ == "__main__":
    main()
