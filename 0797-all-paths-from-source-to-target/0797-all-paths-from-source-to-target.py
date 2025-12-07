class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
       
        """
        Finds all paths from node 0 to the last node in a directed graph using DFS.

        :param graph: A list of lists representing the graph where graph[i] is a list
                    of all neighbors of node i.
        :return: A list of all paths from source (0) to target (len(graph) - 1).
        """
        result = []
        # The target node is the last node in the graph
        target_node = len(graph) - 1

        def dfs(current_node, current_path):
            current_path.append(current_node)

            if current_node == target_node:
            
                result.append(list(current_path))
            else:
                # 3. Explore all neighbors
                for neighbor in graph[current_node]:
                    dfs(neighbor, current_path)
         
            current_path.pop()
        dfs(0, [])
        return result