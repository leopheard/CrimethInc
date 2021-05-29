from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://exworker.libsyn.com/rss"
url2 = "https://crimethinc.com/podcast/feed"
url3 = "https://crimethinc.com/podcast/feed"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/a/7/9/e/a79ece9ad4730f3f/full-size1400px.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/6/2/9/d/629d3079810b02af/NWTCB6-1400.jpg"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/6/b/0/e/6b0e57351d7e6a2c/hotwire-46.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup1 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
