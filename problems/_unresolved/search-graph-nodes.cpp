class Solution {
public:
    UndirectedGraphNode* searchNode(vector<UndirectedGraphNode*>& graph,
                                    map<UndirectedGraphNode*, int>& values,
                                    UndirectedGraphNode* node,
                                    int target) {
        queue<UndirectedGraphNode*> Q;
        set<UndirectedGraphNode*> hash;
        
        Q.push(node);
        hash.insert(node);
        while(!Q.empty()){
            UndirectedGraphNode* head = Q.front();
            Q.pop();
            if (values[head] == target)
                return head;
            
            for (auto n:head->neighbors){
                if (hash.find(n) == hash.end()){
                    hash.insert(n);
                    Q.push(n);
                }
            }
        }
        return NULL;
    }
};