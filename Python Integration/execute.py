
from payment import cashfreeUser

user1 = cashfreeUser()
user1.clientAuth('CF27D9CZCLC0ZHYUE26','b4c83b231adae60400ce303361ecadeacc004916')
user1.expiryCheck()
user1.addBeneficiary('JOHN180121','john doe', 'johndoe@cashfree.com', '9876543210','00091111202233','HDFC0000001','vpa','ABC Street','add 2','Bangalore', 'Karnataka','560001' )
user1.requestTransfer('JOHN18011','100','76723288672267867867','banktransfer','optional')
user1.getTransferStatus('76723288672267867867')
user1.bankDetailsValidation("Joh",'9910115208', '00011020001772', 'HDFC0000001')
user1.getBalance()

