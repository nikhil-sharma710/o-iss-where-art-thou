import xmltodict
import logging
from flask import Flask

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

iss_epoch_data = {}
iss_sighting_data = {}

@app.route('/', methods=['GET'])
def how_to_interact():
    """
    This function provides information on how to interact with the application.

    Args:
        None

    Returns:
        output (str): The function returns a string listing the different routes and each of their functions and other information.
    """
 
    output = '\nHow to interact with the application:\n\n'

    output+='First, load the data from file into memory with /read_data -X POST\n'
    output+='Below is a list of commands that return information:\n\n'

    output+='  1. /list_of_epochs - provides a list of all epochs in the positional data\n'
    output+='  2. /epochs/<epoch_name>/info - provides all information about a specific epoch in the positional data\n'
    output+='         Must provide the exact string of an epoch for <epoch_name> (see /list_of_epochs)\n'
    output+='  3. /list_of_countries - provides a list of all countries in the sighting data\n'
    output+='  4. /<country_name>/info - provides all information about a specific country in the sighting data\n'
    output+='         Must provide the exact string of a country for <country_name> (see /list_of_countries)\n'
    output+='  5. /<country_name>/list_of_regions - provides a list of all epochs in the positional data\n'
    output+='         Must provide the exact string of a country for <country_name> (see /list_of_countries)\n'
    output+='  6. /<country_name>/<region_name>/info - provides a list of all epochs in the positional data\n'
    output+='         Must provide the exact string of a country for <country_name> (see /list_of_countries)\n'
    output+='         Must provide the exact string of a region for <region_name> (see /<country_name>/list_of_regions)\n'
    output+='  7. /<country_name>/<region_name>/list_of_cities - provides a list of all epochs in the positional data\n'
    output+='         Must provide the exact string of a country for <country_name> (see /list_of_countries)\n'
    output+='         Must provide the exact string of a region for <region_name> (see /<country_name>/list_of_regions)\n'
    output+='  8. /<country_name>/<region_name>/<city_name>/info - provides a list of all epochs in the positional data\n'
    output+='         Must provide the exact string of a country for <country_name> (see /list_of_countries)\n'
    output+='         Must provide the exact string of a region for <region_name> (see /<country_name>/list_of_regions)\n'
    output+='         Must provide the exact string of a city for <city_name> (see /<country_name>/<region_name>/list_of_cities)\n\n\n'

    return output

