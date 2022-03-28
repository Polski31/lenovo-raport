import requests
import json
import product

api_url = "https://pcsupport.lenovo.com/pl/en/api/v4/upsell/redport/getIbaseInfo"
headers = {"Content-Type": "application/json"}
request_body = {"serialNumber": "",
                "machineType": "",
                "country": "pl",
                "language": "en"}


def get_base_info(product_to_search: product.Product):
    request_body["serialNumber"] = product_to_search.serial_number
    response = requests.post(api_url, data=json.dumps(request_body), headers=headers)
    return response.json()


def get_machine_type_model(base_info):
    if base_info["msg"]["desc"] == "Success":
        return base_info["data"]["machineInfo"]["product"]
    else:
        return "NOT FOUND"
