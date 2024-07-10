from repositories.share_repository import ShareRepository

class ShareService:
    def __init__(self):
        self.share_repository = ShareRepository()

    def add_share(self, data):
        try:
            share_id = self.share_repository.add_share(data['post_id'], data['user_id'])
            return {"success": True, "share_id": share_id}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_shares_by_post(self, post_id):
        try:
            shares = self.share_repository.get_shares_by_post(post_id)
            return {"success": True, "shares": shares}
        except Exception as e:
            return {"success": False, "error": str(e)}
