from __future__ import print_function


import sys
sys.path.append('../')
import spacexpython

def test_capsules():
    capsules_data=''
    capsules_result= [{'status': 'retired', 'landings': 0, 'missions': [{'flight': 7, 'name': 'COTS 1'}], 'original_launch_unix': 1291822980, 'original_launch': '2010-12-08T15:43:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C101', 'capsule_id': 'dragon1', 'type': 'Dragon 1.0', 'details': 'Reentered after three weeks in orbit'}, {'status': 'retired', 'landings': 1, 'missions': [{'flight': 8, 'name': 'COTS 2'}], 'original_launch_unix': 1335944640, 'original_launch': '2012-05-02T07:44:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C102', 'capsule_id': 'dragon1', 'type': 'Dragon 1.0', 'details': 'First Dragon spacecraft'}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 9, 'name': 'CRS-1'}], 'original_launch_unix': 1349656500, 'original_launch': '2012-10-08T00:35:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C103', 'capsule_id': 'dragon1', 'type': 'Dragon 1.0', 'details': 'First of twenty missions flown under the CRS1 contract'}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 10, 'name': 'CRS-2'}], 'original_launch_unix': 1362165000, 'original_launch': '2013-03-01T19:10:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C104', 'capsule_id': 'dragon1', 'type': 'Dragon 1.0', 'details': None}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 14, 'name': 'CRS-3'}], 'original_launch_unix': 1397849100, 'original_launch': '2014-04-18T19:25:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C105', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'First Dragon v1.1 capsule'}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 18, 'name': 'CRS-4'}, {'flight': 41, 'name': 'CRS-11'}], 'original_launch_unix': 1411278720, 'original_launch': '2014-09-21T05:52:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C106', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'First Dragon capsule to be reused'}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 19, 'name': 'CRS-5'}], 'original_launch_unix': 1420883220, 'original_launch': '2015-01-10T09:47:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C107', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 3, 'missions': [{'flight': 22, 'name': 'CRS-6'}, {'flight': 51, 'name': 'CRS-13'}, {'flight': 82, 'name': 'CRS-18'}], 'original_launch_unix': 1429042200, 'original_launch': '2015-04-14T20:10:00.000Z', 'reuse_count': 2, 'capsule_serial': 'C108', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'Second Dragon capsule to be reused'}, {'status': 'destroyed', 'landings': 0, 'missions': [{'flight': 24, 'name': 'CRS-7'}], 'original_launch_unix': 1435501260, 'original_launch': '2015-06-28T14:21:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C109', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'Destroyed on impact after F9 launch failure'}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 28, 'name': 'CRS-8'}, {'flight': 59, 'name': 'CRS-14'}], 'original_launch_unix': 1460148180, 'original_launch': '2016-04-08T20:43:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C110', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 32, 'name': 'CRS-9'}, {'flight': 64, 'name': 'CRS-15'}], 'original_launch_unix': 1468817100, 'original_launch': '2016-07-18T04:45:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C111', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 36, 'name': 'CRS-10'}, {'flight': 72, 'name': 'CRS-16'}], 'original_launch_unix': 1487515140, 'original_launch': '2017-02-19T14:39:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C112', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 45, 'name': 'CRS-12'}, {'flight': 78, 'name': 'CRS-17'}], 'original_launch_unix': 1502728260, 'original_launch': '2017-08-14T16:31:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C113', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'The last newly manufactured Dragon 1'}, {'status': 'active', 'landings': 1, 'missions': [{'flight': 76, 'name': 'CCtCap Demo Mission 1'}], 'original_launch_unix': 1551512700, 'original_launch': '2019-03-02T07:45:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C201', 'capsule_id': 'dragon2', 'type': 'Dragon 2.0', 'details': 'Destroyed in a test anomaly at LZ-1 on April 20, 2019'}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C202', 'capsule_id': 'dragon2', 'type': 'Dragon 2.0', 'details': "Capsule used to qualify Dragon 2's environmental control and life support systems."}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C203', 'capsule_id': 'dragon2', 'type': 'Dragon 2.0', 'details': 'Rumored to be used for Inflight Abort Test after DM-1'}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C204', 'capsule_id': 'dragon2', 'type': 'Dragon 2.0', 'details': 'Currently in construction for use in DM-2'}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C205', 'capsule_id': 'dragon2', 'type': 'Dragon 2.0', 'details': 'In construction for use in first mission in contract under the CCtCap contract'}]
    capsules_data = spacexpython.capsules.capsules('',1)
    assert capsules_data == capsules_result


def test_upcoming():
    upcoming_result=[{'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C202', 'capsule_id': 'dragon2', 'type': 'Dragon 2.0', 'details': "Capsule used to qualify Dragon 2's environmental control and life support systems."}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C203', 'capsule_id': 'dragon2', 'type': 'Dragon 2.0', 'details': 'Rumored to be used for Inflight Abort Test after DM-1'}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C204', 'capsule_id': 'dragon2', 'type': 'Dragon 2.0', 'details': 'Currently in construction for use in DM-2'}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C205', 'capsule_id': 'dragon2', 'type': 'Dragon 2.0', 'details': 'In construction for use in first mission in contract under the CCtCap contract'}]
    upcoming_data = spacexpython.capsules.upcoming()
    print ("Failure on upcoming capsules")
    assert upcoming_data == upcoming_result


