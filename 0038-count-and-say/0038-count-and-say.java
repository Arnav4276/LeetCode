class Solution {
    public String countAndSay(int n) {
        String result="1";
        for(int i=1;i<n;i++){
            result=nextTerm(result);
        }
        return result;
        
    }
    private String nextTerm(String s){
        StringBuilder sb=new StringBuilder();
        int i=0;
        int n=s.length();
        while(i<n){
            char digit=s.charAt(i);
            int count =0;
            while(i<n && s.charAt(i)==digit){
                count++;
                i++;
            }
            sb.append(count).append(digit);
        }
        return sb.toString();
    }
}