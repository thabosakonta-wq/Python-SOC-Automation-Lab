#!/usr/bin/env python3

log_file = "../logs/security.log"

with open(log_file, "r") as f:
    data = f.read()

failed_logins = data.count("EventID: 4625")
privileged_events = data.count("EventID: 4672")
account_creations = data.count("EventID: 4720")

print("=" * 45)
print(" PYTHON SOC ALERT ENGINE ")
print("=" * 45)

print(f"\nFailed Logins: {failed_logins}")
print(f"Privileged Events: {privileged_events}")
print(f"Account Creations: {account_creations}")

severity = "LOW"

if failed_logins >= 2:
    severity = "MEDIUM"

if privileged_events > 0:
    severity = "HIGH"

if account_creations > 0 and privileged_events > 0:
    severity = "CRITICAL"

print(f"\nOverall Severity: {severity}")

print("\nDetected Activity:")

if failed_logins > 0:
    print("- Failed Login Activity")

if privileged_events > 0:
    print("- Privileged Activity")

if account_creations > 0:
    print("- Account Creation Activity")

if (
    failed_logins > 0
    and privileged_events > 0
    and account_creations > 0
):
    print("\n[POTENTIAL ATTACK CHAIN DETECTED]")
