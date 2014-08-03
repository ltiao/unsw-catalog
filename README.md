UNSW Catalog
============

The open-source *unofficial* UNSW Handbook designed by students, for students.

Currently proof-of-concept.

TODO:

- School is not parsed for some courses
- Faculty format given by the XML in `head` is slightly funky (no space separation). Use the summary field instead.
- `ManyToManyFields` for exclusions and prerequisites of courses
    + Write a CharField for the exlusions and prerequisites and override the `save` method to parse these into `Course`s and save to the respective set
- Test `Meeting` parsing
- Additional information is available in the semester summary. Decide what to do with it, i.e. where to store it
- Filter by course code prefix
- Customize Django admin
- Migrate to Amazon RDS from Heroku Postgres
    + Test spider from heroku
- Set up static files and templates and begin working on views