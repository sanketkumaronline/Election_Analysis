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

### Command Line Output

![terminal_output](./images/terminal_output.png)

### TXT File Output

![notepad_output](./images/notepad_output.png)

* How many votes were cast in this congressional election?
   
    *Ans:* The total number of votes cast in this congressional election is **369,711**.
    

* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct

    *Ans:* Given below is the breakdown of number and percentage of votes in each county.

    ```
    Jefferson: 10.5% (38,855)

    Denver: 82.8% (306,055)

    Arapahoe: 6.7% (24,801)`
    ```
* Which county had the largest number of votes?

    *Ans:* The county with largest number of votes is **Denver**.

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

    *Ans:* Please find below the number and percentage of votes each candidate received.

    ```
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    ```

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
*   Ans:* The details of the winning candidates are:
    ```
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    ```
## Election-Audit Summary