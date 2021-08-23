# Xpanse Behavior CVS Writer

This script can be used for exporting Xpanse Behavior data to CSV.

## Install
```
pip install -r requirements.txt
```

## Usage
This script expects the Bearer token or JWT for the account to be declared as an Environment variable.
ex:
```
export XPANSE_BEARER_TOKEN=<Refresh Token>
or
export XPANSE_JWT_TOKEN=<JWT>
```

Example: download all flows for IPs with the `validated` tag in range `8.8.8.0/24`
```
python export_behavior_to_csv.py behavior.csv  --tags validated --ip 8.8.8.0/24
```


