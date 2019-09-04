import json
import requests
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
import os

def main():

    # open conection with mongodb service
    client = MongoClient('mongodb://mongo', 27017)
    # set the database where we are working on, if it doesnt exist creates it
    db = client['gps_dtpm']
    # set the collection we are working on, if it doesnt exist creates it
    collection_waze = db['pos']

    # read the json file from the API
    web_s_url = os.getenv('web_s_url')
    web_s_r = requests.get(dict_tramos_url ,auth=(os.getenv('web_s_user'), os.getenv('web_s_pass')))
    web_s_r.encoding = 'latin-1'
    json_data = json.loads(web_s.text)

    # creates or overwrites a file with the latest api response
    """
    for some reason if you put this after inserting the document 
    to the collection it fails
    """
    with open('json-file/latests_pos.json', 'w') as latests_pos:  
        json.dump(json_data, latests_pos)

    # add the file as a new document to the collection
    collection_waze.insert_one(json_data) 

    # close the connection with mongo
    client.close()

if __name__ == '__main__':
    # makes it so the function keeps repeating every 300 seconds
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'interval', seconds=60)
    scheduler.start()