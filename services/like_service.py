from repositories.like_repository import LikeRepository

class LikeService:
    def __init__(self):
        self.like_repository = LikeRepository()

    def add_like(self, user_id, data):
        try:
            like_id = self.like_repository.add_like(data['post_id'], user_id)
            like = self.like_repository.get_like(like_id)
            return {"success": True, "like": like}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def delete_like(self, like_id, user_id):
        try:
            like = self.like_repository.get_like(like_id)
            if like and like['user_id'] == user_id:
                self.like_repository.delete_like(like_id)
                return {"success": True}
            return {"success": False, "error": "Unauthorized or like not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_likes_by_post(self, post_id):
        try:
            likes = self.like_repository.get_likes_by_post(post_id)
            return {"success": True, "likes": likes}
        except Exception as e:
            return {"success": False, "error": str(e)}
