# Calm Cadence (Capstone Project for CI - Coleg Gwent Bootcamp)

![Calm Cadence](https://github.com/Libbu/ci-capstone-project/blob/main/media/amiresponsive.JPG)

Calm Cadence is a website which aims to bring together runners of any and all abilities who prefer to take things slow. As a social running community the focus is more on camaraderie, support and making running accessible rather than performance. The idea was sparked in response to frequent posts on social-media sites such as Facebook from casual runners looking for people to join them in training either for social or safety reasons, or to help them be accountable to themselves and their programme. The goal of Calm Cadence is to apply a more structured event booking approach in order to help people find other runners to join them. Despite pervasive elitism in the field, running is for everyone regardless of pace or time and it is hoped that a community built around these principles will bring more people to the sport.

# Purpose

This website has been built using the Django framework for backend and frontend functionality. 

This website provides all essential features to meet its stated goal, such as allowing users to register, create events, attend events, engage with the community through comments on events, see records of events they have created/attended, as well as administrator specific access to approve or decline user-created events, delete comments, and update text on the homepage.

Taking the lead of other sport-related apps such as Strava and Spond; users must be registered in order to access the events on the site.

This website was developed for the capstone project at the conclusion of the Code Institute Bootcamp through Coleg Gwent.

The live website can be accessed here.
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

14. The website allows administrators to approve or decline all event posts.

15. The website allows administrators to delete any event or comment as necessary.

16. The website allows administrators to update the "about" section text on the homepage.

17. Website administrators are contactable through a contact form. 
___

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

IMAGE

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
 
IMAGE

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