def test_past():
    past_result=[{'status': 'retired', 'landings': 0, 'missions': [{'flight': 7, 'name': 'COTS 1'}], 'original_launch_unix': 1291822980, 'original_launch': '2010-12-08T15:43:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C101', 'capsule_id': 'dragon1', 'type': 'Dragon 1.0', 'details': 'Reentered after three weeks in orbit'}, {'status': 'retired', 'landings': 1, 'missions': [{'flight': 8, 'name': 'COTS 2'}], 'original_launch_unix': 1335944640, 'original_launch': '2012-05-02T07:44:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C102', 'capsule_id': 'dragon1', 'type': 'Dragon 1.0', 'details': 'First Dragon spacecraft'}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 9, 'name': 'CRS-1'}], 'original_launch_unix': 1349656500, 'original_launch': '2012-10-08T00:35:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C103', 'capsule_id': 'dragon1', 'type': 'Dragon 1.0', 'details': 'First of twenty missions flown under the CRS1 contract'}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 10, 'name': 'CRS-2'}], 'original_launch_unix': 1362165000, 'original_launch': '2013-03-01T19:10:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C104', 'capsule_id': 'dragon1', 'type': 'Dragon 1.0', 'details': None}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 14, 'name': 'CRS-3'}], 'original_launch_unix': 1397849100, 'original_launch': '2014-04-18T19:25:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C105', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'First Dragon v1.1 capsule'}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 18, 'name': 'CRS-4'}, {'flight': 41, 'name': 'CRS-11'}], 'original_launch_unix': 1411278720, 'original_launch': '2014-09-21T05:52:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C106', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'First Dragon capsule to be reused'}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 19, 'name': 'CRS-5'}], 'original_launch_unix': 1420883220, 'original_launch': '2015-01-10T09:47:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C107', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 3, 'missions': [{'flight': 22, 'name': 'CRS-6'}, {'flight': 51, 'name': 'CRS-13'}, {'flight': 82, 'name': 'CRS-18'}], 'original_launch_unix': 1429042200, 'original_launch': '2015-04-14T20:10:00.000Z', 'reuse_count': 2, 'capsule_serial': 'C108', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'Second Dragon capsule to be reused'}, {'status': 'destroyed', 'landings': 0, 'missions': [{'flight': 24, 'name': 'CRS-7'}], 'original_launch_unix': 1435501260, 'original_launch': '2015-06-28T14:21:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C109', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'Destroyed on impact after F9 launch failure'}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 28, 'name': 'CRS-8'}, {'flight': 59, 'name': 'CRS-14'}], 'original_launch_unix': 1460148180, 'original_launch': '2016-04-08T20:43:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C110', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 32, 'name': 'CRS-9'}, {'flight': 64, 'name': 'CRS-15'}], 'original_launch_unix': 1468817100, 'original_launch': '2016-07-18T04:45:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C111', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 36, 'name': 'CRS-10'}, {'flight': 72, 'name': 'CRS-16'}], 'original_launch_unix': 1487515140, 'original_launch': '2017-02-19T14:39:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C112', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 45, 'name': 'CRS-12'}, {'flight': 78, 'name': 'CRS-17'}], 'original_launch_unix': 1502728260, 'original_launch': '2017-08-14T16:31:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C113', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'The last newly manufactured Dragon 1'}, {'status': 'active', 'landings': 1, 'missions': [{'flight': 76, 'name': 'CCtCap Demo Mission 1'}], 'original_launch_unix': 1551512700, 'original_launch': '2019-03-02T07:45:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C201', 'capsule_id': 'dragon2', 'type': 'Dragon 2.0', 'details': 'Destroyed in a test anomaly at LZ-1 on April 20, 2019'}]
    past_data = spacexpython.capsules.past()
    print ("Failure on past capsules")
    assert past_data == past_result


def test_one():
    one_result={'status': 'unknown', 'landings': 1, 'missions': [{'flight': 14, 'name': 'CRS-3'}], 'original_launch_unix': 1397849100, 'original_launch': '2014-04-18T19:25:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C105', 'capsule_id': 'dragon1', 'type': 'Dragon 1.1', 'details': 'First Dragon v1.1 capsule'}
    one_data = spacexpython.capsules.one('C105')
    print ("Failure on one capsule (C105)")
    assert one_data == one_result


