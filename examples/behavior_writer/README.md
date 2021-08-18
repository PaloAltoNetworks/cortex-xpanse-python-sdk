#xpanse Behavior CVS Writer

This script can be used for exportingxpanse Behavior data to CSV.

## Install
```
pip install -r requirements.txt
```

## Usage
This script expects the Bearer token or JWT for the account to be declared as an Environment variable.
ex:
```
exportxpanse_BEARER_TOKEN=<Refresh Token>
or
exportxpanse_JWT_TOKEN=<JWT>
```

Example: download all flows for IPs with the `validated` tag in range `8.8.8.0/24`
```
python export_behavior_to_csv.py behavior.csv  --tags validated --ip 8.8.8.0/24
```


