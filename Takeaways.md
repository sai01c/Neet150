# Takeaways from Blind 75

- Counter is basically a dictionary. In python, dictionary doesn't store the order. So, if you want to sort them copy to a list while sorting it. sortedCount = sorted(dict.items(), key = lambda x: x[1], reverse = True)
