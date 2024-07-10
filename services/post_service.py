from repositories.post_repository import PostRepository

class PostService:
    def __init__(self):
        self.post_repository = PostRepository()

    def add_post(self, data):
        try:
            post_id = self.post_repository.add_post(data['user_id'], data['content'])
            return {"success": True, "post_id": post_id}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def update_post(self, post_id, data):
        try:
            self.post_repository.update_post(post_id, data['content'])
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def delete_post(self, post_id):
        try:
            self.post_repository.delete_post(post_id)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_post(self, post_id):
        try:
            post = self.post_repository.get_post(post_id)
            if post:
                return {"success": True, "post": post}
            return {"success": False, "error": "Post not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}
