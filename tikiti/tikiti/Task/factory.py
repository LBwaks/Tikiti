# import factory
# from .models import  Sector, Source, Support, Status, Issue, Priority, Task, TaskHistory, TaskFiles
# from django.contrib.auth.models import User
# import uuid,datetime
# # from factory.Faker import Faker
# # fake=Faker()

# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User
#     username=factory.Faker('user_name')
#     email = factory.LazyAttribute(lambda o: '%s@example.com' % o.username)
#     password=  factory.PostGenerationMethodCall('set_password','password123')


# class SectorFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Sector

#     sector_name = factory.Faker("sentence",nb_words=2)
#     slug = factory.LazyFunction(uuid.uuid4)
#     user = factory.SubFactory(UserFactory)
#     description = factory.Faker('sentence',nb_words=10)
#     is_featured = False
#     is_published = False
#     create_date = factory.LazyFunction(datetime.datetime.now)
#     update_date = factory.LazyFunction(datetime.datetime.now)

# class SourceFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model =Source

#     source_name = factory.Faker("random_element",elements=['Customer CAre-2','Technian-Field','WEbsite-0'])
#     slug = factory.LazyFunction(uuid.uuid4)
#     user = factory.SubFactory(UserFactory)
#     description = factory.Faker("paragraph")
#     create_date = factory.LazyFunction(datetime.datetime.now)
#     update_date = factory.LazyFunction(datetime.datetime.now)


# class SupportFactory(factory.django.DjangoModelFactory):
#     class Meta :
#         model =Support
#     support_name = factory.Faker("random_element",elements=['Fiber-Cut','Los2','Slow-0','BLink','Test'])
#     slug = factory.LazyFunction(uuid.uuid4)
#     user = factory.SubFactory(UserFactory)
#     description = factory.Faker("paragraph")
#     create_date = factory.LazyFunction(datetime.datetime.now)
#     update_date = factory.LazyFunction(datetime.datetime.now)


# class IssueFactory(factory.django.DjangoModelFactory):
#     class Meta :
#         model =Issue
#     issue_type = factory.Faker('word')
#     slug = factory.LazyFunction(uuid.uuid4)
#     user = factory.SubFactory(UserFactory)
#     description = factory.Faker("paragraph")
#     create_date = factory.LazyFunction(datetime.datetime.now)
#     update_date = factory.LazyFunction(datetime.datetime.now)


# class StatusFactory(factory.django.DjangoModelFactory):
#     class Meta :
#         model =Status
#     status_name = factory.Faker('word')#factory.Faker("random_element",elements=['New','Working On it','REsolved','Closed','Stop'])
#     slug = factory.LazyFunction(uuid.uuid4)
#     user = factory.SubFactory(UserFactory)
#     description = factory.Faker("paragraph")
#     create_date = factory.LazyFunction(datetime.datetime.now)
#     update_date = factory.LazyFunction(datetime.datetime.now)

# class PriorityFactory(factory.django.DjangoModelFactory):
#     class Meta :
#         model =Priority
#     priority_type = factory.Faker('word')#factory.Faker("random_element",elements=['Critiacl','Major','Blocker','Low','Medium'])
#     slug = factory.LazyFunction(uuid.uuid4)
#     user = factory.SubFactory(UserFactory)
#     description = factory.Faker("paragraph")
#     create_date = factory.LazyFunction(datetime.datetime.now)
#     update_date = factory.LazyFunction(datetime.datetime.now)


# class TaskFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Task

#     sector = factory.SubFactory(SectorFactory)
#     user  = factory.SubFactory(UserFactory)
#     slug = factory.LazyFunction(uuid.uuid4)
#     source =factory.LazyFunction(lambda: Source.objects.first() or SourceFactory())
#     issue_type = factory.SubFactory(IssueFactory)
#     customer_id = factory.Faker("word")
#     title = factory.Faker("sentence")
#     description = factory.Faker("paragraph")
#     support_type = factory.LazyFunction(lambda: Support.objects.first() or SupportFactory())
#     status = factory.LazyFunction(lambda: Status.objects.first() or StatusFactory())
#     priority = factory.SubFactory(PriorityFactory)
#     start_date = factory.LazyFunction(datetime.datetime.now)
#     end_date = factory.LazyFunction(datetime.datetime.now)
#     assigned_to = factory.LazyFunction(lambda: User.objects.first() or UserFactory())
#     create_date = factory.LazyFunction(datetime.datetime.now)
#     update_date = factory.LazyFunction(datetime.datetime.now)