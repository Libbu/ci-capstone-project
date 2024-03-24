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

# Design

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

Sammple event posts with routes as images are using screen-shots from the route-planner on [MapMyRun](https://www.mapmyrun.com/)

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

#### Confirmation Modals

Modals have been used to display confirmation messages to users when they select either an event or comment to delete. The aprupt change in the visual pane is intended to draw user attention to the stated consequences and irreversible nature of the deletion action.
___

# Database Design

- note: the User model displayed below refers to that provided by Django package functionality; selected fields have been included to demonstrate how they relate to the custom models created for Calm Cadence.

![ERD](https://github.com/Libbu/ci-capstone-project/blob/main/media/ERD.png)

## Structure

### Home Page

![Calm Cadence](https://github.com/Libbu/ci-capstone-project/blob/main/media/amiresponsive.JPG)

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

![Calm Cadence](https://github.com/Libbu/ci-capstone-project/blob/main/media/amiresponsivesignup.JPG)

- Allows users to register so that they can access site content

    #### User Goal:
    >   - Register

    #### Website Goals:
    >   - Allow user registration
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.


### Sign In Page

![Calm Cadence](https://github.com/Libbu/ci-capstone-project/blob/main/media/amirelogin.JPG)

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
 
![Event List](https://github.com/Libbu/ci-capstone-project/blob/main/media/amireseventdetail.JPG)

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

IMAGE

- Allows authenticated users to create a new event
- Allows event organisers to update their own event.
- Validates image file input to prevent uploading of file-types outside of those specified.

    #### User Goals:
    >   - Create a new event.
    >   - Update existing events.

    #### Website Goals:
    >   - Allow the user to create/update an event
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

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

## High-fidelity Mobile Wireframes:

## High-fidelity Desktop Wireframes:
