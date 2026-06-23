# MITRE ATT&CK Mapping - Python SOC Automation Lab

## Failed Login Detection
Event ID: 4625

Technique:
- T1110 - Brute Force

Description:
Repeated failed authentication attempts may indicate password guessing or credential stuffing attacks.

---

## Privileged Activity Detection
Event ID: 4672

Technique:
- T1078 - Valid Accounts

Description:
Privileged logon activity may indicate unauthorized use of administrative credentials.

---

## Account Creation Detection
Event ID: 4720

Technique:
- T1136 - Create Account

Description:
New account creation may indicate persistence or unauthorized account provisioning.

---

## Correlated Attack Chain

Detected Sequence:
4625 → 4672 → 4720

ATT&CK Tactics:
- Initial Access
- Privilege Escalation
- Persistence

Severity:
CRITICAL
