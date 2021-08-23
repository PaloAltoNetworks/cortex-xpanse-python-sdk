# Xpanse Bulk Tagger

This script can be used for running bulk tagging operations for domains, certificates, and cloud resources.

## Install
```
pip install -r requirements.txt
```

## Input
File should by a cvs with 4 columns, `type` (domain|certificate|cloud-resource), `assetKey`, `tags` (`|` delimited), `operation` (ASSIGN|UNASSIGN).
This script will skip the header row.

Example: Input csv
```
type,assetKey,tags,operation
domain,my.example.domain.com,dmz|content-validated,ASSIGN
```

## Usage
This script expects the Bearer token or JWT for the account to be declared as an Environment variable.
ex:
```
export XPANSE_BEARER_TOKEN=<Refresh Token>
or
export XPANSE_JWT_TOKEN=<JWT>
```

Example: Bulk tag a group of domains
```
python bulk_tagger.py domains.csv
```

