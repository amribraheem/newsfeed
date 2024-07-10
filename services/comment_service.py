from repositories.comment_repository import CommentRepository

class CommentService:
    def __init__(self):
        self.comment_repository = CommentRepository()

    def add_comment(self, user_id, data):
        try:
            comment_id = self.comment_repository.add_comment(data['post_id'], user_id, data['content'])
            comment = self.comment_repository.get_comment(comment_id)
            return {"success": True, "comment": comment}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def update_comment(self, comment_id, user_id, data):
        try:
            comment = self.comment_repository.get_comment(comment_id)
            if comment and comment['user_id'] == user_id:
                self.comment_repository.update_comment(comment_id, data['content'])
                updated_comment = self.comment_repository.get_comment(comment_id)
                return {"success": True, "comment": updated_comment}
            return {"success": False, "error": "Unauthorized or comment not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def delete_comment(self, comment_id, user_id):
        try:
            comment = self.comment_repository.get_comment(comment_id)
            if comment and comment['user_id'] == user_id:
                self.comment_repository.delete_comment(comment_id)
                return {"success": True}
            return {"success": False, "error": "Unauthorized or comment not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_comments_by_post(self, post_id):
        try:
            comments = self.comment_repository.get_comments_by_post(post_id)
            return {"success": True, "comments": comments}
        except Exception as e:
            return {"success": False, "error": str(e)}
