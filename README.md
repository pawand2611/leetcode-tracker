## LeetCode Integration Research

### Data Source

LeetCode primarily exposes user information through a GraphQL endpoint:

https://leetcode.com/graphql

### Required User Data

* Username
* Real Name
* Ranking
* Contest Rating
* Easy Solved
* Medium Solved
* Hard Solved
* Total Solved
* Avatar

### Planned Flow

User enters username
→ FastAPI requests LeetCode GraphQL API
→ Response parsed
→ Data stored in PostgreSQL
→ Frontend displays profile

### Future Enhancements

* Contest rating history
* Daily solved statistics
* Friend comparison
* Leaderboards
* Streak tracking
