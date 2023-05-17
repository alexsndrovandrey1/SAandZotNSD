import pycti
from stix2 import TLP_GREEN
from datetime import datetime
date = datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")

api_url = 'http://localhost:8088'
api_token = '56ad8745-f2n5-781e-lw3h-658071gr2956'
client = pycti.OpenCTIApiClient(api_url, api_token)

TLP_GREEN_CTI = client.marking_definition.read(id=TLP_GREEN["id"])
with open('dns.log', 'r') as f:
    domains = f.read().splitlines()
k = 1
for domain in domains:
    indicator = client.indicator.create(
    name="Malicious domain {}".format(k),
    description="MPVS hosts",
    pattern_type="stix",
    label="mpvs hosts",
    pattern="[domain-name:value = '{}']".format(domain),
    x_opencti_main_observable_type="IPv4-Addr",
    valid_from=date,
    update=True,
    score=75,
    markingDefinitions=[TLP_GREEN_CTI["id"]],
    )
    print("Создан индикатор:", indicator["id"])
    k += 1