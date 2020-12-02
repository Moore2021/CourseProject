# courseProject
For this project, students from CSC 221 formed teams of two to three members and built a Python software project of their own choosing.

# Urlshortener
For this project, Andrew Moore and Trevor Ryan created a URL shortener in python version 3.

# Library
The Libraries used in this project include the following:

  Tinyurl api - the tiny url library was implemented in the code to create the shortener.

  urllib - this was used to parse, encode and open the links.
  
  sys - This was used to grab the user's input from the command terminal.
  
  re - this was used for the regex that finds the actual shortened url

# How it works
The code grabs the user's arguments passed in with the file run line. Then it uses the tinyurl's api and create link to form the needed links. After that it encodes and opens them. While opening the links you you get prompted to give an alias if u choose todo so. The api link will return a shortened link without the alias. this is because the api link does not support an alias. The create link will return the whole official site, that will get parsed down to just the shortened link with the alias if assigned one. In addition to that, two other links will be printed, one will be to the api site and one is to the official site.

# How to install
To download and use the code, download the urlshortener.py file
Then open it up in a text editor.
If your text editor has a integrated terminal you can run it through there, if it doesn't then run it through the command prompt terminal

# How to run
To actually run the code, open up the terminal you can use.
Then navigate to the same directory as the file you wish to run.
After you do that, type "python3 urlshortener.py <url>...".
The <url> is will your link will go instead of the <url> and the ... means you can do more than one link at a time.
Once you hit enter the file will run, and for each url you will get prompted to give an alias. If you choose not to give an alias just hit enter when you get prompted for one. Once the file is done running, for each link that you inputed, 3 links will be given with some borders around them to help you know the difference between the multiple links if u enter more than one.
