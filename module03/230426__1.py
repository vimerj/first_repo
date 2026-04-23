response = {
    "status": 200,
    "data": {"username": "ivime"}
}
try:
    phone_number = response["data"]["phone_number"]
except:
    phone_number = None
    pass

print("Here is the phone number:", phone_number)