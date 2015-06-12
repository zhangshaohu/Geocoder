# Reference:https://github.com/laurenarcher/SimpleCsvGeocoder/blob/master/csvGeocoder.py
# pygeocoder is a module from http://code.xster.net/pygeocoder/wiki/Home. You need to install this module at first

import csv
import time
from pygeocoder import Geocoder
from pygeocoder import GeocoderError

#A super simple python .csv geocoder
#You can geocode up to 2500 properties a day (per IP Address)
#Upload the resulting newfile.csv to Google Fusion Tables for an instant google map.

input_file = open('C:/Users/shaohu.zhang@sdstate.edu/Desktop/csv/myCSV.csv', 'r') #Open your .csv file
#Make an empty .csv This is where your geocodes will end up. if you are running Python 2.X, please use "wb" flag, which can avoid blank rowin output CSV.
# if Python 3.X, you may use "w" flag.
output_file = open('C:/Users/shaohu.zhang@sdstate.edu/Desktop/csv/newCSV.csv', 'wb') #output your result
data = csv.reader(input_file)
print("begin")
for line in data:
    
    [ID,Location] = line #Make sure the number of columns matches/aligns with the number of fields listed here.
    try:
        if Location == "Location":#This skips the header. Don't geocode the header :D
            Latitude = ["Latitude"]
            Longitude = ["Longitude"]
            Accuracy =["Accuracy"]
            Valid=["Valid"]
            Valid_adrress=["Valid_adrress"]
            new_line = line +Valid_adrress+ Latitude + Longitude + Accuracy+ Valid
            csv.writer(output_file).writerow(new_line)
    
        else:
    #I use a column with the Full Address (Street Number, Street, City, Provice/State, Country) But you could concatenate from multiple fields too.
        
            results = Geocoder.geocode(Location)
            Valid_adrress = [results.formatted_address]   
            Latitude = [results.coordinates[0]] 
            Longitude = [results.coordinates[1]]
            Accuracy =[results.location_type]
            Valid=[results.valid_address]
            #print(results)
            new_line = line +Valid_adrress+ Latitude + Longitude + Accuracy + Valid
            csv.writer(output_file).writerow(new_line)
            time.sleep(.15) #This throttles your requests. The GoogleAPI doesn't like too many requests per second.
    except GeocoderError:
       
        csv.writer(output_file).writerow("\n")
        time.sleep(.15)
        continue    
            
    print new_line #Printing to the console makes the process a lot longer. Omit for speed.
del line,Location
del data


input_file.close()
output_file.close()
   
print"end"


#``r''   Open text file for reading.  The stream is positioned at the
#         beginning of the file.

# ``r+''  Open for reading and writing.  The stream is positioned at the
#         beginning of the file.

# ``w''   Truncate file to zero length or create text file for writing.
#         The stream is positioned at the beginning of the file.

# ``w+''  Open for reading and writing.  The file is created if it does not
#         exist, otherwise it is truncated.  The stream is positioned at
#         the beginning of the file.

# ``a''   Open for writing.  The file is created if it does not exist.  The
#         stream is positioned at the end of the file.  Subsequent writes
#        to the file will always end up at the then current end of file,
#        irrespective of any intervening fseek(3) or similar.

# ``a+''  Open for reading and writing.  The file is created if it does not
#         exist.  The stream is positioned at the end of the file.  Subse-
#         quent writes to the file will always end up at the then current
#         end of file, irrespective of any intervening fseek(3) or similar.""


