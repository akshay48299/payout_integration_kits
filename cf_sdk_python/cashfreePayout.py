# -*- coding: utf-8 -*-

import warnings
import json
import time
import requests


class cashfreeUser:

    token = None
    
    clientId = None
    clientSecret = None
    stage = None
    expiry = None 

    def clientAuth(self, clientId, clientSecret, stage):

        cashfreeUser.clientId = clientId
        cashfreeUser.clientSecret = clientSecret
        cashfreeUser.stage = stage
        linkAuthorize = ""
        if (cashfreeUser.stage == "TEST"):
            linkAuthorize = "https://payout­-gamma.cashfree.com//payout/v1/authorize"
        elif (cashfreeUser.stage == "PROD"):
            linkAuthorize = "https://payout­-api.cashfree.com//payout/v1/authorize"

        headers = {
        'X-Client-Id' : clientId,
        'X-Client-Secret' : clientSecret 
        }
        try:
            jsonData = requests.post(url = linkAuthorize, headers = headers)
            jsonData = json.loads(jsonData.text)
            cashfreeUser.token = jsonData["data"]["token"]
            cashfreeUser.expiry = jsonData["data"]["expiry"]

            return cashfreeUser.token
        except:
            return "Empty JSON response"

    def expiryCheck(self):

        currenttime = int(time.time())
        expirytime = int(cashfreeUser.expiry)

        #makes check for if the token expires within the next minute and generates a new one 
        if (currenttime - expirytime < 60):

            temp = cashfreeUser()
            return temp.clientAuth(cashfreeUser.clientId,cashfreeUser.clientSecret,cashfreeUser.stage)
        else:
            return None

    def addBeneficiary(self,beneId, name, email, phone, bankAccount, ifsc, address1,address2,vpa, city, state, pincode):

        if ((beneId == None) or (name == None) or (email == None) or ( phone == None) or ( address1 == None)):
            return "Mandatory parameters missing" 
        else : 
            userParam = {   
                "beneId" : beneId,
                "name" : name,
                "email" : email ,
                "phone" : phone,
                "bankAccount" : bankAccount, #optional
                "ifsc" : ifsc, #ptional
                "vpa" : vpa,
                "address1" : address1,               
                "address2" : address2, #//optional
                "city" : city, #//optional
                "state" : state, #//optional
                "pincode" : pincode #//optional
            }

            temp = cashfreeUser()
            temp.expiryCheck()


            if (cashfreeUser.stage == "TEST"):
                linkAddBeneficiary  = "https://payout­-gamma.cashfree.com/payout/v1/addBeneficiary"
            
            elif (cashfreeUser.stage == "PROD"):
                linkAddBeneficiary  = "https://payout­-api.cashfree.com/payout/v1/addBeneficiary"

            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " +  str(cashfreeUser.token)
            }
            try : 
                jsonData = requests.post(url = linkAddBeneficiary, headers = headers, data = json.dumps(userParam))
                jsonData = json.loads(jsonData.text)

                return jsonData
            
            except:
                return "Empty JSON response"

    def getBalance(self):

        headers = {
        'Authorization' : "Bearer " + str(cashfreeUser.token)
        }

        temp = cashfreeUser()
        temp.expiryCheck()

        if (cashfreeUser.stage == "TEST"):
            linkAddBeneficiary  = "https://payout-gamma.cashfree.com/payout/v1/getBalance"
        elif (cashfreeUser.stage == "PROD"):
            linkAddBeneficiary  = "https://payout-api.cashfree.com/payout/v1/getBalance"
        
        try:
            jsonData = requests.get(url = linkAddBeneficiary, headers = headers)
            jsonData = json.loads(jsonData.text)

            return jsonData
        except:
            return "Empty JSON response"
    
    def requestTransfer(self,beneId, amount, transferId, transferMode, remarks):
        
        if ((beneId == None) or (amount == None) or (transferId == None)):
            return "Mandatory parameters missing" 
        
        else : 

            userRequestParam = {
                "beneId" : beneId,
                "amount" : amount, 
                "transferId" : transferId,
                "transferMode" : transferMode, #//optional
                "remarks" : remarks# //optional
            }

            temp = cashfreeUser()
            temp.expiryCheck()

            if (cashfreeUser.stage == "TEST"):
                linkRequestTransfer = "https://payout-gamma.cashfree.com/payout/v1/requestTransfer"
            elif (cashfreeUser.stage == "PROD"):
                linkRequestTransfer = "https://payout-api.cashfree.com/payout/v1/requestTransfer"

            headers = {
                'Authorization': "Bearer " +  str(cashfreeUser.token)
            }
            try:
                jsonData = requests.post(url = linkRequestTransfer, headers = headers, data = json.dumps(userRequestParam))
                
                jsonData = json.loads(jsonData.text)
                return jsonData

            except:
                return "Empty JSON response"

    def getTransferStatus(self, transferId):

        if transferId == None :
            return "Mandatory parameters missing"
        else :

            temp = cashfreeUser()
            temp.expiryCheck()
            
            if (cashfreeUser.stage == "TEST"):
                linkTransferStatus = "https://payout-gamma.cashfree.com/payout/v1/getTransferStatus" + "?transferId="+ transferId
            elif (cashfreeUser.stage == "PROD"):
                linkTransferStatus = "https://payout-api.cashfree.com/payout/v1/getTransferStatus" + "?transferId="+transferId  

            headers = {
                'Authorization': "Bearer " +  str(cashfreeUser.token),
                'transferId' : str(transferId)
            }              

            try:
                jsonData = requests.get(url = linkTransferStatus, headers = headers)

                jsonData = json.loads(jsonData.text)
                return jsonData
            except:
                return "Empty JSON response"

    def bankDetailsValidation(self, name, phone, bankAccount,  ifsc):

        if ((name == None) or (phone == None) or (bankAccount == None) or (ifsc == None)):
            return "Mandatory parameters missing" 
        
        else : 

            temp = cashfreeUser()
            temp.expiryCheck()
            
            if (cashfreeUser.stage == "TEST"):
                linkBankValidation = "https://payout-gamma.cashfree.com/payout/v1/validation/bankDetails" + "?name=" + name + "&phone=" + phone + "&bankAccount=" + bankAccount + "&ifsc=" + ifsc
            elif (cashfreeUser.stage == "PROD"):
                linkBankValidation = "https://payout-api.cashfree.com/payout/v1/validation/bankDetails" + "?name=" + name + "&phone=" + phone + "&bankAccount=" + bankAccount + "&ifsc=" + ifsc
            headers = {
                'Authorization': "Bearer " +  str(cashfreeUser.token),
                'name' : name,
                'phone' : phone,
                'bankAccount' : bankAccount,
                'ifsc' : ifsc
            }
            try : 
                jsonData = requests.get(url = linkBankValidation, headers = headers)

                jsonData = json.loads(jsonData.text)
                return jsonData
            except:
                return "Empty JSON response"

