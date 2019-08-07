# Declare URL Variables to be used to make requests

class Domain:
# Base to make request
    main = "https://api.spacexdata.com/v3/"

    # Declaration of the endpoints
    # Launches
    main_launches = "launches"
    latest_launches = main_launches + "/latest"
    next_launches =  main_launches + "/next"
    upcoming_launches = main_launches + "/upcoming"

    # Company information
    main_info = "info"
    main_api = ""

    # Rocket information
    main_rockets = "rockets"
    falcon_1 = main_rockets + "/falcon1"
    falcon_9 = main_rockets + "/falcon9"
    falcon_heavy = main_rockets + "/falconheavy"
    big_falcon_rocket = main_rockets + "/bfr"

    # Capsule Information
    main_capsules = "capsules"
    one=main_capsules
    upcoming_capsules = main_capsules+"/upcoming"
    past_capsules = main_capsules+"/past"
