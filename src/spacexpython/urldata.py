
"""urldata module

This is a module defines the endpoints for the REST SpaceX API
"""
#from builtins import object
class Domain(object):
    """ Base URL from which to assemble request URLs """
    base = "https://api.spacexdata.com"

    """ API Version """
    version = "v3"
    main = base + "/" + version + "/"

    """ Declaration of the endpoints """

    """ Launches """
    main_launches = "launches"
    latest_launches = main_launches + "/latest"
    next_launches =  main_launches + "/next"
    upcoming_launches = main_launches + "/upcoming"

    """ Company information """
    main_info = "info"
    main_api = ""

    """ Rocket information """
    main_rockets = "rockets"
    falcon1 = main_rockets + "/falcon1"
    falcon9 = main_rockets + "/falcon9"
    falconheavy = main_rockets + "/falconheavy"
    bigfalconrocket = main_rockets + "/bfr"

    """ Capsule Information """
    main_capsules = "capsules"
    one=main_capsules
    upcoming_capsules = main_capsules+"/upcoming"
    past_capsules = main_capsules+"/past"
