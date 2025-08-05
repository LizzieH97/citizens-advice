<div align="center">
  <img src="frontend/public/logo.png" alt="Citizens Advice Logo" width="100" height="100" />
    <h1>Citizens Advice SORT</h1>
    <h3>Junior Developer Practical</h3>
</div>

---

## Backend Development

It had been a while since I had worked with Python, so before the project I completed research into the syntax - especially looking at FastAPI, using JSON files e.g. parsing and using the built-in re function for identifying expressions as I had not seen those before.

I discovered a new love for Python through this project, the syntax is simple and user-friendly. I actually now prefer using Python to Java for back-end frameworks!

The main issues I encountered with this was exporting the favicons - the icons for the police and government websites were blocked by a 403 error, so I added error handling and added a default favicon (Citizens Advice) to fall back on.

## Frontend Development

I had set up my layout and api calls quite quickly, but the errors came through manipulating the data to display well. In the content, there were a (link) and b (bold) tags, with which I had to use a HTML parser to show up as links and bold as they should. I also had to include break lines, as the information needed to be broken up to become more reader-accessible.

The other issues I encountered were through TypeScript types, but in order to avoid repeating myself I created a types folder to hold them.

## Final Project

Overall I have enjoyed making this project, particularly exploring Python further, and have conducted plenty of research so that it is user-friendly and accessible.

I am extremely happy with the outcome, I believe it looks clean and the code is DRY, readable and concise.

---

## Viewing Project

In the frontend folder, I used

npm run dev

(after running npm install)

and in the backend I used

poetry run fastapi dev main.py

(after running poetry install --no-root)
