import pandas as pd

# Loading the csv file
df_election = pd.read_csv(r"C:\Users\karki\Downloads\Starter_Code (4)\Starter_Code\PyPoll\Resources\election_data.csv")
df_election.head()
# Calculating the total votes with unique Ballot ID
total_votes = df_election['Ballot ID'].nunique()
total_votes

# Calculating the percentage of votes for each candidates
candidate_votes = df_election['Candidate'].value_counts()
candidate_percentages = (candidate_votes / total_votes) * 100
candidate_percentages

# looking for the candidate with max vote.
winner = candidate_votes.idxmax()
winner

# printing the final result.
election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
for candidate, x in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    election_results += f"{candidate}: {percentage:.3f}% ({votes})\n"
election_results += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------"
)

print(election_results)





