// Last updated: 8/21/2025, 10:01:37 PM
class Solution {
public:
    vector<vector<int>> graph;
    vector<int> indegree_list;
    std::queue<int> no_incoming_queue;
    int num_courses;
    
    void buildGraphAndQueue(vector<vector<int>>& prerequisites){
        graph.resize(num_courses);
        indegree_list.resize(num_courses);
        
        for (auto & pair : prerequisites){
            graph[pair[1]].push_back(pair[0]);
            indegree_list[pair[0]]+=1;
        }
        auto ctr=0;
        for (auto & ai: indegree_list){
            //std::cout<<ctr<<ai<<"\n";
            if(ai==0){
                no_incoming_queue.push(ctr);
                //std::cout<<"Added to queue"<<"\n";
            }
            ctr++;
        }

    }


    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        num_courses = numCourses;
        std::vector<int> order;
        buildGraphAndQueue(prerequisites);
        while(!no_incoming_queue.empty()){
            int node = no_incoming_queue.front();
            no_incoming_queue.pop();
            //std::cout<<node<<" popped\n";
            order.push_back(node);
            for (auto & neighbor: graph[node]){
                indegree_list[neighbor]-=1;
                //std::cout<<neighbor<<" indegree reduced\n";
                if(indegree_list[neighbor]==0){
                    //std::cout<<neighbor<<" added to queue\n";
                    no_incoming_queue.push(neighbor);
                }
            }
        }

        

        if(order.size()==num_courses){
            return order;
        }
        std::vector<int> empty_arr;
        return empty_arr;

    }
};