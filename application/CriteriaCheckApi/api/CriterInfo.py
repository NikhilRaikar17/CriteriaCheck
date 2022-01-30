import requests

class CriteriaInfoClient:
    api_key = '8ca1bf554fe26dff41d635d4e2f866ed'

    @staticmethod
    def get_info(name):
        """ Get all information about the city """
        try:        
            error, name = CriteriaInfoClient.validate_name(name)
            if error:
                raise Exception(error)

            response = requests.request(method="GET", url=f"http://api.openweathermap.org/data/2.5/weather?q={name},de&appid={CriteriaInfoClient.api_key}")
            if response.status_code!= 200:
                raise Exception('Invalid Request')
            
            criteria_info = response.json()

            return criteria_info

        except Exception as e:
            message = e.args[0]
            print(message)
            return {'Error': True,'Message': f'{message}'}
    
    @staticmethod
    def check_criterias(response_json):
        """ Check all criterias """
        try:
            criteria = {}
            count = 0

            criteria,count = CriteriaInfoClient.check_name(criteria,response_json,count)
            if 'ERROR' in criteria.keys():
                raise Exception(criteria['ERROR'])

            criteria,count = CriteriaInfoClient.check_temp(criteria,response_json,count)
            if 'ERROR' in criteria.keys():
                raise Exception(criteria['ERROR'])

            criteria,count = CriteriaInfoClient.check_rival(criteria,response_json,count)
            if 'ERROR' in criteria.keys():
                raise Exception(criteria['ERROR'])

            check = False
            if count == 3:
                check = True
            
            return {'Check': check, 'criteria': criteria}

        except Exception as e:
            message = e.args[0]
            print(message)
            return {'Error': True,'Message': f'{message}'}
    
    @staticmethod
    def check_temp(criteria_dict,response_json,count):
        """ Check temperature value """
        try:
            error, min_term = CriteriaInfoClient.convert_kelvin_to_celcius(int(response_json['main']['temp_min']))
            if error:
                raise Exception(error)

            error, max_term = CriteriaInfoClient.convert_kelvin_to_celcius(int(response_json['main']['temp_max']))
            if error:
                raise Exception(error)

            criteria_dict['daytemp'] = False
            if (min_term > 17 and max_term < 25) or (min_term > 10 and max_term < 15):
                count = count + 1
                criteria_dict['daytemp'] = True
            
            return criteria_dict,count
        except Exception as e:
            message = e.args[0]
            print(message)
            return {'ERROR':'Temperature are not properly formated'}, count
    
    @staticmethod
    def check_rival(criteria_dict,response_json,count):
        """ Check rival temperature and compare it with present city temperature """
        try:
            rival_temp_json = CriteriaInfoClient.get_info('cologne')
            criteria_dict['rival'] = False
            if response_json['main']['temp'] > rival_temp_json['main']['temp']:
                count = count + 1
                criteria_dict['rival'] = True
            return criteria_dict,count
        except Exception as e:
            message = e.args[0]
            print(message)
            return {'ERROR':'Rival Temperature could not be determined properly'},count

    @staticmethod
    def check_name(criteria_dict,response_json,count):
        """ Check whether name has even number of characters """
        try:
            name = response_json['name']
            criteria_dict['naming'] = False
            if len(name) % 2 == 0:
                count = count + 1
                criteria_dict['naming'] = True

            return criteria_dict,count
        except Exception as e:
            message = e.args[0]
            print(message)
            return {'ERROR': 'Name could not be properly verified'}, count

    @staticmethod
    def convert_kelvin_to_celcius(kelvin):
        """ Convert kelvin to celcius """
        try:            
            celcius_in_float = kelvin - 273.15
            celcius = float(format(celcius_in_float, '.3f'))

            return None, celcius

        except Exception as e:
            message = e.args[0]
            print(message)
            return 'Kelvin is not in proper format', None

    @staticmethod
    def validate_name(name):
        """ Validate whether the user has inputed proper name """
        try:
            if not name:
                raise Exception('Name is not passed')
            
            if len(name) <= 2:
                raise Exception('Name is too short')
            
            return None, name
        except Exception as e:
            message = e.args[0]
            print(message)
            return 'Name is too short', None


