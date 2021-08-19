print("1")

def mail(incidient):
    if incidient == 1:
        return "Shart"
    elif incidient == 2:
        return "mailbox"
    else: 
        return "home delivery in master bath"
    
body_function = mail(1)

print(body_function)

body_function = mail(2)
print(body_function)

print(mail("gage"))

