"""
Connector script for the Watson IBM IoT platform
"""

import ibmiotf.device

class ibmiotconnector():
    def __init__(self):

        # For ibm IoT Platform
        orgId = "9fc2hw"
        deviceType = "Accelerometer"
        deviceId = "0"
        authMethod = "token"
        authToken = "!F5drbvs+a5+9biuB0"
        try:
            options = {
                "org": orgId,
                "type": deviceType,
                "id": deviceId,
                "auth-method": authMethod,
                "auth-token": authToken,
                "clean-session": True
            }
            self.client = ibmiotf.device.Client(options)
            self.client.connect()
        except ibmiotf.ConnectionException  as e:
            print("failure in connecting to IBM IoT Platform!")
            print(e)
            quit()

    def sendData(self, myData):
        "sends structured data to the ibm iot backend"
        print("sending data")
        # publishevent(type, id, ...)
        self.client.publishEvent("status", "json", myData)
