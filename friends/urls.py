# friends/urls.py
from django.urls import path
from . import views

app_name = "friends"

urlpatterns = [
    # Search users
    path("search/", views.search_users, name="search_users"),
    path(
        "search_users/", views.search_users, name="search_users"
    ),  # keep for backwards compatibility
    # Send friend request
    path(
        "send_friend_request/<int:user_id>/",
        views.send_friend_request,
        name="send_friend_request",
    ),
    # Manage friend requests
    path(
        "manage_requests/", views.manage_friend_requests, name="manage_friend_requests"
    ),
    # Accept friend request
    path(
        "accept_request/<int:request_id>/",
        views.accept_friend_request,
        name="accept_friend_request",
    ),
    # Decline friend request
    path(
        "decline_request/<int:request_id>/",
        views.decline_friend_request,
        name="decline_friend_request",
    ),
    # View friends
    path("view_friends/", views.view_friends, name="view_friends"),
    # Remove friend
    path("remove_friend/<int:user_id>/", views.remove_friend, name="remove_friend"),
    path(
        "pending_requests_count/",
        views.pending_requests_count,
        name="pending_requests_count",
    ),
]
