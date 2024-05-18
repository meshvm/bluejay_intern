# importing the libraries

from bs4 import BeautifulSoup
import requests
import csv




def main_fun():
    print("Hitting url https://googlecloudcheatsheet.withgoogle.com/ --->")
    url = "https://googlecloudcheatsheet.withgoogle.com/"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text
    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    # print(soup.prettify()) # print the parsed data of html, complete skeleton
    # print(soup.title)
    # print(soup.title.text)
    try:
        gdp_table = soup.find("span", attrs={"class": "sc-ksBlkl TahEY"})
        # print(gdp_table)



    except:
        print("This product is not available on this site --> https://endoflife.date")
if __name__ == '__main__':
    main_fun()












########################################################################################################################
# from googleapiclient import discovery
#
# def list_gcp_services():
#     # Create a discovery client
#     discovery_client = discovery.build('discovery', 'v1')
#
#     # Execute the request to list GCP services
#     services_request = discovery_client.services().list()
#     services_response = services_request.execute()
#
#     # Print detailed information about each service
#     if 'services' in services_response:
#         for service in services_response['services']:
#             print(f"Service Name: {service['name']}")
#             print(f"Service Title: {service['title']}")
#             if 'documentation' in service:
#                 print(f"Service Documentation: {service['documentation']['summary']}")
#             print("")
#
# if __name__ == "__main__":
#     list_gcp_services()
