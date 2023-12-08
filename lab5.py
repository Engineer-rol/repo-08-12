class Candidate:
    def __init__(self, name, votes):
        self.__name = name
        self.__votes = votes
    def get_name(self):
        return self.__name
    def get_votes(self):
        return self.__votes
    def set_votes(self, votes):
        self.__votes = votes
    def set_name(self, name):
        self.__name = name
    def get_percentage_of_total_votes(self, total_votes):
        return (self.__votes / total_votes) * 100
    def __str__(self):
        return f"{self.__name}: {self.__votes} votes"
    def __del__(self):
        print(f"Instance of Candidate with name {self.__name} is being destroyed")

class Elections:
    def __init__(self):
        self.__candidates = []

    def add_candidate(self, candidate):
        self.__candidates.append(candidate)

    def calculate_winner(self):
        return max(self.__candidates, key=lambda candidate: candidate.get_votes())
    def find_winner(self):
        return self.calculate_winner()
    def remove_candidate(self, candidate):
        self.__candidates.remove(candidate)
    def get_candidates(self):
        return self.__candidates

if __name__ == "__main__":
    elections = Elections()
    total_votes = 0
    for i in range(5):
        name = input(f"Enter the name of candidate {i + 1}: ")
        votes = int(input(f"Enter the number of votes for {name}: "))
        total_votes += votes
        candidate = Candidate(name, votes)
        elections.add_candidate(candidate)
    print("\nElection Results:")
    for candidate in elections.get_candidates():
        print(candidate.get_name())
        print(f"Votes: {candidate.get_votes()}")
        print(f"Percentage of Total Votes: {candidate.get_percentage_of_total_votes(total_votes):.2f}%\n")
    winner = elections.find_winner()
    print(f"The winner is {winner.get_name()} with {winner.get_votes()} votes!")
