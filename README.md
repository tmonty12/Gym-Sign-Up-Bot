# Gym-Sign-Up-Bot
During the pandemic, my University's gyms had 2 hour time slots that opened up 6 hours in advance. As you could imagine, they were very competitive and required 
being on your computer exactly when they dropped. To solve this problem I created a Selenium web bot in Python that uses the Windows Task Manager on the backend
to reserve spots when I want. The bot uses a command line interface to receive parameters such as username, password, date, time and location.

You can read more about the details of my bot on this [blog post](https://tmonty.tech/create-an-automated-web-bot-with-selenium-in-python) I wrote.

## Instructions
To use this bot you must first have a Windows OS - I cover other scheduling alternatives in my post.

Create a folder, clone my repository to it and run:
pip install -r requirements.txt

Then you call the script and pass in your arguments:
python scheduler.py --u username --pw password --flr location --d date --t time

