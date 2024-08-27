# Registration of candidates for the election
leader = []
for i in range(1, 6):
    leader_name = input("Enter your leader name :")
    leader.append(leader_name)
n = len(leader)
if n < 5:
    print("You have been successfully registered")
else:
    print("Maximum candidate have been enrolled")

# Registration of voters
voter = []
number = int(input("Enter total number of voters want to cast their vote: "))
for i in range(1, number + 1):
    voter_id = int(input("Enter voter id number: "))
    voter.append(voter_id)

# Variables to keep track of vote counts
leader_votes = [0] * 5

# Voting session
while True:
    if not voter:
        print("Voting session is over")
        max_votes = max(leader_votes)
        winner_index = leader_votes.index(max_votes)
        percent = (max_votes / number) * 100
        print(leader[winner_index], "has won with", percent, "% votes")
        break
    else:
        voter_id = int(input("Enter your voter-id number: "))
        if voter_id in voter:
            print("You are a voter")
            voter.remove(voter_id)
            vote = int(input("Cast your vote for:\n1. {}\n2. {}\n3. {}\n4. {}\n5. {}\nEnter the number of the candidate: ".format(leader[0], leader[1], leader[2], leader[3], leader[4])))
            if 1 <= vote <= 5:
                leader_votes[vote-1] += 1
                print("Thank you for casting your vote")
            else:
                print("Invalid candidate number. Please try again.")
        else:
            print("You are not a voter or have already voted.")

