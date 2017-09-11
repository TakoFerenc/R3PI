import requests
import random


URL = 'http://jsonplaceholder.typicode.com/'


class ControlRestAPI:

    def __init__(self):
        self.user_id = random.randint(1, 10)

    def get_user_data(self):
        # This function returns all data of a random user and prints its address
        self.url = f'{URL}users/{self.user_id}'
        self.open_url = requests.get(self.url)
        self.user_data = self.open_url.json()
        self.address = self.user_data['address']
        print(f'Address of user {self.user_id} is: \n {self.address}')
        return self.user_data

    def get_users_posts_data(self):
        # This function returns a list of the posts of the previous random user
        self.url = f'{URL}posts'
        self.open_url = requests.get(self.url)
        self.post_data = self.open_url.json()
        self.new_list = []
        for data in self.post_data:
            if data['userId'] == self.user_id:
                self.new_list.append(data)
        return self.new_list

    def get_users_specific_data(self, key):
        # This function returns a generator that generates the users's specific post data based on key passed
        self.user_post_data = self.get_users_posts_data()
        for element in self.user_post_data:
            yield element[key]

    def post_new_data(self):
        # This function posts a new post for the user and returns the response code form the server
        self.url = f'{URL}posts'
        self.new_data = {'title': 'TestTitle', 'body': 'TestBody', 'userId': self.user_id}
        self.post = requests.post(self.url, data=self.new_data,)
        return self.post.status_code
