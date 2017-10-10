from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys

key = "87198d53abe5660c6df6acfe563e4f82"
secret = "a69d91c1435bc54c"
# downloads後の待機時間(1以上を指定)
wait_time = 1

# キーワードをチェックする
if len(sys.argv) < 2:
    print("python test/py(keyword)")
    sys.exit()
keyword = sys.argv[1]
savedir = "./" + keyword
if not os.path.exists(savedir):
    os.mkdir(savedir)

# Flickr APIで写真を取得
flickr = FlickrAPI(key,secret,format = 'parsed-json')
res = flickr.photos.search(
    text = keyword,
    per_page = 500,
    media = 'photos',
    sort = "relevance",
    safe_search = 1,
    extras = 'url_q,licence')

# 検索結果を確認
photos = res['photos']
pprint(photos)
try:
    # １つずつ画像をダウンロードする
    for i, photo in enumerate(photos['photo']):
        url_q = photo['url_q']
        filepath = savedir+'/'+photo['id']+'.jpg'
        if os.path.exists(filepath):continue
        print(str(i + 1 )+ ":download=",url_q)
        urlretrieve(url_q,filepath)
        time.sleep(wait_time)
except:
    import traceback
    traceback.print_exc()
