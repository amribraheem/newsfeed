from repositories.follow_repository import FollowRepository


class FollowService:
    def __init__(self):
        self.follow_repository = FollowRepository()

    def add_follow(self, follower_id, data):
        try:
            if follower_id == data['followed_id']:
                return {"success": False, "error": "You cannot follow yourself."}

            follow_id = self.follow_repository.add_follow(follower_id, data['followed_id'])
            follow = self.follow_repository.get_follow(follow_id)
            return {"success": True, "follow": follow}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def delete_follow(self, follow_id, user_id):
        try:
            follow = self.follow_repository.get_follow(follow_id)
            if follow and follow['follower_id'] == user_id:
                self.follow_repository.delete_follow(follow_id)
                return {"success": True}
            return {"success": False, "error": "Unauthorized or follow not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_followers(self, user_id):
        try:
            followers = self.follow_repository.get_followers(user_id)
            return {"success": True, "followers": followers}
        except Exception as e:
            return {"success": False, "error": str(e)}
