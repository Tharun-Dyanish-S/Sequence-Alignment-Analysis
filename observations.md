2 data clusters:

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

nhash=32 / 64 / 128

The lexicHash github output is not clustering friendly


4 data clusters:
k = 10
linkage:
    method = 'complete'
Works the best
k = 15
Even better
Counter({4: 467, 1: 293, 3: 228, 2: 212})


k=10 has more avg distance than k=15 on eyeing it, reasoning(?)

No encoding (plain string) -- vbad accuracy