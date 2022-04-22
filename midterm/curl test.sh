#!/bin/bash
curl -XPOST localhost:8000/reviews \
-H 'content-type:application/json' \
-d '{"original_text":
"La gabapentine est un trÃ¨s bon mÃ©dicament pour traiter les symptÃ´mes. Questo farmaco potrebbe potenzialmente portare a effetti collaterali neurologici potenziati (specialmente in combinazione con il suo oxazepam). Synthroid wirkt, wenn es tÃ¤glich morgens zum FrÃ¼hstÃ¼ck eingenommen wird. AuÃŸerdem sollte es besser auf nÃ¼chternen Magen eingenommen werden. Oxazepam tiene efectos secundarios graves, lea atentamente la etiqueta antes de tomar. Oksazepam uykusuzluÄŸumu tedavi etmemde iÅŸe yaradÄ±. Î— ÏÎ±Î¼Î¹Ï€ÏÎ¯Î»Î· Î­Ï‡ÎµÎ¹ ÏƒÎ¿Î²Î±ÏÎ­Ï‚ Ï€Î±ÏÎµÎ½Î­ÏÎ³ÎµÎ¹ÎµÏ‚, Î½Î± ÎµÎ¯ÏƒÏ„Îµ Ï€ÏÎ¿ÏƒÎµÎºÏ„Î¹ÎºÎ¿Î¯ Ï€ÏÎ¹Î½ Ï„Î· Î»Î®ÏˆÎ·."
}'
