''' Given a string A representing JSON object. Return an array of strings denoting JSON object with proper indentation.

Rules for proper indentation:
Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional '\t'

Note:
[] and {} are only acceptable braces in this case.
Assume for this problem that space characters can be done away with. '''

import json


class Solution:
    # @param A : string
    # @return a list of strings

    # not working
    def prettyJSON(self, A, indent=0):
        json_string = A
        json_string = json_string.replace("\n", "")
        json_string = json_string.replace("\t", "")
        json_string = json_string.replace(" ", "")
        json_string = json_string.replace(",}", "}")
        json_string = json_string.replace(",]", "]")

        json_array = json_string.split(',')
        for i in range(len(json_array)):
            if ':' in json_array[i]:
                key, value = json_array[i].split(':')
                json_array[i] = '\t' * indent + f'"{key}": {value}'
            elif json_array[i].startswith('{'):
                json_array[i] = prettyJSON(json_array[i], indent + 1)
            elif json_array[i].startswith('['):
                json_array[i] = prettyJSON(json_array[i], indent + 1)

        return '\n'.join(json_array)

    # working but test failed always
    def prettyJSONLib(self, A):
        json_string = A
        python_object = json.loads(json_string)

        # Convert the Python object back into a JSON string with proper indentation
        pretty_json_string = json.dumps(python_object, indent=2)
        pretty_json_string_arr = pretty_json_string.split('\n')
        pretty_json_string_arr_new = []
        for line in pretty_json_string_arr:
            count = 0
            new_line = ""
            for ch in line:
                if ch.isspace() and count > 0:
                    ch = ch.replace(" ", "\t")
                elif count == 0 and ch.isspace():
                    count += 1
                    pass
                new_line += ch
            pretty_json_string_arr_new.append(new_line)

        return pretty_json_string_arr_new

    # @param A : string
    # @return a list of strings
    # complete solution from itself
    def prettyJSONFinal(self, A):
        indent = 0
        res = []
        line = ''
        for x in A:
            if x in '{[':
                if line:
                    res.append(line)
                res.append('\t' * indent + x)
                line = ''
                indent += 1
            elif x in ']}':
                if line:
                    res.append(line)
                indent -= 1
                line = '\t' * indent + x  # Might be followed by ','
            else:
                if not line:
                    line = '\t' * indent
                line += x
                if x == ",":
                    res.append(line)
                    line = ''
        if line:
            res.append(line)
        return res


s = Solution()
A = '{"A":"B","C":{"D":"E","F":{"G":"H","I":"J"}}}'
print(s.prettyJSONLib(A))
# print(s.prettyJSON(A))
print(s.prettyJSONFinal(A))
