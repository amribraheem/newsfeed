from repositories.post_repository import PostRepository

class PostService:
    def __init__(self):
        self.post_repository = PostRepository()

    def add_post(self, user_id, data):
        try:
            post_id = self.post_repository.add_post(user_id, data['content'])
            post = self.post_repository.get_post(post_id)
            if post:
                like_count = self.post_repository.get_like_count(post_id)
                share_count = self.post_repository.get_share_count(post_id)
                post['like_count'] = like_count
                post['share_count'] = share_count
                return {"success": True, "post": post}
            return {"success": False, "error": "Post not found after creation"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def update_post(self, post_id, user_id, data):
        try:
            post = self.post_repository.get_post(post_id)
            if post and post['user_id'] == user_id:
                self.post_repository.update_post(post_id, data['content'])
                updated_post = self.post_repository.get_post(post_id)
                like_count = self.post_repository.get_like_count(post_id)
                share_count = self.post_repository.get_share_count(post_id)
                updated_post['like_count'] = like_count
                updated_post['share_count'] = share_count
                return {"success": True, "post": updated_post}
            return {"success": False, "error": "Unauthorized or post not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def delete_post(self, post_id, user_id):
        try:
            post = self.post_repository.get_post(post_id)
            if post and post['user_id'] == user_id:
                self.post_repository.delete_post(post_id)
                return {"success": True}
            return {"success": False, "error": "Unauthorized or post not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_post(self, post_id):
        try:
            post = self.post_repository.get_post(post_id)
            if post:
                like_count = self.post_repository.get_like_count(post_id)
                share_count = self.post_repository.get_share_count(post_id)
                post['like_count'] = like_count
                post['share_count'] = share_count
                return {"success": True, "post": post}
            return {"success": False, "error": "Post not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_all_posts(self):
        try:
            posts = self.post_repository.get_all_posts()
            return {"success": True, "posts": posts}
        except Exception as e:
            return {"success": False, "error": str(e)}
