# Linux Failed Login Detector

## Project Overview

Linux Failed Login Detector is a Python-based cybersecurity tool that analyzes Linux SSH authentication logs and detects failed login attempts.

The tool extracts the username and IP address associated with failed login attempts, counts the number of attempts, assigns a risk level, generates a security alert for high-risk activity, and saves the results in a CSV security report.

## Features

- Detects failed SSH login attempts
- Extracts username and IP address
- Counts failed login attempts
- Classifies security risk
- Generates HIGH-risk security alerts
- Creates a CSV security report
- Records timestamp of detection

## Risk Classification

| Failed Attempts | Risk Level |
|---|---|
| 1–2 | LOW |
| 3–5 | MEDIUM |
| 6+ | HIGH |

## Technologies Used

- Python 3
- Linux
- SSH
- systemd journalctl
- Regular Expressions
- CSV
- Python Counter

## How It Works

1. The program collects SSH authentication logs using `journalctl`.
2. Regular expressions identify failed password attempts.
3. The program extracts usernames and IP addresses.
4. Failed attempts are counted for each IP address.
5. A risk level is assigned.
6. HIGH-risk activity generates a security alert.
7. Results are saved to `security_report.csv`.

## Example Detection

```text
Found 7 failed login attempt(s):

Timestamp  : 2026-10-02 10:08:15
Username   : kali
IP Address : ::1
Attempts   : 7
Risk Level : HIGH

SECURITY ALERT
Suspicious IP detected: ::1
Reason: 7 failed login attempts
Action: Investigate this source
