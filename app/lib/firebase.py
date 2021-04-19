import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from app.settings import settings

class Firebase:
    def __init__(self):
        # アプリケーションのデフォルトの資格情報を使用する
        cred = credentials.Certificate(settings.GOOGLE_APP_CREDENTIALS)
        # 初期済みでない場合に初期化処理を行う
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred, {
                'projectId': settings.FIREBASE_PROJECT_ID,
            })
        self.db = firestore.client()

    def upsert_db_data_to(self, collection="",document="",data=""):
        doc_ref = self.db.collection(collection).document(document)
        # upsert
        doc_ref.set(data, merge=True)

    def get_db_data(self, collection="",document=""):
        doc_ref = self.db.collection(collection).document(document)
        doc = doc_ref.get()
        if doc.exists:
            # print(f'Document data: {doc.to_dict()}')
            return doc.to_dict()
        
        return {}
    
    def delete_db_dataget_db_data(self, collection="",document="",data=""):
        doc_ref = self.db.collection(collection).document(document)
        doc_ref.update(data)

    # firebaseで配列の要素を更新したい場合に使う
    def _array_data_adding_format(self, key, value):
        return {f'{key}': firestore.ArrayUnion(value)}
    
    # firebaseで配列の要素を削除したい場合に使う
    def _array_data_deleting_format(self, key, value):
        return {f'{key}': firestore.ArrayRemove(value)}
    