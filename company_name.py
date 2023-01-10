# Email = "naveen@datagrokr.com"
Email = str(input("enter your Email "))

domain_name = Email.split('@')[1]
Company_name = domain_name.split('.')[0]

print(Company_name)
