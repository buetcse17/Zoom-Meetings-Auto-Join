# Zoom Auto Join
### 1st condition : don't expect too much


If you want to keep your PC on and keep yourself busy with another task and you don't wanna miss any meetings to join, this repo is for you.

## Step 1 : Do some stuffs
* Auto Mute while joining meeting (From Settings)
* Auto Turn Off video while joining meeting (From Settings)
* Auto join audio (From Settings)
* Allow Zoom App to open link always (Mark the Checkbox). This will automatically open the Zoom App. (Picture below).

<img src="assets/allow-zoom-app.png" alt="Zoom Image"/>

## Step 2 : Clone this repo
Go to a directory where you want to keep this script. Clone this repo in this directory. Open terminal/command line in the directory and write the following commands.
```sh
git clone git@github.com:buetcse17/Zoom-Meetings-Auto-Join.git
```

## Step 3

In the directory where you have cloned this repo, open terminal or command line and write the following script. You have to do this only for the first time. 

Btw, if you don't have `pip` in your python, install it first to make the task easy (here I have provided how to install pip in linux. In windows it should be already installed in python)
#### For Linux 
```sh
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
deactivate
chmod +x zoom-cli.sh
```
#### For Windows
```sh
pip install virtualenv
virtualenv myenv
.\myenv\Scripts\activate
pip install -r requirements.txt
.\myenv\Scripts\deactivate
```

## Step 4
#### For Linux 
Done. Now everytime you just have to run the .sh file only
```sh
./zoom-cli.sh
```
#### For Windows
Done. Now everytime you just have to run the `main.py` file only
```sh
.\myenv\Scripts\activate
python main.py
```
<img src="assets/zoom-cli-terminal.png" alt="Zoom Image"/>


If there is any zoom meeting available in the list of data.py, then the meetings will be opened automatically in time.
### Note :
The meetings links I'm using are most probably correct. Make your modifications while necessary (it is not automatically updated). And here is a while loop used which has a pause of 30sec to reduce unnecessary continuous running , so there can be a 30sec late of joining meetings.
This script won't automatically leave meetings (as it can be unexpected/dangerous).

#### Run this script on a terminal/command line on background and don't use this terminal tab/window while this is running. Use another tab/terminal window to do your another works. And to stop this script running, press `Ctrl + C`, the program will stop running.

----
### Author
Kawshik Kumar Paul\
BUET CSE'17\
kawshik.kumar.paul@gmail.com
