# Messaging_system
 

## postman usage
```
run postman
```
##### in "Authorazation" set
``` 
type: Basic Auth 
(admin)
Username: adi
password: adi123456
```

#### Write message
```
Change the method to POST, in the URL paste the link "http://ec2-3-19-79-145.us-east-2.compute.amazonaws.com:8000/create/"
```
###### in the "params" tab set 
```
key: Content-Type 
value: application/json
```

###### set the Body field as following:
```
{
    "sender": "1",
    "receiver": "{Receiver id}",
    "message": "{Message (maximum 500 characters)}",
    "subject": "{Subject (maximum 30 characters)}"
}
```
#### Get all messages for a specific receiver:
```
http://ec2-3-19-79-145.us-east-2.compute.amazonaws.com:8000/messages/?receiver={Receive_id}
```
#### Get all unread message for a specific receiver:
```
http://ec2-3-19-79-145.us-east-2.compute.amazonaws.com:8000/messages/?receiver={Receive_id}&unread=True 
```
#### Delete message:
```
http://ec2-3-19-79-145.us-east-2.compute.amazonaws.com:8000/{Message_id}/delete/
Change the method to Delete
```




