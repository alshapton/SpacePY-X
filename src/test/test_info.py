

import sys
sys.path.append('../')
import spacexpython


def test_api():
    api_result={u'organization_link': u'https://github.com/r-spacex', u'project_name': u'SpaceX-API', u'description': u'Open Source REST API for rocket, core, capsule, pad, and launch data, created and maintained by the developers of the r/SpaceX organization', u'docs': u'https://documenter.getpostman.com/view/2025350/RWaEzAiG', u'project_link': u'https://github.com/r-spacex/SpaceX-API', u'version': u'3.1.0', u'organization': u'r/SpaceX'}
    api_data = spacexpython.info.api()
    print ("Failure on info.api")
    assert api_data == api_result

def test_company():
    company_result={u'launch_sites': 3, u'links': {u'website': u'https://www.spacex.com/', u'twitter': u'https://twitter.com/SpaceX', u'flickr': u'https://www.flickr.com/photos/spacex/', u'elon_twitter': u'https://twitter.com/elonmusk'}, u'test_sites': 1, u'name': u'SpaceX', u'founder': u'Elon Musk', u'ceo': u'Elon Musk', u'employees': 7000, u'vehicles': 3, u'headquarters': {u'city': u'Hawthorne', u'state': u'California', u'address': u'Rocket Road'}, u'summary': u'SpaceX designs, manufactures and launches advanced rockets and spacecraft. The company was founded in 2002 to revolutionize space technology, with the ultimate goal of enabling people to live on other planets.', u'founded': 2002, u'cto_propulsion': u'Tom Mueller', u'cto': u'Elon Musk', u'valuation': 27500000000, u'coo': u'Gwynne Shotwell'}
    company_data = spacexpython.info.company()
    print ("Failure on info.company")
    assert company_data == company_result
