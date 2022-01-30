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
        """ Test name criteria """
        pass
