import requests
import json 
import unittest
from unittest import TestCase
from common import logger

class TestSimpleCrud(TestCase):

    def test_create(self):
        data = {
        'eid': 1999,
        'name': 'Jhon',
        'salary': 23000.0,
        'full_time': False,
        'age': 28
        }
        try:
            response = requests.put('http://localhost:5000', data=json.dumps(data))
        except Exception as ex:
            print("Exception:", str(ex))
            
        logger.info("----------Response-----------")
        logger.info(response.json())
        resp = response.json()
        logger.info("-----------------------------")

        self.assertTrue(resp['status'] == 'success')

    def test_update(self):
        data = {
        'eid': 1234,
        'name': 'Jhon',
        'salary': 45999.0,
        'full_time': False,
        'age': 43
    }
        response = requests.post('http://localhost:5000', data=json.dumps(data))
        logger.info("----------Response-----------")
        logger.info(response.json())
        resp = response.json()
        logger.info("-----------------------------")
        self.assertTrue(resp['status'] == 'success')

    def test_read(self):
        eid=1234
        response = requests.get('http://localhost:5000/' + str(eid))
        logger.info("----------Response-----------")
        logger.info(response.json())
        logger.info("-----------------------------")
        resp = response.json()
        self.assertTrue(resp['status'] == 'success')

    def test_delete(self):
        eid = 1255
        response = requests.delete('http://localhost:5000/' + str(eid))
        logger.info("----------Response-----------")
        resp = response.json()
        logger.info("-----------------------------")
        self.assertTrue(resp['status'] == 'success')


if __name__ == '__main__':
    emp1 = {
        'eid': 1234,
        'name': 'Jhon',
        'salary': 23000.0,
        'full_time': False,
        'age': 28
    }
    emp2 = {
        'eid': 1299,
        'name': 'Amanda',
        'salary': 15000.0,
        'full_time': True,
        'age': 43
    }
    emp3 = {
        'eid': 1255,
        'name': 'Samantha',
        'salary': 33000.0,
        'full_time': True,
        'age': 28
    }

    # test_create(emp2)
    # test_update(emp1_modified)
    # test_read(1255)
    # test_delete(1277)

    unittest.main()