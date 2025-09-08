def get_failure_reason(dnskey, ds, rrsig):
    if not dnskey and not ds:
        return "No DNSSEC records found (DNSKEY and DS missing)"
    if dnskey and not ds:
        return "DNSKEY found but no DS record in parent zone"
    if ds and not dnskey:
        return "DS record exists but no DNSKEY published in child zone"
    if dnskey and ds and not rrsig:
        return "DNSKEY and DS present, but missing RRSIG signatures"
    if dnskey and ds and rrsig:
        return "All DNSSEC records present and valid"
    return "Partial DNSSEC configuration"

def generate_recommendation(domain, dnskey, ds):
    if not dnskey:
        return f"Enable DNSSEC and publish DNSKEY for {domain}"
    if dnskey and not ds:
        return f"Publish DS record in parent zone to complete trust chain for {domain}"
    return f"DNSSEC appears correctly configured for {domain}"

def show_help():
    print("""
Usage:
  python cli.py [domain] [options]

Options:
  --export        Save JSON report
  --visualize     Show trust chain graph
  --about         Show author bio
  --simulate      Run a secure demo domain
  --batch [file]  Validate domains from a file (default: domains.txt)
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

def show_batch_summary(file_path="domains.txt"):
    from dns_query import validate_dnssec
    print(f"\n🔁 Batch Validation from {file_path}")
    try:
        with open(file_path) as f:
            domains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}. Please check the path and try again.")
        return

    print(f"{'Domain':<25} {'Status':<10} {'Reason'}")
    print("-" * 60)
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
        "reason": "All DNSSEC records present and valid",
        "recommendation": "No action needed",
        "timestamp": "2025-09-08T12:34:00"
    }
    print("\n🔐 Simulated Secure Domain")
    visualize_trust_chain("example.secure", result)
