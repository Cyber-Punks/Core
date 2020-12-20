import falcon
import json
import os
import praw


class RedditScraper:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.environ["REDDIT_CLIENT_ID"],
            client_secret=os.environ["REDDIT_CLIENT_SECRET"],
            user_agent=os.environ["REDDIT_USER_AGENT"]
        )


    def parse_url(self, url):
        # Slice off everything before "r/SUBREDDIT_NAME
        split = url.split("/")
        for i in range(len(split)):
            if split[i] == "r":
                split = split[i:]
                break

        # r/SUBREDDIT_NAME/comments/SUBMISSION_ID/submission_slug/COMMENT_ID
        subreddit_name = split[1]
        submission_id = split[3] if len(split) >= 4 else None
        comment_id = split[5] if len(split) >= 6 else None

        return (subreddit_name, submission_id, comment_id)


    def on_get(self, req, res):
        node_url = req.params["node_url"]
        print(node_url)
        (subreddit_name, submission_id, comment_id) = self.parse_url(node_url)
        if (submission_id is None):
            res.status = falcon.HTTP_200
            node = self.scrape_subreddit(self.reddit.subreddit(subreddit_name))
            print(node)
            res.body = json.dumps(node)
        else:
            res.status = falcon.HTTP_400
            res.body = "Support for comments and submissions not yet implemented"


    def scrape_subreddit(self, subreddit):
        children = []

        for submission in subreddit.hot(limit=50):
            children.append(self.scrape_submission(submission))

        return {
            "source": "reddit.com/r" + subreddit.display_name,
            "name": "subreddit",
            "body": "",
            "children": children
        }


    def scrape_submission(self, submission):
        children = []

        for comment in submission.comments:
            children.append(self.scrape_comment(comment))

        return {
            "source": "reddit.com" + submission.permalink,
            "name": "submission",
            "body": submission.selftext,
            "children": children
        }


    def scrape_comment(self, comment):
        comment.replies.replace_more()
        children = []

        for reply in comment.replies:
            children.append({
                "source": "reddit.com" + reply.permalink,
                "name": "comment",
                "body": reply.body,
                "children": self.scrape_comment(reply)
            })

        return {
            "source": "reddit.com" + comment.permalink,
            "name": "comment",
            "body": comment.body,
            "children": children
        }


api = falcon.API()
api.add_route("/scrapeNode", RedditScraper())
# print(scrape_node("https://old.reddit.com/r/2007scape/"))
