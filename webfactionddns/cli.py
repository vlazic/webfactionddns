"""Console script for webfactionddns."""
import os
import sys
import click
import webfactionddns

env_user = os.getenv("WEBFACTION_USER", None)
env_password = os.getenv("WEBFACTION_PASSWORD", None)


@click.command()
@click.option('--user', '-u', required=not env_user, type=str, help="Webfaction user")
@click.option('--password', '-p', required=not env_password, type=str, help="Webfaction password")
@click.option('--domain', '-d', required=True, type=str, help="Domain for which you want to change IP address")
@click.option('--new-ip', '-i', default=False, type=str, help="New IP address for domain. Leave empty and it will use current machine public IP")
def main(user, password, domain, new_ip):
    """Console script for webfactionddns."""
    # if user/pass values are not set via arguments, use environment values
    user = user if user else env_user
    password = password if password else env_password

    # try logging in to Webfaction
    try:
        wddns = webfactionddns.WebfactionDDNS(user, password)
    except Exception as e:
        print(e.faultString)
        return 1

    # try updating DNS for domain
    try:
        new_ip_address = wddns.update_dns(domain, new_ip)

        if new_ip_address:
            click.echo("Your new IP address is: {}".format(new_ip_address))
    except Exception as e:
        print(e.faultString)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
