in linkage:
    metric = 'jaccard' -- 'euclidean' also few are there
    method = 'complete' / 'average' 
hash function:
    farmhash.hash32() / hashlib.sha256()
k-mer size:
    Changeable
   
k=10
Gave ({1:312, 2:288})
k=15
Gave ({1: 315, 2: 285})
k=20
Gave 470s, 120s

nhash = 32 / 64 / 128

The lexicHash github output is not clustering friendly