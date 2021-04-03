
import sys

from app.lib.firebase import Firebase
from app.model.restaurant import RestaurantModel

class Restaurant:
    def __init__(self):
        self.firebase = Firebase()
        self.fb_collection = "testCollection"
        self.fb_document = "testDocument"
        
    def add_favorite(self, restaurants, user_id):
        document = sys._getframe().f_code.co_name.split("_")[1] + self.__class__.__name__
        for k, v in restaurants.items():
            self.firebase.upsert_db_data_to(
                collection= user_id,
                document=self.fb_document,
                data=self.firebase._array_data_adding_format(k, v)
            )
    
    def get_favorite(self, user_id):
        # firestoreからデータを取得する
        document = sys._getframe().f_code.co_name.split("_")[1] + self.__class__.__name__
        fav_data = self.firebase.get_db_data(
            collection=user_id,
            document=self.fb_document,
        )
        return RestaurantModel(ids = list(fav_data.values())[0])

    def delete_favorite(self, restaurants, user_id):
        document = sys._getframe().f_code.co_name.split("_")[1] + self.__class__.__name__
        for k, v in restaurants.items():
            self.firebase.delete_db_dataget_db_data(
                collection=user_id,
                document=self.fb_document,
                data=self.firebase._array_data_deleting_format(k, v)
            )

