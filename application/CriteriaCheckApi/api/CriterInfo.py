import requests

class CriteriaInfoClient:
    api_key = '8ca1bf554fe26dff41d635d4e2f866ed'

    @staticmethod
    def get_info(name):
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
            return {'Error': f'{message}'}
    
    @staticmethod
    def check_criterias(response_json):
        criteria = {}
        name = response_json['name']
        count = 0

        criteria['naming'] = False
        if len(name) % 2 == 0:
            count = count + 1
            criteria['naming'] = True
        

        min_term = int(response_json['main']['temp_min']) - 273.15
        min_term = float(format(min_term, '.3f')) 

        max_term = int(response_json['main']['temp_max']) - 273.15
        max_term = float(format(max_term, '.3f'))
        print(min_term,max_term)
        
        return criteria         

    @staticmethod
    def validate_name(name):
        try:
            if not name:
                raise Exception('Name is not passed ')
            
            if len(name) <= 2:
                raise Exception('Name is too short')
            
            return None, name
        except Exception as e:
            message = e.args[0]
            print(message)
            return 'Name is too short', None


