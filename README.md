# Python SOC Automation Lab

A cybersecurity project focused on Security Operations Center (SOC) automation, threat detection, event correlation, and MITRE ATT&CK mapping using simulated Windows Security Event Logs.

## Overview

This lab demonstrates how SOC analysts identify suspicious authentication activity, privileged account usage, account creation events, and correlate multiple security events to detect potential attack chains.

The project simulates real-world SOC workflows including log analysis, threat detection, severity scoring, incident investigation, and MITRE ATT&CK mapping.

## Features

### Failed Login Detection

Detects repeated failed authentication attempts that may indicate brute-force attacks or unauthorized access attempts.

### Privileged Activity Detection

Detects privileged account activity and administrative logons that may indicate privilege escalation or misuse of valid accounts.

### Account Creation Detection

Identifies newly created user accounts that may indicate persistence mechanisms or unauthorized account provisioning.

### SOC Alert Correlation Engine

Correlates multiple security events and generates severity-based alerts to identify potential attack chains.

## MITRE ATT&CK Coverage

| Technique | Description          |
| --------- | -------------------- |
| T1110     | Brute Force          |
| T1078     | Valid Accounts       |
| T1136     | Create Account       |
| TA0001    | Initial Access       |
| TA0004    | Privilege Escalation |
| TA0003    | Persistence          |

## Technologies Used

* Python 3
* Linux
* Termux
* Windows Security Event Analysis
* Detection Engineering
* MITRE ATT&CK Framework
* Threat Hunting
* Security Monitoring
* Git
* GitHub

## Learning Outcomes

* Security Event Monitoring
* Log Analysis
* Threat Detection
* Event Correlation
* Detection Engineering
* MITRE ATT&CK Mapping
* SOC Operations
* Incident Investigation

## Project Structure

Python-SOC-Automation-Lab/

├── logs/

├── reports/

│   ├── mitre_mapping.md

│   └── python_soc_investigation_report.txt

├── screenshots/

├── scripts/

│   ├── failed_login_detector.py

│   ├── privileged_activity_detector.py

│   ├── account_creation_detector.py

│   └── soc_alert_engine.py

└── README.md

## Reports

### MITRE ATT&CK Mapping

Maps detected security events to relevant MITRE ATT&CK techniques and tactics.

### SOC Investigation Report

Documents event analysis, detection findings, and attack-chain observations.

## Future Enhancements

* Real-Time Log Monitoring
* JSON Alert Export
* Threat Intelligence Integration
* Email Alerting
* Dashboard Visualization
* SIEM Integration
* Automated Incident Reporting

## Screenshots

### Failed Login Detection

failed_login_detector.png

### Privileged Activity Detection

privileged_activity_detector.png

### Account Creation Detection

account_creation_detector.png

### SOC Alert Engine

soc_alert_engine.png

## Sample Detection Output

```text
=============================================
 PYTHON SOC ALERT ENGINE
=============================================

Failed Logins: 2
Privileged Events: 1
Account Creations: 1

Overall Severity: CRITICAL

Detected Activity:
- Failed Login Activity
- Privileged Activity
- Account Creation Activity

[POTENTIAL ATTACK CHAIN DETECTED]
```

## Author

Thabo Sakonta

Microsoft Certified Security Operations Analyst (SC-200)

GitHub: https://github.com/thabosakonta-wq

LinkedIn: https://www.linkedin.com/in/thabo-sakonta-377a3748

## License

This project is provided for educational and portfolio purposes.
