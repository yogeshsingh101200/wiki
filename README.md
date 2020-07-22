# Wiki

Wikipedia-like online encyclopedia.

## To Run App locally
first
```
pip install -r requirements.txt
```
then
```
python manage.py runserver
```

## About
- Main route lists all encyclopedia entries.
- On visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, renders contents of that encyclopedia entry in HTML.
- Search box in side bar allows user to search for an entries. if a match is found user is taken to the page else entries that are substring of query are listed.
- User can create new page by entering content in markdown format and user can also edit content of the encyclopedia entry
- Clicking “Random Page” in the sidebar takes to a random encyclopedia entry.
