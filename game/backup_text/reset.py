def reset(x):
    """
    Reset the game's stats, shop items, and scores.

    Parameters:
    x (bool): If True, reset the scores for each level as well.
    """
    #Restore statistics backup
    with open('game/backup_text/stats_backup.txt','r') as statsFile:
        stats = statsFile.readlines()
    with open('game/stats.txt','w') as textFile:
        outText = ""
        for i in stats:
            outText += i
        textFile.write(outText)
    #Restore shop items backup
    with open('game/backup_text/shop_items_backup.txt','r') as itemsFile:
        items = itemsFile.readlines()
    with open('game/shop_items.txt','w') as textFile:
        outText = ""
        for i in items:
            outText += i
        textFile.write(outText)
    # Resetting scores for each level if x is True
    if x:
        blankScores = "0 0 0 0 0\n- - - - -"
        with open('game/scores/lvl1.txt','w') as textFile:
            textFile.write(blankScores)
        with open('game/scores/lvl2.txt','w') as textFile:
            textFile.write(blankScores)
        with open('game/scores/lvl3.txt','w') as textFile:
            textFile.write(blankScores)
reset(False)