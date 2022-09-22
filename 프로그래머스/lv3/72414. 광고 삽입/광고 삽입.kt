import kotlin.math.*

fun formating(time:Int):String{
    if (time < 10){
        return "0"+time.toString()
    }else return time.toString()
}

fun convert(time:String):Int{
    var t = time.split(":")
    var s = t[0].toInt() * 3600
    s += t[1].toInt() * 60
    s += t[2].toInt()
    return s
}

fun strTime(time:Int):String{
    var h = time / 3600
    var m = time % 3600 / 60
    var s = time % 3600 % 60
    
    var strtime = arrayOf(formating(h), formating(m), formating(s))
    return strtime.joinToString(":")
}

class Solution {
    fun solution(play_time: String, adv_time: String, logs: Array<String>): String {
        var play = convert(play_time)
        var adv = convert(adv_time)
        
        var dp = Array(play+1,{0L})
        
        for (log in logs){
            var l = log.split("-")
            dp[convert(l[0])] += 1L
            dp[convert(l[1])] -= 1L
        }
        
        for (i in 1 until dp.size){
            dp[i] += dp[i-1]
        }
        
        for (i in 1 until dp.size){
            dp[i] += dp[i-1]
        }
        
        
        var viewer = dp[adv]-dp[0]
        var min_time = 0
        for (i in 0 until play - adv){
            if (viewer< dp[i+adv]-dp[i]){
                min_time = i+1
                viewer = dp[i+adv]-dp[i]
            }
        }
        
        return strTime(min_time)
    }
}