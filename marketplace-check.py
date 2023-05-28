import requests
import warnings
import smtplib
import time

warnings.filterwarnings("ignore")


def emailSender(message):
    gmail_user = ''
    gmail_password = ''

    sent_from = gmail_user
    to = ['jon@gmail.com']
    subject = message
    body = message

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)


try:
    response = requests.get("", verify=False)
    #response = requests.get("https://www.patreon.com/sheldonevans", verify=False)
    print(response)

    responseString = response.text
    print(responseString)
    # f = open("new1.txt", "x")
    # f.write(responseString)

    time.sleep(5)

#     if("Capitalist Sold Out".lower() not in responseString.lower()):
#         #print("Sold Out")
#         message = "Capitalist Available"
#         #emailSender(message)
# except Exception as e:
#     #print("Exception occurred")
#     message = str(e)
#     emailSender(message)


    # if(responseString.lower().count('patron_amount_cents') > 4):
    #     #print("Sold Out")
    #     message = "New Tier Available"
    #     print('Number of occurrence', responseString.lower().count('patron_amount_cents'))
    #     emailSender(message)
except Exception as e:
    print("Exception occurred")
#     message = str(e)
#     emailSender(message)

#print('Number of occurrence', responseString.lower().count('patron_amount_cents'))




        #jsonResponse = json.loads(response.te

