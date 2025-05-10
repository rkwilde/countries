from dotenv import load_dotenv
import os
import requests
import logging
import snowflake.connector
import json

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # set here instead of basicConfig to not override logging level cutoffs in dependencies

load_dotenv()

URL = 'https://restcountries.com/v3.1/all'
FILENAME = 'countries.json'

def make_request(url, retries=3):
    logger.info('allow 3 tries to hit API')
    for i in range(retries):
        try:
            req = requests.get(URL)
            if req.status_code == 200:
                return req
        except requests.exceptions.RequestException as e:
            logger.debug(f"exception during api request (attempt {i}): {str(e)}")
            if i == retries-1:
                raise e

def save_result_as_file(result, filename):
    logger.info('save API result as file')
    txt = ''
    for line in result:
        txt += json.dumps(line) + '\n'
    try:
        with open(filename, "w") as f:
            f.write(txt)
    except OSError as e:
        raise e

def upload_to_snowflake(request_result, db='aptive', schema='raw', tbl='countries'):
    logger.info('upload to database')
    logger.debug('connect to database')
    conn = snowflake.connector.connect(
        account = os.getenv('SNOWFLAKE_ACCOUNT'),
        user = os.getenv('SNOWFLAKE_USER'),
        password = os.getenv('SNOWFLAKE_TOKEN')
    )
    cs = conn.cursor()
    logger.debug('create table if necessary and truncate anything already there')
    cs.execute(f'create table if not exists {db}.{schema}.{tbl} (raw variant)')
    cs.execute(f'truncate table {db}.{schema}.{tbl}')
    logger.debug('stage and copy')
    cs.execute(f'put file:///{os.getcwd()}\\{FILENAME} @{db}.{schema}.%{tbl}')
    cs.execute(f'copy into {db}.{schema}.{tbl} from @{db}.{schema}.%{tbl} file_format=(type=json) purge=true')
    # catch errors... no time now

if __name__ == '__main__':
    try:
        r = make_request(URL)
        save_result_as_file(r.json(), FILENAME)
        upload_to_snowflake(FILENAME)
    except requests.exceptions.Timeout as e:
        logger.error(f"API call timed out")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Could not connect to API")
    except requests.exceptions.RequestException as e:
        logger.error(f"Last call attempt to API failed: {str(e)}")
    except OSError as e:
        logger.error(f"Could not save API results to file: {str(e)}")
