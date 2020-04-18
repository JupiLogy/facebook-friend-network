from selenium.webdriver import Chrome
import time
import pickle
from tqdm import tqdm
from dotenv import load_dotenv
import os

# Some utilities:
def get_name(link):
    # Get username from mutual friends link
    split = str.split(link, sep="/")
    return split[-2]

load_dotenv()

# Part 1: Getting list of your friends

driver = Chrome(os.getenv("CHROME_DRIVER_PATH"))

driver.get("https://www.facebook.com")
input("Press enter here when you have logged in to Facebook.")
# You need to log into your account to view your mutual friends lists.

driver.get("https://www.facebook.com/{}".format(os.getenv("FRIENDS_LIST")))

# Load page fully...
old_no_friends = -1
while len(driver.find_elements_by_class_name("b1v8xokw")) != old_no_friends:
    old_no_friends = len(driver.find_elements_by_class_name("b1v8xokw"))
    # Using space key to scroll down page, to fully load
    driver.find_elements_by_class_name("_6s5d")[0].send_keys("     ")
    time.sleep(3)
# Page loaded!
friends = driver.find_elements_by_class_name("b1v8xokw")

# Get list of mutual friend links, add it to friend_links dictionary
print("Getting the list of mutual friends...")
friend_links = {}
for friend in tqdm(friends):
    link_to_mutuals = friend.get_attribute("href")
    name = get_name(link_to_mutuals)
    friend_links[name] = link_to_mutuals

# Dumping list of names with links, saving progress in case we lose connection
with open("friend_links", "wb") as file:
    pickle.dump(friend_links, file)
print("'friend_links' saved")


# Part 2: Getting mutual friends lists
mutuals = {}

for friend in tqdm(friend_links.keys()):
    driver.get(friend_links[friend])

    # Scroll until friends all load
    old_no_friends = -1
    while len(driver.find_elements_by_class_name("b1v8xokw")) != old_no_friends:
        old_no_friends = len(driver.find_elements_by_class_name("b1v8xokw"))
        # Scroll using space key
        driver.find_elements_by_class_name("_6s5d")[0].send_keys("     ")
        time.sleep(3)

    # Grab friends
    raw_mutuals = driver.find_elements_by_class_name("b1v8xokw")
    mutuals[friend] = [get_name(friend.get_attribute("href")) for friend in raw_mutuals]

# Dumping names with list of mutual friends. We can disconnect from Facebook now.
with open("mutuals", "wb") as f:
    pickle.dump(mutuals, f)
print("'mutuals' saved")

# Part 3: Getting csv

# Anyone without a facebook username will be listed as "www.facebook.com"
# So we need to delete those entries
del mutuals["www.facebook.com"]

# csv_out will be our csv string we write to file
csv_out = ""

for friend in tqdm(mutuals.keys()):
    # Append friend name, followed by their mutual friends names.
    # As long as their mutual friend is not called "www.facebook.com".
    mutuals[friend].insert(0, friend)
    csv_out += (
        " ".join(
            [
                human
                for human in mutuals[friend]
                if human != "www.facebook.com"
            ]
        )
        + "\n"
    )

# Finally, write out the csv!
with open("facebook.csv", "w") as f:
    f.write(csv_out)
print("Output saved in 'facebook.csv'")
