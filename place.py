import requests
class Test_new_location():
    """Работа с новой локацией"""
    def test_create_new_location(self):
        """Создание новой локации"""
        base_url = "https://rahulshettyacademy.com" #базовый урл
        key = "?key=qaclick123" #Параметр для всех запросов

        """Создание новой локации"""
        post_resource = "/maps/api/place/add/json" #Ресурс метода post

        post_url = base_url+ post_resource + key
        print(post_url)
        json_for_create_new_location = {

            "location": {

                "lat": -38.383494,

                "lng": 33.427362

            }, "accuracy": 50,

            "name": "Frontline house",

            "phone_number": "(+91) 983 893 3937",

            "address": "29, side layout, cohen 09",

            "types": [

                "shoe park",

                "shop"

            ],

            "website": "http://google.com",

            "language": "French-IN"

        }
        result_post=requests.post(post_url,json=json_for_create_new_location)
        assert result_post.status_code==200,"Проверить статус код"
        print(result_post.text,result_post.status_code)
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Статус код ответа: " + check_info_post)
        assert  check_info_post == "OK",("Статус код не ОК")
        place_id = check_post.get("place_id")
        print(place_id)
        """Проверка создания новой локации"""


        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key +"&place_id="+place_id
        print(get_url)
        result_get=requests.get(get_url)
        print(result_get.text)
        assert 200 == result_get.status_code,("Статус код не 200 a:"+str(result_get.status_code))
        print(str(result_get.status_code)+", проверка создания новой лоакции прошла успешно")
        """Изменения новой локации"""

        put_resource = "/maps/api/place/update/json"
        put_url= base_url+put_resource+key
        print(put_url)
        json_for_update_new_location ={
            "place_id":place_id,

            "address":"100 Lenina street, RU",

            "key":"qaclick123"
        }
        result_put=requests.put(put_url,json=json_for_update_new_location)
        print(result_put.text)
        assert 200 == result_put.status_code, ("Статус код не 200")
        print("статус код 200, проверка изменения новой лоакции прошла успешно")
        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        assert check_put_info == "Address successfully updated"
        print(check_put_info)
        """Проверка изменения новой локации"""
        result_get = requests.get(get_url)
        print(result_get.text)
        assert 200 == result_get.status_code, ("Статус код не 200 a:" + str(result_get.status_code))
        print(str(result_get.status_code) + ", проверка изменения новой локации прошла успешно")


        check_address = result_get.json()
        check_address_info = check_address.get("address")
        assert check_address_info == "100 Lenina street, RU"
        print(check_address_info)

        """удаления новой локации"""
        delete_recource = "/maps/api/place/delete/json"
        json_for_delete_location={
        "place_id" : place_id
        }
        delete_url= base_url+delete_recource+key
        print(delete_url)
        result_delete= requests.delete(delete_url,json=json_for_delete_location)
        print(result_delete)
        print(result_delete.text)
        check_status= result_delete.json()
        check_status_info = check_status.get("status")
        assert check_status_info =="OK"
        print(check_status_info)
        assert 200 == result_delete.status_code, ("Статус код не 200 a:" + str(result_delete.status_code))
        """Проверка удаления локации"""
        result_get = requests.get(get_url)
        print(result_get.text)
        assert 404 == result_get.status_code, ("Статус код не 404 a:" + str(result_get.status_code))
        print(str(result_get.status_code) + ", проверка удаления новой локации прошла успешно")

        check_msg = result_get.json()
        check_msg_info = check_msg.get("msg")
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        print(check_msg_info)


new_place = Test_new_location()
new_place.test_create_new_location()
