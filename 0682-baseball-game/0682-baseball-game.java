class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();
        for(String i : operations)
        {
            if(i.equals("+"))
            {
                int top = stack.pop();
                int t2 = stack.peek();
                stack.push(top);
                stack.push(top + t2);
            }
            else if(i.equals("D"))
            {
                int top = stack.peek();
                stack.push(top*2);
            }
            else if(i.equals("C"))
            {
                stack.pop();
            }
            else
            {
                stack.push(Integer.parseInt(i));
            }
        }
        int sum = 0;
        while(!stack.isEmpty())
        {
            sum += stack.pop();
        }
        return sum;
    }
}