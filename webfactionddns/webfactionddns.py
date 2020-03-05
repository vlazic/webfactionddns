"""Main module."""
import xmlrpc.client
import requests
import os


class WebfactionDDNS:
    __my_ip_url = 'http://ip.fs.rs'
    __webfaction_api_url = 'https://api.webfaction.com/'

    def __init__(self, username, password):
        self.__server = xmlrpc.client.ServerProxy(self.__webfaction_api_url)
        self.__session_id = self.__server.login(username, password)[0]

    def change_my_ip_provider(self, my_ip_url):
        self.__my_ip_url = my_ip_url

    def update_dns(self, domain_to_check, new_ip=False):
        domains = self.__server.list_dns_overrides(self.__session_id)

        if not new_ip:
            new_ip = requests.get(self.__my_ip_url).text

        for domain_info in domains:
            domain = domain_info['domain']

            if domain == domain_to_check:
                old_ip = domain_info['a_ip']

                if old_ip == new_ip:
                    print("IP's are the same")
                    return
                else:
                    return self.change_domain_ip(domain_to_check, old_ip, new_ip)

        print("This domain is not created. You need to create it first")

    def change_domain_ip(self, domain, old_ip, current_ip):
        self.__server.delete_dns_override(self.__session_id, domain, '')
        self.__server.create_dns_override(
            self.__session_id, domain, current_ip)

        return current_ip
