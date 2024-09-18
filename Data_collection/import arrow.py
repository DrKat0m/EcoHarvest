import arrow
import requests
import json

start = arrow.get('2021-05-15')
end = arrow.get('2021-05-17')

response = requests.get(
  'https://api.stormglass.io/v2/bio/point',
  params={
    'lat': 39.99123863014912,   
    'lng': -75.20719492025617 ,
    'params': ','.join(['ph']),
    'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
    'end': end.to('UTC').timestamp(),      # Convert to UTC timestamp
  },
  headers={
    'Authorization': 'df8ed950-4f3c-11ee-a26f-0242ac130002-df8ed9e6-4f3c-11ee-a26f-0242ac130002'
  }
)

print(json.dumps(response.json(), indent=4))
