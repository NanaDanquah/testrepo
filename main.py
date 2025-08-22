import yagmail

yag = yagmail.SMTP(user="pythonlesson25@gmail.com", password="************")

yag.send(
    to="recevieremail@gmail.com",
    subject="Holiday Plans",
    contents="Hello Gabriel, what are your plans for the upcoming holidays?"
)

