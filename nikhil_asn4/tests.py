import requests
import json 

from common import logger

base_url = 'http://localhost:5000/'
headers = {'Content-Type': 'application/json'}

def test_create(data):

    try:
        response = requests.put(base_url, headers=headers, data=json.dumps(data))
    except Exception as ex:
        print("Exception:", str(ex))
        
    logger.info("----------Response-----------")
    logger.info(response.json())
    resp = response.json()
    logger.info("-----------------------------")


def test_update(data):

    response = requests.post(base_url, headers=headers, data=json.dumps(data))
    logger.info("----------Response-----------")
    logger.info(response.json())
    resp = response.json()
    logger.info("-----------------------------")


def test_read(eid):
    response = requests.get(base_url+str(eid))
    logger.info("----------Response-----------")
    logger.info(response.json())
    logger.info("-----------------------------")
    resp = response.json()


def test_delete(eid):
    response = requests.delete(base_url+str(eid))
    logger.info("----------Response-----------")
    resp = response.text
    logger.info(response.text)
    logger.info("-----------------------------")



if __name__ == '__main__':
    emp1 = {
        'eid': 1234,
        'name': 'Jhon',
        'salary': 23000.0,
        'full_time': False,
        'age': 28
    }
    emp2 = {
        'eid': 7799,
        'name': 'Amanda',
        'salary': 15000.0,
        'full_time': True,
        'age': 43
    }
    emp3 = {
        'eid': 7799,
        'name': 'Samantha',
        'salary': 33000.0,
        'full_time': True,
        'age': 28
    }

    # test_create(emp2)
    # test_update(emp3)
    # test_read(7799)
    test_delete(1999)
