# Election Analysis

## Overview of Election Audit

### Background
I am assisting a Colorado Board of Elections employee in election audit of tabulated results for a US Congressional precinct in Colorado. The election data is provided in a CSV file with following columns:

* Ballot ID
* Country
* Candidate

### Purpose
 Our task is to find:
1. The total number votes cast in this congressional elections
2. The total number of votes for each candidate
3. The percentage of votes for each candidate
4. Determine winner of the election based on popular vote
5. Total number of votes for each county
6. Percentage of votes for each county
7. Determine county with largest turnout   

### Resources
- Data Source: election_results.csv
- Software: Python 3.7.6; Visual Studia Code 1.52.1
## Electon-Audit Results

* How many votes were cast in this congressional election?

    `The total number of votes cast in this congressional election is **369,711**.`


* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct

    Given below is the breakdown of number and percentage of votes in each county.

    `Jefferson: 10.5% (38,855)`

    `Denver: 82.8% (306,055)`

    `Arapahoe: 6.7% (24,801)`

### 3. Which county had the largest number of votes?
Ans: The county with largest number of votes is **Denver**.

![largest_county_turnout](./images/largest_county_turnout.png)
### 4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Ans: Please find below the total and percentage of votes each candidate received.
* Charles Casper Stockham : 85,213 votes (23.0% of total)
* Diana DeGette : 272,892 votes (73.8% of total)
* Raymon Anthony Doane : 11,606 votes (3.15 of total)

![candidate_votes](./images/candidate_votes.png)
### 5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Ans: The details of the winning candidates are:
* Name of Winner : Diana DeGette
* Vote Count for Winner : 272,892
* Percentage of Votes : 73.8% 

![winning_candidate](./images/winning_candidate.png)

## Election-Audit Summary