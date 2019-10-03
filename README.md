# tenminutesemail_py

## Create a temporal e-mail using the [10minutemail](https://10minutemail.com/) service.

### Dependencies
- Python 3.x
- requests
- datetime

### Usage
**Generate a new e-mail**
```
In [1]: email = TenMinutesEmail()
In [2]: email
Out[2]: (b3763093@urhen.com, seconds_left=594)
```
**Check seconds left**
```
In [3]: email.seconds_left()
Out[3]: 472
```
> You can use `email.seconds_left(True)`, to get a more precise value but is a little bit more slow

**Verify if the e-mail is expired**
```
In [4]: email.is_alive()
Out[4]: True
```
> You can use `email.is_alive(True)`, to get a more precise value but is a little bit more slow

**Request 10 minutes more**
```
In [5]: email.reset_time()
```

**Get the messages recieved**
```
In [6]: messages = email.get_messages()
In [7]: type(messages)
Out[7]: list
In [8]: messages
Out[8]:
[{'subject': 'Subject example',
  'attachments': [],
  'formattedDate': 'Oct 3, 2019 12:46:18 PM',
  'bodyPreview': "Hello, I'm the body of the e-mail.",
  'attachmentCount': 0,
  'repliedTo': False,
  'bodyPlainText': "Hello, I'm the body of the e-mail.",
  'primaryFromAddress': 'kirbylife@protonmail.com',
  'read': False,
  'forwarded': False,
  'bodyText': "<div>Hello, I'm the body of the e-mail.<br></div>",
  'fromList': ['kirbylife@protonmail.com'],
  'recipientList': ['b3763093@urhen.com'],
  'sentDate': 1570124778000,
  'expanded': False,
  'id': '18326103452296378'}]
```

**Get the total number of messages**
```
In [9]: email.total_messages
Out[9]: 1
In [10]: # Another way
In [11]: len(email.messages)
Out[11]: 1
```

### TO-DO
- [x] Access to the e-mails received
