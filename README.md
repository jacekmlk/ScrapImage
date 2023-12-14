# ScrapImage
Simple script designed to scrap images from WMS servers.  
https://docs.geoserver.org/main/en/user/services/wfs/reference.html  
Support only 1.3.0 WMS version.  

Check in GetCapabilities if downloading is allowed.  
Use on your own responsibility.  

Warning! There's no errorhandling
### Usage:
1. Check GetCapabilities of server:  
https://docs.geoserver.org/main/en/user/services/wfs/reference.html#getfeature

1. Insert data to script based on above:

```
format = ""                     # <----- Define format
layername = ""                  # <----- Insert layername
servername = ""                 # <----- Insert servername
crs = ""                        # <----- Insert crs

def main():
    """INPUT"""
    width = 2000                # <----- Height of tile in px
    height = 2000               # <----- Width of tile in px

    resolution = 5              # <----- Resolution

    start_x = 360240            # <----- X coordinate of startpoint (center of area)
    start_y = 4732060           # <----- Y coordinate of startpount (center of area)

    tile_x = 1                  # <----- Number of tiles in x direction
    tile_y = 1                  # <----- Number of tiles in y direction
```
2. Run script
3. Program will generate set of images and worldfiles.
4. Open and merge images in prorgram like QGis.
