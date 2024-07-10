from repositories.like_repository import LikeRepository

class LikeService:
    def __init__(self):
        self.like_repository = LikeRepository()

    def add_like(self, data):
        try:
            like_id = self.like_repository.add_like(data['post_id'], data['user_id'])
            return {"success": True, "like_id": like_id}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_likes_by_post(self, post_id):
        try:
            likes = self.like_repository.get_likes_by_post(post_id)
            return {"success": True, "likes": likes}
        except Exception as e:
            return {"success": False, "error": str(e)}
