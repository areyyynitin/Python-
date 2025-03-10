users = [
    {"name": "Rishi", "email": "rishi@yahoo.com"},
    {"name": "Aman", "email": "aman@gmail.com"},
    {"name": "Himanshu", "email": "himanshu@gmail.com"},
    {"name": "Deep", "email": "deep@outlook.com"},
    {"name": "Darshan", "email": "darshan@yahoo.com"}
]


domain_users = {}


for user in users:
    name = user["name"]
    domain = user["email"].split("@")[1]  
    
    if domain not in domain_users:
        domain_users[domain] = []
    
    domain_users[domain].append(name)


print(domain_users)
