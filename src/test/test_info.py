

import sys
sys.path.append('../')
import spacexpython



def test_api():
    api_result={'organization_link': 'https://github.com/r-spacex', 'project_name': 'SpaceX-API', 'description': 'Open Source REST API for rocket, core, capsule, pad, and launch data, created and maintained by the developers of the r/SpaceX organization', 'docs': 'https://documenter.getpostman.com/view/2025350/RWaEzAiG', 'project_link': 'https://github.com/r-spacex/SpaceX-API', 'version': '3.1.0', 'organization': 'r/SpaceX'}
    api_data = spacexpython.info.api()
    print ("Failure on info.api")
    assert api_data == api_result


def test_company():
    company_result={'launch_sites': 3, 'links': {'website': 'https://www.spacex.com/', 'twitter': 'https://twitter.com/SpaceX', 'flickr': 'https://www.flickr.com/photos/spacex/', 'elon_twitter': 'https://twitter.com/elonmusk'}, 'test_sites': 1, 'name': 'SpaceX', 'founder': 'Elon Musk', 'ceo': 'Elon Musk', 'employees': 7000, 'vehicles': 3, 'headquarters': {'city': 'Hawthorne', 'state': 'California', 'address': 'Rocket Road'}, 'summary': 'SpaceX designs, manufactures and launches advanced rockets and spacecraft. The company was founded in 2002 to revolutionize space technology, with the ultimate goal of enabling people to live on other planets.', 'founded': 2002, 'cto_propulsion': 'Tom Mueller', 'cto': 'Elon Musk', 'valuation': 27500000000, 'coo': 'Gwynne Shotwell'}
    company_data = spacexpython.info.company()
    print ("Failure on info.company")
    assert company_data == company_result
