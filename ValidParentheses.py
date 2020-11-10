import array


class ValidParenthe:
    def __init__(self) -> None:

        self._parenthes_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        self._parenthes_ary = array.array('u')

    def valid(self, input: str) -> bool:
        input_n = list(input)
        for i in range(len(input_n)):
            if input_n[i] in self._parenthes_map.values():
                self._parenthes_ary.append(input_n[i])
            elif input_n[i] not in self._parenthes_map.values() and \
                    input_n[i] not in self._parenthes_map:
                continue
            elif self._parenthes_map[input_n[i]] != self._parenthes_ary.pop():                
                return False        
        return True


vp = ValidParenthe()
print(vp.valid(""))
print(vp.valid("{}[]"))
print(vp.valid("[{}()]"))
print(vp.valid("[{1}(1)]"))
print(vp.valid("[{test}test(test)]"))
print(vp.valid("[{}))]"))
