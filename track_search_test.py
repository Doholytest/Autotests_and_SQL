import sender_stand_request
import data


def create_order_track():     # Создаем заказ и вытаскиваем номер заказа
    order = sender_stand_request.create_order_url(data.order_body)
    return order.json()["track"]


track = create_order_track()     # Присвоил переменной результат функции для собственного удобства


def test_search_order_track():        # Сам тест test
    result_body = sender_stand_request.search_order_url(track)            # Сохранил в переменной результат поиска по ранее вытащенному номеру заказа
    assert result_body.status_code == 200       # Проверяем, что статус 200

 # Пирожков Артём, 9-й поток - Финальный проект. Инженер по тестированию плюс