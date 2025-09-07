import subprocess

def fetch_dns_records(domain):
    try:
        result = subprocess.run(["dig", domain, "+dnssec"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error fetching DNS records: {e}"
