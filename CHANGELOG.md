# CHANGELOG

## v3.0.2

### Issues

- Closes #11
- Closes #12

### Added

- _get_data now has `id_override=None` so you can override `&starting_after=` as you wish
- `id_override=0` implemented in Logs get_logs()

### Changed

- Changed paginaition to work without compounding to a `414`

## v3.0.1

### Issues

- Closes #9

## Changed

- Changed paginaition to work, now returns obj not response
- good catch @bryanheinz

## v3.0.0

- Closes #3

## Changed

- removed forced encoding for `GET` responses
- added some pylint comments

## v2.1.0

### Issues

- Closes #5

### Changed

- fixed module names

## v2.0.0

### Issues

- Closes #1

### Added

- Partial/Full Support for:
  - Assignment Groups
  - Custom Attributes
  - Custom Configuration
  - DEP Servers
  - Enrollments
  - Logs
  - Lost Mode
  - Webhooks
- (Somewhat) Help(ful) Strings

### Changed

- removed PIP items for now

### Base

- forked from [SteveKueng/simple_mdm_py](https://github.com/SteveKueng/simple_mdm_py/blob/master/setup.py) at [cf6650f](https://github.com/SteveKueng/simpleMDMpy/commit/cf6650fe72220577abd5c654d03476c88b81bcb0)
