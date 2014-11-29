centos-server
=============

The full configurations for my CentOS 5.11 server from an old semester project. Includes web services, extended logging, mail service, compiled kernels, security configurations, VoIP service, IM service, and more.

<h3>Full list of configurations and roles</h3>

<ul>
  <li>Apache webserver configured for two additional name-based virtual hosts, ~user/public_html/ requests, php, and cgi scripting, and .htaccess directory-level access protection
  <li>Saltstack configuration management, infrastructure automation, and remote cloud execution software
  <li>Apache-Tomcat webserver
  <li>Oracle GlassFish server
  <li>Bacula backup system and scheduler
  <li>Webmin and Usermin installation and configuration
  <li>RDP server
  <li>rsyslog logger service without otput to mySQL database and readable from Adiscon LogAnalyzer web application
  <li>Zsh shell with custom configurations for special accounts
  <li>Concurrent user- and group-level login limitations
  <li>Lynis security audit application
  <li>Asterisk PBX server with Twinkle and Ekiga softphones
  <li>Implementation of disk quotas for user accounts
  <li>Custom compiled Linux 2.6.18 kernel
  <li>Dhrystone and Lmbench benchmarking suites
  <li>mySQL, php, and WordPress
  <li>Mantis BugTracker project management web application
  <li>CUPS network printer configuration
  <li>Mail services via dovecot and sendmail with spam protection via Spamassassin
  <li>Samba shares
  <li>UnrealIRCd irc messaging server
  <li>Creation of additional XFS filesystems
  <li>Sudo permissions for special accounts
  <li>Manual iptables firewall configurations for all aforementioned services
