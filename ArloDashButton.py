import os
import boto3

from pyarlo import PyArlo

def lambda_handler(event, context):

    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']
    PRIMARY_CONTACT = os.environ['PRIMARY_CONTACT']
    SECONDARY_CONTACT = os.environ['SECONDARY_CONTACT']

    arlo = PyArlo(USERNAME, PASSWORD)

    if event['clickType'] == "DOUBLE":
        base.mode = 'disarmed'
    else:
        base.mode = 'armed'

   batt_levels = base.get_camera_battery_level
