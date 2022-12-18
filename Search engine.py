def matchscore(sen1,sen2):
    score=0
    match1=sen1.split(" ")
    match2=sen2.split(" ")
    for match1 in match1:
        for match2 in match2:
            if match1.lower()==match2.lower():
                score+=1
    return score
if __name__ == '__main__':
    lists = ["Python is good", "Python is interesting", "You are not human", "I will not speak with you"]
    query = input("Enter your query string:")
    scores=[matchscore(query,sentence) for sentence in lists]
    sentscorelist=[sentscore for sentscore in sorted(zip(scores,lists),reverse=True)]
    print(f"{len(sentscorelist)} results found!")
    for score,item in sentscorelist:
        print(f"{item} with score of {score}")