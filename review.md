Review
# Data Structure
What -> Use to store data structure. 
Why -> For high efficent access

Linear Table
- Array
    nums = []*10
    size is fixed.
    1. read/write in O(1)
    2. insert/detele/append O(N)
        ex: implement append/delete
        ex: Dynamic Array 
            .get(i)
            .set(i)
            .append(x)
            .deletetail(x)
            .insert(i, x)

- List (LinkedList)
    size is dynamic 
    1. read/write in O(n)
    2. insert/delete/append O(1)
        ex: list find loop
        ex: reverse list

- Extension
    1. Stack
    2. Queue
    
Hash Table
- Dictonary/Map key->value
    size is dynamic
    1. read/write O(1)
    2. insert/delete/append O(1)
      ex: how to implement dictonary. array + hash func.
      ex: hash collision - separate chaining + open addressing
      ex: random hash table. getRandom() -> util.Random(0, N)
- Set: key
    1. no value.


Tree
    - Binary Tree
        children = 2
        topology -> enough
        ex: find common ancesor
        ex: reconstruct with inorder + preorder/postorder
        ex: copy tree
    - Binary Search Tree (BST)
        is binary tree
        node, left.val < node.val < right.val
        data - >Search.
        ex: create bst with sorted array.


Heap
    - Implement with nums[]. -> details is not required, how to use it critical.
    - Put tree structure into array: nums[i] has two children: nums[2*i] nums[2*i+1]
    - Compared with BST, nums[i] > nums[2*i] && nums[i] > nums[2*i + 1]
    - read must be top O(1) nums[0], i.e., top priority.
    - insert is O(logN).
    - removal is top O(logN)
        ex: find kth largestment in array. -> create a heap with size k, min heap, storing k larget elements.

Graph
    - Node.
    - AdjacencyTable/AdjacencyList
    - Children is a list of Node.
    - Direct/InDirectly
    - Cyclic/Ascynlic
    - Connected/Forested
        ex: find a loop in graph? whether a loop in graph?


# Algorithm
To operate on data structure, to achieve some objective
Metric: complexity. 

# Binary Search
    Must be on sorted array.
    while lo < hi
        mid = ()/2
        check 
        if 
            lo = mid + 1
        else hi = mid
    if nums[lo] meets requirement
    ex: h-index

# Depth-first Search -> most challenge
    Search for solution.
        Solution be a single value (find whether x exists), or a list (find path sum).
    dfs(x)
        if x already been visited:
            return
        visit(x)
        for each neight y of x:
            dfs(y) 
    -> on binary tree travseral
        inorder
        postorder
        preorder
    
    -> backtracking
        backtracking(x, currentRes[]):
            if currentRes is optimal:
                return 
            for each neight y of x:
                currentRes.append(y)
                backtracking(y, currentRes)
                currentRes.delete(y)
        -ex: eight queen
    
    -> dfs + memory
        -ex: sample
# Breath-first Search
    Iterative solution.
    Queue
    ->
        dist = 0
        queue.add(node)
        while queue.isEmpty() == false:
            dist++
            qszie = queue.size()
            for i = range(qsize):
                cur = queue.pop();
                visit(cur)
                queue.insert(cur.neight)
    ex: find shortest path from node x to node y.
    ex: serailize and desearilize tree ->  297


# Dynamic Programming
    dp := []
    dp[i] = d[0]..dp[i-1]
    return dp[lenght]
    ex: find panlindrome
        -> use dfs
        -> use dp
    ex: find min coin
    ex: packsack problem
    ex: find optimal/minimal/best/max
    non-ex: find solution structure

# Sorting Algorithm
    mergeSort() -> recruisve
    QuickSort() -> divide and conquer

# Greedy
