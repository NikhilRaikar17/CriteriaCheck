from application.CriteriaCheckApi.api.CriterInfo import CriteriaInfoClient
import pytest

class TestCriteriaCheck:
    def test_url(self):
        """ Test url with valid parameters """
        name = 'Karlsruhe'
        response = CriteriaInfoClient.get_info(name)
        assert response['cod'] == 200
    
    def test_url_with_unknown_name(self):
        """ Test url with unknown name """
        name = 'Karlsrasdasdsaduhe'
        response = CriteriaInfoClient.get_info(name)
        assert response['Error'] == 'Invalid Request'
    
    def test_url_with_small_name(self):
        """ Test url with city name less than 2 characters """
        name = 'de'
        response = CriteriaInfoClient.get_info(name)
        assert response['Error'] == 'Name is too short'
    
    def test_name_criteria(self):
        """ Test name criteria with odd number """
        criteria_dict = {}
        response_json = {'name': 'test_name'}
        count = 0
        response,count = CriteriaInfoClient.check_name(criteria_dict,response_json,count)
        assert criteria_dict['naming'] == False
    
    def test_name_criteria(self):
        """ Test name criteria with even number """
        criteria_dict = {}
        response_json = {'name': 'test_names'}
        count = 0
        response,count = CriteriaInfoClient.check_name(criteria_dict,response_json,count)
        assert criteria_dict['naming'] == True
    
    def test_temp_criteria_17_25(self):
        """ Check temperature criteria with greater 
        than 17 and less than 25 """
        criteria_dict = {}
        response_json = {'main': {'temp_min': 291.8,
                                'temp_max': 296.80
                                } 
                        }
        count = 0
        response,count = CriteriaInfoClient.check_temp(criteria_dict,response_json,count)
        assert count == 1
    
    def test_temp_criteria_10_15(self):
        """ Check temperature criteria with greater 
        than 10 and less than 15 """
        criteria_dict = {}
        response_json = {'main': {'temp_min': 284.8,
                                'temp_max': 287.80
                                } 
                        }
        count = 0
        response,count = CriteriaInfoClient.check_temp(criteria_dict,response_json,count)
        assert count == 1
    
    def test_rival_temp(self):
        """ Check rival temp greater than 280 """
        criteria_dict = {}
        response_json = {'main': {'temp': 284.8 } }
        count = 0
        response,count = CriteriaInfoClient.check_rival(criteria_dict,response_json,count)
        assert count == 1
    
    def test_rival_temp(self):
        """ Check rival temp lesser than 280 """
        criteria_dict = {}
        response_json = {'main': {'temp': 278.8 } }
        count = 0
        response,count = CriteriaInfoClient.check_rival(criteria_dict,response_json,count)
        assert count == 0
    
    



