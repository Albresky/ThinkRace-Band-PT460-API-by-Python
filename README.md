# ThinkRace Band PT460 API by Python

## Introduction
- This is a library written for ThinkRace Band(Model: PT460).
- Support:
  - Automatically get APPID and APPKEY, storing them in `config.ini` as well.
    - Support validate check and then update token.
  - Get Band with official APIs with the help of `Requests` lib.
  - Data including:
    - GPS(Latitude & Longitude)
    - GPS time
    - Heart rate
    - Blood pressure (HP & LP)
    - Blood Oxygen
    - Bood temperature
    - Footsteps
  - Support send command mannually.
    -  Set band's data-update-rate as you wish.