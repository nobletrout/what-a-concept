#!/usr/bin/env python3
import sys
import os
import datetime
try:
    import dns.resolver
except ImportError:
    print("The dnspython module is required. Install it using 'pip install dnspython'.")
    sys.exit(1)

def month_name(month):
    """Return the month name for a given month number."""
    return datetime.date(1900, month, 1).strftime('%B')

def main():
    print("When is the next BSM?")
    # does  DNS lookup for the date the next BSM is
    # common usage using dig is dig august.2025.whenisbsm.com via DNS TXT record
    # like dig august.2025.whenisbsm.com TXT +short
    # if no parameters are provided, dns lookup for the current month and year

    if len(sys.argv) > 1:
        try:
            month_year = sys.argv[1]
            month, year = month_year.split('.')
            month = int(month)
            year = int(year)
        except ValueError:
            print("Usage: whenisbsm.py [month.year]")
            sys.exit(1)
    else:
        now = datetime.datetime.now()
        month = now.month
        year = now.year
        month_year = f"{month}.{year}"
    # Check if the month is valid
    if month < 1 or month > 12:
        print("Invalid month. Please provide a month between 1 and 12.")
        sys.exit(1)
    # Check if the year is valid
    if year < 1970 or year > 9999:
        print("Invalid year. Please provide a year between 1970 and 9999.")
        sys.exit(1)
    # Print the result
    print(f"The next BSM is in {month_year}.")

    domain = f"{month_name(month)}.{year}.whenisbsm.com"
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                print(f"{txt_string.decode('utf-8')}")
    except dns.resolver.NXDOMAIN:
        print(f"No DNS TXT record found for {domain}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
