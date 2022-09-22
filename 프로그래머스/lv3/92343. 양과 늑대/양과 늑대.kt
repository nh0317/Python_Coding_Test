import kotlin.math.*
var maxx : Int = 0


fun cntSheepAndWolf(info: IntArray, mst:ArrayList<Int>):IntArray{
    var sheep = 0
    var wolf = 0
    
    for (u in mst){
        if (info[u] == 0) sheep ++
        else wolf ++
    }
    var res = IntArray(2)
    res[0] = sheep
    res[1] = wolf
    return res
}

fun dfs(info: IntArray, graph: MutableList<MutableList<Int>>, visited: Array<Boolean>, mst:ArrayList<Int>){
    
    var vnear = ArrayList<Int>(0)
    
    for (u in mst){
        for (v in graph.get(u)){
            if (!(v in vnear) && !(v in mst)){
                vnear.add(v)
            }
        }
    }
    var sheapAndWolf = cntSheepAndWolf(info, mst)
    if (sheapAndWolf[0] > sheapAndWolf[1]){
        maxx = max(maxx, sheapAndWolf[0])
    }
    
    for (v in vnear){
        if (!(v in mst)){
            mst.add(v)
            if (info[v]==0) sheapAndWolf[0]++
            else sheapAndWolf[1]++
            
            if(sheapAndWolf[0] > sheapAndWolf[1])
                dfs(info, graph, visited,mst)
            
            mst.remove(v)
            if (info[v]==0) sheapAndWolf[0]--
            else sheapAndWolf[1]--
        }
    }
    
}

class Solution {
    fun solution(info: IntArray, edges: Array<IntArray>): Int {
        var answer: Int = 0
        
        var graph : MutableList<MutableList<Int>>
        var visited = Array(info.size, {false})
        
        graph = ArrayList()
        for (i in 0 until info.size){
            graph.add(ArrayList())
        }
        for (edge in edges){
            graph.get(edge[0]).add(edge[1])
            // graph.get(edge[1]).add(edge[0])
        }
        var mst = ArrayList<Int>(0)
        mst.add(0)
        dfs(info, graph, visited,mst)
        return maxx
    }
}