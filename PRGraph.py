from github import Github
from bargraph import Bargraph
from threading import Timer
from datetime import datetime
from dateutil.relativedelta import relativedelta

file = open("accessToken.txt")
accessToken = file.read()
file.close()
g = Github(accessToken)
prAgeThreshold = datetime.now()-relativedelta(months=6)

org = g.get_organization("hmrc")
team = org.get_team_by_slug("seiss")
peopleIds = [x.id for x in team.get_members()]
repos = [x for x in team.get_repos()]

display = Bargraph()
display.setLevel(0)

running = True

def flatmap(function, list):
    result = []
    for x in list:
        subList = function(x)
        for item in subList:
            result.append(item)
    return result

def prsForRepo(repo):
    result = [pr for pr in repo.get_pulls("open") if pr.user.id in peopleIds and pr.updated_at > prAgeThreshold]
    if len(result) > 0:
        print(repo.name)
        for pr in result:
            print("\t" + pr.title)
    return result

def scheduleUpdate():
    t = Timer(10 * 60.0, updateDisplay)
    t.daemon = True
    t.start()

def updateDisplay():
    print(str(datetime.now()), "updating display ...")
    prs = flatmap(prsForRepo, repos)

    display.moveToLevel(len(prs), 0.5)
    print(str(datetime.now()), "Done!")
    if running:
        scheduleUpdate()

updateDisplay()

raw_input("hit enter to end")
running = False
display.close()

