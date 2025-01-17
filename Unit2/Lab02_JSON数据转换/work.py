import json

sample_data =  {
        "portId": "1",
        "enabled": True,
        "status": "Connected",
        "isUplink": False,
        "errors": [
            "PoE overload",
            "Very high proportion of CRC errors"
        ],
        "warnings": [
            "SecurePort authentication in progress",
            "PoE port was denied power",
            "High proportion of CRC errors"
        ],
        "speed": "10 Gbps",
        "duplex": "full",
        "usageInKb": {
            "total": 40867,
            "sent": 23008,
            "recv": 17859
        },
        "cdp": {
            "systemName": "",
            "platform": "MS350-24X",
            "deviceId": "0c8ddbddee:ff",
            "portId": "Port 20",
            "nativeVlan": 1,
            "address": "10.0,0.1",
            "managementAddress": "10.0.0.100",
            "version": "1",
            "vtpManagementDomain": "",
            "capabilities": "Switch"
        },
        "lldp": {
            "systemName": "MS350-24X - Test",
            "systemDescription": "MS350-24X Cloud Managed PoE Switch",
            "chassisId": "0c:8d:db:dd:ee:ff",
            "portId": "20",
            "managementVlan": 1,
            "portVlan": 1,
            "managementAddress": "10.0.0.100",
            "portDescription": "Port 20",
            "systemCapabilities": "switch"
        },
        "clientCount": 10,
        "powerUsageInWh": 55.9,
        "trafficInKbps": {
            "total": 2.2,
            "sent": 1.2,
            "recv": 1
        },
        "securePort": {
            "enabled": True,
            "active": True,
            "authenticationStatus": "Authentication in progress",
            "configOverrides": {
                "type": "trunk",
                "vlan": 12,
                "voiceVlan": 34,
                "allowedVlans": "all"
            }
        }
    }
    
#Task1. 将上面的sample_data用json库保存为data.json文件（数据序列化）



#Task2. 将client.json文件转换为Python字典，保存在client变量中并print出来（数据反序列化）



