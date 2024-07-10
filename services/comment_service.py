from repositories.comment_repository import CommentRepository

class CommentService:
    def __init__(self):
        self.comment_repository = CommentRepository()

    def add_comment(self, data):
        try:
            comment_id = self.comment_repository.add_comment(data['post_id'], data['user_id'], data['content'])
            return {"success": True, "comment_id": comment_id}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_comments_by_post(self, post_id):
        try:
            comments = self.comment_repository.get_comments_by_post(post_id)
            return {"success": True, "comments": comments}
        except Exception as e:
            return {"success": False, "error": str(e)}
