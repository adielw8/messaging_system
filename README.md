# Messaging_system
 

## postman usage

run postman

#### Write message
Change the method to POST, in the url pase the link "http://127.0.0.1:8000/create/"

###### in "params" tab set 
key: Content-Type 
value: application/json
###### in "Authorazation" set
type: Basic Auth
(admin)
Username: adi
password: adi123456

###### set the Body field as folow:

{
    "sender": "1",
    "receiver": "{Receiver id}",
    "message": "{Message (maximum 500 characters)}",
    "subject": "{Subject (maximum 30 characters)}"
}

#### Get all messages for a specific receiver:
http://127.0.0.1:8000/users/messages/{Receiver_id}
http://127.0.0.1:8000/messages/?receiver={Receive_id}

#### Get all unread message for specific receiver:
http://127.0.0.1:8000/messages/?receiver={Receive_id}&unread=True 

#### Delete message:
http://127.0.0.1:8000/{Message_id}/delete/
Change the method to Delete

##### in "Authorazation" set
type: Basic Auth

(admin)
Username: adi
password: adi123456




