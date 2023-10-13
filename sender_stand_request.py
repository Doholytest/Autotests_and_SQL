import configuration
import requests
import data

def create_order_url(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body,  # передаем тело
                         headers=data.headers)  # передаем заголовки


def search_order_url(number):
    return requests.get(configuration.URL_SERVICE + configuration.SEARCH_ORDER_PATH,  # подставляем полный url
                        params={"t": number})            #передаем параметр