#########################################################
#     Simple script to scrap images from WMS server     #
#           Use on your own responsibility              #
#   Check in GetCapabilities if downloading is allowed  #
#           Work only with 1.3.0 WMS version            #
#           Warning! There's no errorhandling           #
#########################################################

import urllib.request as u
import urllib.parse as p

"""INPUT"""
"""All input data get from GetCapabilities https://docs.geoserver.org/main/en/user/services/wfs/reference.html#getcapabilities """
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

    """CODE"""
    step = {}
    step["width"] = width * resolution
    step["height"] = height * resolution

    image = {}
    image["width"] = width
    image["height"] = height

    start = {}
    start["x"] = start_x
    start["y"] = start_y

    tile = {}
    tile["x"] = tile_x
    tile["y"] = tile_y

    for line in matrix(tile, start, step):
        url = servername + "?service=WMS&request=GetMap&version=1.3.0&" + parse(image, coordinate(line, step))

        namefile = "/DCIM/" + layername + '_' + line["name"] + "." + format

        #File extension

        worldfile(resolution, line, step, namefile)

        u.urlretrieve(url, namefile)
    aream = str(step["width"] * tile_x) + 'm x ' + str(step["height"] * tile_y)
    areapx = str(image["width"] * tile_x) + 'px x ' + str(image["height"] * tile_y)
    print(f"Area: {aream}m ({areapx}px)" )
 
def parse(image, bbox):
    data ={}
    
    #Data from GetFeature
    data["layers"] = layername
    data["styles"] = ""
    data["format"] = "image/" + format
    data["transparent"] = "true"
    data["continuousWorld"] = "true"
    data["minZoom"] = 0
    data["maxZoom"] = 26
    data["crs"] = crs
    data["width"] = image["width"]
    data["height"] = image["height"] 
    data["bbox"] = str(bbox["min_x"]) + ',' + str(bbox["min_y"]) + ',' + str(bbox["max_x"]) + ',' + str(bbox["max_y"])

    return p.urlencode(data)

def coordinate(start, step):

    ctr_x = start["x"]
    ctr_y = start["y"]

    min_x = ctr_x - (step["width"] / 2)
    min_y = ctr_y - (step["height"] / 2)
    max_x = ctr_x + (step["width"] / 2)
    max_y = ctr_y + (step["height"] / 2)

    coordinate = {"min_x" : min_x,
                   "min_y" : min_y,
                   "max_x" : max_x,
                   "max_y" : max_y}

    return coordinate

def matrix(tile, start, step):

    tile_x = tile["x"]
    tile_y = tile["y"]

    begin_x = start["x"] - (tile_x * step["width"]/2) + step["width"]/2
    begin_y = start["y"] - (tile_y * step["height"]/2) + step["height"]/2

    array = []
    for i in range(0, tile_y):
        for j in range(0, tile_x):
            ctr = {}
            ctr["x"] = begin_x + step["width"] * j
            ctr["y"] = begin_y + step["height"] * i
            ctr["name"] = str(i) + '_' + str(j) 
            array.append(ctr)
    
    return array

def worldfile(resolution, coordinate, step, namefile):
    A = resolution
    D = 0.0
    B = 0.0
    E = resolution * -1
    C = coordinate["x"] - step["width"] / 2 + resolution / 2
    F = coordinate["y"] + step["height"] / 2 - resolution / 2

    #Worldfile extension
    name = namefile + "w"

    with open(name, 'w') as f:
        f.write(f"{A}\n{D}\n{B}\n{E}\n{C}\n{F}")
    f.close()


if __name__ == "__main__":
    main()






