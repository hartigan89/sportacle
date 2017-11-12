{"filter":false,"title":"ranker.py","tooltip":"/ranker/ranker.py","undoManager":{"mark":47,"position":47,"stack":[[{"start":{"row":100,"column":0},"end":{"row":118,"column":37},"action":"remove","lines":["def getStats(prob, gamesWon):","    numGames = len(prob)","    expWon = 0","    edge = 0","    p = 0","    ","    #get p-value","    pb = PoiBin(prob)","    ","    if gamesWon > 0:","        p = 1-pb.cdf(gamesWon-1)","    else:","        p = 1-pb.cdf(gamesWon)","        ","    #get expected number of games won","    expWon = sum(prob)","    ","    #get probability edge","    edge = (gamesWon-expWon)/numGames"],"id":201}],[{"start":{"row":99,"column":0},"end":{"row":100,"column":0},"action":"remove","lines":["",""],"id":202}],[{"start":{"row":98,"column":107},"end":{"row":99,"column":0},"action":"remove","lines":["",""],"id":203}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":69},"action":"remove","lines":["    return {'numGames':numGames, 'expWon':expWon, 'edge':edge, 'p':p}"],"id":204}],[{"start":{"row":99,"column":0},"end":{"row":100,"column":0},"action":"remove","lines":["",""],"id":205}],[{"start":{"row":98,"column":107},"end":{"row":99,"column":0},"action":"remove","lines":["",""],"id":206}],[{"start":{"row":98,"column":12},"end":{"row":98,"column":49},"action":"remove","lines":["'expWon':expWon, 'edge':edge, 'p':p, "],"id":207}],[{"start":{"row":5,"column":4},"end":{"row":8,"column":9},"action":"remove","lines":["numGames = 0","    expWon = 0","    edge = 0","    p = 0"],"id":208}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":["    "],"id":209}],[{"start":{"row":4,"column":38},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":210}],[{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"insert","lines":["S"],"id":211}],[{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"insert","lines":["m"],"id":212}],[{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"insert","lines":["o"],"id":213}],[{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"insert","lines":["o"],"id":214}],[{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"insert","lines":["t"],"id":215}],[{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"insert","lines":["h"],"id":216}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":26},"action":"remove","lines":["prob, gamesWon"],"id":217},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["p"]}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["V"],"id":218}],[{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["a"],"id":219}],[{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["l"],"id":220}],[{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["u"],"id":221}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["e"],"id":222}],[{"start":{"row":9,"column":4},"end":{"row":15,"column":17},"action":"remove","lines":["#get stats","    dict = getStats(prob, gamesWon)","    ","    numGames = dict[\"numGames\"]","    expWon = dict[\"expWon\"]","    edge = dict[\"edge\"]","    p = dict[\"p\"]"],"id":223}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":224}],[{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"remove","lines":["",""],"id":225}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":226}],[{"start":{"row":7,"column":21},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":227}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["n"],"id":228}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["u"],"id":229}],[{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["m"],"id":230}],[{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["G"],"id":231}],[{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["a"],"id":232}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["m"],"id":233}],[{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["e"],"id":234}],[{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["s"],"id":235}],[{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":[","],"id":236}],[{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":[" "],"id":237}],[{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"remove","lines":["e"],"id":238}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"remove","lines":["u"],"id":239}],[{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"remove","lines":["l"],"id":240}],[{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"remove","lines":["a"],"id":241}],[{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"remove","lines":["V"],"id":242}],[{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"remove","lines":["h"],"id":243}],[{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"remove","lines":["t"],"id":244}],[{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"remove","lines":["o"],"id":245}],[{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"remove","lines":["o"],"id":246}],[{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"remove","lines":["m"],"id":247}],[{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"remove","lines":["S"],"id":248}]]},"ace":{"folds":[],"scrolltop":771.5,"scrollleft":0,"selection":{"start":{"row":15,"column":35},"end":{"row":15,"column":35},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":54,"state":"start","mode":"ace/mode/python"}},"timestamp":1510094453896,"hash":"4406093eaf1eadd5721484f9647eb4b25be465e7"}