# Last updated: 10/14/2025, 7:13:23 PM
#rank on most pos 1 votes, then pos 2, then so on and so forth
#all voters rank all teams-at most 26

import heapq



class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        #priority queue 
        voteDict = {}
        n_teams = len(votes[0])
        #set up dict:
        for i in range(n_teams):
            team = votes[0][i]
            voteDict[team] = [0]*n_teams
            voteDict[team][i] = 1
        
        for i, vote in enumerate(votes[1:]):
            for j in range(n_teams):
                team = vote[j]
                voteDict[team][j]+=1
        pq = []
        heapq.heapify(pq)
        for key in voteDict.keys():
            teamVotes = [-x for x in voteDict[key]]
            teamVotes.append(key)
            heapq.heappush(pq, teamVotes)
        
        outputStr = ""

        while pq:
            dmp = heapq.heappop(pq)
            outputStr += dmp[-1]

        return outputStr


        