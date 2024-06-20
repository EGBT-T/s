from io import StringIO
import requests

response = requests.get(
                        'https://',
                        auth=('',''))

_data = response.text.replace(';', ',')
_data = StringIO(_data[:])
_data = pd.read_csv(_data)

_data
