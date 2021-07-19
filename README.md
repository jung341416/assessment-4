# Assessment 4: Django
- **Craigslist Jr**

## Important Grading Information
- Make sure you read the [Assessment-4 Grading Rubric](https://docs.google.com/spreadsheets/d/11bCD5tstmbPhq8eqQD6NswuFOhiBLEBZv56ujREpPtQ/edit?usp=sharing).
  - Django Front-End (50%)
  - Django Back-End (40%)
  - Code Style (10%) 
- This assessment is worth 15% of your final grade. You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - 5% penalty: If you complete and submit the retake within **one week** of receiving your grade. 
  - 10% penalty: If you complete and submit the retake afterwards.

## Rules / Process
- This test is fully open notes and open Google, but is not to be completed with the help of other students/individuals
- Do not open a pull request against this repository. We will evaluate your code individually with you.

## Requirements
- This assessment must be completed using Django. 
- You may use either SQLite3 or PostgreSQL for your database. (SQLite3 preferred)

## Challenge
Everyone loves going on Craigslist to find interesting people and interesting items. The joy of Craigslist is that it doesn't upgrade itself to stay up to date with the times - it's the same old Craigslist that everyone knows and loves. The core schema has also remained relatively unchanged over the years. Today, you will build a basic Craigslist CRUD app with nested routes. We will call this site: Craigslist Junior.

Here are a list of the routes you will need to build:
- `/categories`: A page listing all the categories
- `/categories/new`: A page with a form to create a new category
- `/categories/:category_id`: A page to view the detail of a specific category and a list of all of its associated posts 
- `/categories/:category_id/edit`: A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here. 
- `/categories/:category_id/delete`: A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here. 
- `/categories/:category_id/posts/new`: A page with a form to create a new post, under the current category by default.
- `/categories/:category_id/posts/:post_id`: A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (`/categories/:category_id/`)
- `/categories/:category_id/posts/:post_id/edit`: A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.
- `/categories/:category_id/posts/:post_id/delete`: A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.

NOTE: For creating, updating, or deleting data... all actions should automatically redirect to another appropriate page, if successful, or display an error message if unsuccessful.

You do not need to style your pages (as Craigslist really doesn't make an effort to), but you should still have a nice basic visual presentation. You can earn a small bonus if you choose to add in some nice CSS styling to your front-end.  
