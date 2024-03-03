from datetime import datetime
import requests
import os
from urllib.parse import urljoin
from typing import List
from models import LabelModel, VehicleModelItem, AuthResModel

expires_at = None
access_token = None
refresh_token = None

def get_token():
    '''
    Get access_token, refresh_token and its expires_at from login API and store it in memory in global variables
    '''
    base_url = os.environ.get('BAUBUDDY_URL')
    auth = os.environ.get('BAUBUDDY_AUTH')
    username = os.environ.get('BAUBUDDY_USERNAME')
    password = os.environ.get('BAUBUDDY_PASSWORD')
    headers = {
        'Authorization': f'basic {auth}',
        'Content-Type': 'application/json'
    }

    res = requests.post(urljoin(base_url, 'index.php/login'), json={ 'username': username, 'password': password }, headers=headers)
    if res.ok:
        body = AuthResModel(**res.json())
        global access_token, refresh_token, expires_at
        access_token = body.oauth.get('access_token', None)
        refresh_token = body.oauth.get('refresh_token', None)
        expires_at = datetime.now().timestamp()/1000 + body.oauth.get('expires_in')
    else:
        raise Exception('Auth error', res.text)


def active_vehicles() -> List[VehicleModelItem]:
    '''
    Fetch the list of active vehicles
    It requires a valid access_token, if not present or expired it will try to fetch new access_token
    '''
    global access_token, expires_at
    if access_token is None or datetime.now().timestamp() >= expires_at:
        get_token()
    base_url = os.environ.get('BAUBUDDY_URL')
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    res = requests.get(urljoin(base_url, 'dev/index.php/v1/vehicles/select/active'), headers=headers)
    if res.ok:
        vehicles = [VehicleModelItem(**i).model_dump() for i in res.json()]
        return vehicles
    else:
        raise Exception('Error retreiving data of active vehicles', res.text)
    

def resolve_color_codes(label_ids: list) -> dict:
    '''
    Fetch colorCodes of given label_ids.
    It requires a valid access_token, if not present or expired it will try to fetch new access_token
    '''
    global access_token, expires_at
    if access_token is None or datetime.now().timestamp() >= expires_at:
        get_token()
    print('label_ids:', label_ids)
    base_url = os.environ.get('BAUBUDDY_URL')
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    label_map = {}
    for label_id in label_ids:
        res = requests.get(urljoin(base_url, f'dev/index.php/v1/labels/{label_id}'), headers=headers)
        if res.ok:
            body = LabelModel(**res.json()[0])
            label_map[label_id] = body.colorCode
        else:
            print(f'Error retreiving colorCode of labelId {label_id}')
            print(res.text)
    return label_map