# Changelog

All notable changes to this this project will be documented in this file.

The format is based on [changelog.md](https://changelog.md/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.5] - 2021-05-21
- Added type support
- Added support for Behavior Risk Rules endpoint

## [0.3.4] - 2021-05-20
- Added ability to disable ssl certificate checks
- Added new Issues counts endpoint
- Fixed issue where negation filters didn't work for services
  
## [0.3.3] - 2021-05-18
- Fixed bug where requests to refresh JWT were not using proxy settings

## [0.3.2] - 2021-04-14
- Documentation and Dependency Updates

## [0.3.1] - 2021-02-05
- Added requests proxy support

## [0.3.0] - 2021-01-05
- Added support for the Services API
- Added support for the Issues Policies API
- Added support for the Behavior Risky-Flows GET endpoint
- Added deprecation warnings for Exposures, Cloud Exposures, and Events

## [0.2.1] - 2020-10-26

### Changed
- Updates doc strings and docs reStructuredText files to support pdf documentation generation.

## [0.2.0] - 2020-09-29

### Added
- Added new Targeted IPs API.

## [0.1.2] - 2020-09-29

### Changed
- Updated Issues API documentation to be more descriptive.

## [0.1.1] - 2020-08-24

### Changed
- Updated a parameter name for the issues API.

### Added
- Added a new example script for bulk-updating Issues.

## [0.1.0] - 2020-08-14

### Changed
- Version bump for general consumption

## [0.0.15] - 2020-08-07

### Changed
- License text updated

## [0.0.14] - 2020-07-30

### Added
- Added additional Example scripts

### Fixed
- Fixed documentation for the Behavior API.

## [0.0.13] - 2020-07-28

### Added
- Include Documentation and Examples in package.

## [0.0.12] - 2020-07-27

### Added
- Added support to build documentation using Sphinx from an install wheel.

## [0.0.11] - 2020-07-27

### Added
- Added support for the Issues API

## [0.0.10] - 2020-07-22

### Added
- Added support for CSV exports of exposures

## [0.0.9] - 2020-07-20

### Fixed
- User-Agent header values were out of order, product should come first

## [0.0.8] - 2020-07-16

### Added
- Added support for pulling all Cloud Exposures

## [0.0.7] - 2020-07-07

### Added
- New Annotations v3 API (Tags only)
- New bulk annotation assignment endpoints for Assets v2 API

## [0.0.6] - 2020-06-16

### Fixed
- Added missing Behavior filtering functionality

## [0.0.5] - 2020-06-10

### Fixed
- Typo in exception response string
- ConnectionError during JWT refresh was not being retried
- Wrap potential KeyError in ExResultIterator

## [0.0.4] - 2020-05-22

### Added
- New devices Exposure types to valid exposures for the Cloud Exposures API

## [0.0.3] - 2020-05-12

### Fixed
- ConnectionResetError would cause requests to fail after inactivity, added this to the allowed retry cases

## [0.0.2] - 2020-04-27

### Fixed
- Cloud Exposures CSV exports mistakenly didn't require `header` or `labels` params
- Exposure Summaries worked incorrectly if a string was provided rather than a list for some parameters

## [0.0.1] - 2020-03-31

### Added
- Support for Entities API v1
- Support for Assets API v2
- Support for Exposures API v2
- Support for Behavior API v1
- Support for Cloud Exposures API v1
- Support for Events API v1

