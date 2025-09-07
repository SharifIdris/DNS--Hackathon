import json
from datetime import datetime

def export_report(domain, result):
    filename = f"{domain.replace('.', '_')}_dnssec_report.json"
    report = {
        "domain": domain,
        "timestamp": datetime.now().isoformat(),
        "status": result["status"],
        "details": result["details"]
    }
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
    print(f"Report saved to {filename}")
