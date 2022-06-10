# Assessment 2: Object Oriented Programming + CSV Reading
- **Video Inventory Manager**

## Important Grading Information
- Make sure you read the [Assessment-2 Grading Rubric](https://docs.google.com/spreadsheets/d/1AlAQukmB3SS7IyW2hu0zY-9RaQnHY3lLeTi2O1fUb30/edit?usp=sharing).
  - Application Correctness (60%)
  - Code Design (40%)
- You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - *5% penalty*: If you complete and submit the retake **within one week** of receiving your grade. 
  - *10% penalty*: If you complete and submit the retake **by the start of week 12**. A retake for this assessment WILL NOT be accepted after this date.

## Rules / Process
- This test is fully open notes and open Google, but is not to be completed with the help of other students/individuals.
- Push your solution up to a private repo in your personal Github account.

## Requirements
- This assessment should be completed using Python.

## Challenge
*Back in the day*, humans would actually leave their homes to go rent a physical video copy of movies (what a strange concept, right?). Blockbuster was the leading video rental company in this era. Today, there is only one Blockbuster location left which is located in Bend, Oregon. We are going to ask you to build a video inventory application for this Blockbuster!

Your Video Inventory Management application should manage the following data:
- Manage customer information:
  - customer id
  - customer account type (sx/px/sf/pf)
    - "sx" = standard account: max 1 rental out at a time
    - "px" = premium account: max 3 rentals out at a time
    - "sf" = standard family account: max 1 rental out at a time AND can not rent any "R" rated movies
    - "pf" = premium family account: max 3 rentals out at a time AND can not rent any "R" rated movies   
  - customer first name
  - customer last name 
  - current list of video rentals (*by title*), each title separated by a forward slash "/"
- Manage the store's video inventory:
  - video id
  - video title
  - video rating
  - video release year
  - number of copies currently available in-store

Your application should allow:
- Viewing the current video inventory for the store
- Viewing a customer's current rented videos
  - customer *by id*
  - each title should be listed separately (i.e. not displayed with slashes from the CSV file)
- Adding a new customer
  - you should not have an initial list of video rentals assigned to a newly created customer
  - can you prevent duplicate ids from existing?
- Renting a video out to a customer
  - video *by title*
  - customer *by id*
  - **IMPORTANT:** Customers should be limited based on their account type. Your application should enforce these limitations when attempting to rent a video!
- Returning a video from a customer
  - video *by title*
  - customer *by id*
- Exiting the application

Be sure to give careful consideration into what data structures & data types (including classes) you might need to use in your application logic. 

Your menu should look something like this: 
```
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View customer rented videos
3. Add new customer
4. Rent video
5. Return video
6. Exit
```
