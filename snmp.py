import pysnmp

COMMUNITY_STRING = 'per1sc0pe'
SNMP_PORT = 161

a_device = ('205.234.19.42', COMMUNITY_STRING, SNMP_PORT) 

snmp_data = snmp_get_oid(a_device, oid='.1.3.6.1.2.1.1.1.0', display_errors=True)
output = snmp_extract(snmp_data)

print output



sif you want %{TIMESTAMP_ISO8601} I believe