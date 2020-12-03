# from django.test import SimpleTestCase
#
# import requests
# import httpretty
#
# class TestBase(SimpleTestCase):
#
#     movies_url = "https://ghibliapi.herokuapp.com/films"
#     people_url = "https://ghibliapi.herokuapp.com/people"
#     url_404 = "https://ghibliapi.herokuapp.com/404"
#
#     movies_response = [
#         {
#             "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
#             "title": "Castle in the Sky",
#             "description": "The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit the evil Muska, who plans to use Laputa's science to make himself ruler of the world.",
#             "director": "Hayao Miyazaki",
#             "producer": "Isao Takahata",
#             "release_date": "1986",
#             "rt_score": "95",
#             "people": [
#                 "https://ghibliapi.herokuapp.com/people/"
#             ],
#             "species": [
#                 "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
#             ],
#             "locations": [
#                 "https://ghibliapi.herokuapp.com/locations/"
#             ],
#             "vehicles": [
#                 "https://ghibliapi.herokuapp.com/vehicles/"
#             ],
#             "url": "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
#         },
#         {
#             "id": "12cfb892-aac0-4c5b-94af-521852e46d6a",
#             "title": "Grave of the Fireflies",
#             "description": "In the latter part of World War II, a boy and his sister, orphaned when their mother is killed in the firebombing of Tokyo, are left to survive on their own in what remains of civilian life in Japan. The plot follows this boy and his sister as they do their best to survive in the Japanese countryside, battling hunger, prejudice, and pride in their own quiet, personal battle.",
#             "director": "Isao Takahata",
#             "producer": "Toru Hara",
#             "release_date": "1988",
#             "rt_score": "97",
#             "people": [
#                 "https://ghibliapi.herokuapp.com/people/"
#             ],
#             "species": [
#                 "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
#             ],
#             "locations": [
#                 "https://ghibliapi.herokuapp.com/locations/"
#             ],
#             "vehicles": [
#                 "https://ghibliapi.herokuapp.com/vehicles/"
#             ],
#             "url": "https://ghibliapi.herokuapp.com/films/12cfb892-aac0-4c5b-94af-521852e46d6a"
#         },
#         {
#             "id": "5fdfb320-2a02-49a7-94ff-5ca418cae602",
#             "title": "When Marnie Was There",
#             "description": "The film follows Anna Sasaki living with her relatives in the seaside town. Anna comes across a nearby abandoned mansion, where she meets Marnie, a mysterious girl who asks her to promise to keep their secrets from everyone. As the summer progresses, Anna spends more time with Marnie, and eventually Anna learns the truth about her family and foster care.",
#             "director": "Hiromasa Yonebayashi",
#             "producer": "Yoshiaki Nishimura",
#             "release_date": "2014",
#             "rt_score": "92",
#             "people": [],
#             "species": [
#                 "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
#             ],
#             "locations": [
#                 "https://ghibliapi.herokuapp.com/locations/"
#             ],
#             "vehicles": [
#                 "https://ghibliapi.herokuapp.com/vehicles/"
#             ],
#             "url": "https://ghibliapi.herokuapp.com/films/5fdfb320-2a02-49a7-94ff-5ca418cae602"
#         }
#     ]
#
#     people_respone = [
#         {
#             "id": "fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
#             "name": "Pazu",
#             "gender": "Male",
#             "age": "13",
#             "eye_color": "Black",
#             "hair_color": "Brown",
#             "films": [
#                 "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
#             ],
#             "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
#             "url": "https://ghibliapi.herokuapp.com/people/fe93adf2-2f3a-4ec4-9f68-5422f1b87c01"
#         },
#         {
#             "id": "598f7048-74ff-41e0-92ef-87dc1ad980a9",
#             "name": "Lusheeta Toel Ul Laputa",
#             "gender": "Female",
#             "age": "13",
#             "eye_color": "Black",
#             "hair_color": "Black",
#             "films": [
#                 "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
#             ],
#             "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
#             "url": "https://ghibliapi.herokuapp.com/people/598f7048-74ff-41e0-92ef-87dc1ad980a9"
#         },
#         {
#             "id": "3bc0b41e-3569-4d20-ae73-2da329bf0786",
#             "name": "Dola",
#             "gender": "Female",
#             "age": "60",
#             "eye_color": "Black",
#             "hair_color": "Peach",
#             "films": [],
#             "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
#             "url": "https://ghibliapi.herokuapp.com/people/3bc0b41e-3569-4d20-ae73-2da329bf0786"
#         }
#     ]
#
#     response_404 = '{"length": null}'
#
#     def setUp(self):
#         # httpretty.register_uri(
#         #     httpretty.GET,
#         #     self.movies_url,
#         #     body=str(self.movies_response),
#         #     content_type="application/json")
#
#         # httpretty.register_uri(
#         #     httpretty.GET,
#         #     self.people_url,
#         #     body=str(self.people_respone),
#         #     content_type="application/json")
#
#         httpretty.register_uri(
#             httpretty.GET,
#             self.url_404,
#             body='{"length": null}',
#             content_type="application/json",
#             status=404)
#         httpretty.enable()
#
#     def test_stub_data(self):
#         # response = requests.get(self.movies_url)
#         # print(response.json())
#         # print(self.movies_response)
#         # self.assertEqual(self.movies_response, response.json())
#
#         # response = requests.get(self.people_url)
#         # self.assertEqual(self.people_respone, response.json())
#
#         response = requests.get(self.url_404)
#         self.assertEqual(response.status_code, 404)
