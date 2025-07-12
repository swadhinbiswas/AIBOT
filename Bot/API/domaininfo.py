import requests
from Bot.settings.setting import settings
import asyncio

"""


Once a joker, always a joker
This code is part of the Bot API for fetching domain information.
It retrieves detailed information about a domain, including web data, DNS records, IP information, and related data.
"""


async def format_data(data):
    formatted_data = []

    formatted_data.append(f"### Domain Information\n\n- **Domain**: {data['domain']}\n")

    web = data['web']
    formatted_data.append("### Web Data")
    formatted_data.append(f"\n- **Rank**: {web['rank']}")
    formatted_data.append(f"\n- **URL**: {web['url']}")
    formatted_data.append(f"\n- **IP**: {web['ip']}")
    formatted_data.append(f"\n- **Date**: {web['date']}")
    formatted_data.append(f"\n- **Length**: {web['length']}")
    formatted_data.append(f"\n- **Server**: {web['server']}")
    formatted_data.append(f"\n- **Encoding**: {web['encoding']}")
    formatted_data.append(f"\n- **Title**: {web['title']}")
    formatted_data.append(f"\n- **Links**:")
    for link in web['links']:
        formatted_data.append(f"  - {link}")

    dns = data['dns']
    formatted_data.append("\n### DNS Information")
    formatted_data.append(f"\n- **Domain**: {dns['domain']}")
    formatted_data.append("\n- **A Records**:")
    for record in dns['a']:
        formatted_data.append(f"  - {record}")
    formatted_data.append("\n- **AAAA Records**:")
    for record in dns['aaaa']:
        formatted_data.append(f"  - {record}")
    formatted_data.append("\n- **MX Records**:")
    for record in dns['mx']:
        formatted_data.append(f"  - {record}")
    formatted_data.append("\n- **NS Records**:")
    for record in dns['ns']:
        formatted_data.append(f"  - {record}")

    ipinfo = data['ipinfo']
    formatted_data.append("\n### IP Information")
    for ip, info in ipinfo.items():
        formatted_data.append(f"\n#### IP: {ip}")
        formatted_data.append(f"\n- **City**: {info['city']}")
        formatted_data.append(f"\n- **Region**: {info['region']}")
        formatted_data.append(f"\n- **Country**: {info['country']}")
        formatted_data.append(f"\n- **Location**: {info['loc']}")
        formatted_data.append(f"\n- **Postal**: {info['postal']}")
        formatted_data.append(f"\n- **Timezone**: {info['timezone']}")
        formatted_data.append(f"\n- **ASN**:")
        formatted_data.append(f"  - **ASN**: {info['asn']['asn']}")
        formatted_data.append(f"  - **Name**: {info['asn']['name']}")
        formatted_data.append(f"  - **Domain**: {info['asn']['domain']}")
        formatted_data.append(f"  - **Route**: {info['asn']['route']}")
        formatted_data.append(f"  - **Type**: {info['asn']['type']}")

    related = data['related']
    formatted_data.append("\n### Related Information")
    formatted_data.append("\n- **IP Addresses**:")
    for ip in related['ip']:
        formatted_data.append(f"  - {ip['value']} ({ip['count']} occurrences)")
    formatted_data.append("\n- **ASNs**:")
    for asn in related['asn']:
        formatted_data.append(f"  - {asn['value']} ({asn['count']} occurrences)")
    formatted_data.append("\n- **NS Records**:")
    for ns in related['ns']:
        formatted_data.append(f"  - {ns['value']} ({ns['count']} occurrences)")
    formatted_data.append("\n- **MX Records**:")
    formatted_data.append("  - No occurrences")
    formatted_data.append("\n- **Backlinks**:")
    for backlink in related['backlinks']:
        formatted_data.append(f"  - {backlink['value']} ({backlink['count']} occurrences)")
    formatted_data.append("\n- **Redirects**:")
    for redirect in related['redirects']:
        formatted_data.append(f"  - {redirect['value']} ({redirect['count']} occurrences)")

    return "\n".join(formatted_data)





async def domaininfo(domain:str):
  try:
        url=f"""https://host.io/api/full/{domain}?token={settings.HOST_API}"""

        response=requests.get(url)

        data=response.json()
        finaaldata=format_data(data)

        return finaaldata

  except Exception as e:
        return e
