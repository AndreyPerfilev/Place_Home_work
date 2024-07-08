# 1. Отправить метод DELETE,  с помощью которого удалить 2-й и 4-й place_id из текстового файла,
# полученного в результате выполнения предыдущего задания (удалить значит не стереть,
# это значит что в файле по-прежнему 5  значений, но 2-я и 4-я локация не существуют)
#
# 2. Отправить метод Get который будет читать place_id из текстового файла,
# и сделает отбор на существующие и несуществующие локации
#
# 3. Создать новый файл и поместить в него 3 существующие локации (place_id),
# которые были отобраны в результате метода GET
#
# 4. Добавить в код комментарии, аннотации, print, проверки на статус код для лучшей читаемости кода
#
#
# ------------НЕОБХОДИМО ОЧИЩАТЬ СОЗДАННЫЙ ФАЙЛ
import requests

location_post_count = int(input("Напишите цифрой количество локаций для создания>>>:"))
var = "5f0d22ac730e336883aec3ea10458caa"
var_1 = ""
id_place_dict = {1: '123', 2: '321', 3: "231"}
id_place_list = []
sorted_id_place_list = []
url_post = "https://rahulshettyacademy.com/maps/api/place/add/json?key=qaclick123"
url_get = "https://rahulshettyacademy.com/maps/api/place/get/json?key=qaclick123"
url_delete = "https://rahulshettyacademy.com/maps/api/place/delete/json?key=qaclick123"

json_for_new_location = {

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

"""Метод записи текста в файл, в конец строки"""


def write_in_file(text):
    fwid = open('filewithid.txt', 'a+', encoding='utf-8')
    fwid.write(text + '\n')
    fwid.close()


"""Метод записи текста в новый файл, в конец строки"""


def write_in_new_file():
    fwid = open('filewithnewid.txt', 'a+', encoding='utf-8')
    for i in sorted_id_place_list:
        fwid.write(i + '\n')
    fwid.close()


"""Метод чтения записи из файла"""


def read_file():
    frid = open('filewithid.txt', "r")
    text = frid.read()
    frid.close()
    return text


"""Метод для создания локаций, в нужном количесетсве и запись их в файл"""


def post_locations(location_post_count):
    for i in range(location_post_count):
        result_post = requests.post(url_post, json=json_for_new_location)
        assert result_post.status_code == 200, (f"Статус код не 200, статус код:{result_post.status_code}")
        json_post = result_post.json()
        # print(json_post)
        place_id = json_post.get("place_id")
        id_place_dict[i + 1] = place_id
        print(str("POST ") + f"Создали {i + 1} локацию, id равен: {place_id}")
        write_in_file(place_id)


"""метод проверки созданных локаций"""


def get_locations(text):
    place_id = ""
    for i in text:
        place_id = place_id + i.strip()
        # place_id = place_id + i
        if len(place_id) <= 31:
            continue
        else:
            id_place_list.append(place_id)
            result_get = requests.get(url_get + f'&place_id={place_id}')
            # assert result_get.status_code == 200, (f"Статус код не 200, статус код: {result_get.status_code}")
            print(str("GET ") + f"Локация с id: {place_id} существует, статус код:" + str(result_get.status_code))
            place_id = ''


"""метод удаления локации по айди"""
def delete_locations(id_location):
    body = {
        "place_id": id_location}
    delete_result = requests.delete(url_delete, json=body)
    print(f'DELETE Локация с id: {id_location} УДАЛЕНА. {delete_result.text} Локации не существует')
    result_get = requests.get(url_get + f'&place_id={id_location}')
    assert result_get.status_code == 404, ('КОД не 404')


"""Метод сортировки существующих локаций"""
def sorted_locations():
    for i, j in id_place_dict.items():
        result_get = requests.get(url_get + f'&place_id={j}')
        if result_get.status_code == 200:
            sorted_id_place_list.append(j)
            print(str(i) + " локация существует. Код: " + str(result_get.status_code))
        else:
            print(str(i) + " локация не существует, статус код: " + str(result_get.status_code))
    print("Список отсортированных локаций" + str(sorted_id_place_list))


post_locations(location_post_count)
get_locations(read_file())
delete_locations(id_place_dict.get(2))
delete_locations(id_place_dict.get(4))
sorted_locations()
write_in_new_file()
