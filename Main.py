import  re



#Email address Validation
pattern= '^[a-z 0-9]+[\._}?[a-z 0-9]+[@]\w+[.]\w{2,3}+[.]\w{2}$'
user_id=input('Enter the email id : ')
if re.search(pattern,user_id):
    print("The email is valid....")
    
else: 
    print('invalid')
