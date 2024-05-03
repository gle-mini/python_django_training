#!/usr/bin/python3

import sys
import antigravity

def main():
    if len(sys.argv) != 4:
        print("3 arguments required (latitude, longitude, datedow)")
        sys.exit(1) 
    
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
    except ValueError:
        print("Latitude and longitude must be valid numbers.")
        sys.exit(1)
    
    datedow = sys.argv[3].encode('utf-8')
    
    antigravity.geohash(latitude, longitude, datedow)
    sys.exit(0)

if __name__ == '__main__':
    main()

