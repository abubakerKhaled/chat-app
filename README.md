# Chat Application

This chat application allows users to communicate in real-time, create chat rooms, manage contacts, and customize their profiles. Below is a step-by-step guide on implementing its functionalities.

## Table of Contents
1. [User Authentication](#1-user-authentication)
2. [Real-Time Chat](#2-real-time-chat)
3. [Room Creation and Management](#3-room-creation-and-management)
4. [Direct Messaging](#4-direct-messaging)
5. [Friend Search](#5-friend-search)
6. [Recent Chats](#6-recent-chats)
7. [User Profile](#7-user-profile)
8. [Friend Status Indicator](#8-friend-status-indicator)
9. [Add Contacts with Invitation](#9-add-contacts-with-invitation)
10. [User Status (Active/Busy)](#10-user-status-activebusy)
11. [Edit Profile Information](#11-edit-profile-information)
12. [Delete Friend](#12-delete-friend)
13. [View Friend Information](#13-view-friend-information)
14. [Change Password](#14-change-password)

---

### 1. User Authentication
**Description:**  
Users can sign up for a new account or log in to an existing one.

**Implementation Steps:**

1. **Sign Up:**
   - Create a registration form to collect user details: **username** (unique), **email**, **password**, **name**, and **profile image**.
   - Implement server-side validation to ensure the username and email are unique.
   - Hash the password using a secure hashing algorithm like **bcrypt** before storing it in the database.
   - Save the user details in the **Users** table/collection.
   - After successful registration, redirect the user to the login page or automatically log them in.

2. **Login:**
   - Create a login form to collect **username/email** and **password**.
   - Upon submission, verify that the provided credentials match those in the database.
   - Initiate a user session or issue a JWT token to authenticate subsequent requests.
   - Redirect the user to the main chat interface/dashboard upon successful login.

### 2. Real-Time Chat
**Description:**  
Users can chat in real-time with friends or in chat rooms.

**Implementation Steps:**

1. **WebSocket Setup:**
   - Integrate WebSocket technology (e.g., **Socket.IO** for Node.js or **Django Channels** for Django) to enable real-time communication.
   - Establish a WebSocket server that listens for incoming connections from clients.

2. **Client-Side Implementation:**
   - Implement WebSocket client-side scripts to connect to the WebSocket server.
   - Define events for sending and receiving messages.

3. **Message Handling:**
   - Define server-side event handlers to broadcast messages to appropriate recipients (individual users or rooms).
   - Ensure messages are delivered instantly and reliably.

### 3. Room Creation and Management
**Description:**  
Users can create chat rooms and share them with friends for group conversations.

**Implementation Steps:**

1. **Room Creation:**
   - Provide an interface/button for users to create a new chat room.
   - Collect necessary details such as **room name**, **description**, and **privacy settings** (public/private).
   - Generate a unique **room ID** or **invite link**.
   - Save the room details in a **Rooms** table/collection with references to the creator.

2. **Sharing Room with Friends:**
   - Implement functionality to share the **room ID** or **invite link** via the application or external platforms.
   - Allow invited users to join the room upon accepting the invitation.

3. **Room Management:**
   - Allow room creators or administrators to **add/remove members**, **assign roles**, and **modify room settings**.
   - Implement a feature to **delete** or **archive** rooms.

4. **Real-Time Communication in Rooms:**
   - Use WebSocket channels specific to each room to ensure messages are broadcasted only to room members.
   - Implement features like **typing indicators**, **read receipts**, and **message notifications** within rooms.

### 4. Direct Messaging
**Description:**  
Users can send direct messages to their friends privately.

**Implementation Steps:**

1. **Initiating Chat:**
   - Provide a **contacts list** or **search functionality** for users to find and select friends to chat with.
   - On selecting a friend, open a **chat window** or **screen** dedicated to that conversation.

2. **Message Sending and Receiving:**
   - Implement real-time sending and receiving of messages using WebSockets.
   - Save each message in a **Messages** table/collection with references to the **sender**, **receiver**, **timestamp**, and **message content**.

3. **Chat History:**
   - Retrieve and display past conversations between users when they open the chat window.
   - Implement **pagination** or **infinite scroll** for loading older messages.

4. **Notifications:**
   - Notify users of new messages when they are not in the chat window through **in-app notifications** or **push notifications**.

### 5. Friend Search
**Description:**  
Users can search for friends using a unique username.

**Implementation Steps:**

1. **Search Interface:**
   - Provide a **search bar** where users can input a **username** to search for other users.

2. **Backend Search Logic:**
   - Implement an API endpoint that searches the **Users** database/table for matches to the inputted username.
   - Ensure the search is **case-insensitive** and returns relevant results.

3. **Displaying Results:**
   - Show a list of matching users with basic information like **profile picture**, **name**, and **username**.
   - Provide an option to **send a friend request** or **view profile** directly from the search results.

4. **Handling No Results:**
   - Display an appropriate message if no users are found matching the search criteria.

### 6. Recent Chats
**Description:**  
Users can view a list of their recent chats with friends.

**Implementation Steps:**

1. **Chat History Retrieval:**
   - Query the **Messages** database/table to fetch the latest message from each conversation the user is part of.

2. **Displaying Recent Chats:**
   - Present a **list view** showing recent chats with details like **friend's name**, **profile picture**, **last message snippet**, and **timestamp**.
   - Sort the list by **most recent activity**.

3. **Unread Messages Indicator:**
   - Highlight conversations with **unread messages** using badges or bold text.
   - Keep track of the last read message in each conversation for accurate unread counts.

4. **Navigating to Chat:**
   - Allow users to click/tap on a conversation to open the full chat history and continue messaging.

### 7. User Profile
**Description:**  
Each user has a profile containing personal information such as name, image, email, etc.

**Implementation Steps:**

1. **Profile Data Structure:**
   - Define additional fields in the **Users** database/table for storing **full name**, **profile image URL**, **bio**, **email**, **phone number**, and any other relevant information.

2. **Profile View Page:**
   - Create a dedicated page or modal where users can view their own profile information.
   - Display all profile details in a structured and visually appealing format.

3. **Profile Picture Upload:**
   - Implement functionality to **upload** and **store** profile images securely.
   - Use services like **AWS S3**, **Cloudinary**, or store them on the server with proper access controls.

4. **Privacy Settings:**
   - Allow users to set privacy levels for different pieces of information (e.g., making email visible only to friends).

### 8. Friend Status Indicator
**Description:**  
Users can see whether their friends are currently active or not.

**Implementation Steps:**

1. **Tracking User Activity:**
   - Update the user's **status** in the database when they **log in**, **log out**, or become **idle**.
   - Utilize WebSocket connections to detect real-time activity. When a user connects/disconnects, update their status accordingly.

2. **Displaying Status:**
   - Show a **green dot** or **"Online"** label next to friends who are currently active.
   - Indicate **inactive** or **offline** status with a grey dot or appropriate label.

3. **Real-Time Updates:**
   - Implement real-time updates so that when a friend's status changes, it immediately reflects in the user's interface.

4. **Last Seen Timestamp:**
   - Optionally, display the **last active** time for offline users.

### 9. Add Contacts with Invitation
**Description:**  
Users can add contacts by sending an invitation message to another user's email.

**Implementation Steps:**

1. **Add Contact Form:**
   - Provide a form where users can enter the **email address** of the person they want to add and write an **invitation message**.

2. **Invitation Email:**
   - Upon submission, send an **email invitation** to the provided email address containing the **invitation message** and a **link** to join the chat application or accept the contact request.
   - Use email services like **SendGrid**, **Mailgun**, or **SMTP** servers for sending emails.

3. **Handling Invitations:**
   - If the recipient is **not registered**, direct them to a **sign-up page** upon clicking the link.
   - If the recipient is **already a user**, notify them of the **contact request** within the application, allowing them to **accept** or **decline**.

4. **Updating Contacts List:**
   - Upon acceptance, add each user to the other's **contacts/friends list** in the database.
   - Allow users to view pending **sent** and **received** invitations.

### 10. User Status (Active/Busy)
**Description:**  
Users can set their status to indicate if they are active or busy.

**Implementation Steps:**

1. **Status Selection Interface:**
   - Provide options in the user interface for users to select their current status: **Active**, **Busy**, **Away**, etc.

2. **Updating Status:**
   - When a user selects a status, update this information in their **user profile** in the database.
   - Broadcast the status change to all friends or relevant contacts through WebSockets.

3. **Displaying Status:**
   - Show the user's current status next to their profile picture or name in chats and contact lists.
   - Use different **icons** or **colors** to represent different statuses for easy recognition.

4. **Automatic Status Changes:**
   - Implement logic to automatically change the user's status to **Away** after a period of inactivity.
   - Allow users to customize these settings according to their preferences.

### 11. Edit Profile Information
**Description:**  
Users can edit their profile information except for their unique username.

**Implementation Steps:**

1. **Edit Profile Interface:**
   - Create an **Edit Profile** page or modal where users can update their information such as **name**, **email**, **profile picture**, **bio**, etc.
   - Disable or hide the **username** field to prevent changes.

2. **Form Validation:**
   - Implement client-side and server-side validation to ensure data integrity (e.g., valid email format).

3. **Updating Database:**
   - Upon submission, update the user's information in the **Users** database/table.
   - Handle profile picture uploads and updates appropriately, replacing old images if necessary.

4. **Feedback and Notifications:**
   - Provide feedback to the user upon successful or failed updates.
   - Optionally, notify friends of significant profile changes like a new profile picture.

### 12. Delete Friend
**Description:**  
Users can remove a friend from their contacts list.

**Implementation Steps:**

1. **Delete Option:**
   - Provide a **delete** or **remove** button next to each contact in the user's friends list or within the friend's profile view.

2. **Confirmation Prompt:**
   - Before deletion, display a **confirmation dialog** to prevent accidental removals.

3. **Updating Contacts:**
   - Upon confirmation, remove the association between the two users in the **Contacts/Friends** table/collection.
   - Optionally, delete the chat history between the two users or archive it based on privacy policies.

4. **Notifications:**
   - Decide whether to notify the other user about the removal. If so, send an appropriate notification or message.

5. **Handling Edge Cases:**
   - Ensure that after deletion, neither user can send messages to each other unless a new friend request is accepted.

### 13. View Friend Information
**Description:**  
Users can view detailed information about their friends.

**Implementation Steps:**

1. **Friend Profile Page:**
   - Create a **profile view** for each friend displaying information such as **full name**, **profile picture**, **bio**, **email** (if shared), **status**, and **last active time**.

2. **Accessing Profile:**
   - Allow users to access a friend's profile by clicking on their name or profile picture in chats or contact lists.

3. **Privacy Considerations:**
   - Respect the friend's **privacy settings**, displaying only the information they have chosen to share.

4. **Common Actions:**
   - Include options on the friend's profile page to **start a chat**, **remove friend**, or **view mutual friends**.

### 14. Change Password
**Description:**  
Users can change their account password for security purposes.

**Implementation Steps:**

1. **Change Password Interface:**
   - Provide a **form** where users can enter their **current password**, **new password**, and **confirm new password**.

2. **Form Validation:**
   - Validate that the **current password** matches the one in the database.
   - Ensure the **new password** meets security requirements (e.g., minimum length, includes numbers and special characters).
   - Confirm that **new password** and **confirm new password** fields match.

3. **Updating Password:**
   - Hash the new password using a secure algorithm like **bcrypt**.
   - Update the user's password in the **Users** database/table.

4. **Feedback and Notifications:**
   - Inform the user of a successful password change.
   - Optionally, send an email notification to the user's registered email address informing them of the password change. This can help in detecting unauthorized changes.

5. **Handling Errors:**
   - Provide appropriate error messages for issues like incorrect current password or weak new password.


**Next Steps:**
- Define the **technology stack** to be used (e.g., **Frontend**: React, Angular; **Backend**: Node.js, Django; **Database**: MongoDB, PostgreSQL).
- Set up the **development environment** and **version control** using Git and GitHub.
- Implement **security measures** such as input sanitization, authentication tokens, and secure password storage.
- Develop a **testing strategy** to ensure all functionalities work as intended.
- Plan for **deployment** and **scaling** of the application.
