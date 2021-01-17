# Election Analysis

## Overview of Election Audit

### Background
I am assisting a Colorado Board of Elections employee in election audit of tabulated results for a US Congressional precinct in Colorado. The election data is provided in a CSV file with following columns:

* Ballot ID
* Country
* Candidate

### Purpose
 Our task is to find:
1. The total number votes cast in this elections
2. The total number of votes for each candidate
3. The percentage of votes for each candidate
4. Determine the winner of the election
5. Total number of votes for each county
6. Percentage of votes for each county
7. Determine county with largest turnout   

### Resources
- Data Source: election_results.csv
- Software: Python 3.7.6; Visual Studio Code 1.52.1
## Election-Audit Results

### Command Line Output

![terminal_output](./images/terminal_output.PNG)

### TXT File Output

![notepad_output](./images/notepad_output.PNG)

* How many votes were cast in this congressional election?
   
    *Answer:* The total number of votes cast in this congressional election is **369,711**
    

* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct

    *Answer:* Given below is the breakdown of number and percentage of votes in each county.

    ```
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)`
    ```
* Which county had the largest number of votes?

    *Answer:* The county with largest number of votes is **Denver**.

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

    *Answer:* Please find below the number and percentage of votes each candidate received.

    ```
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    ```

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

   *Answer:* The details of the winning candidates are:
    ```
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    ```
## Election-Audit Summary

The script used to analyze the election data for Colorado Board of Elections is versatile and efficient. It can be used to analyze hundreds of thousands of data elements in few seconds. The script is written in Python, which is one of the most widely used programming language in the world. 

This script can be used to analyze not only the current Congressional elections but any other elections with few modifications. For e.g.:

 1. The script can be used for *Senatorial Elections*. In this case, we will have senatorial districts instead of counties. However, the basic code will remain the same with few minor changes.
 
    * The variables and data structures will have descriptive names indicating that these represent senatorial districts instead of counties. 
    * In print statements, we can substitute "County" with "Senatorial District".
    * No changes will be required for counting votes (and percentage of votes) for each candidate. The code to determine the winner will also remain the same. 

    Similarly, the script can be used for *Local Elections* as well. 

 2. In an election, there are different types of *voting methods*. For e.g., in the Congressional Elections analyzed earlier, there were three voting methods: 
    * Mail-In Ballots 
    * Punch Cards 
    * Direct Recording Electronic (DRE) Machines.  

    Using the coding pattern we earlier used to count the number of votes and percentage of votes for each county, we can count 
    
    * The number of votes cast through a voting method
    * The percentage of votes cast through each voting method
    * The most widely used (or least used) voting method 
    
    However, this will require the voting method of each Ballot ID to be listed in the election results dataset.

3. In case some additional data about voters or candidates are given in the election results dataset, we can use the same script with few additional modifications to analyze the voting patterns and preferences. For e.g.,

    * Demographic Data: In case certain demographic details (gender or age-group) about each Ballot Id are available, we can analyze which demographic group votes most actively. Or, with some further modifications, which candidate is popular among certain demography.
    * In case more than one candidates in contest from a political party, we can edit the script to determine which party received the highest number of votes, apart from vote counts for each candidate. In this case, additional column about party of each candidate will be required in the dataset. 



