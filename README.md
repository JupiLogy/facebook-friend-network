# Facebook friend network

Please make an issue if it is not working for you! I'll do my best to help :)
Please read this entire readme before doing anything.

## How to use:

### Getting data:
- Check you have all the requirements installed.
- Go to facebook.py and search for TODO. Those comments will tell you the necessary changes you should make.
- Run `python facebook.py`.
- Log in to Facebook in the pop up window, then go back to the terminal and press enter.

### Constructing Graph
- Once it has finished, open Gephi and click `new project`.
- Go to `Data Laboratory`, then `edges`. Now, `import spreadsheet`. Select `facebook.csv`.
- Go to `Overview`. Choose the `Force Atlas` layout and press play.
- Just kinda play around with Gephi until you get something you like :) you can even colour nodes.

### Saving Graph
- Go to `preview` to make sure you like how it looks.
- `File > Export >` whatever filetype you want.
- Finally you can go to an image editor to draw labels and stuff.

## Requirements:
- Chrome browser
- Selenium: `pip install Selenium`
- Driver according to your Chrome version and OS: https://chromedriver.chromium.org/downloads
- Gephi, unless you have some other plan for drawing your graph

## More info:
Currently does not detect facebook friends who do not have usernames.
For example, `www.facebook.com/user_name` is detected, but `www.facebook.com/profile.php?id=123456789` is not.

Also ignores friends who have no mutual friends, and those whose accounts are deactivated.

Waits a few seconds before going to different profiles.
This makes it slow, but if we go too fast, Facebook will give a temporary ban.

I have tried to reduce the risk of getting a temporary ban, but I can't guarantee anything.
If you get banned, it is not my responsibility.