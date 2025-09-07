def validate_dnssec(output):
    result = {"status": "Unknown", "details": ""}

    if "SERVFAIL" in output:
        result["status"] = "Broken ❌"
        result["details"] = "DNSSEC validation failed (SERVFAIL)"
    elif "RRSIG" in output and "DNSKEY" in output:
        result["status"] = "Secure ✅"
        result["details"] = "DNSSEC records found and signed"
    elif "DNSKEY" in output and "RRSIG" not in output:
        result["status"] = "Insecure ⚠️"
        result["details"] = "DNSKEY present but no RRSIG signatures"
    else:
        result["status"] = "Insecure ⚠️"
        result["details"] = "No DNSSEC records found"

    return result
