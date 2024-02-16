import pandas as pd
import requests 
import json

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app"'

df = pd.read_csv(r'C:\Users\victor.rodriguess\Documents\EstudoPython\SantanderDevWeek\SDW2023.CSV', encoding='utf-8')
userID = df['UserID'].tolist()



def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None


users = [user for id in userID if(user := get_user(id)) is not None]
print(json.dumps(users, indent=2))
