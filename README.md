# Python SOC Automation Lab

A Python-based Security Operations Center (SOC) automation project designed to demonstrate log analysis, detection engineering, alert correlation, incident investigation, and MITRE ATT&CK mapping.

---

## Overview

This project simulates a SOC workflow using Python scripts to analyze Windows security events, identify suspicious activity, generate alerts, and support incident investigations.

The lab demonstrates how security analysts automate repetitive monitoring tasks and investigate security events using Python.

---

## Features

### Failed Login Detection

- Detects Windows Event ID 4625
- Identifies repeated authentication failures
- Supports brute-force detection scenarios

### Privileged Activity Detection

- Detects Windows Event ID 4672
- Identifies elevated account activity
- Highlights privilege escalation indicators

### Account Creation Detection

- Detects Windows Event ID 4720
- Identifies newly created user accounts
- Supports persistence detection scenarios

### SOC Alert Engine

- Correlates multiple security events
- Assigns severity ratings
- Detects potential attack chains
- Produces consolidated alerts

### Incident Investigation

- Documents findings
- Assesses severity
- Provides response recommendations

---

## MITRE ATT&CK Coverage

| Event ID | Technique | Description |
|----------|-----------|-------------|
| 4625 | T1110 | Brute Force |
| 4672 | T1078 | Valid Accounts |
| 4720 | T1136 | Create Account |

---

## Technologies Used

- Python
- Linux
- Termux
- Git
- GitHub
- MITRE ATT&CK

---

## Project Structure

```text
Python-SOC-Automation-Lab
├── logs
│   └── security.log
├── reports
│   ├── mitre_mapping.md
│   └── python_soc_investigation_report.txt
├── screenshots
│   ├── account_creation_detector.png
│   ├── failed_login_detector.png
│   ├── privileged_activity_detector.png
│   └── soc_alert_engine.png
├── scripts
│   ├── account_creation_detector.py
│   ├── failed_login_detector.py
│   ├── privileged_activity_detector.py
│   └── soc_alert_engine.py
└── README.md
```

## Screenshots

### Failed Login Detector
![Failed Login Detector](https://raw.githubusercontent.com/thabosakonta-wq/Python-SOC-Automation-Lab/main/screenshots/failed_login_detector.png)

### Privileged Activity Detector
![Privileged Activity Detector](https://raw.githubusercontent.com/thabosakonta-wq/Python-SOC-Automation-Lab/main/screenshots/privileged_activity_detector.png)

### Account Creation Detector
![Account Creation Detector](https://raw.githubusercontent.com/thabosakonta-wq/Python-SOC-Automation-Lab/main/screenshots/account_creation_detector.png)

### SOC Alert Engine
![SOC Alert Engine](https://raw.githubusercontent.com/thabosakonta-wq/Python-SOC-Automation-Lab/main/screenshots/soc_alert_engine.png)

## Learning Outcomes

- Python Log Parsing  
- Detection Engineering  
- Security Monitoring  
- Threat Detection  
- Event Correlation  
- Incident Investigation  
- SOC Operations  
- MITRE ATT&CK Mapping  

---

## Author

Thabo Sakonta

Microsoft Certified Security Operations Analyst (SC-200)

- GitHub: https://github.com/thabosakonta-wq  
- LinkedIn: https://www.linkedin.com/in/thabo-sakonta-377a3748  

---

## License

This project is intended for educational, research, and portfolio demonstration purposes.
