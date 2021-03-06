# DevOps_Oct2021_Team04
This is the dev repo used by P01 Team 4 for Ngee Ann Polytechnic DevOps module's assignment.

## DevOps Team Formation

| Role | Member Name |
| --- | --- |
| `Project Manager` | Zeng Zihui |
| `Technical Lead` | Swah Jian Oon |
| `Quality Assurance Lead` | Ryan Lee Rui Yuan |
| `Developer` | Zheng Jiongjie |
| `Quality Assurance` | Chua Qi Heng |


## Project Background
```
You are the mayor of Simp City, and you want to build the happiest and most prosperous 
city possible, i.e., score the most points.
This city-building strategy game is played over 16 turns. In each turn, you will build one 
of two randomly-selected buildings in your 4x4 city. In the first turn, you can build 
anywhere in the city. In subsequent turns, you can only build on squares that are 
connected to existing buildings. The other building that you did not build is discarded.
Each building scores in a different way. The objective of the game is to build a city that 
scores as many points as possible
```

## Project Approach 
```
This Simp City project will be split into 2 development iterations. 
Each iteration will be done over a period of 3-4 weeks.
The software development methodologies used for this project is Kanban Methodology for Agile software development.
```
### Iteration 1
In this iteration, we will cover the following features:
1. Display Main Menu
2. Start New Game
3. Exit Game
4. Display Game Menu
5. Build a Building (without the game logic & randomization of building)
6. See Remaining Buildings
7. Exit to Main Menu

### Class Diagram As Of Iteration 1
<img src="https://user-images.githubusercontent.com/64000939/145531915-82ef0a93-6965-4b1d-86cf-63c5fdfe394d.png" width=60%>

### Iteration 2
In this iteration, we will be covering the follow features:
1. Load Saved Game
2. Add Game Logic & Randomization of building
3. See Current Score
4. Save Game
5. Display Final Score
6. Choose Building Pool
7. Choose City Size
8. Update High Score List
9. Show High Score
10. Always Displaying Remaining Buildings Left

### Class Diagram As Of Iteration 2
<img src="https://user-images.githubusercontent.com/64000939/152786084-d73bb25f-9abe-490e-9fc9-0a9db7649e35.png" width=60%>

### 4 Software Development Methodologies Considered
1. Spiral Model
2. Iterative Model
3. Evolutionary Model
4. Kanban Model (Agile)

## Project Board 
Automated Kanban board is used.

| Column Name | Description |
| --- | --- |
| `User Story` | Contains user stories that are not used for development yet |
| `Filter Cards` | Contains filter cards for all the members |
| `project Backlog` | Contains current requirement tasks for development |
| `Dev Backlog Tasks` | Contains current Dev backlog tasks for developer to take |
| `QA Backlog Tasks` | Contains current QA backlog tasks for QA to take |
| `In Progress` | Contains tasks that are still doing |
| `In Review` | Contains tasks that are completed and require reviewers to review |
| `Done` | COntains tasks that are completed and reviewed |

**Please take note, finished user stories will still be in Project Backlog Column. The issue will be closed and it will be placed at the bottom of the Project Backlog column.*

### User Story Card
<img src="https://user-images.githubusercontent.com/93191650/145514046-923f3303-1fc3-4a6c-ba1b-3e703ec53fcf.png" width=60%>
Inside the User Story card, the following components will be there

| Component | Description |
| --- | --- |
| `Title` | User story |
| `Acceptance Criteria` | acceptance criteria for this user story is added in the description of the issue |
| `Assignees` | PM will assign to Tech Lead & QA Lead to complete this user story requirement |
| `Developer Tasks List` | Contains current QA backlog tasks for QA to take |
| `QA Tasks List` | Contains tasks that are still doing |
| `Label` | "user story" and user story ID are used  |
| `Milestone` | Identifies the current development iteration  |
| `Pull Request` | the corresponding pull requests for this user story are linked  |


**Tasks list is used to monitor the individual user story progress*
