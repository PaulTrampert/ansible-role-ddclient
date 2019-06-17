Role Name
=========

Installs and configures ddclient to keep a dynamic domain name up to date.

Requirements
------------

None.

Role Variables
--------------

| Variable              | Required | Default Value | Description                                      |
|-----------------------|----------|---------------|--------------------------------------------------|
| ddclient_domains      | yes      |               | Comma separated list of domains to update        |
| ddclient_pw           | yes      |               | The password to update your dynamic dns provider |
| ddclient_login        | yes      |               | The user id used for your dynamic dns provider   |
| ddclient_server       | yes      |               | The update server for your dynamic dns provider  |
| ddclient_ssl          | no       | yes           | Connect to your provider with ssl?               |
| ddclient_use          | no       | web           | How to determine your IP address                 |
| ddclient_protocol     | no       | dyndns2       | The protocol used by your dynamic dns provider   |
| ddclient_mail         | no       | root          | Where to mail status updates                     |
| ddclient_mail_failure | no       | root          | Where to mail failures                           |
| ddclient_daemon       | no       | 300           | How often to update IP                           |

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: ddclient
           vars:
             ddclient_domains: mydomain.com,derp.com
             ddclient_pw: somepw
             ddclient_login: somelogin
             ddclient_server: domains.google.com

License
-------

MIT
