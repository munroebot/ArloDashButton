from arlo.Arlo import Arlo
import os
import boto3

def lambda_handler(event, context):

    USERNAME = os.environ['username']
    PASSWORD = os.environ['password']
    PRIMARY_CONTACT = os.environ['PRIMARY_CONTACT']
    SECONDARY_CONTACT = os.environ['SECONDARY_CONTACT']
   
    message = None

    arlo = Arlo(USERNAME, PASSWORD)
    basestation = [ device for device in arlo.GetDevices() if device['deviceType'] == 'basestation' ]

    if event['clickType'] == "DOUBLE":
	    arlo.Disarm(basestation[0]['deviceId'], basestation[0]['xCloudId'])
        message = "Arlo Cameras DISABLED"
    else:
        arlo.Arm(basestation[0]['deviceId'], basestation[0]['xCloudId'])
        message = "Arlo Cameras ENABLED"

    sns_client = boto3.client('sns')
    sns_client.publish(PhoneNumber=PRIMARY_CONTACT,Message=message)
    sns_client.publish(PhoneNumber=SECONDARY_CONTACT,Message=message)
