import os 
import json
import http.client


class Users:
    def __init__(self, app_url, client_id, client_secret):
        """
        Initiates user class for CRUD Operations 
        Params : 
            app_url (str) : URL for the Auth0 app            
        """
        self.app_url = app_url
        self.user_end_point = "/api/v2/users"
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self.get_token()
        self.headers = { 
                    'authorization': "Bearer "+ self.token,
                    'Content-Type': 'application/json' ,
                    'Accept': 'application/json' 
                    }


    def get_token(self):
        """
        Gets the auth0 token using app credentials.
        """
        conn = http.client.HTTPSConnection(self.app_url)
        payload = {
                    "grant_type" : "client_credentials",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "audience":"https://dev-vv275rnobnn6sb2u.us.auth0.com/api/v2/"
                }
        headers = { 'content-type': "application/json" }
        conn.request("POST", "/oauth/token", json.dumps(payload), headers)
        res = conn.getresponse()
        data = res.read()
        token = data = json.loads((data.decode("utf-8")))["access_token"]
        return token

    def get_user(self, id):
        """
        Retrieves a user from Auth0 DB
        Params:
            id (str) : user id (Required)
        """
        conn = http.client.HTTPSConnection(self.app_url)
        url = self.user_end_point + '/'+ id
        conn.request("GET", url, headers=self.headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

    def create_user(self, user_json):
        """
        Create a new user in Auth0 DB
        Params:
            user_json (dict) : json payload contains all the 
                               details to create a user (Required)
        """
        conn = http.client.HTTPSConnection(self.app_url)
        conn.request("POST", self.user_end_point, headers=self.headers, body = json.dumps(user_json))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

    def delete_user(self, id):
        """
        Delete a user in Auth0 DB
        Params:
            id (str) : id of the to be delete
        """
        conn = http.client.HTTPSConnection(self.app_url)
        conn.request("DELETE", self.user_end_point + "/" + id, headers=self.headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

    def update_user(self, id, user_json):
        """
        Update a user in Auth0 DB
        Params:
            id (str) : id of the to be updated
            user_json (dict) : json payload of updated details of user
        """
        conn = http.client.HTTPSConnection(self.app_url)
        conn.request("PATCH", self.user_end_point + "/" + id, headers=self.headers, body=json.dumps(user_json) )
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")


app_url = os.environ["APP_URL"]
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

user_factory = Users("dev-vv275rnobnn6sb2u.us.auth0.com", client_id, client_secret)
print(user_factory.get_user("auth0|6645bcd44e4cb5859ff4b06c"))