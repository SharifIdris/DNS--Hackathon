def validate_dnssec(domain):
    import subprocess
    from datetime import datetime
    from utils import get_failure_reason, generate_recommendation

    def dig(domain, record_type):
        try:
            output = subprocess.check_output(["dig", "+dnssec", domain, record_type], text=True)
            return output
        except subprocess.CalledProcessError:
            return ""

    dnskey = dig(domain, "DNSKEY")
    ds = dig(domain, "DS")
    rrsig = dig(domain, "RRSIG")
    nsec = dig(domain, "NSEC")

    dnskey_found = "DNSKEY" in dnskey
    ds_found = "DS" in ds
    rrsig_found = "RRSIG" in rrsig
    nsec_found = "NSEC" in nsec or "NSEC3" in nsec

    status = "Secure" if dnskey_found and ds_found and rrsig_found else (
        "Broken" if dnskey_found and not ds_found else "Insecure"
    )
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
