# Movie List
The Movie List Project is a Python application to consume Ghibli APIs and display a list movies, with their related people, in the movies page `/movies/`.
 
The data displayed is cached using memcached, and the cache expires every 60 seconds.

The project is built using **Python 3.9** and **Django 3.1.3**

##Installation
* To install **memcached** on a mac, using homebrew, run the following commands:
```
brew update
brew doctor
brew install memcached

cp /usr/local/Cellar/memcached/1.6.9/homebrew.mxcl.memcached.plist ~/Library/LaunchAgents/
launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.memcached.plist

# Install Lunchy, a gem that simplifies the command line interface to launchctl; And configure lunchy to start/stop memcached using simple lunchy commands
gem install lunchy
lunchy start memcached
lunchy stop memcached

# Validate the insatllation
memcached -V 

# You can access memcached using
telnet localhost 11211

# To Invalidate All Cache Items
echo 'flush_all' | nc localhost 11211 
```


* To **install the project's requirements** run: `pip3 install -r requirements.txt` 


* To **start the web server** run: `python3 manage.py runserver` and access `http://127.0.0.1:8000/`

* To run the tests: `python3 manage.py test`
