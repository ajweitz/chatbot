# chatbot
Attempt to create a chatbot with python

## Prerequisites
1.  python
2.  postgresql

## Configuration
To add default phrases, you can modify the `*.lsv` files in `defaults` directory.
- `unknown.lsv` - phrases that the bot will say in case he didn't find a matching reply.
- `greetings.lsv` - default greeting.  

To add a new package for the project, open `InstallPackages.py` and add a `install('<PACKAGE_NAME>')`.

## Installation
- Clone the repo:
	`git clone https://github.com/ajweitz/chatbot.git`
- install python.
- install postgresql.
- To setup the packages and the database, run `Setup.py`.

## Ideas
- robot will learn that A -> B from interaction, probably from counting how many times was said A is B or A's are B's.
- robot might also learn from asking is A -> B.
- robot will need to understand negative or positive answers.
- robot will need to understand a sentence if it has spelling mistakes, probably by using some kind of library for spelling checks.
