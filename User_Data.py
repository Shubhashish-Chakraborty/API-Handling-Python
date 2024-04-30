import requests


def Fetch_UserData():

    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random" # Kaun se url se data le rhe / Kaun se URL se request ker rhe

    # Use Methods (Like : GET,POST...etc) With Request
    
    response = requests.get(url) #Say ek response aayi

    # Convert this response to JSON format, Which is our data

    DATA = response.json()


    # Checking if data has arrived on our request or not

    if (DATA["success"]) and ("data" in DATA):

        UserData = DATA["data"]

        UserName = UserData["login"]["username"]
        UserPassword = UserData["login"]["password"]
        UserCountry = UserData["location"]["country"]

        return {"USER_NAME": UserName , "USER_PASSWORD": UserPassword , "USER_COUNTRY": UserCountry}

        # return [UserName , UserPassword , UserCountry]
        # return UserName , UserPassword , UserCountry
        
    
    #Agar Data Nhi AArha

    else:

        raise Exception("Failed to fetch User Data!!")



def main():
    try:
        USER_DATA = Fetch_UserData() #Dictionary / JSON format
        print(USER_DATA)
        

    except Exception as e:

        print(str(e))


if __name__ == "__main__":

    main()