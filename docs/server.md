# naclpost server

# 1. Description of the service

Since naclpost is just a proof of concept project, it will be rather simple. Users can
post messages on the website. Messages are authenticated using public key authentication.

On the site, all messages are publicly visible. Users can either sort by newest or see
an overview of all posts of a given user.

# 2. Users

Users register by uploading a public key to the server, accompanied by a signed message
which will be their alias ('username').

The server will store the following information about each user:
* alias (username)
* public key
* unique user id
* registration time and date
* all uploaded posts

# 3. Posts
Posts are plain text messages. To submit a new post, a user uses their private key to
sign it and upload it to the server. The server only accepts posts with a signature made
by a known public key.

Duplicate posts will be rejected.

The following information will be stored about each post:
* post id
* user id
* post date and time
* raw post text (including signature)

## 3.1 Commands
Non-post commands could be implemented using the same procedure as posts, but they will
contain a special header that identifies them as a command.

### 3.1.1 Deleting posts
As an optional feature, deleting posts could be implemented by submitting a post like
this:
```
------ naclpost command -------
delete $post_id
------ naclpost command -------
```
