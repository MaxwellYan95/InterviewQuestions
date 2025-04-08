class Solution:
    def operating(self, num1: int, num2: int, operator: str):
        if operator == "+":
            return num1 + num2;
        elif operator == "-":
            return num1 - num2;
        elif operator == "*":
            return num1 * num2;
        return int(num1 / num2);
    def evalRPN(self, tokens: list[str]) -> int:
        stack = [];
        for tok in tokens:
            if len(tok) == 1 and ord(tok) < 48:
                num1 = stack.pop();
                num2 = stack.pop();
                result = self.operating(num2, num1, tok);
                stack.append(result);
            else:
                stack.append(int(tok));
        return stack[len(stack)-1];
