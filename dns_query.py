import subprocess
from datetime import datetime
from utils import get_failure_reason, generate_recommendation

def dig(domain, record_type):
    try:
        return subprocess.check_output(["dig", "+dnssec", domain, record_type], text=True)
    except subprocess.CalledProcessError:
        return ""

def validate_dnssec(domain):
    dnskey = dig(domain, "DNSKEY")
    ds = dig(domain, "DS")
    rrsig = dig(domain, "RRSIG")
    nsec = dig(domain, "NSEC")

    dnskey_found = "DNSKEY" in dnskey
    ds_found = "DS" in ds
    rrsig_found = "RRSIG" in rrsig
    nsec_found = "NSEC" in nsec or "NSEC3" in nsec

    if dnskey_found and ds_found and rrsig_found:
        status = "Secure"
    elif dnskey_found and not ds_found:
        status = "Broken"
    else:
        status = "Insecure"

    emoji = "✅" if status == "Secure" else "❌" if status == "Broken" else "⚠️"

    return {
        "domain": domain,
        "dnskey_found": dnskey_found,
        "ds_found": ds_found,
        "rrsig_found": rrsig_found,
        "nsec_found": nsec_found,
        "status": status,
        "emoji": emoji,
        "reason": get_failure_reason(dnskey_found, ds_found, rrsig_found),
        "recommendation": generate_recommendation(domain, dnskey_found, ds_found),
        "timestamp": datetime.now().isoformat()
    }
