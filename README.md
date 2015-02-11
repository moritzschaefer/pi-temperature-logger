# Introduction

This is just some code to read and store some sensor value (DHT22, temperature and humidity) to a google spreadsheet from a Raspberry Pi

# Usage

The python file is for uploading the data fields to google docs. 
measurement.sh is called by a cronjob and reads sensor data with help from loldht(a compiled file from https://github.com/technion/lol_dht22).

# Results

The values are written in an google drive document, here are our first results:
https://docs.google.com/spreadsheets/d/14JzzkR-GSvNfv0T1aBTtl-jEyk5lY0UoAlre-AM7Qh0/edit?usp=sharing
Attention: Google Calc documents can't have more than 400'000 cells, cause that we have a limitation. When we measure every minute, we can writing measurements for ~200 days.

# License

Use at own risk. Do what you want.
