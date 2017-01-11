import re

url = '''<tr>
<td style="text-align: center; vertical-align: middle;">e3</td>
<td style="text-align: center; vertical-align: middle;">16 sol/s</td>
<td style="text-align: center; vertical-align: middle;">15 sol/s</td>
<td style="text-align: center; vertical-align: middle;">0.6%</td>
<td style="text-align: center; vertical-align: middle;"><script>document.write(formatTimestampUptoMinute(new Date(1484099475)))</script></td>
</tr>

<tr>
<td style="text-align: center; vertical-align: middle;">gtx980</td>
<td style="text-align: center; vertical-align: middle;">270 sol/s</td>
<td style="text-align: center; vertical-align: middle;">213 sol/s</td>
<td style="text-align: center; vertical-align: middle;">0.7%</td>
<td style="text-align: center; vertical-align: middle;"><script>document.write(formatTimestampUptoMinute(new Date(1484099462)))</script></td>
</tr>'''

stations = re.findall('\d{1,3}'+'\s', url)
print stations
#pprint(dict(stations), indent=4) +'[sol/s] '[>]'+