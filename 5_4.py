salutation='salut'
name = 'Artem'
product = 'butter'
verbed = 'spocked'
room = 'Main room'
animals = 'lions'
amount = 5
percent = 89
spokesman = 'no'
job_title = 'manager'

letter = 'Dear {} {},\n\
Thank you for your letter. We are sorry that our {}\n\
{} in your {}. Please note that it should never\n\
be used in a {}, especially near any {}.\n\
Send us your receipt and {} for shipping and handling.\n\
We will send you another {} that, in our tests,\n\
is {} % less likely to have {}.\n\
Thank you for your support.\n\
Sincerely,\n\
{}\n\
{}'.format(salutation, name, product, verbed, room, room, animals, amount, product, percent, verbed, spokesman, job_title)
print (letter)
