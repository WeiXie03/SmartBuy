"""
script to download Noteb's database of laptop models, as JSON
"""
import requests, json
from pprint_db import pprint
import os

def savef_list_info(req_data, datf_path, noteb_url):
    '''
    gets and saves Noteb list of models as a JSON, uses Noteb's list_models method to easily get all laptops in database, so only contains model id, names, thumbnails, links, etc. but no specs
    resp: the HTTP response object
    datf_path: the path of the file to save to relative to this script
    '''
    with open(datf_path, 'w') as dataf:
        # get JSON response from POST request to Noteb
        req_data["method"] = "list_models"
        resp = requests.post(noteb_url, data=req_data)
        # for dry running, to test for endless loops
        #resp = {"name": "Asus ROG Zephyrus Duo 15 GX550"}

        # ignore headers
        sav_data = resp.json()["result"]
        json.dump(sav_data, dataf)
    print("saved to file ", datf_path)

def list_to_full_db(sav_path, src_path, noteb_url, req_data, max_models=10):
    """ save Noteb get_model_info response for each model_id
    """

    #with open(datf_path, "r+") as dataf:
    # back up for now
    with open(src_path, "r") as srcf:
        src_data = json.load(srcf)
        req_data["method"] = "get_model_info"
        #print(req_data)

        full_data = {}
        # limit to max_models, don't have many requests
        for model_num in range(max_models):
            print(model_num)
            #print(src_data[model_num])

            # copy model_id from src data file
            req_data["param[model_id]"] = src_data[str(model_num)]["model_info"][0]["id"]
            model_info = requests.post(noteb_url, data=req_data)
            # dry run
            #model_info = {"name": "Asus ROG Zephyrus Duo 15 GX550"}

            #print(f"{model_num}: {model_info}")
            # just directly insert Noteb get_model_info response, except the headers
            full_data[model_num] = model_info.json()["result"]
            # dry run \/
            #full_data[model_num] = model_info

    # save new, complete data to separate new file
    with open(sav_path, "w") as savef:
        json.dump(full_data, savef)
    print("saved to file ", sav_path)

def DT_reformat_data(sav_path, src_path, max_models=10):
    """ fit full data to jQuery DataTables' requirement, using DataTables for browsing, searching, filtering on main page
    """
    with open(src_path, "r") as srcf:
        src_data = json.load(srcf)

        # jQuery DataTables (library) requires everything to be in array mapped from "data"
        reformed_data = {"data": []}
        # limit to max_models
        for model_num in range(max_models):
            #print(model_num)
            print(src_data[str(model_num)].keys())
            # just throw original data in except without all the model numbers
            temp_i = next(iter(src_data[str(model_num)]))
            reformed_data["data"].append(src_data[str(model_num)][temp_i])

    # save new, reformatted data to separate new file
    with open(sav_path, "w") as savef:
        json.dump(reformed_data, savef)
    print("saved to file ", sav_path)

if __name__ == "__main__":
    NOTEB_URL = "https://noteb.com/api/webservice.php"
    API_KEY_PATH = os.path.join("..", "noteb_APIkey.txt")
    with open (API_KEY_PATH, 'r') as apikey_f:
        api_key = apikey_f.read()

    # TODO: command line args
    # first had list_models data
    INTER_DATAF_PATH = os.path.join("..", "data","full_data.json")
    DATAF_PATH = os.path.join("..", "data","DT_data.json")
    # first stage \/
    #INTER_DATAF_PATH = os.path.join("data","data.json")
    #DATAF_PATH = os.path.join("data","full_data.json")

    # POST HTTP request to get model info with filtering, must be in "form-data form"
    req_data = {
        "apikey": api_key,
        "method": "",
        "param[model_id]": "",
        "param[model_name]": ""
    }

    # tried to loop through all model_ids, assumed every number assigned, but list_models method easier
    '''
    for m_id in range(250, 301):
        req_data["param[model_id]"] = m_id
    '''

    #savef_list_info(req_data, DATF_PATH, 30)
    #list_to_full_db(DATAF_PATH, INTER_DATAF_PATH, NOTEB_URL, req_data, 30)
    DT_reformat_data(DATAF_PATH, INTER_DATAF_PATH, 30)
