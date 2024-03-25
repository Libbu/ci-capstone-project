# Calm Cadence (Capstone Project for CI - Coleg Gwent Bootcamp)

![Calm Cadence](https://github.com/Libbu/ci-capstone-project/blob/main/media/amiresponsive.JPG)

Calm Cadence is a website which aims to bring together runners of any and all abilities who prefer to take things slow. As a social running community the focus is more on camaraderie, support and making running accessible rather than performance. The idea was sparked in response to frequent posts on social-media sites such as Facebook from casual runners looking for people to join them in training either for social or safety reasons, or to help them be accountable to themselves and their programme. The goal of Calm Cadence is to apply a more structured event booking approach in order to help people find other runners to join them. Despite pervasive elitism in the field, running is for everyone regardless of pace or time and it is hoped that a community built around these principles will bring more people to the sport.

# Purpose

This website has been built using the Django framework for backend and frontend functionality. 

This website provides all essential features to meet its stated goal, such as allowing users to register, create events, attend events, engage with the community through comments on events, see records of events they have created/attended, as well as administrator specific access to approve or decline user-created events, delete comments, and update text on the homepage.

Taking the lead of other sport-related apps such as Strava and Spond; users must be registered in order to access the events on the site.

This website was developed for the capstone project at the conclusion of the Code Institute Bootcamp through Coleg Gwent.

The live website can be accessed [here](https://calm-cadence-4a2a00c3b627.herokuapp.com/).
___

# UX Design

Target audience:
- Individuals in the South Wales area who are looking for an inclusive running community through which they can meet like-minded (and like-paced) runners.

## User stories

### Epic: User Navigation

- As a **site user** I can **easily navigate through the site** so that I can **view the content I want to**.
- As a **site user** I can **access an about section** so that **I can understand the purpose of the page**.


### Epic: User Registration

- As a **site user** I can **register/login** so that I can **access content only for logged-in users**.
- As a **site user** I can **logout** so that I can **disconnect from the app**.


### Epic: User Event Management

- As a **site user** I can **see a paginated list of run events** so that **I can join in**.
- As a **site user** I can **click on an event in the list of events** so that **I can see more information**.
- As a **site user** I can **expect that events will be removed from the listing page when expired** so that **the page doesn't become cluttered**.
- As a **site user** I can **create events** so that **other users can participate with me**.
- As a **site user who has made an event** I can **edit my own event** so that I can **communicate changes/updates**.
- As a **site user** I can **delete my event** so that I can **remove any unwanted events that I have made**.
- As a **site user** I can **see a consolidated list of events I've said I will attend and those I have attended** so that **I can keep track of my activity**.
- As a **site user** I can **see a consolidated list of events I've organised** so that **I can keep track of my plans**.

### Epic: User Community Engagement

- As a **site user** I can **say that I will attend an event** so that **the event creator knows I will be there**.
- As a **logged-in site user** I can **write comments on events** so that I can **engage with the community**.

## Administrator user stories

### Epic: Site Administration

- As a **site admin** I can **Delete any events on the site** so that **I can better control content**.
- As a **site admin** I can **approve events created by registered site users** so that **the events show for all site users**.
- As a **site admin** I can **update the about section on the homepage** so that **changes can be displayed to site users**.
- As a **site admin** all site users can **contact me through a form** so that I can **collaborate/answer questions**.

## UAC

### User Acceptance Criteria Derived From User Stories

1. The website should be responsive on any device.

2. The website should have a homepage that makes it's purpose clear.

3. Website navigation should be clear and intuitive for users.

4. Website navigation bar should be accessible from any page on the site.

5. A registration form allowing users to create an account is present.

6. The website should have a list of events the user can view after logging in.

7. Each event should link to a separate page where more detail can be viewed.

8. Users can access a form enabling them to create their own events. 

9. Each event should have the option for users to attend it via clicking a button.

10. Users are able to edit or delete their own events.

11. Users can easily keep track of their planned/past attendance.

12. Users can easily keep track of events they have planned themselves.

13. Users are able to leave comments on events.

14. The website allows administrators to approve or decline event posts.

15. The website allows administrators to delete any event or comment as necessary.

16. The website allows administrators to update the "about" section text on the homepage.

17. Website administrators are contactable through a contact form. 
___

## Scope

### High-level Essential Features

 - A home page
 - A navigation menu
 - Authentication-dependent access
 - An event list page
 - An event detail page
 - Front-end add, read, edit and delete (CRUD) functionality for events
 - Admin-specific approval and deletion rights
 - Registration, login and logout pages


| **Home Page**   | **Event List**   | **Event Details** | **Website as a whole** |
|---|---|---|---|
| Purpose of website | List of Events | Event Content | Site nav bar |
| Calls to action |Event detail loads on click | Comment Section| Footer with social media links |
| Admin can update 'About Us' | | Ability to attend/cancel attendance| Sign-in/up/out options |
| | |Role-specific access to edit/delete |Ability to create event |
| | | Messages confirming user actions|Messages confirming user actions|
| | | |Admin have site-wite delete access|
| | | |Consistent Site Aesthetic |


|  **Feature** | **Value**  |  **Effort** |
|---|---|---|
| Home Page |  High |  Medium |
| Paginated List of Events  | High  |  Medium |
| User Registration | High  | Low  |
| User Login/Logout| High  | Low  |
| Navbar|  High | Low  |
| Footer | Medium  |Low   |
| Users Can Create Events | High | High |
| Users Can Edit Own Events| High  |High |
| Users Can Delete Own Events | High | High |
| Users Can Can Attend Events | Medium | High |
| Users Can Cancel Attendance| Medium | High |
| Admin Can Approve Events | High | Medium |
| Admin Can Delete User-Created Content | High | Medium |
| Users Can Comment | Medium | High |
| Form to Contact Site Admin | Low | High |


| Feature  |  Priority |
|---|---|
| Home Page | 1 |
| Paginated List of Events  | 1  |
| User Registration | 1  |
| User Login/Logout| 1  |
| Navbar|  1 |
| Footer | 3 |
| Users Can Create Events | 1 |
| Users Can Edit Own Events| 1  |
| Users Can Delete Own Events | 1 |
| Users Can Can Attend Events | 2 |
| Users Can Cancel Attendance| 2 |
| Admin Can Approve Events | 1 |
| Admin Can Delete User-Created Content | 4 |
| Users Can Comment | 4|
| Form to Contact Site Admin | 5 |

___

## Design

Calm Cadence is intended to have a simple layout, with a colour-scheme and aesthetic drawing from both common Holistic Wellness and Fitness marketing schema.

The home page is intended to give a professional impression, soothing the viewer with calming hues and a subtle background gradient, while hints of energy are present in the colour used to render text as well as through the use of images.

The colour aesthetic is kept consistent throughout the website; from registration and login pages, to the form users use in order to create events, and the admin approval page for site administrators.

### Colour Scheme

![Palette](https://github.com/Libbu/ci-capstone-project/blob/main/media/palatte2.JPG)

Deep blue-green hues are the dominant feature of the website; with tea-green selected for text colour against this background on account of the contrast it provides.

A light pink and deep purple which each coordinate well with the dominant colours are in use in hover effects on site buttons.

Overall, this colour palette creates a sense of calm with a touch of energy. The blue shades are associated with tranquility and the natural world, while the tea-green injects the element of physical exertion running entails. The abrput shift in colour when the users hover over site button elements contributes to feedback that an action is possible.

### Typography

[Raleway](https://fonts.google.com/specimen/Raleway) is elegant, in use on many websites with a focus on physical activity, and forms part of a clean, minimalistic design. This font is used in headings and subheadings.

[Lato](https://fonts.google.com/specimen/Lato) is lightweight, minimalistic, and often found used in websites promoting wellness or health. All other text on the website uses Lato.

### Images

The images in this project were all sourced from [Unsplash](https://unsplash.com/)

Sample event posts with routes as images are using screen-shots from the route-planner on [MapMyRun](https://www.mapmyrun.com/)

The favicon was edited from the file at the following URL using [Favicon Generator](https://www.favicon.cc/?action=edit_image&file_id=856421)

## Visual Effects

#### Shadows

A shadow is used on the "About Our Community" section on the home page to give a sense of depth to the text present. Combined with the background gradient, as the user scrolls to this section it seems to appear from the page and occupy physical space within their area of sight.

#### Image-Overlays

As the user mouses over either of the two images beneath the "About Our Community" section on the home page, a translucent overlay drops down containing a link to register or log in to the site respectively. On mobile devices this overlay appears if the users tap the images. This perhaps unexpected but nonetheless unbotrusive visual stimulation is intended to engage the user in the website as a whole.

#### Hover Effect

Hover effects are present in many areas of the webpage.

The navbar links, as well as event links and all buttons include a hover effect in order to promote interactivity. When a user hovers over a link or button, its colour or background colour changes. This feature has also been used to provide feedback to the user, for example on hovering over the delete button the background becomes fairytale-pink and the text deep-purple; this abrupt change from the website aesthetic of light-on-dark to dark-on-light alerts the user that they are about to take a certain type of action.

A hover effect which causes the event card to lift slightly on the event listing page has been used to further promote interactivity as users browse events.

Hover effects are also present on the social media icons in the footer, reinforcing to the user that further engagement with the community is just a click away.

#### Confirmation Modals

Modals have been used to display confirmation messages to users when they select either an event or comment to delete. The aprupt change in the visual pane is intended to draw user attention to the stated consequences and irreversible nature of the deletion action.
___

## Database Design

- note: the User model displayed below refers to that provided by Django package functionality; selected fields have been included to demonstrate how they relate to the custom models created for Calm Cadence.

![ERD](https://github.com/Libbu/ci-capstone-project/blob/main/media/ERD.png)

# Structure

Page flow:

![PageFlow](https://github.com/Libbu/ci-capstone-project/blob/main/media/pageflow.png)

### Home Page

![Home Page](https://github.com/Libbu/ci-capstone-project/blob/main/media/amiresponsive.JPG)

- Uses text and images to communicate the site purpose
- Presents opportunities for further actions 

    #### User Goals:
    >   - Understand the main purpose of the website.
    >   - Have access to registration.
    >   - Be able to navigate publically available content.
    >   - Connect with affiliated social media.

    #### Website Goals:
    >   - Communicate main purpose of the page.
    >   - Engage users and interest potential memebers.
    >   - Call to action.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Sign Up Page

![Sign Up](https://github.com/Libbu/ci-capstone-project/blob/main/media/amiresponsivesignup.JPG)

- Allows users to register so that they can access site content

    #### User Goal:
    >   - Register

    #### Website Goals:
    >   - Allow user registration
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.


### Login Page

![Login](https://github.com/Libbu/ci-capstone-project/blob/main/media/amirelogin.JPG)

- Allows users to sign in

    #### User Goal:
    >   - Sign in.

    #### Website Goals:
    >   - Allows users to sign in so that they can access content.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Event List Page

![Event List](https://github.com/Libbu/ci-capstone-project/blob/main/media/amiresevent_list.JPG)

- Shows admin-approved, user-created events in order of the most recent first.
- List of events is paginated by 6 so as not to overwhelm the user.
- Each card has a link the user can click on for more details. 
- Available only to view by authenticated users.

    #### User Goals:
    >   - Browse the events
    >   - Open the events to see them in more detail.

    #### Website Goals:
    >   - Provide a list of events.
    >   - Provide some information on each event in a preview.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Event Detail Page
 
![Event Detail](https://github.com/Libbu/ci-capstone-project/blob/main/media/amireseventdetail.JPG)

- Shows the details of the run such as how many people the organiser is looking to have join them, the location and what other users are going. 
- Allows authenticated users to see and write comments on the event, as well as manage their own comments.
- Allows authenticated users to say they will attend the event, also allows them the option of cancelling their own attendance.
- Allows the event organiser to manage the event post.
- Allows superusers/site admin to delete the post and/or any comments on it.
- Available only for authenticated users.

    #### User Goals:
    >   - See the details of the event.
    >   - Indicate attendance or cancel attendance.
    >   - Leave comments on the event to ask questions if needed.
    >   - Manage the event if you are the organiser.
    >   - Delete the event and/or any comments on it if you are an administrator.

    #### Website Goals:
    >   - Show the detail of an event.
    >   - Allows users to interact with the event.
    >   - Allow users to record/cancel their attendance.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Create/Update Post Page

![Create Post](https://github.com/Libbu/ci-capstone-project/blob/main/media/createevent.JPG)

- Allows authenticated users to create a new event
- Allows event organisers to update their own event.
- Validates image file input to prevent uploading of file-types outside of those specified.

    #### User Goals:
    >   - Create a new event.
    >   - Update existing events.

    #### Website Goals:
    >   - Allow the user to create/update an event
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### User Events Page

![User Events ](https://github.com/Libbu/ci-capstone-project/blob/main/media/myeventspc.JPG)

- Allows authenticated users to see a list of events they've organised.
- Is separated into Future and Past sections.

    #### User Goals:
    >   - Keep track of events they've organised.
    >   - See a record of what they have organised in the past.

    #### Website Goals:
    >   - Keep the user engaged in the community by consolidating information.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### User Attendance Page

![User Attendance](https://github.com/Libbu/ci-capstone-project/blob/main/media/attendancepc.JPG)

- Allows authenticated users to see a list of events where they are in the attendees
- Is separated into Future and Past sections.

    #### User Goals:
    >   - Keep track of events they intend to participate in.
    >   - See a record of what they have attended in the past.

    #### Website Goals:
    >   - Keep the user engaged in the community by consolidating information.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Admin Approval Page

![Admin Approval](https://github.com/Libbu/ci-capstone-project/blob/main/media/adminapprovepc.JPG)

- Allows Site Administrators to see a list of events to approve
- Allows Site Administrators to Approve or Decline user-created Events

    #### Admin Goals:
    >   - Control user-created site content

    #### Website Goals:
    >   - Provide a moderation mechanism through which events must pass so that inappropriate content can be hidden.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Admin Update homepage "About" Section

![Admin Update](https://github.com/Libbu/ci-capstone-project/blob/main/media/updateaboutpc.JPG)

- Allows Site Administrators to update the About section on the homepage.


    #### Admin Goals:
    >   - Keep site content on the landing page relevant.

    #### Website Goals:
    >   - Allow some updates to landing page to be made in response to feedback by admin users.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Logout Page

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/logoutbig.JPG)

- Allows users to Logout

    #### User Goal:
    >   - Logout.

    #### Website Goals:
    >   - Allows users to logout after confirming they wish to do so.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.
    
___
# Development Plan

## Agile design

Prioritisation of user stories and tasks to develop Calm Cadence has followed an Agile methodology, using GitHub's projects to prioritize and track user stories and high-level development tasks. This approach enables the implementation and testing of ideas based on their importance to the project, ensuring that MVP (minimum viable product) functionality for the project's purpose is reached as soon as it can be. 

The Project Board for Calm Cadence can be found [here](https://github.com/users/Libbu/projects/7).

The following categories were applied as custom labels to project user-stories:

- Must Have
- Should Have
- Could Have
- Won't Have

### User Story Breakdown

![User Story Breakdown](https://github.com/Libbu/ci-capstone-project/blob/main/media/userstorybreakdown.JPG)

### User Story MoSCoW

![User Story MosCoW](https://github.com/Libbu/ci-capstone-project/blob/main/media/moscow.JPG)

- Note: As a primary feature of MVP for Calm Cadence is to deliver full database CRUD (create, read, update and delete) functionality for events to the end-user; the implementation of end-user features connected to this has priority over other common event-management features such as registering attendence.
___
# Wireframes

## Low-fidelity Mobile Wireframes:

### Home Page  
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidmobhome.png>
</details>

### Registration and Login Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidmobreglogin.png>
</details>

### Event List and Event Detail Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidmoblistdet.png>
</details>

### Create Event and Admin Event Approval Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidmobeventcreateadminapp.png>
</details>

### User Attendance and User-Created Events Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidmobuserevents.png>
</details>

### Admin Update 'About' Form and Logout Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidmobupdateaboutlogout.png>
</details>

## Low-fidelity Desktop Wireframes:

### Home Page  
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidpchome1.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidpchome2.png>
</details>

### Registration and Login Pages
<details><summary>click to expand</summary>
Registration:
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/registration.png>

Login:
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidpclogin.png>
</details>

### Event List and Event Detail Pages
<details><summary>click to expand</summary>
Event List:
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidpceventlist.png>

Event Detail:
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidpceventdet.png>
</details>

### Create Event Form
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidpccreate.png>
</details>


### User Attendance and User-Created Events Pages
<details><summary>click to expand</summary>
User Attendance:
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidpcuserattend.png>

User Events:
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidpcuserevents.png>
</details>

### Admin Event Approval and Admin Update 'About' Form 
<details><summary>click to expand</summary>
Admin Event Approval:
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidpcadminapp.png>

Admin Update 'About Our Community' Form:
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/lowfidpcadminupdateabout.png>
</details>

## High-fidelity Mobile Wireframes from site Screenshots:

### Home Page  
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/mobhomewf.png>
</details>

### Registration and Login Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/mobreglogin.png>
</details>

### Event List and Event Detail Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/mobeventlistdetail.png>
</details>

### Create Event and Admin Event Approval Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/mobcreateadmin.png>
</details>

### Admin Update 'About' Form and Logout Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/mobupdatelogout.png>
</details>

## High-fidelity Tablet Wireframes from site Screenshots:

### Home Page  
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/tablet1.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/tablet2.png>
</details>

### Registration and Login Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/tabletreg.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/tabletlogin.png>
</details>

### Event List and Event Detail Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/tableteventlist.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/tableteventdetail.png>
</details>

### Create Event and Admin Event Approval Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/tableteventcreate.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/tabletadminapprove.png>
</details>

### Admin Update 'About' Form and Logout Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/tabletupdateabout.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/tabletlogout.png>
</details>

## High-fidelity Desktop Wireframes from Site Screenshots:

### Home Page  
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/homepage.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/homepage2.png>
</details>

### Registration and Login Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/wfregistration.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/wflogin.png>
</details>

### Event List and Event Detail Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/wfeventlist.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/wfeventdetails.png>
</details>

### Create Event and Admin Event Approval Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/wfcreate.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/wfadminapp.png>
</details>

### Admin Update 'About' Form and Logout Pages
<details><summary>click to expand</summary>
<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/wfupdateabout.png>

<img src=https://github.com/Libbu/ci-capstone-project/blob/main/media/wflogout.png>
</details>

___
# Testing

For all testing, including UAC and User Story testing, please refer to the [TESTING.md](TESTING.md) file.

___
# Implemented Features

## Home Page

The fully responsive Home Page has three distinct sections which reveal themselves to the user as they scroll down.

- __The landing page__

  - The landing page image is a high quality photograph depicting the activity around which Calm Cadence is centered.
  - It introduces the brand name and aesthetic, as well as featuring a brief statement of purpose.

- __The about section__

 - This section describes the purpose of the community.

- __The Join Us and Login Images__

 - Featuring dynamic overlays as the user mouses over these images or taps, this area furthers the call to action from the About section to join us or log in.

Desktop:

![HomePage](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureshome.png)

![HomePage](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureshome2.png)

Tablet:

![HomePage](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureshometablet.png)

![HomePage](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureshometablet2.png)

Mobile:

![HomePage](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureshomemob.png)

![HomePage](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureshomemob2.png)

## Navbar

Featured site-wide, the links in the fully responsive navigation bar change based on whether the user is logged-in or not, and whether the user is an administrator.

  - The navigatopn bar allows the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button.
  - It features drop-down functionality to keep links organised and prevent unecessary visual clutter in the navigation pane.
  - The current page is underlined, so that users are never in any doubt as to where they are in the website.
  - Although the links present in the navigation bar will change in accordance with role-based access, the look and feel is consistent no matter what role the user is in when they interact with it.

Desktop:

![NavBar](https://github.com/Libbu/ci-capstone-project/blob/main/media/adminnav.JPG)

Tablet:

![NavBar](https://github.com/Libbu/ci-capstone-project/blob/main/media/tabletnav.JPG)

Mobile:

![NavBar](https://github.com/Libbu/ci-capstone-project/blob/main/media/adminnavmob.JPG)

## Footer

 - The footer includes links the user can follow to access our social media content on different platforms, encouraging them to stay connected with our brand and community.
 - The footer displays consistently across all pages and is fully responsive.
 - Although not directly referenced by a user story, this feature has been included as it is unbiquitous across modern websites
 - Icons on the footer have a hover-effect which sees them turn light-pink against a dark-purple backgroun, providing further visual delight to the user.

Desktop:

![Footer](https://github.com/Libbu/ci-capstone-project/blob/main/media/footerdesk.JPG)

Tablet:

![Footer](https://github.com/Libbu/ci-capstone-project/blob/main/media/footertab.JPG)

Mobile:

![Footer](https://github.com/Libbu/ci-capstone-project/blob/main/media/footermob.JPG)

## Paginated List of Events 

 The fully responsive paginated list of events allows users to see what other people have scheduled across the site, each event card can be clicked on to get more information.

 - The event cards feature an image which can be uploaded by the user who created the event, or populated with a default placeholder image from Unsplash.
 - Events are organised in the list based on those closest in time today first.
 - Six events will show before the user needs to naviate to the next page in order to see more. 

Desktop:

![Event_List](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureseventlist.JPG)

Tablet:

![Event_List](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureseventlisttablet.JPG)

Mobile:

![Event_List](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureseventlistmob.JPG)

### Event Cards:

Summary details of the event are visible on cards styled in accordance with the site aesthetic, on desktop the cards hover as the user mouses over them.

Desktop:

![Event_List](https://github.com/Libbu/ci-capstone-project/blob/main/media/eventcard.JPG)

Tablet:

![Event_List](https://github.com/Libbu/ci-capstone-project/blob/main/media/featurestableteventcard.JPG)

Mobile:

![Event_List](https://github.com/Libbu/ci-capstone-project/blob/main/media/featuresmobeventcard.JPG)

## Event Detail

The event detail contains additional information about the run that the event organiser has added when they created the event.

 - This page provides the opportunity for community members to engage with each other through attending runs and leaving comments
 - The buttons which show against the event detail are role-specific and determined by the users relationship to the event; Site administrators can always delete events; otherwise regular users are able to delete or update their own events, but not those of others; all logged-in site users can register or cancel their attendance for a run.

 Desktop:

![Event Detail](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureseventdetail.JPG)

Tablet:

![Event Detail](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureseventdetailtablet.JPG)

![Event Detail](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureseventdetailtablet2.JPG)

Mobile:

![Event Detail](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureseventdetailmobile.JPG)

![Event Detail](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureseventdetailmobile2.JPG)

## User Registration

- __Authentication - Django AllAuth__

[Django AllAuth](https://docs.allauth.org/en/latest/) provides one of the most popular libraries for managing user authentication, and has been used in this project to manage the registration, login and logout features.

Using this library means that users are able to register for the website with minimal barriers, and that there is plenty of scope in the future to allow users to sign in with their social media accounts, reset passwords, and sent email confirmation of registration.

Django AllAuth HTML templates have been styled with custom CSS and Crispy forms bootstrap to match the look and feel of Calm Cadence, as well as to ensure that they are fully responsive.

Authenticating users before allowing them to view events or activities scheduled is a common feature of many fitness-focussed apps on the market. 

Desktop:

![Registration](https://github.com/Libbu/ci-capstone-project/blob/main/media/registerpc.JPG)

Tablet:

![Registration](https://github.com/Libbu/ci-capstone-project/blob/main/media/registertablet.JPG)

Mobile:

![Registration](https://github.com/Libbu/ci-capstone-project/blob/main/media/registermob.png)


## User Login/Logout

Django AllAuth HTML templates for login and logout functions have been styled with custom CSS and Crispy forms bootstrap to match the look and feel of Calm Cadence, as well as to ensure that they are fully responsive.

- __Login__

Desktop:

![Login](https://github.com/Libbu/ci-capstone-project/blob/main/media/loginpc.JPG)

Tablet:

![Login](https://github.com/Libbu/ci-capstone-project/blob/main/media/logintablet.JPG)

Mobile:

![Login](https://github.com/Libbu/ci-capstone-project/blob/main/media/loginmob.JPG)

- __Logout__

Desktop:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/logoutbig.JPG)

Tablet:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/tabletlogout.JPG)

Mobile:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/logoutmob.JPG)


## Users Can Create, Edit and Delete Own Events

- __Create__

Users are able to create events using the Create Event option in navigation after logging in, and submitting the Create Event Form;

Desktop:

![Create Event](https://github.com/Libbu/ci-capstone-project/blob/main/media/createevent.JPG)

Tablet:

![Create Event](https://github.com/Libbu/ci-capstone-project/blob/main/media/featurescreatetablet.JPG)

Mobile:

![Create Event](https://github.com/Libbu/ci-capstone-project/blob/main/media/createeventmob1.png)

![Create Event](https://github.com/Libbu/ci-capstone-project/blob/main/media/createeventmob2.png)

Events users create need to be approved by admin before they will show on the Event List page.

- __Edit and Delete__

Users have access to edit and delete their own events, but not other people's. Site Admin have access to delete any event on the site.

On all devices can find the option to update their events on the Event Detail page:

Desktop:

![Update](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureseventdetail.JPG)

Tablet:

![Update Event](https://github.com/Libbu/ci-capstone-project/blob/main/media/featuresuserowneventtablet.JPG)

Mobile:

![Update Event](https://github.com/Libbu/ci-capstone-project/blob/main/media/featuresuserowneventmob.JPG)

Chosing to Update the Event will cause the Create Event form to pre-populate with the current event details. Updated events need to be approved by a site admin before they will show on the Event List once more.

![Update Event](https://github.com/Libbu/ci-capstone-project/blob/main/media/updateevent.JPG)

Users have access to delete their own events, and Site Admin have access to delete any event. 

Chosing to delete an event will cause a confirmation modal to appear, the event will only be deleted after the the Delete button on the confirmation has been selected.


![Delete Event](https://github.com/Libbu/ci-capstone-project/blob/main/media/featdeleteevent.JPG)


## User's Attendance

Registered site users can attend events by clicking "count me in!" or they can cancel their attendance. The options available changes based on whether or not the user has said they will attend.

![attend](https://github.com/Libbu/ci-capstone-project/blob/main/media/attendbutton.JPG)

![cancel](https://github.com/Libbu/ci-capstone-project/blob/main/media/cancelattendbutton.JPG)


## Users Can Keep Track of Their Activity

There are two areas of the site where users can keep track of their activity, User Events which lists past and future events the user has organised, and Attendance which lists past and future events the user has registered their attendance for.

To maintain stylistic consistency both of these areas are styled similarly to the Event List page both in terms of the use of Event Cards and responsiveness.

Past events show without the image on the card so as not to clutter the visual field, though this can still be accessed by clicking on the card which will take the user to event detail.

### User Events

Desktop:

![User Events](https://github.com/Libbu/ci-capstone-project/blob/main/media/featusereventspc.JPG)

Tablet:

![User Events](https://github.com/Libbu/ci-capstone-project/blob/main/media/featusereventstablet.JPG)

Mobile:

![User Events](https://github.com/Libbu/ci-capstone-project/blob/main/media/featusereventsmob.JPG)

### Attendance

Desktop:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/featattendpc.JPG)

Tablet:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/featattendtablet.JPG)

Mobile:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/featattendmob.JPG)

## Comments

Logged-in users are able to leave comments on the Event Detail page using the Comment form:

Desktop:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/commentsectionpc.JPG)

Tablet: 

![Event Detail](https://github.com/Libbu/ci-capstone-project/blob/main/media/featureseventdetailtablet2.JPG)

Mobile:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/commentsectionmobile.JPG)

Users are able to edit and delete their own comments; Site Admin are able to delete any comment.

## Site Admin Specific Functionality

Administrators have specific access to enable them to control content on the site. This inlcudes the ability to approve or decline events, and the ability to update the About Our Community section on the homepage.

### Admin Approval Page for Events:

Desktop:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/adminapprovepc.JPG)

Tablet: 

![Event Detail](https://github.com/Libbu/ci-capstone-project/blob/main/media/adminapprovetablet.JPG)

Mobile:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/adminapprovemob.png)

### Admin Update About Form:

Desktop:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/updateaboutpc.JPG)

Tablet: 

![Event Detail](https://github.com/Libbu/ci-capstone-project/blob/main/media/updateabouttablet.JPG)

Mobile:

![Logout](https://github.com/Libbu/ci-capstone-project/blob/main/media/updateaboutmob.JPG)


# Future Features:

The contact form which was classed as a "Won't Have" for this release is still a needed site feature and should be implemented in the future.

Ideally a platform such as this would enable users to message one another, support comment threads, notifications, likes and automatic emails. I think that these featuers, inbuilt already to major social-media platforms, are part of why I see much of this activity happening in the comment sections of Facebook posts in running groups.

The event booking system is heavily influenced by blog aesthetics; in the future it would be nice to have an actual blog function attached to Calm Cadence.

Categories either for types of runs, whether they are lead by a licensed running coach and the exact location within South Wales would also enhance the usability of the site.

## Known Issues and Bugs

- Ideally once an event has passed users would no longer be able to say they were attending and numbers would be frozen, however this is not currently implemented.

- The 'Update About' section for admin is currently plain text due to insurmountable obstacles integrating SummerNoteAdmin fields in the project. Ideally administrators would not have to utilise HTML tags for linebreaks etc in writing updates, however currently this is what they must do.

- Mobile view in chrome dev tools places a lot of empty space at the bottom of some pages, however in testing this was not replicated on an actual mobile device. This was noted in UAC logs.

- Currently users can upload image files of any size, this could slow the website down in future and compression or cropping of user-uploaded images should be implemented to solve this.

- Currently users are unable to add alt-text to images that they upload. This presents an accessibility problem and should be remedied to ensure the website reflecting an inclusive community is truly inclusive in it's own design.

- The loading performance on mobile leaves much to be desired. This is likely due to image size and future site versions will be deployed with smaller image resolution.

- Ideally event organisers would be automatically added to event attendees, this can be implemented in view logic for an upcoming release.

- Event Organisers can continue to edit the details of the event they scheduled after it has passed. Preventing this may need looking at in the future.

___
# Technologies

## Languages

- Python+Django, JavaScript, HTML, CSS

## Programs, Frameworks and Libraries;

- [HTML](https://en.wikipedia.org/wiki/HTML) is used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) is used for the main site design and layout.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) is used in places for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for displaying delete confirmation modals, and delete and edit comment functions.
- [Python](https://www.python.org) is the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add .`, `git commit -m "commit message here`, `git push`)
- [GitHub](https://github.com) is where my repo is hosted.
- [Heroku](https://www.heroku.com) is used for hosting the deployed site.
- [Gitpod](https://gitpod.io) was my cloud-based IDE for development.
- [Bootstrap 4.3](https://getbootstrap.com) was used as a frontend framework for modern responsiveness and pre-built components.
- [Font Awesome](https://fontawesome.com/) - was used for icons.
- [Django](https://www.djangoproject.com) is the Python framework for the site.
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/) was used for registration, login and logout.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) for for forms.
- [Crispy Bootstrap](https://pypi.org/project/crispy-bootstrap5/) for simple styling on forms.
- [Google Fonts](https://fonts.google.com/) for typography.
- [Coolors](https://coolors.co/)for palette generation.
- [ElephantSQL](https://www.elephantsql.com) Is the database management service used.
- [Cloudinary](https://cloudinary.com/) Is the image-hosting service used to host user-uploaded images.
- [W3C HTML Markup Validator](https://validator.w3.org/) to validate HTML code.
- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code.
- [JS Hint](https://jshint.com/) to validate JS code.
- [CI Python Linter](https://pep8ci.herokuapp.com) to validate python code.
- [LucidChart](https://lucid.app/documents#/dashboard) for ERD.
- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) Template to generate the workspace for the project.
- [Balsamiq](https://balsamiq.com/) was the wireframing tool.

___
# Deployment

## Github

The base environment for this project was created by navigating to the [gitpod CI template](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking 'Use this template'. 

After making a new respository for my capstone project from the CI template, I created a workspace in gitpod where all of my development took place.

## Development Environment Set-Up

Calm Cadence makes use of many Django packages. For ease of set-up I pasted the contents of the requirements.txt file from our [third hackathon](https://github.com/Libbu/Full-Craic) into my workspace and used the following command to install all base packages I believed I needed at the start of the project:

`pip3 install -r requirements.txt`

I then created a Procfile and added a line of code for Heroku deployment: `web: gunicorn calm_cadence.wsgi`

After doing this I set up external services(covered below) in gitignored env.py, added any packages to INSTALLED_APPS in settings.py where necessary and then used the following commands to perform any database migrations (these steps were repeated later in development as I developed my own models):

`python3 manage.py makemigrations`

`python3 manage.py migrate`

To commit the changes to my Github repo I used the following terminal commands:

`git add .`
`git commit -m "commit message here"`
`git push`

I had my basic project and app structure in place before preparing for early Heroku deployment

## Heroku

Heroku is used to host Calm Cadence. Heroku is a container-based cloud Platform for building, deploying and managing apps. This project was first deployed to Heroku in the very early stages following app structure setup.

The steps are as follows:

Login or create an account on [Heroku](https://www.heroku.com/). 

Click `new` in the top right corner and choose `create new app`.

Choose a unique app name and your region and click `create app`.

Navigate to the `Settings` tab, and click `Reveal Config Vars`.

**Setup External Services:**

Log in or create an account on [Cloudinary](https://cloudinary.com/).
Navigate to the `Dashboard` on Cloudinary, copy and store the value of the 'API Environment Variable" ( begins with cloudinary:// ) and paste it into your config vars `CLOUDINARY_URL` = `cloudinary://<your_value>`

Log in or create an account on [ElephantSQL](https://www.elephantsql.com/).
Create a new instance. Select the free plan Tiny Turtle and leave the tags blank.
Select the region and choose the nearest data centre to your location or the one that works.
Click 'review' and check the details and click the button to create the instance.
Click on the instance you created copy the ElephantSQL database URL from the instance details and paste it into your config vars `DATABASE_URL` = `postgres://<your_value>`

Navigate to the `Deploy` tab and select GitHub as a deployment method.
Find the repository to connect to and choose the branch to deploy.
Wait for the app to build, click on `View`.

Towards the end of the project I regenerated the SECRET_KEY and did the following;

Add Django secret key to config vars `SECRET_KEY`

I redeployed to Heroku roughly once a day.

Prior to submitting the finished project I ensured I had `DEBUG=False` in settings.py

___
# Credits 

- [Stack Overflow](https://stackoverflow.com/) for helping debug more difficult issues.
- [She Codes](https://www.shecodes.io/) for help with bootstrap styling.
- [Django Docs](https://docs.djangoproject.com/en/5.0/) for detailed explanations and help with troubleshooting.
- [Geeks for Geeks - Django](https://www.geeksforgeeks.org/getting-started-with-django/) for developing my understanding of MVT logic.
- [W3Schools](https://www.w3schools.com/) for providing guidance on the custom 404 page.
- [Lucidchart](lucidchart.com) for creating my ERD.
- [Am I Responsive](https://ui.dev/amiresponsive) for the responsive test screenshot.
- [Code Institute LMS walkthrough project: I think therefore I blog](https://github.com/Libbu/django-blog), from which I sourced the Comment JS logic (linked repo is my following of this walkthrough).
- [Django Wednesdays YouTube Playlist – Codemy.com](https://www.youtube.com/watch?v=HHx3tTQWUx0&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy) - for helping me get started with event management in Django.
- [Chat GPT](https://chat.openai.com/) for simple debugging.
- [doctypeKieran](https://github.com/doctypeKieran/ci-capstone-project) whose previous work developing an events booking system for CI Bootcamp I was able to draw on when developing mine.
- [Oksana Erm](https://github.com/oks-erm) whose fantastic project [Help U](https://github.com/oks-erm/help-u) helped me with the structure and content of my README.

## Personal Acknowledgements

- I would like to thank my amazing bootcamp cohort for being some of the best, most interesting people I could ever expect to meet. I don't know what I'm going to do now that I won't be seeing your faces (or at least your avatars) on a daily basis. I hope that each and every one of us finds the future we are searching for.

- I would like to thank our facilitator Iris Smok, and our two coding coaches amd SMEs Martin McInerney and Kevin Loughrey for their patience, encouragement, humour and clear instruction.

- I would like to thank my partner James, without his encouragement I might have "wussed out" so to speak before even starting. 

- I would also like to thank the CI admissions officer who pushed me to take up the place when I wavered. I never could have anticipated such an enjoyable four months.

- Lastly, I would like to thank my Code Institute mentor, Ronan McClelland for his insight and encouragement during the final capstone project.