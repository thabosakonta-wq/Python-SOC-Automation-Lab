# Executive Summary

## Python SOC Automation Lab

### Objective

This project demonstrates how Python can automate common Security Operations Center (SOC) detection and investigation tasks by parsing Windows Security Event Logs, identifying suspicious activity, correlating events, and mapping detections to the MITRE ATT&CK framework.

---

## Investigation Summary

The automated analysis identified multiple security events associated with a potential attack sequence:

- Multiple failed authentication attempts
- Privileged account activity
- New user account creation

The correlated events indicate behavior consistent with an attempted compromise followed by privilege escalation and persistence.

---

## Key Findings

| Detection | Event ID | Severity |
|-----------|----------|----------|
| Failed Login Attempts | 4625 | High |
| Privileged Activity | 4672 | High |
| Account Creation | 4720 | Medium |

Overall Risk Level:

**CRITICAL**

---

## MITRE ATT&CK Coverage

| Technique | ID |
|-----------|----|
| Brute Force | T1110 |
| Valid Accounts | T1078 |
| Create Account | T1136 |

---

## Analyst Assessment

The observed attack chain demonstrates a realistic SOC investigation workflow:

1. Authentication failures detected.
2. Elevated account activity identified.
3. New account creation observed.
4. Events correlated into a single incident.

This workflow illustrates how automation assists SOC analysts by reducing manual analysis time while improving detection consistency.

---

## Recommendations

- Investigate affected user accounts.
- Validate privileged account activity.
- Review newly created accounts.
- Reset compromised credentials.
- Continue monitoring for recurring attack patterns.

---

**Status:** Investigation Complete

**Outcome:** Python successfully automated detection, alert correlation, and incident reporting.
