class Solution:
    def makeFancyString(self, s: str) -> str:
        string_list = list(s)
        i = 0

        while i < len(string_list) - 2:
            if string_list[i] == string_list[i + 1] == string_list[i + 2]:
                print(f"Item removed: {string_list[i]}")
                string_list.pop(i)
                print(string_list)
            else:
                i += 1

        return "".join(string_list)


ddx = 8
dx = 5


a = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1111111111111111111111111111111111111111111111111111111111,
]

# Pesquisar quais pre commits usar
# Indicaçoes: black, isort, flake8  ;  bandit  ;  commitizen
