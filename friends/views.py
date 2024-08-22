from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import FriendRequest
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import logging

User = get_user_model()
logger = logging.getLogger(__name__)


# Helper function to find a user by username or email
def find_user_by_username_or_email(username_or_email):
    return (
        User.objects.filter(username=username_or_email).first()
        or User.objects.filter(email=username_or_email).first()
    )


@login_required
def search_users(request):
    query = request.GET.get("query", "")
    results = []
    if query:
        results = User.objects.filter(username__icontains=query) | User.objects.filter(
            email__icontains=query
        )
    context = {"results": results, "query": query}
    return render(request, "friends/search_users.html", context)


@login_required
def send_friend_request(request, user_id):
    from_user = request.user
    to_user = get_object_or_404(User, id=user_id)

    if from_user != to_user:
        friend_request, created = FriendRequest.objects.get_or_create(
            from_user=from_user, to_user=to_user
        )
        if created:
            messages.success(request, f"Friend request sent to {to_user.username}.")
        else:
            messages.info(
                request, f"Friend request already sent to {to_user.username}."
            )
    else:
        messages.error(request, "You cannot send a friend request to yourself.")

    return redirect("friends:search_users")


def index_view(request):
    # ... other context data ...
    pending_requests_count = FriendRequest.objects.filter(
        to_user=request.user, accepted=False
    ).count()
    context = {
        # ... other context data ...
        "pending_requests_count": pending_requests_count,
    }
    return render(request, "index.html", context)


@login_required
def manage_friend_requests(request):
    received_requests = FriendRequest.objects.filter(
        to_user=request.user, accepted=False
    )
    context = {"received_requests": received_requests}
    return render(request, "friends/manage_friend_requests.html", context)


@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(
        FriendRequest, id=request_id, to_user=request.user
    )
    if friend_request.accepted == False:
        friend_request.accepted = True
        friend_request.save()

        # Add users to each other's friend lists
        request.user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(request.user)

        messages.success(
            request, f"You are now friends with {friend_request.from_user.username}."
        )
    else:
        messages.info(request, "This friend request has already been accepted.")

    return redirect("friends:manage_friend_requests")


@login_required
def decline_friend_request(request, request_id):
    friend_request = get_object_or_404(
        FriendRequest, id=request_id, to_user=request.user
    )
    friend_request.delete()
    messages.success(request, "Friend request declined.")
    return redirect("friends:manage_friend_requests")


@login_required
def view_friends(request):
    friends = request.user.friends.all()
    context = {"friends": friends}
    return render(request, "friends/view_friends.html", context)


@login_required
def pending_requests_count(request):
    pending_requests_count = FriendRequest.objects.filter(
        to_user=request.user, accepted=False
    ).count()
    context = {"pending_requests_count": pending_requests_count}
    return render(request, "index.html", context)


@login_required
def remove_friend(request, user_id):
    friend = get_object_or_404(User, id=user_id)
    if request.user.friends.filter(id=friend.id).exists():
        request.user.friends.remove(friend)
        friend.friends.remove(request.user)
        messages.success(request, f"Friend {friend.username} removed successfully.")
    else:
        messages.error(request, "This user is not your friend.")
    return redirect("friends:view_friends")
