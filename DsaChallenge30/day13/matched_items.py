class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleKeys = {
            "type" : 0,
            "color" : 1,
            "name" : 2
        }
        matchedItems = 0
        for i in items:
            if i[ruleKeys[ruleKey]] == ruleValue:
                matchedItems += 1
        return matchedItems
