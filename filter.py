from __future__ import division
import json
import sys

import numpy as np

keep_words = ["Movie", "Film", "netflix", "tv", "series", "watch"]
keep_words = [word.lower() for word in keep_words]


def keep(tweet):
    """Keep a word if it contains a keep word."""
    text = tweet["Text"].lower()
    hashtags = " ".join(tweet["Hashtags"]).lower()
    for word in keep_words:
        if word in text:
            # print("{} in text {}".format(word, text))
            return True
        if word in hashtags:
            # print("{} in hashtags {}".format(word, hastags))
            return True
    return False


def filterAll(media_list_file, in_movie_dir, out_movie_dir):
    """Filter all tweets in Movies folder, save to FilteredMovies."""
    with open(media_list_file) as f:
        names = json.load(f)

    counts = []
    for name in names:
        with open("{}/{}.json".format(in_movie_dir, name)) as f:
            tweets = json.load(f)
            kept_tweets = [t for t in tweets.values() if keep(t)]
            print("total = {}\tkeep = {}\tName = {}".format(
                len(tweets), len(kept_tweets), name))
            counts.append(len(kept_tweets) / len(tweets))
        with open("{}/{}.json".format(out_movie_dir, name), "w") as f:
            json.dump(kept_tweets, f)
    print("Mean kept tweets = {}".format(np.mean(counts)))
