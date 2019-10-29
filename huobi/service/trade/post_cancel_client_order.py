from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *



class PostCancelClientOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/order/orders/submitCancelClientOrder"

        def parse(dict_data):
            return dict_data.get("data", -2)  # order cancel status

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)





