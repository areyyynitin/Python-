emails = [
"alice@example.com",
"bob@sample.org",
"charlie@mydomain.net"
]

for email in emails:
    print(email.split('@')[0] , " " , email.split('@')[1])
