# Messaging_system
 

## postman usage

run postman

#### Write message
Change the method to POST, in the url pase the link "http://ec2-18-189-20-151.us-east-2.compute.amazonaws.com:8000/create/"

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
http://ec2-18-189-20-151.us-east-2.compute.amazonaws.com:8000/users/messages/{Receiver_id}
http://ec2-18-189-20-151.us-east-2.compute.amazonaws.com:8000/messages/?receiver={Receive_id}

#### Get all unread message for specific receiver:
http://ec2-18-189-20-151.us-east-2.compute.amazonaws.com:8000/messages/?receiver={Receive_id}&unread=True 

#### Delete message:
http://ec2-18-189-20-151.us-east-2.compute.amazonaws.com:8000/{Message_id}/delete/
Change the method to Delete

##### in "Authorazation" set
type: Basic Auth

(admin)
Username: adi
password: adi123456




