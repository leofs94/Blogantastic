from models import User

user = User.objects.create(username='Leonardo', password='1234')

user.save()

print(User.objects.first().username)
