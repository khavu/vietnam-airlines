#!/usr/bin/env python3
"""
Script import data from exel file to MySQL database
"""

import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("/home/khavq/Downloads/Copy1.xlsx")
sheet = book.sheet_by_name("sheet")

# Establish a MySQL connection
database = pymysql.connect(host="localhost", user="root", passwd="123.abc", db="vnairline")
cursor = database.cursor()

# Set utf8
database.set_charset('utf8')
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

# Create the INSERT INTO sql query
query = """INSERT INTO user_info (ID_NUMBER, FIRST_NAME, MIDDLE_INITIALS, SURNAME, DOB1, GENDER, CREATE_DATE,
EMBOSSED_NAME, STATUS_CODE, PREFERRED_LANGUAGE, NAMING_CONVENTION, TITLE, SALUTATION, ADDITIONAL_TEXT, BUS_COMPANY_NAME,
INSTRUCTION, STREET_FREE_TEXT, ADDRESS_2, ADDRESS_3, CITY_NAME, STATE_PROVINCE_NAME, POSTAL_CODE, COUNTRY_CODE,
ENROLLMENT_DATE, TIER, TIER_START_DATE, TIER_ENDS_DATE, NATIONALITY, LIFE_AMOUNT, POINTS_EXP_DATE, POINTS_EXP_AMOUNT,
POINTS_AMOUNT, TMBQPER_AMOUNT, TMBQPER_START_DATE, TMBQPER_END_DATE, TMBQPER_SEGMENTS, COUNTRY, NATIONALITY_CODE,
PASSWORD, EMAIL_ADDRESS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    ID_NUMBER = sheet.cell(r, 0).value
    FIRST_NAME = sheet.cell(r, 1).value
    MIDDLE_INITIALS = sheet.cell(r, 2).value
    SURNAME = sheet.cell(r, 3).value
    DOB1 = sheet.cell(r, 4).value
    GENDER = sheet.cell(r, 5).value
    CREATE_DATE = sheet.cell(r, 6).value
    EMBOSSED_NAME = sheet.cell(r, 7).value
    STATUS_CODE = sheet.cell(r, 8).value
    PREFERRED_LANGUAGE = sheet.cell(r, 9).value
    NAMING_CONVENTION = sheet.cell(r, 10).value
    TITLE = sheet.cell(r, 11).value
    SALUTATION = sheet.cell(r, 12).value
    ADDITIONAL_TEXT = sheet.cell(r, 13).value
    BUS_COMPANY_NAME = sheet.cell(r, 14).value
    INSTRUCTION = sheet.cell(r, 15).value
    STREET_FREE_TEXT = sheet.cell(r, 16).value
    ADDRESS_2 = sheet.cell(r, 17).value
    ADDRESS_3 = sheet.cell(r, 18).value
    CITY_NAME = sheet.cell(r, 19).value
    STATE_PROVINCE_NAME = sheet.cell(r, 20).value
    POSTAL_CODE = sheet.cell(r, 21).value
    COUNTRY_CODE = sheet.cell(r, 22).value
    ENROLLMENT_DATE = sheet.cell(r, 23).value
    TIER = sheet.cell(r, 24).value
    TIER_START_DATE = sheet.cell(r, 25).value
    TIER_ENDS_DATE = sheet.cell(r, 26).value
    NATIONALITY = sheet.cell(r, 27).value
    LIFE_AMOUNT = sheet.cell(r, 28).value
    POINTS_EXP_DATE = sheet.cell(r, 29).value
    POINTS_EXP_AMOUNT = sheet.cell(r, 30).value
    POINTS_AMOUNT = sheet.cell(r, 31).value
    TMBQPER_AMOUNT = sheet.cell(r, 32).value
    TMBQPER_START_DATE = sheet.cell(r, 33).value
    TMBQPER_END_DATE = sheet.cell(r, 34).value
    TMBQPER_SEGMENTS = sheet.cell(r, 35).value
    COUNTRY = sheet.cell(r, 36).value
    NATIONALITY_CODE = sheet.cell(r, 37).value
    PASSWORD = sheet.cell(r, 38).value
    EMAIL_ADDRESS = sheet.cell(r, 39).value

    # Assign values from each row
    values = (ID_NUMBER, FIRST_NAME, MIDDLE_INITIALS, SURNAME, DOB1, GENDER, CREATE_DATE, EMBOSSED_NAME, STATUS_CODE,
              PREFERRED_LANGUAGE, NAMING_CONVENTION, TITLE, SALUTATION, ADDITIONAL_TEXT, BUS_COMPANY_NAME, INSTRUCTION,
              STREET_FREE_TEXT, ADDRESS_2, ADDRESS_3, CITY_NAME, STATE_PROVINCE_NAME, POSTAL_CODE, COUNTRY_CODE,
              ENROLLMENT_DATE, TIER, TIER_START_DATE, TIER_ENDS_DATE, NATIONALITY, LIFE_AMOUNT, POINTS_EXP_DATE,
              POINTS_EXP_AMOUNT, POINTS_AMOUNT, TMBQPER_AMOUNT, TMBQPER_START_DATE, TMBQPER_END_DATE, TMBQPER_SEGMENTS,
              COUNTRY, NATIONALITY_CODE, PASSWORD, EMAIL_ADDRESS)

    # Execute sql Query
    cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("I just imported {columns} columns, {rows} rows".format(columns=columns, rows=rows))
