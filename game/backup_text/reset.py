def reset():
    with open('game/backup_text/stats_backup.txt','r') as statsFile:
        stats = statsFile.readlines()
    with open('game/stats.txt','w') as textFile:
        outText = ""
        for i in stats:
            outText += i
        textFile.write(outText)

    with open('game/backup_text/shop_items_backup.txt','r') as itemsFile:
        items = itemsFile.readlines()
    with open('game/shop_items.txt','w') as textFile:
        outText = ""
        for i in items:
            outText += i
        textFile.write(outText)

    with open('game/scores.txt','w') as textFile:
        textFile.write("")
reset()