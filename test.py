data="{"created_at":"Tue Jul 30 19:24:01 +0000 2019","id":1156284329779191808,"id_str":"1156284329779191808","text":"Technical events 2019 I am look for in this tweet Register here - https:\/\/t.co\/HKWCtyzXyv","source":"\u003ca href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\"\u003eTwitter Web App\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":2784419143,"id_str":"2784419143","name":"Ayush","screen_name":"heyayushh","location":"Jaipur, India","url":"http:\/\/heyayush.dev","description":"Microsoft Student Partner | Azure certified AI Associate | love espresso","translator_type":"none","protected":false,"verified":false,"followers_count":162,"friends_count":284,"listed_count":4,"favourites_count":5153,"statuses_count":730,"created_at":"Mon Sep 01 16:52:09 +0000 2014","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"000000","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"91D2FA","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"000000","profile_text_color":"000000","profile_use_background_image":false,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1105649372895694848\/XB8TyzI2_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1105649372895694848\/XB8TyzI2_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/2784419143\/1495116975","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[{"url":"https:\/\/t.co\/HKWCtyzXyv","expanded_url":"https:\/\/events.yourstory.com\/techsparks","display_url":"events.yourstory.com\/techsparks","indices":[66,89]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"en","timestamp_ms":"1564514641600"}"

objects = data.splitlines()
for line in objects:
    d = json.loads(line)
text = list(d['text'])
urls = []


if 'entities' in d:
    if 'urls' in d['entities']:
        for url in d['entities']['urls']:
            urls.append(url['expanded_url'])
            pass
