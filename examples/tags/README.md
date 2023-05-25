# Cortex Xpanse Tag Management
This script assigns and removes tags from a set of 100 Assets or Owned IP Ranges.

This example uses:
* Assets API
* Owned IP Ranges API
* Tags API

## Install
```
pip install -r requirements.txt
```

## Usage
Example:
```
python assign_and_remove_tags.py --data-type "OWNED_IP_RANGES" --tags "Tag 1" --tags "Tag 2"
```
