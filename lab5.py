class Candidate: 
    """
    Створює клас Candidate який показує його і'мя та кількість голосів.
    """
    def __init__(self, candidete_name, candidete_votes):
        self.name = candidete_name
        self.__votes = candidete_votes
    
    def get_name(self):
        return self.name
    
    def get_votes(self):
        return self.__votes
    
    def set_votes(self, votes):
        self.__votes = votes
    
    def set_name(self, name):
        self.name = name
    
    def get_percentage_of_total_votes(self, total_votes1):
        return (self.__votes / total_votes1) * 100
    
    def __str__(self):
        return f"{self.name}: {self.__votes} голосів"
    
    def __del__(self):
        print(f"Обєкт Candidate з ім'ям {self.name} видаляється")

class Elections:
    """
    Створює клас Elections який відображає виборчий процес з участю кандидатів та їх голосів.
    """
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
