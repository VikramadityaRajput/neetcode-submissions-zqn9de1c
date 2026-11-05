#include <queue>
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        int rows = grid.size();
        int cols = grid.at(0).size();
        std::set<pair<int, int>> visits;
        int islands = 0;
        
        for (unsigned int r = 0; r < rows; r++) {
            for (unsigned int c = 0; c < cols; c++) {
                if (grid.at(r).at(c) == '1' && !visits.contains({r, c})) {
                    bfs(r, c, grid, visits); 
                    islands += 1;
                }
            }
        }
        return islands; 
    }
private:
    void bfs(int r, int c, vector<vector<char>>& grid, std::set<pair<int, int>>& visits) {
        std::queue<pair<int, int>> q;
        visits.insert({r, c});
        q.push({r, c});
        
        int rows = grid.size();
        int cols = grid.at(0).size();
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        while (!q.empty()) {
            pair<int, int> curr = q.front();
            q.pop();
            
            // 2. Fixed 'cur' to 'curr'
            int cr = curr.first; 
            int cc = curr.second;
            
            for (pair<int, int> dir : directions) {
                int dr = dir.first;
                int dc = dir.second;
                int nr = cr + dr;
                int nc = cc + dc;
                
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && 
                    grid[nr][nc] == '1' && !visits.contains({nr, nc})) {
                    
                    visits.insert({nr, nc});
                    q.push({nr, nc});
                }
            }
        }
    } 
}; 