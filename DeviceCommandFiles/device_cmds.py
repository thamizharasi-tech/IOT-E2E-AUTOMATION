from openpyxl import load_workbook
import subprocess
import json
import time

from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel



excel_path = r"C:\C2Cloud_U2Testing\C2TestData\API_testData.xlsx"

wb = load_workbook(excel_path)

# -------- Read Config --------
config_sheet = wb["Device_Config"]
config = {}

for row in config_sheet.iter_rows(min_row=2, values_only=True):
    key, value = row
    config[key] = value

adb_path = config["adb_path"]
paho_path = config["paho_path"]
ld_library = config["ld_library"]
host = config["host"]
port = config["port"]
base_topic = config["base_topic"]

# -------- Read Test Data --------
data_sheet = wb["VHAL_Data"]

for row in data_sheet.iter_rows(min_row=2, values_only=True):
    property_id, area, value, event_type = row

    if not property_id:
        continue

    payload = json.dumps([{
        "id": property_id,
        "area": area,
        "value": value
    }])

    topic = f"{base_topic}/{event_type}/VEHICLE"

    command = (
        f'{adb_path} shell '
        f'"export LD_LIBRARY_PATH={ld_library}; '
        f'{paho_path} -h {host} -p {port} '
        f'-t {topic} -m \'{payload}\'"'
    )

    print(f"Executing: {command}")
    subprocess.run(command, shell=True)

    time.sleep(1)