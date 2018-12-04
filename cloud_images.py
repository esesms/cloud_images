import flickrapi
import urllib.request

api_key = '8ae389de9dbb32ad931ae7745672484f'
api_secret = 'd6454322bc20a4b5'

flickr = flickrapi.FlickrAPI(api_key, api_secret)

urls = []

ix = 0

for photo in flickr.walk(
        tags = 'cloud, clouds, sky, -plane, -airplane',
        tag_mode='all',    #all for AND, any for OR
        min_taken_date = '2018-11-01 12:00:00',
        max_taken_date = '2018-11-30 12:00:00',
        sort = 'relevance',    
        safe_search = 1,
        content_type = 1,
        extras = 'url_c',
        per_page = 10,
        color_codes = '8'):     #7 for cyan, 8 for blue, c for white
    title = photo.get('title')  #get title
    url = photo.get('url_c')    #get url
    urls.append(url)            #add url to the urls array
    print(title)                #print the title of the image               
    print(url)                  #print the url of the image
    print(ix)                   #print the index
    ix += 1
  
    

for index,s in enumerate(urls):
    i = index
    print(i)                    #print the index
    if urls[i]:
        urllib.request.urlretrieve(urls[i], str(i) + '.jpg')    #Download image from the url and save it to '00001.jpg'
    
