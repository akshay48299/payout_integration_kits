#  Cashfree Python Integration 

Python bindings for interacting with the Cashfree API. This is useful for merchants who are looking to automate their bank transfers programatically. 

# Using 

As you can see there are two files. "Execute.py" is a guide to calling the API.
NOTE : Ensure that "execute.py" and "cfPayout.py" are in the same folder.

# Setting Up

You will need to authenticate client by calling the clientAuth function as follows : 

```python
from cfPayout import cashfreeUser

user1 = cashfreeUser()
user1.clientAuth('dummyClientId','dummyClientSecret',"TEST/PROD"

```

# Functionality

You can perform the following functions : 

**Add Beneficiary**

```
user1.addBeneficiary('JOHN180121','john doe', 'johndoe@cashfree.com', '9876543210','00091111202233','HDFC0000001','vpa','ABC Street','add 2','Bangalore', 'Karnataka','560001' )
```

**Request Transfer**
```
user1.requestTransfer('JOHN18011','100','76723288672267867867','banktransfer','optional')
```
**Get Transfer Status**

```
user1.getTransferStatus('76723288672267867867')
```
**Validate Bank Details**

```
user1.bankDetailsValidation("Joh",'9910115208', '00011020001772', 'HDFC0000001')
```

**Check Balance**

```
user1.getBalance()
```