@app.route('/list_of_epochs', methods=['GET'])
def get_all_epochs():
    """
    This function provides a list of all epochs in the positional data.

    Args:
        None

    Returns
        output (str): The function returns a string of all epochs in the positional data.
    """ 
 
    output = ''

    for i in range(len(iss_epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'])):
        output+=(str(iss_epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH']) + '\n')

    return output

@app.route('/epochs/<epoch_name>/info', methods=['GET'])
def get_specific_epoch_info(epoch_name):
    """
    This function provides all information about a specific Epoch in the positional data.

    Args:
        epoch_name (str): This string is entered in the route and is the specific epoch whose information is listed.

    Returns:
        The function returns a dictionary of all the information about the entered epoch, including X, Y, and Z and X_DOT, Y_DOT, and Z_DOT.
    """
    
    names = []

    for i in range(len(iss_epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'])):
        names.append(iss_epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'])

    if epoch_name not in names:
        logging.error('Not a valid entry for <epoch_names>.')
    else:
        for i in range(len(iss_epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'])):
            if (iss_epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'] == epoch_name):
                return iss_epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'][i]

@app.route('/list_of_countries', methods=['GET'])
def get_all_countries():
    """
    This function provides a list of all countries from the sighting data.
    
    Args:
        None

    Returns:
        output (str): The function returns a string of all countries in the sighting data, which in this case, is just United_States.
    """

    output = ''

    countries = []

    for i in range(len(iss_sighting_data['visible_passes']['visible_pass'])):
        if iss_sighting_data['visible_passes']['visible_pass'][i]['country'] not in countries:
            countries.append(iss_sighting_data['visible_passes']['visible_pass'][i]['country'])

    for i in range(len(countries)):
        output+=(str(countries[i]) + '\n')   

    return output

@app.route('/<country_name>/info', methods=['GET'])
def get_specific_country_info(country_name):
    """
    This function provides all information about a specific country in the sighting data.

    Args:
        country_name (str): This string is entered in the route and is the specific country whose information will be listed.

    Returns:
        output (str): This function returns a string of every dictionary whose country is the specific country entered in the route.
    """

    output = ''

    for i in range(len(iss_sighting_data['visible_passes']['visible_pass'])):
        if (iss_sighting_data['visible_passes']['visible_pass'][i]['country'] == country_name):
            output+=(str(dict(iss_sighting_data['visible_passes']['visible_pass'][i])) + '\n')

    return output

@app.route('/<country_name>/list_of_regions', methods=['GET'])
def get_regions_in_country(country_name):
    """
    This function provides a list of regions associated with a given country in the sighting data.

    Args:
        country_name (str): This string is entered in the route and is the specific country whose regions will be listed.

    Returns:
        output (str): This function returns a string of all regions in the specific country.
    """

    output = ''

    regions = []

    for i in range(len(iss_sighting_data['visible_passes']['visible_pass'])):
        if (iss_sighting_data['visible_passes']['visible_pass'][i]['country'] == country_name):
            if iss_sighting_data['visible_passes']['visible_pass'][i]['region'] not in regions:
                regions.append(iss_sighting_data['visible_passes']['visible_pass'][i]['region'])

    for i in range(len(regions)):
        output+=(str(regions[i]) + '\n')

    return output

@app.route('/<country_name>/<region_name>/info', methods=['GET'])
def get_specific_region_info(country_name, region_name):
    """
    This function provides all information about a specific region in the sighting data.

    Args:
        country_name (str): This string is entered in the route and is the specific country used to narrow down the regions.
        region_name (str): This string is entered in the route and is the specific region whose information will be listed.

    Returns:
        output (str): This function returns a string of every dictionary whose region and country are the specific region and country entered in the route.
    """

    output = ''

    for i in range(len(iss_sighting_data['visible_passes']['visible_pass'])):
        if (iss_sighting_data['visible_passes']['visible_pass'][i]['country'] == country_name and iss_sighting_data['visible_passes']['visible_pass'][i]['region'] == region_name):
            output+=(str(dict(iss_sighting_data['visible_passes']['visible_pass'][i])) + '\n')

    return output

@app.route('/<country_name>/<region_name>/list_of_cities', methods=['GET'])
def get_cities_in_country_and_region(country_name, region_name):
    """
    This function provides a list of cities associated with a given country and region in the sighting data.

    Args:
        country_name (str): This string is entered in the route and is the specific country used to narrow down the regions.
        region_name (str): This string is entered in the route and is the specific region whose cities will be listed.

    Returns:
        output (str): This function returns a string of all cities that are in the specific region of the specific country.
    """

    output = ''

    cities = []

    for i in range(len(iss_sighting_data['visible_passes']['visible_pass'])):
        if (iss_sighting_data['visible_passes']['visible_pass'][i]['country'] == country_name and iss_sighting_data['visible_passes']['visible_pass'][i]['region'] == region_name):
            if iss_sighting_data['visible_passes']['visible_pass'][i]['city'] not in cities:
                cities.append(iss_sighting_data['visible_passes']['visible_pass'][i]['city'])

    for i in range(len(cities)):
        output+=(str(cities[i]) + '\n')

    return output

@app.route('/<country_name>/<region_name>/<city_name>/info', methods=['GET'])
def get_specific_city_info(country_name, region_name, city_name):
    """
    This function provides all information about a specific region in the sighting data.

    Args:
        country_name (str): This string is entered in the route and is the specific country used to narrow down the regions.
        region_name (str): This string is entered in the route and is the specific region used to narrow down the cities.
        city_name (str): This string is entered in the route and is the specific city whose information will be listed.

    Returns:
        output (str): This function returns a string of every dictionary whose city, region, and country are the specific city, region, and country entered in the route.
    """

    output = ''

    for i in range(len(iss_sighting_data['visible_passes']['visible_pass'])):
        if (iss_sighting_data['visible_passes']['visible_pass'][i]['country'] == country_name and iss_sighting_data['visible_passes']['visible_pass'][i]['region'] == region_name and iss_sighting_data['visible_passes']['visible_pass'][i]['city'] == city_name):
            output+=(str(dict(iss_sighting_data['visible_passes']['visible_pass'][i])) + '\n')

    return output

@app.route('/read_data', methods=['POST'])
def read_data_from_file_into_dict():
    """
    This function reads two different XML files and converts them into two dictionaries - iss_epoch_data and iss_sighting_data.

    Args:
        None

    Returns:
        The function returns a message confirming that the data has been read from the file.
    """

    global iss_epoch_data
    global iss_sighting_data

    with open('ISS.OEM_J2K_EPH.xml', 'r') as f:
        iss_epoch_data = xmltodict.parse(f.read())

    with open('XMLsightingData_citiesUSA08.xml', 'r') as f:
        iss_sighting_data = xmltodict.parse(f.read())

    return f'Data has been read from file\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
