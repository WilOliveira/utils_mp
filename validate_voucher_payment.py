# coding=utf-8
import requests
import time
import csv 
import datetime

processed = 0
access_token = 'insert ACCESS_TOKEN'
mkt =  'insert cust_mkt'
data = open('data.csv')

#Cust/external
list_ = csv.DictReader(data)


f= open("find_payment.csv","w+")
f.write('payments,amount,external,date_created'+"\r\n")

for item in list_:

	#print('https://api.mercadopago.com/v1/payments/search?access_token=' + access_token + '&marketplace=1022828159376640&description=Pagamento de voucher de desconto&collector.id='+item['Cust'] + '&external_reference='+item['external'])
	request_payment = requests.get('https://api.mercadopago.com/v1/payments/search?access_token=' + access_token + '&marketplace=' + mkt + '&description=Pagamento de voucher de desconto&status=approved&collector.id='+item['Cust'] + '&external_reference='+item['external'])
	payment_data = request_payment.json()


	for r in payment_data["results"]:
		line = str(r["id"])  + ","+  str(r['transaction_amount']) + ","+ r['external_reference'] + ","+ str(r['date_created'])
		#print(line)
		f.write(line+"\r\n")
	

	processed = processed +1

	print("Processado: " + str(processed) + " - "  + item['external'])
f.close() 


