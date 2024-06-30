class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        for i in range(len(command)):
            if command[i] == "G":
                ans.append("G")
            elif command[i]=="(":
                if command[i+1]==")":
                    ans.append("o")
                elif command[i+1] == 'a':
                    ans.append("al")

        return "".join(ans)