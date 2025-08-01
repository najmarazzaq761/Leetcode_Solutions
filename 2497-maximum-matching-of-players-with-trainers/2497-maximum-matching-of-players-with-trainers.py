class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i,j=0,0
        players.sort()
        trainers.sort()
        while i<len(players) and j<len(trainers):
            if trainers[j]>=players[i]:
                i+=1
            j+=1
        return i