import  re



#Email address Validation
pattern= '([a-z 0-9_.+-]+@[a-z 0-9]+\.[a-z 0-9 -.]+)'
user_id=input('Enter the email id : ')
if re.search(pattern, user_id):
    print("The email is valid....")
    
else: 
    print('invalid')
