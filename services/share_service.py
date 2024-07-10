from repositories.share_repository import ShareRepository

class ShareService:
    def __init__(self):
        self.share_repository = ShareRepository()

    def add_share(self, user_id, data):
        try:
            share_id = self.share_repository.add_share(data['post_id'], user_id)
            share = self.share_repository.get_share(share_id)
            return {"success": True, "share": share}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def delete_share(self, share_id, user_id):
        try:
            share = self.share_repository.get_share(share_id)
            if share and share['user_id'] == user_id:
                self.share_repository.delete_share(share_id)
                return {"success": True}
            return {"success": False, "error": "Unauthorized or share not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_shares_by_post(self, post_id):
        try:
            shares = self.share_repository.get_shares_by_post(post_id)
            return {"success": True, "shares": shares}
        except Exception as e:
            return {"success": False, "error": str(e)}
