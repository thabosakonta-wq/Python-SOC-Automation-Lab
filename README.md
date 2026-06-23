Python SOC Automation Lab

A cybersecurity project focused on Security Operations Center (SOC) automation, log analysis, threat detection, event correlation, and MITRE ATT&CK mapping using simulated Windows security logs.

Overview

This lab demonstrates how SOC analysts detect and investigate suspicious security events, correlate multiple indicators, identify potential attack chains, and prioritize incidents based on severity.

Features

Failed Login Detection

Detects repeated failed login attempts that may indicate brute-force attacks or credential abuse.

Privileged Activity Detection

Identifies privileged account activity and administrative logons that may indicate unauthorized access or privilege escalation.

Account Creation Detection

Detects new account creation events that may indicate persistence mechanisms or unauthorized account provisioning.

Alert Correlation Engine

Correlates multiple security events to identify potential attack chains and generate severity-based alerts.

MITRE ATT&CK Coverage

Technique| Description
T1110| Brute Force
T1078| Valid Accounts
T1136| Create Account
TA0001| Initial Access
TA0004| Privilege Escalation
TA0003| Persistence

## Reports

### MITRE ATT&CK Mapping

Maps detections to ATT&CK techniques and tactics.

### SOC Investigation Report

Documents findings, event analysis, and attack-chain observations from simulated security events.

Technologies Used

- Python 3
- Linux
- Termux
- Security Log Analysis
- MITRE ATT&CK Framework
- Detection Engineering
- SOC Operations
- Git
- GitHub

Learning Outcomes

- Security Event Monitoring
- Log Analysis
- Threat Detection
- Event Correlation
- Detection Engineering
- MITRE ATT&CK Mapping
- SOC Operations
- Incident Investigation

Project Structure

Python-SOC-Automation-Lab/

├── logs/

├── reports/

├── screenshots/

├── scripts/

│   ├── failed_login_detector.py

│   ├── privileged_activity_detector.py

│   ├── account_creation_detector.py

│   └── soc_alert_engine.py

└── README.md

Future Enhancements

- Real-Time Log Monitoring
- JSON Alert Export
- Threat Intelligence Integration
- Email Alerting
- Dashboard Visualization
- SIEM Integration
- Automated Incident Reporting

Screenshots

Failed Login Detection

failed_login_detector.png

Privileged Activity Detection

privileged_activity_detector.png

Account Creation Detection

account_creation_detector.png

SOC Alert Engine

soc_alert_engine.png

Author

Thabo Sakonta

Microsoft Certified Security Operations Analyst (SC-200)

GitHub: https://github.com/thabosakonta-wq

LinkedIn: https://www.linkedin.com/in/thabo-sakonta-377a3748

License

This project is provided for educational and portfolio purposes.
