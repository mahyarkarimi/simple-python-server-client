from typing import List, Optional
from fastapi import BackgroundTasks, FastAPI, UploadFile
import pandas as pd
from datetime import datetime, date
from baubuddy import active_vehicles, resolve_color_codes
import calendar
from fastapi.responses import FileResponse
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

for env in ['BAUBUDDY_URL', 'BAUBUDDY_AUTH', 'BAUBUDDY_USERNAME', 'BAUBUDDY_PASSWORD']:
    if os.environ.get(env) is None:
        raise Exception(f'{env} env variable does not exists')

PORT = os.environ.get('PORT', 5000)

def add_months(sourcedate: date, months: int) -> date:
    '''
    Adds x month to a given date and return the new created date object
    '''
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return date(year, month, day)


def colorize(s, highlight_by_label_ids: bool, label_color_map: dict):
    '''
    Change the highlight color of each row based on time difference of `hu` field with current time
    It also changes the text color of each row when the labelIds column has equivalent colorCode hex value
    '''
    hu = datetime.strptime(s.hu, '%Y-%m-%d')
    now = datetime.now().date()
    styles = []
    if add_months(hu, 3) > now:
        styles = ['background-color: #007500'] * len(s)
    elif add_months(hu, 12) > now:
        styles = ['background-color: #FFA500'] * len(s)
    else:
        styles = ['background-color: #b30000'] * len(s)

    if highlight_by_label_ids and s.labelIds is not None:
        label_ids = str(s.labelIds).split(',')
        for label_id in label_ids:
            color = label_color_map.get(label_id, '')
            if color.startswith('#'):
                styles = [s+'; text:'+color for s in styles]
                break
    return styles


def cleanup(path: str):
    '''
    Delete a file at given path
    '''
    os.remove(path)

@app.post('/merge-convert')
async def merge(file: UploadFile, colored: bool, columns : Optional[str], background_tasks: BackgroundTasks):
    uploaded = pd.read_csv(file.file, delimiter=';|,', engine='python')

    cols = ['rnr', 'hu', 'kurzname']
    if columns is not None and len(columns.split(',')) > 0:
        cols.extend(columns.split(','))

    df = pd.DataFrame(active_vehicles())

    df = df[df['rnr'].notnull()]
    uploaded = uploaded[uploaded['rnr'].notnull()]

    df = df.set_index(['rnr']).combine_first(uploaded.set_index(['rnr'])).reset_index()

    df = df[df['hu'].notnull()]
    df.sort_values(by='gruppe')
    
    export_name = f'/tmp/vehicles_{datetime.now().isoformat()}.xlsx'
    
    label_color_map = {}
    if colored:
        cols.append('labelIds')
        label_ids = df[df['labelIds'].notnull()]['labelIds'].to_list()
        label_color_map = resolve_color_codes(label_ids)
    df.style.apply(colorize, highlight_by_label_ids=colored, label_color_map=label_color_map, axis=1).to_excel(export_name, engine='openpyxl', index=False, columns=cols)
    background_tasks.add_task(cleanup, export_name)
    return FileResponse(export_name)
