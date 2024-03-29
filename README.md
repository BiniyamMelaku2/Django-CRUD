# Django-CRUD

Django Models - Building A Blog Application With Django 

## Resources

-[Building A Blog Application With Django](https://djangocentral.com/building-a-blog-application-with-django/)

-[How to Create a Blog Application Using Django](https://pythonsansar.com/how-create-blog-application-using-django/)

-[Django timezone.now](https://stackoverflow.com/questions/10783864/django-1-4-timezone-now-vs-datetime-datetime-now)

-[starter file](https://github.com/TobeTek/Zuri/tree/main/starter-files/Django-CRUD)

#### 1. Create a virtual env 

> $ python3 -m venv venv

#### 2. Activate virtual env

> $ source venv/bin/activate


#### 3. Install Django on venv

> (venv) $ sudo pip3 install Django

#### 4. Create a Django project

> $ django-admin startproject I4G000675LXH

#### 5. create a Django app

> $ sudo python3 manage.py startapp blog

#### 6. Add the blog app to the main_projects INSTALLED_APPS. 
open your `settings.py` file
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
]
```

#### 7. Create a new model in the `blog` app called `Post`. 
It should have the following fields:
Database `Models.py`
```
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    
 
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
```

#### 8. Migrate the change into our database.

```
(django) $ sudo python3 manage.py makemigrations
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post

(django) $ sudo python3 manage.py migrate

  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
```

#### 9. Creating An Administration Site

> (django) $ sudo python3 manage.py createsuperuser

> (django) $ sudo python3 manage.py runserver

#### 10. Adding Models To The Administration Site

Open the `blog/admin.py` file to edit with...

```
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

#### 11. Building Views 
- In `blog/views.py`,  create a new view/class `PostListView`, which inherits django’s generic `ListView`,  
it’s config/attributes should be:

```
model = Post
```

- Create another view, PostCreateView, which inherits django’s generic CreateView, with attributes:

```
model = Post
fields = “__all__”
success_url  = reverse_lazy(“blog:all”)
```
 
- Create another view, PostDetailView, which inherits django’s generic DetailView, with attributes:

```
model = Post
```
 
- Create another view PostUpdateView, which inherits django’s generic UpdateView, with attributes:

```
model = Post
fields = “__all__”
success_url  = reverse_lazy(“blog:all”)
```
 
- Create another view PostDeleteView, which inherits django’s generic UpdateView, with attributes:

```
model = Post
fields = “__all__”
success_url  = reverse_lazy(“blog:all”)
```

#### 12. Adding url patterns for Views

- Create a file, `blog/urls.py`, if it doesn’t already exist and update the contents.

#### 13. Creating templates for Views

- Create a new folder `templates` under the blog app.  Make templates to render the results. Configure the template settings.

- Check out 

> (django) $ sudo python3 manage.py runserver

`http://127.0.0.1:8000/`

`http://127.0.0.1:8000/admin/`

`http://127.0.0.1:8000/blog/`

#### Screenshots

![](screenshot.JPG)
