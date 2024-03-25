# Testing

Click [Here](README.md) to return back to the README.

Calm Cadence was tested thoroughly throughout development as new features were added; and bugs remedied as they arose. 

Additional code validation, structured user acceptabce testing and user story testing has also been carried out an is detailed below.

## HTML Validation

[W3C Markup Validation](https://validator.w3.org/) was used to validate HTML code for all templates used in the project.

HTML code stripped of Django template tags was accessed by viewing the page source of each template. Code was validated by direct input. Where errors in HTML were detected these were remedied. Any code which had to be fixed was validated again by direct input to check the error had been resolved, and then by URI

Unremedied errors consisted of the behaviour of Django template elements which I was unable to change.

### Results for HTML URI Testing:
<details><summary>Click to expand</summary>

Home page:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmlhomepage.JPG>

Registration:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmlreg.JPG>

Login:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmllogin.JPG>

Event List:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmleventlist.JPG>

Event Detail:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmleventdetail.JPG>

Create Event/Update Event:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmlcreateevent.JPG>

User Events: 

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmluserevents.JPG>

Attending:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmluserattend.JPG>

Admin Approval Page:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmladminapp.JPG>

Update About Page:

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/htmlupdate.JPG>

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

Python was validated using the **[CI Python Linter](https://pep8ci.herokuapp.com)**

Only files in which I wrote my own code were validated. The rest of the python code in the project was part of thje Django installation package.

 #noqa comments were used on lengthy lines of code (E501), which I was not able to shorten without disrupting site functionality.

- For the main app this includes line 54 of views.py

- For the events app this includes lines 16 and 23 of models.py; lines 9 - 11 and 13-17 of urls.py; lines 15 and 29 of forms.py; and lines 106, 140, 168, 170, 222, 254, 257, 318, 334, 337, 355, and 358 of views.py;

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

    *due to limitations of the linter line 170 of event/views.py is split over two lines of display inside the linter within one line of code; meaning a trailing white space error (W291) persists in the linter where no trailing white space is present and despite #noqa.

From the `calm_cadence` project directory:

| File | Grade |
| -----| ------|
| `urls.py` | pass |


## Site Lighthouse Testing

The website was tested for load times using Lighthouse, the results are below. 

Desktop:

![Lighthouse Desktop](https://github.com/Libbu/ci-capstone-project/blob/main/media/lighthousefinal.JPG)

Mobile:

![Lighthouse Desktop](https://github.com/Libbu/ci-capstone-project/blob/main/media/lighthousefinalmob.JPG)

## Cross-Browser Testing

[Browserling](https://www.browserling.com/edge-testing) was used to test Calm Cadence across common web browsers:

Microsoft Edge
Mozilla Firefox
Opera

No bugs in display were found during this test.

The site was tested manually on my own devices for:

Google Chrome
Safari

## Manual Site Testing

### User-Acceptance-Criteria (UAC) Derived Testing

Test cases were grouped into logical units of site functionality for this task:

- TC001 Site responsiveness.
- TC002 Site purpose on landing (home) page.
- TC003 Navigation and authentication.
- TC004 Viewing events.
- TC005 User create, edit, delete own events.
- TC006 Attending and cancelling attendance.
- TC007 Users can see own attending/attended events.
- TC008 Users can see own organising/organised events.
- TC009 User create, edit and delete own comments.
- TC010 Site admin functionality and admin role-specific access.

![Testing 1](https://github.com/Libbu/ci-capstone-project/blob/main/media/unittesting1.JPG)

![Testing 2](https://github.com/Libbu/ci-capstone-project/blob/main/media/unittesting2.JPG)

![Testing 3](https://github.com/Libbu/ci-capstone-project/blob/main/media/unittesting3.JPG)

![Testing 4](https://github.com/Libbu/ci-capstone-project/blob/main/media/unittesting4.JPG)

### User Story Testing

- As a **site user** I can **easily navigate through the site** so that I can **view the content I want to**.

Calm Cadence has all information organised in correct areas with a clear, responsive navigation bar across the top of all pages in the website.

The navigation bar has all the links correctly connected so that users can easily find the information and functionality they need.

Drop-down menus prevent clutter in the navigation pane and contain logically organised links within

Below is a sample of what unregistered or logged out users will see, and what administrators see; regular site users will not see the option for an Admin drop down, and users who have yet to register or who have logged out will only be able to see the options to Register or Login.

For unregistered users:

![Unregistered User Nav Bar](https://github.com/Libbu/ci-capstone-project/blob/main/media/navbarloggedout.JPG)

For registered site users (admin access also displayed)

![Admin Nav Bar](https://github.com/Libbu/ci-capstone-project/blob/main/media/adminnav.JPG)

![Admin Nav Bar Mobile](https://github.com/Libbu/ci-capstone-project/blob/main/media/adminnavmob.JPG)


- As a **site user** I can **access an about section** so that **I can understand the purpose of the page**.

The "About our Community" section in Calm Cadence in prominently displayed on the home page. The text can be updated by site administrators as an when needed.

![About Us](https://github.com/Libbu/ci-capstone-project/blob/main/media/aboutpc.JPG)

![About Us Mobile](https://github.com/Libbu/ci-capstone-project/blob/main/media/aboutmob.png)

- As a **site user** I can **register/login** so that I can **access content only for logged-in users**.

For site-users who are not logged in, the only links in the nav bar available to them will be the home page, registration, and login pages. The registration and login pages provide a seamless aesthetic experience for first time users and those returning to the site on both large and small screens

![Registration](https://github.com/Libbu/ci-capstone-project/blob/main/media/registerpc.JPG)

![Login](https://github.com/Libbu/ci-capstone-project/blob/main/media/loginpc.JPG)

The forms are responsive on mobile;

![Registration](https://github.com/Libbu/ci-capstone-project/blob/main/media/registermob.png)

![Login](https://github.com/Libbu/ci-capstone-project/blob/main/media/signinmob.png)

Calm Cadence provides user feedback so that users know they are logged in, and who they are logged in as.

![Registration](https://github.com/Libbu/ci-capstone-project/blob/main/media/loginconf.JPG)

- As a **site user** I can **logout** so that I can **disconnect from the app**.

Logged in site users are able to logout by navigating to the logout page, and clicking the logout button

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/logoutpc.JPG)

![Logoutmob](https://github.com/Libbu/ci-capstone-project/blob/main/media/logoutmob.JPG)

- As a **site user** I can **see a paginated list of run events** so that **I can join in**.

The Event List page is accessible to logged in site users under the Events dropdown menu. The Events List page is paginated by 6, and lists upcoming runs organised by other users.

It is ordered from runs that will occur soon first, to those that are scheduled a long time from today. Cards featuring images are used to display the event along with some summary detail. Given the nature of the page, runners may choose to use the image field to upload a proposed route. These cards hover slightly when moused over.

![Event List PC](https://github.com/Libbu/ci-capstone-project/blob/main/media/eventlistpc.JPG)

![Event List Mobile](https://github.com/Libbu/ci-capstone-project/blob/main/media/eventlistmob.png)

- As a **site user** I can **click on an event in the list of events** so that **I can see more information**.

Users can click on the title of a single responsive event card to open a page with more detail about the event

![Event card PC](https://github.com/Libbu/ci-capstone-project/blob/main/media/eventcard.JPG)

The event detail page contains details of the run the organiser is wishing to schedule, any images they have uploaded (a placeholder image appears if they choose none), as well as the options to register attendance, cancel attendance, leave a comment, edit the event (if the event organiser is visiting an event detail page of their own) or delete the event (for the event organiser and also for site administrators.)

![Event detail PC](https://github.com/Libbu/ci-capstone-project/blob/main/media/eventdetailpc.JPG)

![Event detail mobile](https://github.com/Libbu/ci-capstone-project/blob/main/media/eventdetailmob1.png)

![Event detail mobile](https://github.com/Libbu/ci-capstone-project/blob/main/media/eventdetailmob2.png)

- As a **site user** I can **expect that events will be removed from the listing page when expired** so that **the page doesn't become cluttered**.

Events disappear from the Event List page once the event date has passed.

- As a **site user** I can **create events** so that **other users can participate with me**.

The Create Event option under Events in the Navigation Bar allows registered users to access a form that they can submit to schedule their own run on which they want some company. The event they wish to create will not show to other users through the Event List until administrators have approved it. 

![Create event form](https://github.com/Libbu/ci-capstone-project/blob/main/media/createevent.JPG)

![Create event mobile](https://github.com/Libbu/ci-capstone-project/blob/main/media/createeventmob1.png)

![Create event mobile](https://github.com/Libbu/ci-capstone-project/blob/main/media/createeventmob2.png)

- As a **site user who has made an event** I can **edit my own event** so that I can **communicate changes/updates**.

Site users are able to edit their events using the same form as above through the "Update Event" button on the event detail page. The option to edit an event will show on events the site user has created for themselves only, editing an event will cause the event to return to administrators for approval before it reappears under Event Listing.

![Buttons](https://github.com/Libbu/ci-capstone-project/blob/main/media/buttonseventdetail.JPG)


- As a **site user** I can **delete my event** so that I can **remove any unwanted events that I have made**.

Site users are able to delete their events through the "Delete Event" button on the event detail page. The option to delete an event will show on events the site user has created for themselves only, A modal notification will appear to confirm the user's wishes to delete their event, and make them aware that it cannot be reversed.

![Buttons](https://github.com/Libbu/ci-capstone-project/blob/main/media/buttonseventdetail.JPG)

![Delete Modal](https://github.com/Libbu/ci-capstone-project/blob/main/media/deletemodal.JPG)

- As a **site user** I can **see a consolidated list of events I've said I will attend and those I have attended** so that **I can keep track of my activity**.

Under the Events drop-down menu users are able to navigate to a section of the website called Attendance. Here they will find two sections; "Events I'm going to:" lists events they are going to, "Events I've been at:" lists events they have been at. The design aesthetic of this page is consistent with that used in the Event List, with the exception that it is not intended to paginate.

![Attendance PC](https://github.com/Libbu/ci-capstone-project/blob/main/media/attendancepc.JPG)

![Attendance mob](https://github.com/Libbu/ci-capstone-project/blob/main/media/attendancemob.png)

- As a **site user** I can **see a consolidated list of events I've organised** so that **I can keep track of my plans**.

Under the Events drop-down menu users are able to navigate to a section of the website called My Events. Here they will find two sections; "Future runs you've created:" lists events they have organised which have not yet happened, "Past runs you've organised:" lists past events they have organised. The design aesthetic of this page is consistent with that used in the Event List, with the exception that it is not intended to paginate.

![My Events PC](https://github.com/Libbu/ci-capstone-project/blob/main/media/myeventspc.JPG)

![My Events mob](https://github.com/Libbu/ci-capstone-project/blob/main/media/usereventsmob.png)

- As a **site user** I can **say that I will attend an event** so that **the event creator knows I will be there**.

On the Event Detail of an individual event registered, logged-in users can click or tap the "Count me in!" button to register their attendance. They can then cancel this with the "Cancel Attendance" button. If the run is already full they will be redirected to the Event List page with a message informing them that the run is full.

Count me in!

![attendance pc](https://github.com/Libbu/ci-capstone-project/blob/main/media/attendpc.JPG)

![cancel attendance](https://github.com/Libbu/ci-capstone-project/blob/main/media/cancelattendmob.JPG)

- As a **logged-in site user** I can **write comments on events** so that I can **engage with the community**.

A responsive comment form and comment section is present on all Event Detail pages. Users can create comments, edit and delete their own comments, and site administrators can delete any comment.

![Comments pc](https://github.com/Libbu/ci-capstone-project/blob/main/media/commentsectionpc.JPG)

![Comments mobile](https://github.com/Libbu/ci-capstone-project/blob/main/media/commentsectionmobile.JPG)

#### Administrator user stories

- As a **site admin** I can **Delete any events on the site** so that **I can better control content**.

Site administrators will always have acess to a delete button under Event Detail, and they will always be allowed to delete events regardless of whether they are the organiser or not.

- As a **site admin** I can **approve events created by registered site users** so that **the events show for all site users**.
 
 Site administrators have access to the role-specific Admin navigation dropdown menu, from which they can access the Admin Approval page. Styled consistently with the Event Detail page, events created by users come here first for approval before they will show on the Event List page. The Event Cards here feature the option to Approve the event or Decline and Remove it.

![Admin approval pane pc](https://github.com/Libbu/ci-capstone-project/blob/main/media/adminapprovepc.JPG)

![Admin approval pane mobile](https://github.com/Libbu/ci-capstone-project/blob/main/media/adminapprovemob.png)

- As a **site admin** I can **update the about section on the homepage** so that **changes can be displayed to site users**.

Site administrators have access to the role-specific Admin navigation dropdown menu, from which they can access the Update About form. This allows them to publish an updated about us section to the homepage.

![Update about pc](https://github.com/Libbu/ci-capstone-project/blob/main/media/updateaboutpc.JPG)

![Update about mobile](https://github.com/Libbu/ci-capstone-project/blob/main/media/updateaboutmob.JPG)

- As a **site admin** all site users can **contact me through a form** so that I can **collaborate/answer questions**.

Due to prioritisation this feature was not implemented in the current release. It will be looked at for future releases. 



https://www.browserling.com/edge-testing


Click [Here](README.md) to return back to the README.
