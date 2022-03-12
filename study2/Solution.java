import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.*;

class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        List<LocalTime> timetables = new ArrayList<>();
        String answer = "";

        for (String time : timetable){
            timetables.add(LocalTime.parse(time , DateTimeFormatter.ofPattern("HH:mm")));
        }

        Collections.sort(timetables);
        LocalTime startTime = LocalTime.of(9,0);
        for (int i = 0; i<n; i++){
            if (i!=0){
                startTime = startTime.plusMinutes(t);
            }
            int capa = m;
            LocalTime lastTime = startTime;
            for (int j =0 ; j < m; j++){
                if(!timetables.isEmpty()
                   && (timetables.get(0).isBefore(startTime)
                       || timetables.get(0).equals(startTime))){

                    lastTime=timetables.get(0);
                    timetables.remove(0);
                    capa--;
                }
                if (i==n-1 && capa==0){
                    answer = lastTime.minusMinutes(1).toString();
                }else if(i==n-1 && capa > 0){
                    answer = startTime.toString();
                }
            }

        }
        return answer;
    }
}

//약 1시간 소요