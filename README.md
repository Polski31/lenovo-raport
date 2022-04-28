# Raport-Lenovo-Scrap
Scrapping Machine Type Model with Serial Number

Script takes csv file with SN and with usage of LenovoAPI retrieves MTM. Results are stored in csv file and sended to mongoDB.

usage:
  main.py [-h] source destination

  * source       path to source csv file with SN(s)
  * destination  path to destination csv file with SN(s) and MTM(s)

  - in db directory create .env file containing:
    - MONGO_URI=[connection_string]
    - DB_NAME=[database_name]
    - COLLECTION_NAME=[collection_name]

Packages:
  - python-dotenv
  - requests
  - pymongo
  - dnspython
