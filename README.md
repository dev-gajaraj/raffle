# Raffle App

You will be writing a raffle app for an upcoming event. The raffle will be seed funded with an initial amount and attendees can purchase a ticket to participate in the draw. Attendees can also purchase additional tickets to increase their chances of winning, and maybe strike the jackpot!

Let's get to work!    

## Ticket Structure
1. Users can purchase up to a maximum of 5 tickets per draw. Value of each ticket is $5. 
2. Raffle will be seeded with an initial pot of $100
3. All proceeds from ticket sales contribute directly to the pot. For e.g. if total number of tickets sold is 20, total pot size for draw = $100 (seed funding) + 20 tickets*$5 = $200
4. Each ticket contains a set of 5 **randomly generated and unique** numbers between **[1-15]**

## Rewards Structure
| Prize Group       | Numbers Matched   | Reward           |
| ----------------- |:-----------------:| ----------------:|
| Group 2           | 2 winning numbers | 10% of total pot |
| Group 3           | 3 winning numbers | 15% of total pot |
| Group 4           | 4 winning numbers | 25% of total pot |
| Group 5 (Jackpot) | 5 winning numbers | 50% of total pot |

- If there is more than 1 winning ticket per group, the reward will be shared evenly among all ticket holders.
- Any remaining money in the pot will be rolled over to the next draw

## Game Mechanics

Create a console app that displays the following options (aka main menu) to users-
~~~
Welcome to My Raffle App
Status: Draw has not started

[1] Start a New Draw
[2] Buy Tickets
[3] Run Raffle
~~~

User can enter `1`, `2` or `3` to proceed

### Option 1
Option `1` allows user to start a new round of Raffle with a pot size of $100.
Control should return to the main menu after a new draw has been created

### Option 2
Users can buy tickets using Option `2`. They will be asked to enter their name and no of tickets they would like to purchase
~~~
Enter your name, number of tickets to purchase (for e.g. a valid input will be **James,1** )
~~~
When the user enters the above info, app should perform the following tasks

**a) Buy Tickets For User**

App should generate the required number of tickets for the new user. 

Each ticket should consist of 5 unique randomly generated numbers between [1-15] as mentioned in the Ticket Structure.

**b) Display Tickets to User**

App should display the purchased tickets to the user. User can press any key to return to the main menu.

More users can purchase tickets using Option `2` again

### Option 3
When all users have purchased tickets, user can enter option `3` to run the raffle. App will perform the following tasks-

**a) Get Winning Ticket**

App should generate a winning ticket- consisting of 5 unique and random numbers between [1-15]

**b) Get Winners**

App should match all purchased tickets against the winning ticket and 
- Identify the winning tickets for Groups 2, 3, 4 and 5
- Calculate the rewards for the winning tickets based on %reward for the respective groups. 

**c) Display Winners**

App should display the Group 2, 3, 4 and 5 winners and their total rewards.


## Example

The following simulation runs through the user interactions for a typical draw of the Raffle app. Take note of the pot size increasing as users purchase more tickets. The rewards distribution for winning tickets is based on the Rewards Structure mentioned above and reminder that multiple winning tickets within the same Group will share the group %reward.  

~~~
Welcome to My Raffle App
Status: Draw has not started

[1] Start a New Draw
[2] Buy Tickets
[3] Run Raffle
~~~
>input: 1

```
New Raffle draw has been started. Initial pot size: $100
Press any key to return to main menu
```
~~~
Welcome to My Raffle App. 
Status: Draw is ongoing. Raffle pot size is $100

[1] Start a New Draw
[2] Buy Tickets
[3] Run Raffle


~~~

>input: 2

~~~
Enter your name, no of tickets to purchase
~~~

>input: James,1

~~~
Hi James, you have purchased 1 ticket(s)-
Ticket 1: 4 7 8 13 14

Press any key to return to main menu
~~~

~~~
Welcome to My Raffle App
Status: Draw is ongoing. Raffle pot size is $105

[1] Start a New Draw
[2] Buy Tickets
[3] Run Raffle

~~~

>input: 2

~~~
Enter your name, no of tickets to purchase
~~~

>input: Ben,2

~~~
Hi Ben, you have purchased 2 ticket(s)-
Ticket 1: 3 6 9 11 13
Ticket 2: 3 7 8 11 14

Press any key to return to main menu
~~~

~~~
Welcome to My Raffle App
Status: Draw is ongoing. Raffle pot size is $115

[1] Start a New Draw
[2] Buy Tickets
[3] Run Raffle

~~~

>input: 2

~~~
Enter your name, no of tickets to purchase
~~~

>input: Romeo,3

~~~
Hi Romeo, you have purchased 3 ticket(s)-
Ticket 1: 3 7 9 14 15
Ticket 2: 4 5 10 12 15
Ticket 3: 1 2 7 12 13

Press any key to return to main menu
~~~

~~~
Welcome to My Raffle App
Draw is ongoing. Raffle pot size is $130

[1] Start a New Draw
[2] Buy Tickets
[3] Run Raffle

~~~

>input: 3

~~~
Running Raffle..
Winning Ticket is 3 7 8 11 12

Group 2 Winners:
James with 1 winning ticket(s)- $3.25
Ben with 1 winning ticket(s)- $3.25
Romeo with 2 winning ticket(s)- $6.5

Group 3 Winners:
Nil

Group 4 Winners:
Ben with 1 winning ticket(s)- $32.5

Group 5 Winners (Jackpot):
Nil

Press any key to return to main menu
~~~

~~~
Welcome to My Raffle App
Status: Draw has not started

[1] Start a New Draw
[2] Buy Tickets
[3] Run Raffle
~~~

>input: 1
```
New Raffle draw has been started. Initial pot size: $184.5
Press any key to return to main menu
```

## Coding Guidelines
- Include unit tests with code coverage for options 1,2 & 3 

Happy coding!
