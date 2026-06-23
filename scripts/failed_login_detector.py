#!/usr/bin/env python3

log_file = "../logs/security.log"

with open(log_file, "r") as f:
    data = f.read()

failed_logins = data.count("EventID: 4625")

print("=" * 35)
print(" FAILED LOGIN DETECTOR ")
print("=" * 35)

print(f"\nFailed Logins: {failed_logins}")

if failed_logins > 0:
    print("\n[ALERT] Failed login activity detected")
