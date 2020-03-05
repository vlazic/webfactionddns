======================
Webfaction Dynamic DNS
======================


.. .. image:: https://img.shields.io/pypi/v/webfactionddns.svg
..         :target: https://pypi.python.org/pypi/webfactionddns

.. .. image:: https://img.shields.io/travis/vlazic/webfactionddns.svg
..         :target: https://travis-ci.com/vlazic/webfactionddns

.. .. image:: https://readthedocs.org/projects/webfactionddns/badge/?version=latest
..         :target: https://webfactionddns.readthedocs.io/en/latest/?badge=latest
..         :alt: Documentation Status


.. .. image:: https://pyup.io/repos/github/vlazic/webfactionddns/shield.svg
..      :target: https://pyup.io/repos/github/vlazic/webfactionddns/
..      :alt: Updates



Use Webfaction as DDNS provider


* Free software: MIT license

.. * Documentation: https://webfactionddns.readthedocs.io


Features
--------

CLI example:

.. code:: text

    $ webfactionddns -u webfaction-user -p webfaction-password -d my-domain.com
    Your new IP address is: 22.22.22.22

    $ you can use enviroment variables for user/pass as well
    $ WEBFACTION_USER=webfaction-user WEBFACTION_PASSWORD=webfaction-password webfactionddns -d my-domain.com
    Your new IP address is: 22.22.22.22


    $ webfactionddns --help

    Usage: webfactionddns [OPTIONS]

        Console script for webfactionddns.

    Options:
        -u, --user TEXT      Webfaction user  [required]
        -p, --password TEXT  Webfaction password  [required]
        -d, --domain TEXT    Domain for which you want to change IP address
                            [required]
        -i, --new-ip TEXT    New IP address for domain. Leave empty and it will be
                            set for current machine public IP
        --help               Show this message and exit.

Code example:

.. code:: python

        import webfactionddns

        # try logging in to Webfaction
        try:
                wddns = webfactionddns.WebfactionDDNS(user, password)
        except Exception as e:
                print(e.faultString)

        # try updating DNS for domain
        try:
                new_ip_address = wddns.update_dns(domain, new_ip)
                if new_ip_address:
                        click.echo("Your new IP address is: {}".format(new_ip_address))
        except Exception as e:
                print(e.faultString)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
