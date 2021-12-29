from csv import writer
import pandas as pd

print("Compose email [1] or view mail? [2]")
decision = input()
decision = int(decision)

if decision == 1:
    print("What would you like to send to your local network?")
    msg = input()
    with open('messages.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(msg)
        f_object.close()

elif decision == 2:
    mail = pd.read_csv("messages.csv", sep='\t')
    mail = mail.apply(lambda x: x.str.replace(',', ''))
    print(mail)
    
    
    
