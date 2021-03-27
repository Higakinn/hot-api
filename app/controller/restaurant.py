
from app.lib.firebase import Firebase

class Restaurant:
    def __init__(self):
        print("Restaurant init")
        self.firebase = Firebase()
    
    def add_favorite(self, restaurants):
        self.firebase.add_db_data_to(
            collection="testCollection",
            document="testDocument",
            data=restaurants
        )
    
    def get_favorite(self, count):
        pass

    def delete_favorite(self, restaurants):
        pass

    

