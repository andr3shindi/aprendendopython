from simple_salesforce import Salesforce

# Replace these variables with your Salesforce credentials
username = 'andre.miashiro@greenpeace.org.test'
password = 'kl^CnP4R#0SBV%'
security_token = '8pKXBozzFmxrcXvhXtk43ZkyL'

# Establish connection
sf = Salesforce(username=username, password=password, security_token=security_token, domain='test')

soql_query = "SELECT Id, Name FROM Contact LIMIT 2"

contacts = sf.query(soql_query)

for contact in contacts['records']:
    print(f"Id: {contact['Id']}, Name: {contact['Name']}")

#for contact in contacts


'''
# Replace '003XXXXXXXXXXXXXXX' with the actual Contact ID you want to retrieve
contact_id = '0035d00006tQs8eAAC'

# Retrieve the contact
contact = sf.Contact.get(contact_id)

# Print the retrieved contact details
print(contact)
'''
