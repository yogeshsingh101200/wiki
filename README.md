# Wiki

Wikipedia-like online encyclopedia.

## To Run App locally
```
pip install -r requirements.txt

export SECRET_KEY=<your_secret_key_here>

python manage.py runserver
```

optionally, run
```
python manage.py migrate
```
to turn off warning about migrations.

## About
- Main route lists all encyclopedia entries.
- On visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, renders contents of that encyclopedia entry in HTML.
- Search box in side bar allows user to search for an entries. if a match is found user is taken to the page else entries that are substring of query are listed.
- User can create new page by entering content in markdown format and user can also edit content of the encyclopedia entry
- Clicking “Random Page” in the sidebar takes to a random encyclopedia entry.
