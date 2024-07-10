from repositories.follow_repository import FollowRepository

class FollowService:
    def __init__(self):
        self.follow_repository = FollowRepository()

    def add_follow(self, data):
        try:
            follow_id = self.follow_repository.add_follow(data['follower_id'], data['followed_id'])
            return {"success": True, "follow_id": follow_id}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_followers(self, user_id):
        try:
            followers = self.follow_repository.get_followers(user_id)
            return {"success": True, "followers": followers}
        except Exception as e:
            return {"success": False, "error": str(e)}
