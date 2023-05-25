# Cortex Xpanse Incident Management
This script updates a set of Incidents' severity and status whose Alerts contain specific Attack Surface Rules.

This example uses:
* Attack Surface Rules API
* Alerts API
* Incidents API

## Install
```
pip install -r requirements.txt
```

## Usage
Example:
```
python update_incidents.py --attack-surface-rules "MySQL Server" --attack-surface-rules "SSH Server" --severity "critical" --status "UNDER_INVESTIGATION"
```
