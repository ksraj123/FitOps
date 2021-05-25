# FitOps
Your fitbit insights on steroids ;)


## Motivation

Fitbit is being used on a humongous scale and it takes away all your data and owns it.<br>
Technically, the company can choose to just stop providing you your data and your access to your fitness-oriented data which you captured over eons of time over your fitbit will be long own.
<br><br>
Apart from that, you have to rely on the engineers of fitbit to be able to provide you "hopefully" good insights over your data via some bunch of dashboards. There is hardly any flexibility around tweaking the level and granularity of the insights which you'd possibly want to have, as those dashboards are majorly static.

So, to tackle all these concerns

### Enter FitOps

FitOps targets towards accomplishing two goals:
* **Democratization of your fitbit data** - FitOps fetches your fitbit's data periodically and stores it under your roof making "you!" the owner and sole proprietar of your own data. The control and ownership of your data becomes completely yours!
* **E2E control of the level and granularity of insights** - FitOps cooks up a grafana dashboard at your disposal encompassing a fantastic set of panels to depict a holistic view of your fitbit-oriented health insights. 
And you can flexibly control the E2E mechanics of all those panels by tweaking the panels in any way you'd want ranging low-level to high-level granularity.

## Setup

* Get your fitbit dev account created by going to dev.fitbit.com and make a note of all the credentials it provides upon completion.

* Clone this repository
```sh
git clone https://github.com/yashvardhan-kukreja/fitops
```

* Run the provided docker-compose to setup your elasticsearch and grafana in one-go
```sh
docker-compose -f fitops-elk-grafana-docker-compose.yml up
```

* Wait for a few seconds :P

* Go to `localhost:3000` of your browser and enter the default creds as "admin" (username) and "admin" (password) (Please change this :P)

* Go for the "FitOps" dashboard over grafana and get amazed :D

---
