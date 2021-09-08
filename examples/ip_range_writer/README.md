# Xpanse IP Range Writer

This script can be used for exporting Xpanse IP Range Data to CSV or JSON.

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

Example: download all IP Ranges with the `validated` tag within the `8.8.0.0/16`
Accepts a json or csv file name and will format output accordingly.
```
python ip_range.py ranges.json --tags validated --ip 8.8.0.0/16 --include-attribution
```


