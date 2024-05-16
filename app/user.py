import json
import http.client


class Users:
    def __init__(self, app_url):
        """
        Initiates user class for CRUD Operations 
        Params : 
            app_url (str) : URL for the Auth0 app            
        """
        self.app_url = app_url
        self.user_end_point = "/api/v2/users"
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
        payload = "{\"client_id\":\"fbqGGrziNaGSMCkvZMrqIuZSElJXMTLS\",\"client_secret\":\"kpnG5fZJmuxJhNL7gYRCrfHua_cUC490wPifhwS3s1fgGIdjyu4hH11d5CKJjtbf\",\"audience\":\"https://dev-vv275rnobnn6sb2u.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"
        headers = { 'content-type': "application/json" }
        conn.request("POST", "/oauth/token", payload, headers)
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

user_factory = Users("dev-vv275rnobnn6sb2u.us.auth0.com")
