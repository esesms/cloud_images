import flickrapi
import urllib.request
#from PIL import Image


api_key = u'8ae389de9dbb32ad931ae7745672484f'
api_secret = u'd6454322bc20a4b5'

flickr = flickrapi.FlickrAPI(api_key, api_secret)

keyword = 'clouds'

urls = []

for photo in flickr.walk(tag_mode='all',
        tags = 'cloud, sky',
        extras = 'url_c',
        sort = 'relevance',
        min_upload_date = '1543510800',
        max_upload_date = '1543597200',
        content_type = 1,
        per_page = 10,
        color_codes = 'c'):    #7 for cyan, 8 for blue, c for white
    title = photo.get('title') #get title
    url = photo.get('url_c')   #get url
    urls.append(url)           #add url to the urls array
    print(title)
    print(url)
    #i = len(urls)-1
    #print(i)
  
    #Download image from the url and save it to '00001.jpg'

for index,s in enumerate(urls):
    i = index
    print(i)
    urllib.request.urlretrieve(urls[i], str(i) + '.jpg')
    


#local_filename, headers = urllib.request.urlretrieve(urls[10])
#html = open(local_filename)
    
    
