# The Instant Traveler
    #### Video Demo:  <https://youtu.be/Y3FecMEvG4c>
    #### Description:

    This project is for those who want to pack up and hit the world.

    Its main purpose is to give live information about flights which will take off within 24 hours. It takes as input one departure 
    and one arrival point and gives information about the incoming flights. Such information is the city name, airline, departure 
    and arrival airports, local date and time as well as the flight number. The program is designed to use Aviationstack API which 
    gives all of the needed information about the flight.

    On the technical side the program consists of one main function and five extra functions:

    main function - contains all of the other functions and processes the information that is returned. It sets the title of the 
    project using the PyFiglet library. Unpack the API key, URL, arrival airport and departure airport from the get_info function 
    and using the requests library to get the data for the flights between the two airports. If no data is found the program 
    outputs "Failed to receive flight info" and eventually if indeed it is, the program checks if there are flights between the two 
    destinations. If flights are found the program checks all of them to find if they are already departed or not. If at least one 
    flight is still to take place the main function outputs the airports' names, airline, local dates and time and the flight number. 
    All of the information used is from Aviationstack API.

    get_info function - contains the API key, URL of the Aviationstack website and asks the user for departure and arrival 
    destinations. Returns all the information to the main function.

    format_schedule function - finds the date and time of the flight from the API's data, groups it by using regular expressions.
    Then sorts it and returns it to the main function.

    get_iata_code function - using a JSON file that contains a list of around 10 000 dictionaries. In every one of them is stored 
    the city name, IATA code of the airport, abbreviation of the country as well as the timezone. if the input is the actual IATA 
    code confirmed by the file, the code is returned to the main function. If the input does not match any IATA code it is assumed 
    it is the city name so it goes a second round in the JSON file, but this time trying to match the city name. In case the search 
    finds the city the program returns the IATA code that matched the city to the main function. If not, the program executes 
    sys.exit and prints "City not found". An exception is used to verify that no "NoneType" will be returned to the main function 
    by using sys.exit with "City not found" message.

    get_city_name function - similar to the get_iata_code function except it returns the name of the city to the main function to 
    be printed as a note indicating the departure city and the arrival city.

    check_time function - uses the scheduled time for the flight from the API and compares it to the actual time at the moment with
    datetime and pytz to determine if the flight is already departed. Returns True if the flight is still to take place or False if 
    it is already departed.

    This was my final project for CS50P.
    This was CS50.
