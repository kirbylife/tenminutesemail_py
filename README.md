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

### TO-DO
1. Access to the e-mail received
