import argparse
import requests
from urllib.parse import urlencode
from collections import OrderedDict
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
PORT = os.environ.get('PORT', 5000)

parser = argparse.ArgumentParser(
                    prog='vehicleTest',
                    description='It is a CLI tool to connect with the merge API to retreive the information of cars',
                    epilog='Example usage: $ python3 client.py vehicles.csv --keys info,lagerort,labelIds -c')

parser.add_argument('filepath', help='Path to the csv file')
parser.add_argument('-k', '--keys', required=True, help='Names of the columns (if more than one column is specified it should be separated by comma e.g. --keys info,lagerort,labelIds)')
parser.add_argument('-c', '--colored', required=True, help='Set this field to colorize the texts of each row based on labelIds colorCode',
                    action='store_true')


def run():
  args = parser.parse_args()

  files=[
    ('file',('file',open(args.filepath,'rb')))
  ]
  url = f'http://localhost:{PORT}/merge-convert'

  query_string = urlencode(OrderedDict(colored=args.colored,columns=args.keys))
  url = url + '?' + query_string 

  res = requests.post(url, files=files, stream=True)
  res.raise_for_status()
  with open(f'vehicles_{datetime.now().date().isoformat()}.xlsx', 'wb') as file:
      for chunk in res.iter_content(chunk_size=512 * 1024): 
          if chunk: # filter out keep-alive new chunks
              file.write(chunk)
      file.close()

run()