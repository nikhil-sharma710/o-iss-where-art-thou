## Midterm Project: O ISS, Where Art Thou?

The objective of this project is to write and containerize a Flask application for tracking ISS positions. Four scripts are found in this repository:

* `app.py`: A Flask application that parses ISS positional and sighting data to return information about epochs, countries, regions, and cities through routes.
* `test_app.py`: Tests methods in `app.py`.
* `Dockerfile`: text file that contains all commands to build the image.
* `Makefile`: text file that

### Running Instructions

The code must be run sequentially as follows.

#### Step 1: Retrieve XML Files

Use the following commands to retrieve `ISS_OEM/ISS.OEM_J2K_EPH.xml` and `XMLsightingData_citiesUSA08.xml` from the web. These XML files are the data used by `app.py`.

```
$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml
$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA08.xml
```

#### Step 2: Pull or Build Docker Image

```
$ make pull
```

Use the command above to pull and use he existing image on Docker Hub. The image is called `midterm` and the tag is `1.0`. The command `make pull` can be used because `docker build -t ${NAME}/midterm:1.0 .` is already in `Makefile`.

OR

```
$ docker build -t <username>/midterm:1.0 .
```

Use the command above to build the Docker image using the Dockerfile. Replace `<username>` with your Docker username.


#### Step 3: Run Docker Image

```
$ make run
```

Use the command above the run the Docker image. The command `make run` can be used because `docker run --rm -d -p 5029:5000 --name nikhil-midterm ${NAME}/midterm:1.0` is already in `Makefile`.
    
#### Step 4: Use Flask Applicaton

```
$ curl localhost:5029/
```

Use the command above to run the Flask application `app.py`. This will provide information on how to interact with the application. In order to get information from the data, use the following command:

```
$ curl localhost:5029/read_data -X POST
```

This will use the `POST` operation to load the data from file into memory. Below is a list of commands that return information:

curl localhost:5029/list_of_epochs - provides a list of all epochs in the positional data
curl localhost:5029/epochs/<epoch_name>/info - provides all information about a specific epoch in the positional data
curl localhost:5029/list_of_countries - provides a list of all countries in the sighting data
curl localhost:5029/<country_name>/info - provides all information about a specific country in the sighting data
curl localhost:5029/<country_name>/list_of_regions - provides a list of all epochs in the positional data
curl localhost:5029/<country_name>/<region_name>/info - provides a list of all epochs in the positional data
curl localhost:5029/<country_name>/<region_name>/list_of_cities - provides a list of all epochs in the positional data
curl localhost:5029/<country_name>/<region_name>/<city_name>/info - provides a list of all epochs in the positional data

#### Step 5: Test Pytest File

```
docker run --rm -it nikhilsharma710/midterm:1.0 pytest /code/
```

Use the command above to run the Pytest Application. The application tests the `how_to_interact` method in `app.py`, asserting that it returns a `str` value. If the test passes, the resulting message should be as follows:

```
================================================================================ test session starts ================================================================================
platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
rootdir: /code
collected 1 item                                                                                                                                                                    

test_app.py .                                                                                                                                                                 [100%]

================================================================================= 1 passed in 0.31s =================================================================================
```
