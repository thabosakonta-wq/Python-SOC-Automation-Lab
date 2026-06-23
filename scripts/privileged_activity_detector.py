#!/usr/bin/env python3

log_file = "../logs/security.log"

with open(log_file, "r") as f:
    data = f.read()

privileged_events = data.count("EventID: 4672")

print("=" * 40)
print(" PRIVILEGED ACTIVITY DETECTOR ")
print("=" * 40)

print(f"\nPrivileged Events: {privileged_events}")

if privileged_events > 0:
    print("\n[HIGH ALERT] Privileged activity detected")