def test_capsulesP():
    capsulesP_result=[{'status': 'retired', 'landings': 0, 'missions': [{'flight': 7, 'name': 'COTS 1'}], 'original_launch_unix': 1291822980, 'original_launch': '2010-12-08T15:43:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C101', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a000001', 'type': 'Dragon 1.0', 'details': 'Reentered after three weeks in orbit'}, {'status': 'retired', 'landings': 1, 'missions': [{'flight': 8, 'name': 'COTS 2'}], 'original_launch_unix': 1335944640, 'original_launch': '2012-05-02T07:44:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C102', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a000002', 'type': 'Dragon 1.0', 'details': 'First Dragon spacecraft'}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 9, 'name': 'CRS-1'}], 'original_launch_unix': 1349656500, 'original_launch': '2012-10-08T00:35:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C103', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a000003', 'type': 'Dragon 1.0', 'details': 'First of twenty missions flown under the CRS1 contract'}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 10, 'name': 'CRS-2'}], 'original_launch_unix': 1362165000, 'original_launch': '2013-03-01T19:10:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C104', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a000004', 'type': 'Dragon 1.0', 'details': None}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 14, 'name': 'CRS-3'}], 'original_launch_unix': 1397849100, 'original_launch': '2014-04-18T19:25:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C105', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a000005', 'type': 'Dragon 1.1', 'details': 'First Dragon v1.1 capsule'}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 18, 'name': 'CRS-4'}, {'flight': 41, 'name': 'CRS-11'}], 'original_launch_unix': 1411278720, 'original_launch': '2014-09-21T05:52:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C106', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a000006', 'type': 'Dragon 1.1', 'details': 'First Dragon capsule to be reused'}, {'status': 'unknown', 'landings': 1, 'missions': [{'flight': 19, 'name': 'CRS-5'}], 'original_launch_unix': 1420883220, 'original_launch': '2015-01-10T09:47:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C107', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a000007', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 3, 'missions': [{'flight': 22, 'name': 'CRS-6'}, {'flight': 51, 'name': 'CRS-13'}, {'flight': 82, 'name': 'CRS-18'}], 'original_launch_unix': 1429042200, 'original_launch': '2015-04-14T20:10:00.000Z', 'reuse_count': 2, 'capsule_serial': 'C108', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a000008', 'type': 'Dragon 1.1', 'details': 'Second Dragon capsule to be reused'}, {'status': 'destroyed', 'landings': 0, 'missions': [{'flight': 24, 'name': 'CRS-7'}], 'original_launch_unix': 1435501260, 'original_launch': '2015-06-28T14:21:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C109', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a000009', 'type': 'Dragon 1.1', 'details': 'Destroyed on impact after F9 launch failure'}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 28, 'name': 'CRS-8'}, {'flight': 59, 'name': 'CRS-14'}], 'original_launch_unix': 1460148180, 'original_launch': '2016-04-08T20:43:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C110', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a00000a', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 32, 'name': 'CRS-9'}, {'flight': 64, 'name': 'CRS-15'}], 'original_launch_unix': 1468817100, 'original_launch': '2016-07-18T04:45:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C111', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a00000b', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 36, 'name': 'CRS-10'}, {'flight': 72, 'name': 'CRS-16'}], 'original_launch_unix': 1487515140, 'original_launch': '2017-02-19T14:39:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C112', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a00000c', 'type': 'Dragon 1.1', 'details': None}, {'status': 'active', 'landings': 2, 'missions': [{'flight': 45, 'name': 'CRS-12'}, {'flight': 78, 'name': 'CRS-17'}], 'original_launch_unix': 1502728260, 'original_launch': '2017-08-14T16:31:00.000Z', 'reuse_count': 1, 'capsule_serial': 'C113', 'capsule_id': 'dragon1', '_id': '596eb5fc611279d39a00000d', 'type': 'Dragon 1.1', 'details': 'The last newly manufactured Dragon 1'}, {'status': 'active', 'landings': 1, 'missions': [{'flight': 76, 'name': 'CCtCap Demo Mission 1'}], 'original_launch_unix': 1551512700, 'original_launch': '2019-03-02T07:45:00.000Z', 'reuse_count': 0, 'capsule_serial': 'C201', 'capsule_id': 'dragon2', '_id': '596eb5fc611279d39a00000e', 'type': 'Dragon 2.0', 'details': 'Destroyed in a test anomaly at LZ-1 on April 20, 2019'}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C202', 'capsule_id': 'dragon2', '_id': '596eb5fc611279d39a00000f', 'type': 'Dragon 2.0', 'details': "Capsule used to qualify Dragon 2's environmental control and life support systems."}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C203', 'capsule_id': 'dragon2', '_id': '596eb5fc611279d39a000010', 'type': 'Dragon 2.0', 'details': 'Rumored to be used for Inflight Abort Test after DM-1'}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C204', 'capsule_id': 'dragon2', '_id': '596eb5fc611279d39a000011', 'type': 'Dragon 2.0', 'details': 'Currently in construction for use in DM-2'}, {'status': 'active', 'landings': 0, 'missions': [], 'original_launch_unix': None, 'original_launch': None, 'reuse_count': 0, 'capsule_serial': 'C205', 'capsule_id': 'dragon2', '_id': '596eb5fc611279d39a000012', 'type': 'Dragon 2.0', 'details': 'In construction for use in first mission in contract under the CCtCap contract'}]
    capsulesP_data = spacexpython.capsules.capsules('{"capsule_serial":"C112", "id":"true"}')
    assert capsulesP_data == capsulesP_result
