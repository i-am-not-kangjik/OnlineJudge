import java.util.HashMap;
import java.util.Map;

// 내가 푼 코드
class Solution {
    public String solution(String[] participant, String[] completion) {
       HashMap<String, Integer> map = new HashMap<>();

       for (String name : participant) {
        map.put(name, map.getOrDefault(name, 0) + 1);
       }

       for (String name : completion) {
        int count = map.get(name);
        if (count == 1) {
            map.remove(name);
        } else {
            map.put(name, count - 1);
        }
       }

       return map.keySet().iterator().next();
    }
}

// // 다른사람의 풀이를 참고한 코드
// class Solution {
//     public String solution(String[] participant, String[] completion) {
//         HashMap<String, Integer> map = new HashMap<>();

//         for (String name : participant)  map.put(name, map.getOrDefault(name, 0) + 1);
//         for (String name : completion) map.put(name, map.get(name) - 1);

//         for (Map.Entry<String, Integer> entry : map.entrySet()){
//             if (entry.getValue() != 0){
//                 return entry.getKey();
//             }
//         }
//         return "";
//     }
// }