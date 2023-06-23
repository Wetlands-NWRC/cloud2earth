# Cloud 2 Earth
Google Cloud Storage Too Google Earth Engine provides a simple command line tool for creating cloud
backed assets.

# Usage
To run the tool you only need 2 things. You need a destination image collection and a csv or text 
file that has all of the gcp uris you wish to write to the desintaion image collection.


## Notes
If passing a csv mamifest, the csv must have a column called URI in it this denotes the column that
stores the uris. 

If an error should happen i.e. a 400, 404, etc it will get logged in the error.log file.