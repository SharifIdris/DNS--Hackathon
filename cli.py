import sys
from banners import show_random_banner
from dns_query import validate_dnssec
from visualizer import visualize_trust_chain
from utils import (
    show_about,
    show_help,
    show_batch_summary,
    simulate_secure_domain
)

def main():
    args = sys.argv[1:]

    if not args or "--help" in args:
        show_help()
        return

    if "--about" in args:
        show_about()
        return

    if "--simulate" in args:
        simulate_secure_domain()
        return

    if "--batch" in args:
        show_batch_summary("domains.txt")
        return

    domain = args[0]
    mode = next((arg.split("=")[1] for arg in args if arg.startswith("--mode=")), None)
    show_random_banner(mode)

    result = validate_dnssec(domain)

    print(f"\nDNSSEC Status: {result['status']} {result['emoji']}")
    print("Details:")
    print(f"- DNSKEY: {'✅' if result['dnskey_found'] else '❌'}")
    print(f"- DS: {'✅' if result['ds_found'] else '❌'}")
    print(f"- RRSIG: {'✅' if result['rrsig_found'] else '❌'}")
    print(f"- NSEC/NSEC3: {'✅' if result['nsec_found'] else '❌'}")
    print(f"Reason: {result['reason']}")
    print(f"Recommendation: {result['recommendation']}")

    if "--export" in args:
        import json
        filename = f"{domain.replace('.', '_')}_dnssec_report.json"
        with open(filename, "w") as f:
            json.dump(result, f, indent=2)
        print(f"Report saved to {filename}")

    if "--visualize" in args:
        visualize_trust_chain(domain, result)

    print("\n🙏 Thanks for using Cyber Monk. Stay secure, stay curious.")

if __name__ == "__main__":
    main()
