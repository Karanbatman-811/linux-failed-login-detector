import subprocess
import re
import csv
from collections import Counter
from datetime import datetime


def get_logs(test_mode=False):
    """Get SSH authentication logs."""

    if test_mode:
        with open("test_logs.txt", "r") as file:
            return file.read()

    result = subprocess.run(
        [
            "sudo",
            "journalctl",
            "-u",
            "ssh",
            "--no-pager",
            "-n",
            "100"
        ],
        capture_output=True,
        text=True
    )

    return result.stdout


def detect_failed_logins(test_mode=False):
    """Analyze SSH logs and return failed login information."""

    logs = get_logs(test_mode)

    pattern = r"Failed password for (\S+) from ([0-9a-fA-F:.]+)"

    matches = re.findall(pattern, logs)

    results = []

    if not matches:
        return results

    ip_counts = Counter(
        ip for username, ip in matches
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    for ip, count in ip_counts.items():

        if count <= 2:
            risk = "LOW"
        elif count <= 5:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        username = next(
            username
            for username, address in matches
            if address == ip
        )

        results.append({
            "timestamp": timestamp,
            "username": username,
            "ip": ip,
            "attempts": count,
            "risk": risk
        })

    save_report(results)

    return results


def save_report(results):
    """Save detection results to CSV."""

    if not results:
        return

    with open(
        "security_report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Timestamp",
            "Username",
            "IP Address",
            "Attempts",
            "Risk Level"
        ])

        for result in results:

            writer.writerow([
                result["timestamp"],
                result["username"],
                result["ip"],
                result["attempts"],
                result["risk"]
            ])


def print_results(results):
    """Display results in the terminal."""

    print("=== Linux Failed Login Detector ===")

    if not results:
        print("\nNo failed SSH login attempts found.")
        return

    print(
        f"\nFound {sum(r['attempts'] for r in results)} "
        "failed login attempt(s):\n"
    )

    for result in results:

        print(f"Timestamp  : {result['timestamp']}")
        print(f"Username   : {result['username']}")
        print(f"IP Address : {result['ip']}")
        print(f"Attempts   : {result['attempts']}")
        print(f"Risk Level : {result['risk']}")
        print("-" * 40)

        if result["risk"] == "HIGH":

            print("SECURITY ALERT")
            print(
                f"Suspicious IP detected: "
                f"{result['ip']}"
            )
            print(
                f"Reason: "
                f"{result['attempts']} failed login attempts"
            )
            print("Action: Investigate this source")
            print("-" * 40)

    print(
        "\nSecurity report saved as "
        "security_report.csv"
    )


if __name__ == "__main__":

    import sys

    test_mode = (
        len(sys.argv) > 1
        and sys.argv[1] == "--test"
    )

    results = detect_failed_logins(test_mode)

    print_results(results)
