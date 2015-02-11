#!/usr/bin/env python

import gdata.spreadsheet.service
import argparse
import time
import datetime
from credentials import USERNAME, PASSWORD, SPREADSHEET_KEY

worksheet_id = 'od6' # default

def main():
    #argparser
    parser = argparse.ArgumentParser()
    parser.add_argument('--humidity', required=True, type=str, help='the value of humidity')
    parser.add_argument('--temperature', required=True, type=str, help='the value of temperature')
    args = parser.parse_args() 

    client = gdata.spreadsheet.service.SpreadsheetsService()
    client.debug = False 
    client.email = USERNAME
    client.password = PASSWORD
    client.source = 'test client'
    client.ProgrammaticLogin()

    row = {'humidity':args.humidity.replace('.',','),'temperature':args.temperature.replace('.',','),'date':time.strftime('%d.%m.%Y %H:%M:%S')}

    try:
        client.InsertRow(row, SPREADSHEET_KEY, worksheet_id)
    except Exception as e:
        print e

    return

if __name__ == '__main__':
    main()

