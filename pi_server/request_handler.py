import requests

class request_handler_:

    def get_sync(self, get_sync_url):
        PARAMS = {}
        r = requests.get(url = get_sync_url, params = PARAMS)
        # data = r.json()
        # if 1st crisis is true, trigger light to change and make noise and set it to 1st stage mode
        # object.set_first_warning
        # print(data)

    # def get_request(self):
    #     PARAMS = {}
    #     r = requests.get(url = self.api_endpoint, params = PARAMS)
    #     data = r.json()
    #     # set data members based on what r.json() returns
    #     print(data)

    def post_sync(self, post_sync_url):
        DATA = {"is_home" : self.is_home}
        r = requests.post(url = post_sync_url, data = DATA)
