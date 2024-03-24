# Testing

Click [Here](README.md) to return back to the README.

## HTML Validation

[W3C Markup Validation](https://validator.w3.org/) was used to validate HTML code for all templates used in the project.

HTML code stripped of Django template tags was accessed by viewing the page source of each template. Code was validated by direct input. Where errors in HTML were detected these were remedied. Any code which had to be fixed was validated again by direct input to check the error had been resolved, and then by URI

Unremedied errors consisted of the behaviour of Django template elements which I was unable to change.

### Results for HTML URI Testing:
<details><summary>click to expand</summary>

Home page:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmlhomepage.JPG>

Registration:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmlreg.JPG>

Login:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmllogin.JPG>

Event List:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmleventlist.JPG>

Event Detail:

Create Event/Update Event:

User Events: 

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmluserevents.JPG>

Attending:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmluserattend.JPG>

Admin Approval Page:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmladminapp.JPG>

Update About Page:

Logout:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmllogout.JPG>

</details>

## CSS Validation

Calm Cadence has passed CSS validation using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

![CSS validation](https://github.com/Libbu/ci-capstone-project/blob/main/media/cssvalid.JPG)

## JavaScript Validation

Javascript was validated with the [JSHint Validator](https://jshint.com)

There were 26 warnings associated with variable names (const and let ) and their availability on different browsers. Bootstrap was flagged as an undefined variable however it is imported elsewhere in the project, outside of script.js.

![JavaScript validation](https://github.com/Libbu/ci-capstone-project/blob/main/media/jsvalid.JPG)

## Python Validation

Python was validated using the ![CI Python Linter](https://pep8ci.herokuapp.com/)

Only files in which I wrote my own code were validated. The rest of the python code in the project was part of thje Django installation package.

#noqa comments were used on lengthy lines of code (E501), but which I was not able to shorten without disrupting site functionality.

- For the main app this includes line 54 of views.py

- For the events app this includes lines 16 and 23 of models.py; lines 9 - 11 and 13-17 of urls.py

From the `main` app:

| File | Grade |
| ---- | ----- |
| `admin.py` | pass |
| `models.py` | pass |
| `urls.py` | pass |
| `forms.py` |pass |
| `views.py` | pass w/noqa |

From the `events` app:

| File | Grade |
| ---- | ----- |
| `admin.py` | pass |
| `models.py` | pass w/noqa |
| `urls.py` | pass w/noqa |
| `forms.py` |pass |
| `views.py` | pass w/noqa*|

    *due to limitations of the linter line 170 of views is split over two lines meaning a trailing white space error (W291) persists where no trailing white space is present and despite #noqa.

From the `calm_cadence` project directory:

| File | Grade |
| -----| ------|
| `urls.py` | |