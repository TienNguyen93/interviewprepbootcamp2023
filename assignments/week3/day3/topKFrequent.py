# input = ["i","love","leetcode","i","love","coding"]
# k = 2
# output = ["i","love"]
def topKFrequent(self, words: List[str], k: int) -> List[str]:
      if len(words) < k:
          return []

      dic = {}
      for w in words:
          dic[w] = dic.get(w, 0) + 1
  
      # use negated trick to store the words
      heap = []
      for d in dic:
          heapq.heappush(heap, (-dic[d], d))     # heap = [(-2, 'i'), (-2, 'love'), (-1, 'leetcode'), (-1, 'coding')]

      res = []
      while k > 0:
          freq, word = heapq.heappop(heap)
          res.append(word)
          k -= 1
      return res
