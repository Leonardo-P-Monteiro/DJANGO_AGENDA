

    # # django_categories = (Category(name=name) for name in categories)

    # # for category in django_categories:
    # #     category.save()

    # # django_contacts = []

    # # for _ in range(NUMBER_OF_OBJECTS):
    # #     profile = fake.profile()
    # #     email = profile['mail']
    # #     first_name, last_name = profile['name'].split(' ', 1)
    # #     phone = fake.phone_number()
    # #     created_date: datetime = fake.date_this_year()
    # #     description = fake.text(max_nb_chars=100)
    # #     category = choice(django_categories)

    # #     django_contacts.append(
    # #         Contact(
    # #             first_name=first_name,
    # #             last_name=last_name,
    # #             phone=phone,
    # #             email=email,
    # #             created_date=created_date,
    # #             description=description,
    # #             category=category,
    # #         )
    # #     )

    # # if len(django_contacts) > 0:
    # #     Contact.objects.bulk_create(django_contacts)