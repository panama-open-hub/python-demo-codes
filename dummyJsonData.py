import json

class dummyJsonData():
    def addData(self):
        _data = [
            {
                "id": 1,
                "username": "admin",
                "email": "admin@admin.com",
                "password": 1234
            },
            {
                "id": 2,
                "username": "developer",
                "email": "devops@gmail.com",
                "password": 5678
            }
            ]
        return _data
    def tableNames(self):
        tns = ['cards', 'devices', 'members', 'readings', 'records', 'io']
        return tns
        
    def addmembersJson(self):
        membersJson = [
            {
                #"MemberId": 1,
                "FirstName": "Pablo",
                "LastName": "Gonzalez",
                "Phone": 66865816,
                "Email": "p.gonzalez7027@gmail.com",
                "Country":"Panama",
                "City":"Chitre",
                "UserName":"pangoro24",
                "Deleted": 0,
                "Password":"123456",
                "Created_at":"17/10/2019 15:30:16",
                "Updated_at":"17/10/2019 15:30:16"
            },
            {
                #"MemberId": 2,
                "FirstName": "Jorge",
                "LastName": "Fadul",
                "Phone": 65014655,
                "Email": "jorgeluisfadul@gmail.com",
                "Country":"Panama",
                "City":"Chitre",
                "UserName":"JorgeFadul",
                "Deleted": 0,
                "Password":"161098",
                "Created_at":"22/10/2019 15:16:00",
                "Updated_at":"22/10/2019 15:16:00",
            },
            {
                #"MemberId": 3,
                "FirstName": "Andres",
                "LastName": "Escribano",
                "Phone": 67879073,
                "Email": "andres1900escribanos@gmail.com",
                "Country":"Panama",
                "City":"Chitre",
                "UserName":"andres18-gb",
                "Deleted": 0,
                "Password":"181102",
                "Created_at":"17/10/2019 15:20:00",
                "Updated_at":"17/10/2019 15:20:00"
            }
            ]
        return membersJson
    
    def addcardsJson(self):
        cardsJson = [
            {
                "CardId":1,
                "Tag": 589468108090,
                "Texto":"pangoro24",
                "MemberId": 1,
            },
            {
                "CardId":2,
                "Tag": 955087023985,
                "Texto":"JorgeFadul",
                "MemberId": 2,
            },
            {
                "CardId":3,
                "Tag": 22179825260,
                "Texto":"andres18-gb",
                "MemberId": 3,
            }
            ]
        return cardsJson
  
    def addrecordsJson(self):
        recordsJson = [
            {
                "RecordId": 1,
                "DeviceId": 1,
                "GetIn": "22/10/2019  14:00 ",
                "Leave": "22/10/2019  16:00",
                "MemberId" : 1,
            },
            {
                "RecordId": 2,
                "DeviceId": 1,
                "GetIn": "22/10/2019  14:08 ",
                "Leave": "22/10/2019  16:00",
                "MemberId" : 2
            },
            {
                "RecordId": 3,
                "DeviceId": 1,
                "GetIn": "22/10/2019  14:05 ",
                "Leave": "22/10/2019  16:00",
                "MemberId" : 3,
            }
            ]
        return recordsJson

    def adddevicesJson(self):
        devicesJson = [
            {
                "DeviceId":1,
                "Name":"CheckStation1",
                "Status":"ON",
                "Location":"Puerta Trasera",
                "Version": 1.1,
                "Created_at":"17/10/2019 15:04:00",
                "Updated_at":"17/10/2019 15:04:00"
            }
            ]
        return devicesJson

    def addreadingsJson(self):
        readingsJson = [
            {
                #"ReadingId": 1,
                "SensorId": 1,
                "Value1" : 32.5,
                "Value2" : 95,
                "Value3" : 0.0,
                "Reading_at" :"22/10/2019 18:00:00" 
            }
            ]
        return readingsJson
            
    def addioJson(self):
        ioJson = [
            {
                #"IoId": 1,
                "Name": "DHT22",
                "Status": "ON",
                "DeviceId": 1,
            },
            {
                #"IoId": 2,
                "Name": "LED Rojo",
                "Status": "ON",
                "DeviceId": 1,
            }
            ]
        return ioJson






