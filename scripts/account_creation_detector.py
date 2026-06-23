#!/usr/bin/env python3

log_file = "../logs/security.log"

with open(log_file, "r") as f:
    data = f.read()

account_events = data.count("EventID: 4720")

print("=" * 35)
print(" ACCOUNT CREATION DETECTOR ")
print("=" * 35)

print(f"\nAccount Creation Events: {account_events}")

if account_events > 0:
    print("\n[ALERT] New account creation detected")
