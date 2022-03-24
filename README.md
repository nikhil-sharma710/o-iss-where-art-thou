## Midterm Project: O ISS, Where Art Thou?

The objective of this project is to write and containerize a Flask application for tracking ISS positions. Four scripts are found in this repository:

* `app.py`: 
* `test_app.py`: 
* `Dockerfile`: text file that contains all commands to build the image.
* `Makefile`: text file that

### Running Instructions

The code must be run sequentially as follows.

#### Step 1:

```
$ docker pull nikhilsharma710/midterm:1.0
```

Use the command above to pull and use the existing image on Docker Hub. The image is called `midterm` and the tag is `1.0`.

#### Step 2:

```
$ docker build -t nikhilsharma710/midterm:1.0 .
```

Use the command above to build the Docker image using the Dockerfile.

#### Step 3:

Use the following commands to retrieve `ISS_OEM/ISS.OEM_J2K_EPH.xml` and `XMLsightingData_citiesUSA08.xml` from the web. These XML files are the data used by `app.py`.

```
$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml
$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA08.xml
```
#### Step 4:

Open a new Terminal window and navigate to this directory. To start the Flask service on unique port 5029, use the following commands:

.. code-block:: console

    $ export FLASK_APP=app.py
    $ export FLASK_ENV=development
    $ flask run -p 5029
     * Serving Flask app "app.py" (lazy loading)
     * Environment: development
     * Debug mode: on
     * Running on http://127.0.0.1:5029/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 317-915-949



Use the command above to run the program `ml_data_analysis.py` using the data fromm `Meteorite_Landings.json`. The program will summarize the findings from each of the sites listed in the data, including the average mass of each meteorite, the amount of meteorites that land in each quadrant (Northeastern, Northwestern, Southeastern, Southwestern), and the amount of each class of meteorites that occurs. If you'd like to download your own data, such as the sample data `ML_Data_Sample.json`, use the following command:

```
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

This will add the JSON file `ML_Data_Sample.json` to the repository. To run `ml_data_analysis.py` with the new data, replace `Meteorite_Landings.json` with `ML_Data_Sample.json` as so:

```
$ ./ml_data_analysis.py ML_Data_Sample.json
```

If you would like to use your own data, it would have to be in the following format as a JSON file:

{
  "meteorite_landings": [
    {
      "name": "",
      "id": "",
      "recclass": "",
      "mass (g)": "",
      "reclat": "",
      "reclong": "",
      "GeoLocation": ""
    },
    {
      "name": "",
      "id": "",
      "recclass": "",
      "mass (g)": "",
      "reclat": "",
      "reclong": "",
      "GeoLocation": ""
    },
    ...
  ]
  
}
    
#### Step 4:

```
$ python3 test_ml_data_analysis.py
```

Use the command above to run the containerized suite with pytest. It runs five tests for each of the methods in `ml_data_analysis.py` while using sample data. There should be no output as the code is error-free.
