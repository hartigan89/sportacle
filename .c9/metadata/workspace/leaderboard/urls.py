{"filter":false,"title":"urls.py","tooltip":"/leaderboard/urls.py","undoManager":{"mark":90,"position":90,"stack":[[{"start":{"row":0,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["from django.conf.urls import url","from gamelist import views","","urlpatterns = [","url(r'^gamelist/$', views.GameList, name='gamelist'),","url(r'^(?P<sport_slug>[-\\w]+)/$', views.GameList, name='game_list_by_sport'),","]"],"id":2}],[{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":["t"],"id":3}],[{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":["s"],"id":4}],[{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"remove","lines":["i"],"id":5}],[{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"remove","lines":["l"],"id":6}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":["e"],"id":7}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["m"],"id":8}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["a"],"id":9}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["g"],"id":10}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["l"],"id":11}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["e"],"id":12}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["a"],"id":13}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["d"],"id":14}],[{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["e"],"id":15}],[{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["r"],"id":16}],[{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["b"],"id":17}],[{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["o"],"id":18}],[{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["a"],"id":19}],[{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["r"],"id":20}],[{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["d"],"id":21}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":77},"action":"remove","lines":["url(r'^(?P<sport_slug>[-\\w]+)/$', views.GameList, name='game_list_by_sport'),"],"id":22}],[{"start":{"row":4,"column":53},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":23}],[{"start":{"row":4,"column":49},"end":{"row":4,"column":50},"action":"remove","lines":["t"],"id":24}],[{"start":{"row":4,"column":48},"end":{"row":4,"column":49},"action":"remove","lines":["s"],"id":25}],[{"start":{"row":4,"column":47},"end":{"row":4,"column":48},"action":"remove","lines":["i"],"id":26}],[{"start":{"row":4,"column":46},"end":{"row":4,"column":47},"action":"remove","lines":["l"],"id":27}],[{"start":{"row":4,"column":45},"end":{"row":4,"column":46},"action":"remove","lines":["e"],"id":28}],[{"start":{"row":4,"column":44},"end":{"row":4,"column":45},"action":"remove","lines":["m"],"id":29}],[{"start":{"row":4,"column":43},"end":{"row":4,"column":44},"action":"remove","lines":["a"],"id":30}],[{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"remove","lines":["g"],"id":31}],[{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"insert","lines":["l"],"id":32}],[{"start":{"row":4,"column":43},"end":{"row":4,"column":44},"action":"insert","lines":["e"],"id":33}],[{"start":{"row":4,"column":44},"end":{"row":4,"column":45},"action":"insert","lines":["a"],"id":34}],[{"start":{"row":4,"column":45},"end":{"row":4,"column":46},"action":"insert","lines":["d"],"id":35}],[{"start":{"row":4,"column":46},"end":{"row":4,"column":47},"action":"insert","lines":["e"],"id":36}],[{"start":{"row":4,"column":47},"end":{"row":4,"column":48},"action":"insert","lines":["r"],"id":37}],[{"start":{"row":4,"column":48},"end":{"row":4,"column":49},"action":"insert","lines":["b"],"id":38}],[{"start":{"row":4,"column":49},"end":{"row":4,"column":50},"action":"insert","lines":["o"],"id":39}],[{"start":{"row":4,"column":50},"end":{"row":4,"column":51},"action":"insert","lines":["a"],"id":40}],[{"start":{"row":4,"column":51},"end":{"row":4,"column":52},"action":"insert","lines":["r"],"id":41}],[{"start":{"row":4,"column":52},"end":{"row":4,"column":53},"action":"insert","lines":["d"],"id":42}],[{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"remove","lines":["t"],"id":43}],[{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"remove","lines":["s"],"id":44}],[{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"remove","lines":["i"],"id":45}],[{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"remove","lines":["L"],"id":46}],[{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"remove","lines":["e"],"id":47}],[{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"remove","lines":["m"],"id":48}],[{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"remove","lines":["a"],"id":49}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"remove","lines":["G"],"id":50}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["l"],"id":51}],[{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["e"],"id":52}],[{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":["a"],"id":53}],[{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"insert","lines":["d"],"id":54}],[{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["e"],"id":55}],[{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"insert","lines":["r"],"id":56}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":32},"action":"remove","lines":["leader"],"id":57},{"start":{"row":4,"column":26},"end":{"row":4,"column":44},"action":"insert","lines":["leaderboard_page()"]}],[{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"remove","lines":["t"],"id":58}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"remove","lines":["s"],"id":59}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"remove","lines":["i"],"id":60}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"remove","lines":["l"],"id":61}],[{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["e"],"id":62}],[{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"remove","lines":["m"],"id":63}],[{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"remove","lines":["a"],"id":64}],[{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"remove","lines":["g"],"id":65}],[{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["l"],"id":66}],[{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["e"],"id":67}],[{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["a"],"id":68}],[{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["d"],"id":69}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["e"],"id":70}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["r"],"id":71}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["b"],"id":72}],[{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["o"],"id":73}],[{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["a"],"id":74}],[{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["r"],"id":75}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["d"],"id":76}],[{"start":{"row":4,"column":46},"end":{"row":4,"column":47},"action":"remove","lines":[")"],"id":77}],[{"start":{"row":4,"column":45},"end":{"row":4,"column":46},"action":"remove","lines":["("],"id":78}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"remove","lines":["d"],"id":79}],[{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"remove","lines":["r"],"id":80}],[{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"remove","lines":["a"],"id":81}],[{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"remove","lines":["o"],"id":82}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"remove","lines":["b"],"id":83}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"remove","lines":["r"],"id":84}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"remove","lines":["e"],"id":85}],[{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["d"],"id":86}],[{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"remove","lines":["a"],"id":87}],[{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"remove","lines":["e"],"id":88}],[{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"remove","lines":["l"],"id":89}],[{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"remove","lines":["$"],"id":90}],[{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"remove","lines":["/"],"id":91}],[{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"remove","lines":["^"],"id":92}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":53},"end":{"row":4,"column":53},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1510085807889,"hash":"627addab8672a10104be47abb84492d7c83e26c4"}