# Xpanse Bulk Issue Updater

This script can be used for running bulk update operations on Issues in Xpanse.

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

Example: 
This example will set the priority of any `Unenecrypted FTP Server` issues that appear on assets with the tag `dmz` to `Medium` from the default priority, `High`.
```
python bulk_issue_update.py --issue-type "Unencrypted FTP Server" --tags dmz --priority Medium
```
