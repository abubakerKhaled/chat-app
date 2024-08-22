from django.db import models
from django.conf import settings

class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="sent_friend_requests",
        on_delete=models.CASCADE,
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="received_friend_requests",
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def accept(self):
        self.from_user.friends.add(self.to_user)
        self.to_user.friends.add(self.from_user)
        self.delete()
        
    def decline(self):
        self.delete()

    def __str__(self):
        return f"{self.from_user} to {self.to_user}"
    
    