def get_failure_reason(dnskey, ds, rrsig):
    if not dnskey and not ds:
        return "NO_DNSSEC"
    if dnskey and not ds:
        return "NO_DS_RECORD"
    if ds and not dnskey:
        return "NO_DNSKEY"
    if dnskey and ds and not rrsig:
        return "NO_RRSIG"
    return "UNKNOWN"

def generate_recommendation(domain, dnskey, ds):
    if not dnskey:
        return f"Enable DNSSEC and publish DNSKEY for {domain}"
    if dnskey and not ds:
        return f"Publish DS record at parent zone (.ug) for {domain}"
    return "DNSSEC appears correctly configured"

def show_help():
    print("""
Usage:
  python cli.py [domain] [options]

Options:
  --export        Save JSON report
  --visualize     Show trust chain graph
  --about         Show author bio
  --simulate      Run a secure demo domain
  --batch         Validate domains from domains.txt
  --mode=[theme]  Choose banner theme (cyber, owl, falcon, etc.)
  --help          Show this help message
""")

def show_about():
    print("""
Cyber Monk DNSSEC Validator
Built by Angole Sharif Abubakar

Certified Virtual Assistant · AI Tools Expert · Developer
Founder of Sharif Digital Hub | https://sharifabubakar.netlify.app

Built in collaboration with GitHub Copilot — a creative and technical partner throughout development.
""")

def show_batch_summary(file_path):
    from dns_query import validate_dnssec
    print(f"\n🔁 Batch Validation from {file_path}")
    try:
        with open(file_path) as f:
            domains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ domains.txt not found. Please create the file and list domains line by line.")
        return

    print(f"{'Domain':<25} {'Status':<10} {'Reason'}")
    print("-" * 50)
    for domain in domains:
        result = validate_dnssec(domain)
        print(f"{domain:<25} {result['status']:<10} {result['reason']}")

def simulate_secure_domain():
    from visualizer import visualize_trust_chain
    result = {
        "domain": "example.secure",
        "dnskey_found": True,
        "ds_found": True,
        "rrsig_found": True,
        "nsec_found": True,
        "status": "Secure",
        "emoji": "✅",
        "reason": "All records present",
        "recommendation": "No action needed",
        "timestamp": "2025-09-07T19:50:00"
    }
    print("\n🔐 Simulated Secure Domain")
    visualize_trust_chain("example.secure", result)
