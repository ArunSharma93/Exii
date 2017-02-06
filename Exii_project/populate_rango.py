import os
from random import randint


def populate():
    python_cat = add_cat('Python')

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",
        views = randint(1,100))

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        views = randint(1,100))

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        views = randint(1,100))

    django_cat = add_cat("Django")

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        views = randint(1,100))

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views = randint(1,100))

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
        views = randint(1,100))

    frame_cat = add_cat("Other Frameworks")

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views = randint(1,100))

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
        views = randint(1,100))

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Exii_project.settings')

    import django
    django.setup()
    from rango.models import Category, Page

    populate()