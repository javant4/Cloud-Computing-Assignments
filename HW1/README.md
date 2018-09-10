# cs5165_hw1 Avant   

Project:

My webapp takes 3 inputs and outputs a plot of the quadratic equation and it's roots.
The user is asked to enter, from the form ax^2 + bx + c the respective coefficients.
Source code used for the project:
1. https://docs.djangoproject.com/en/1.10/intro/tutorial01/
2. http://hplgit.github.io/web4sciapps/doc/pub/._web4sa_django006.html
3. container_commands:
  01_setup_apache:
    command: "cp .ebextensions/enable_mod_deflate.conf /etc/httpd/conf.d/enable_mod_deflate.conf"

Components of web application:
1. Runs on Django
2. Deployed through apache and mod_wsgi on AWS BeanStalk
 - in my /.ebextension/ folder I have a 0_apache.config file with the following apache container command:
 container_commands:
  01_setup_apache:
    command: "cp .ebextensions/enable_mod_deflate.conf /etc/httpd/conf.d/enable_mod_deflate.conf"
3. Database configured on RDS database using "postgresql"


Challenges:

Configuring the website onto AWS. I was comfortable designing the site but took my a very long time to learn the steps to host the public page.
I wanted to make sure I got a comprehensive understanding of the assignment before I turned it in incomplete. Not having Ubuntu slowed me down,
but I did install Putty had trouble connecting to my instance often.

What I learned:

1. A new tool for designing a web application
2. AWS EC/BEanStalk
3. Putty configuration and more linux commands

