UNSW Catalog
============

The official, open-source, unofficial UNSW Handbook designed by students, for students.

Currently a proof-of-concept.

## Installation ##

This project, being entirely implemented in Python, is incredibly easy to install/deploy/migrate to other environements.

We highly recommend you use the very popular `virtualenvwrapper` to manage you `virtualenv`s. It goes without saying that we highly recommend that you use a `virtualenv`. The reasons for these will become apparent very shortly.

1. `pip install -r requirements.txt`
2. We recommend that you specify the `DJANGO_SETTINGS_MODULE` environment variable (e.g. `export DJANGO_SETTINGS_MODULE=unsw_catalog.settings.local`) to allow version control and switching between different settings for different environments. By default, the settings module `unsw_catalog.settings.base` will be used.
3. We use `dj_database_url` for database settings. This means that you must specify the `DATABASE_URL` environment variable. See https://crate.io/packages/dj-database-url/ for how to set database url's for different database types. `dj_database_url` is great because while you definitely want to version control your settings files, you do not want to save your plaintext password in there as well.

You should set the environment variables in the `postactivate` bash script for your virtual environment. If you are new to Django, you might not understand or appreciate why this has been done. If this is the case and you want to take your Django-fu to the next level, we highly recommend that you check out [Two Scoops of Django: Best Practices for Django 1.5](http://twoscoopspress.org/products/two-scoops-of-django-1-5).

## About ##

This project was inspired by a number of things, but was probably borne out of boredom more than anything else.

## Disclaimer ##

This project is under the MIT license. 

**tl;dr** - though it is a priority of this project that all data provided is up-to-date and accurate, we cannot be held liable for any claim arising from, out of, or in connection with the software and its use, yada, yada, yada.

## TODO ##

- [ ] School is not parsed for some courses
- [ ] Faculty format given by the XML in `head` is slightly funky (no space separation). Use the summary field instead.
- [ ] `ManyToManyFields` for exclusions and prerequisites of courses
    + [ ] Write a CharField for the exlusions and prerequisites and override the `save` method to parse these into `Course`s and save to the respective set
- [x] Test `Meeting` parsing
- [ ] Instructor information
- [ ] Additional information is available in the semester summary. Decide what to do with it, i.e. where to store it
    + [ ] Add `Semester` model  
- [ ] Filter by course code prefix
- [ ] Customize default Django admin functionality 
- [ ] Customize RESTful API functionality
- [x] Migrate to Amazon RDS from Heroku Postgres
    + [ ] Test spider from heroku
    + [ ] Scrape data to DB
- [ ] Set up static files and templates and begin working on views
    + [x] templates
    + [ ] static files
- [ ] Amazon affiliate program
    + [ ] Add `Book` Model
    + [ ] Scrape data    
- [ ] Webmaster
- [ ] Analytics
- [ ] Migrate from sqlite to Postgres and fix field length -related bugs
- [ ] Hit Count and Popularity view
- [ ] Capacity progress bar
- [ ] Punchcard timetable
- [ ] `TimeField` for start and end times 
- [ ] I'm Feeling Lucky
- [ ] Done this course? Rate it
- [ ] Filter by days, start time, etc.
- [ ] Campus Map
- [ ] Write a better README