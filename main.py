import yagmail

yag = yagmail.SMTP(user="pythonlesson25@gmail.com", password="prhjzbqxjoeaarjf")

yag.send(
    to="danquahbadugabriel@gmail.com",
    subject="Holiday Plans",
    contents="Hello Gabriel, what are your plans for the upcoming holidays"
)
