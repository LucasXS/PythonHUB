import socket as s

#host = "upsites.digital"
host = str(input("Site: "))
print(f'SITE: {host}\nIP: {s.gethostbyname(host)}')