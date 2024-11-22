# Django BDD UI Testing With Behave and Playwright

This project was created to validate some issues around creating BDD UI tests using Behave, Behave-Django and Playwright.

## Issues

- The main issue experienced during the development of the BDD UI tests using Behave and Django was the data in the database was getting flushed in between scenarios.
- This was not ideal as when the first scenario runs, everything will work as expected and then subsequent scenario will fail due to the flushing take place after the first scenario.
- This issue and other issues will be documented further in the docs in the [dis-wagtail](https://github.com/ONSdigital/dis-wagtail) repo.

## Links to Django Docs That Validate The Issues Experienced With Behave and Playwright

- [Django Testing Topics](https://docs.djangoproject.com/en/5.1/topics/testing/)
- [Django Testing Overview](https://docs.djangoproject.com/en/5.1/topics/testing/overview/)
- [Django Testing Tools](https://docs.djangoproject.com/en/5.1/topics/testing/tools/)
- [Django Static Files](https://docs.djangoproject.com/en/5.1/howto/static-files/)
- [Django Static Files Deployment](https://docs.djangoproject.com/en/5.1/howto/static-files/deployment/)
- [Django Testing Tools](https://docs.djangoproject.com/en/5.1/topics/testing/tools/)
- [Django Advanced Testing](https://docs.djangoproject.com/en/5.1/topics/testing/advanced/)

## To Run The Project and BDD Tests

To Install The Dependencies

```bash
poetry install
```

To Run The Local Dev Env Server: This can be useful if you want to spin up the local dev env server and tweak the step definitions in `steps.py` to hit the local dev env server when you run the Behave tests using `python manage.py behave` to see the tests working/ mock the behaviour without using the Django Test Client. This can be useful to see visually what should be happening when the tests are run.

```bash
python manage.py runserver
```

To Run The Behave Tests Correctly Using Django's Test Client: Make sure to have configured the step definitions in `steps.py` to use the Django Test Client instead of the local dev env server.


```bash
python manage.py behave
```
