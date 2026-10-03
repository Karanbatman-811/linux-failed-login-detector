import sys
import subprocess
import re
import csv
from collections import Counter
from datetime import datetime

print("=== Linux Failed Login Detector ===")

if len(sys.argv) > 1 and sys.argv[1] == "--test":
    logs = open("test_logs.txt").read()
else:
    result = subprocess.run(
        ["sudo", "journalctl", "-u", "ssh", "--no-pager", "-n", "100"],
        capture_output=True,
        text=True
    )
    logs = result.stdout

pattern = r"Failed password for (\S+) from ([0-9a-fA-F:.]+)"
matches = re.findall(pattern, logs)

if not matches:
    print("\nNo failed SSH login attempts found.")

else:
    print(f"\nFound {len(matches)} failed login attempt(s):\n")

    ip_counts = Counter(ip for username, ip in matches)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("security_report.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Timestamp",
            "Username",
            "IP Address",
            "Attempts",
            "Risk Level"
        ])

        for ip, count in ip_counts.items():

            if count <= 2:
                risk = "LOW"
            elif count <= 5:
                risk = "MEDIUM"
            else:
                risk = "HIGH"

            username = next(
                username for username, address in matches
                if address == ip
            )

            print(f"Timestamp  : {timestamp}")
            print(f"Username   : {username}")
            print(f"IP Address : {ip}")
            print(f"Attempts   : {count}")
            print(f"Risk Level : {risk}")
            print("-" * 40)

            if risk == "HIGH":
                print("SECURITY ALERT")
                print(f"Suspicious IP detected: {ip}")
                print(f"Reason: {count} failed login attempts")
                print("Action: Investigate this source")
                print("-" * 40)

            writer.writerow([
                timestamp,
                username,
                ip,
                count,
                risk
            ])

    print("\nSecurity report saved as security_report.csv")
