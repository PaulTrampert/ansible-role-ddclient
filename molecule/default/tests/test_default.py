import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ddclient_config(host):
    f = host.file('/etc/ddclient.conf')
    expectedFileContent = (
        "daemon=300\n"
        "syslog=yes\n"
        "mail=root\n"
        "mail-failure=root\n"
        "pid=/var/run/ddclient.pid\n"
        "protocol=dyndns2\n"
        "use=web\n"
        "ssl=yes\n"
        "server=example.com\n"
        "login=asdfasdf\n"
        "password='asdfasdf'\n"
        "mydomain.com\n"
    )
    assert f.content_string == expectedFileContent
