import requests

def get_profile(username: str):

    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        username
    
        profile {
          realName
          ranking
          userAvatar
        }
    
        submitStats {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """

    response = requests.post(
        "https://leetcode.com/graphql",
        json={
            "query": query,
            "variables": {
                "username": username
            }
        }
    )

    response_data = response.json()

    if response_data["data"]["matchedUser"] is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    data = response_data["data"]["matchedUser"]

    stats = data["submitStats"]["acSubmissionNum"]

    return {
        "username": data["username"],
        "real_name": data["profile"]["realName"],
        "ranking": data["profile"]["ranking"],
        "avatar": data["profile"]["userAvatar"],
        "total_solved": stats[0]["count"],
        "easy_solved": stats[1]["count"],
        "medium_solved": stats[2]["count"],
        "hard_solved": stats[3]["count"]
    }