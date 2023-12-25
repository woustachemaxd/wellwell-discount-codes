import requests
import random
import time
import re
import json
import string
import uuid


def generate_random_string(length=10, characters=string.ascii_letters + string.digits):
    return ''.join(random.choice(characters) for _ in range(length))


def generate_random_email():
    # Replace this with your logic to generate random emails
    domains = ["gmail.com", "yahoo.com", "test.com"]
    return f"{generate_random_string()}@{random.choice(domains)}"


def getCode(response_data):
    json_data_match = re.search(r'\{.*\}', response_data, re.DOTALL)
    if json_data_match:
        json_data = json_data_match.group(0)
        parsed_data = json.loads(json_data)
        code_value = parsed_data['Data']['code']
        return code_value
    else:
        return "######"


# def generate_custom_uuid():
#     # Generate a random UUID
#     random_uuid = uuid.uuid4()
#     formatted_uuid = f"{random_uuid.hex[:8]}-1d7b-08dbcee64ca4"
#     return formatted_uuid


def generate_three_digit_number():
    return random.randint(100, 999)


while True:
    name = generate_random_string()
    email = generate_random_email()
    uid = generate_three_digit_number()
    uuid = "0ae01d83-ecd7-41f1-1d7d-08dbcee64ca4"
    api_url = f"https://dashboard.wheelio-app.com/api/wheelioapp/generatecode?jsonp=WheelioAppJSONPCallback913&d=shop-wellwell.myshopify.com&c=6219e1ec-6abb-4fb2-74a6-08dbcee64c90&co={uuid}&uid={uid}&name={name}&email={email}"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "cross-site",
        "Referer": "https://shopwellwell.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    response = requests.get(api_url, headers=headers)
    print(getCode(response.text))
    with open("test.txt", "a") as f:
        f.write(response.text)
    with open("codes.txt", "a") as f:
        f.write(getCode(response.text) + '\n')
    time.sleep(1)
