# Django Note -- Get Started

## Some useful commands

- create a project: `django-admin startproject <project-name>`
- create an app: `python3 manage.py startapp <app-name>`
- start the webserver for development: `python3 manage.py runserver [[ip:]port]`
- check sql command going to run: `python3 manage.py sqlmigrate`
- apply database changes: `python3 manage.py migrate`
- play with API in shell: `python3 manage.py shell`
- create an admin user: python3 manage.py createsuperuser

## Some concepts to learn

- project vs app
    project can include multiple apps and an app can be included in different projects. In Django, app means a Web Application.

- view
    web pages and other content are delivered by views. Each view is represented by a simple Python function (or method, in the case of class-based views). Django will choose a view by examing the URL that's requested.

## Some files' function

- views.py in an app's directory: 
- urls.py in an app's directory: map the view to a URL. urls.py creates a set of URLconf.
- models.py in an app's directory: describe the model for the database

## Something important

### models

- add `__str__()` to each models: not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin



## References

### Model

- [Accessing related objects](https://docs.djangoproject.com/en/2.1/ref/models/relations/): More information on model relations
- [Field lookups](https://docs.djangoproject.com/en/2.1/topics/db/queries/#field-lookups-intro): How to use double underscores to perform field lookups via the API
- [Database API reference](https://docs.djangoproject.com/en/2.1/topics/db/queries/): Full details on the database API
- [URL dispatcher](https://docs.djangoproject.com/en/2.1/topics/http/urls/): insturctions in the use of URLconfs
- [Template Guide](https://docs.djangoproject.com/en/2.1/topics/templates/)
- [HttpRequest](https://docs.djangoproject.com/en/2.1/ref/request-response/): Request and Response Documentation
- [Generic View](https://docs.djangoproject.com/en/2.1/topics/class-based-views/)
- [Selenium](http://seleniumhq.org/): in-browser framework to test html and javascript
- [LiveServerTestCase](https://docs.djangoproject.com/en/2.1/topics/testing/tools/#django.test.LiveServerTestCase): integrations with tools like Selenium
- [Tesing in Django](https://docs.djangoproject.com/en/2.1/topics/testing/)
- [the static files howto](https://docs.djangoproject.com/en/2.1/howto/static-files/)
- [the staticfiles reference](https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/)
- [deploying static files](https://docs.djangoproject.com/en/2.1/howto/static-files/deployment/): how to use static files on real server
- [list display](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)
- [template loading documentation](https://docs.djangoproject.com/en/2.1/topics/templates/#template-loading)
- [Topic Guides](https://docs.djangoproject.com/en/2.1/topics/)
- [How-to guides](https://docs.djangoproject.com/en/2.1/howto/)
- [FAQ](https://docs.djangoproject.com/en/2.1/faq/): Common questions
- [guides for projects for public use](https://docs.djangoproject.com/en/2.1/howto/deployment/)
- [package django app](https://docs.djangoproject.com/en/2.1/intro/reusable-apps/)
