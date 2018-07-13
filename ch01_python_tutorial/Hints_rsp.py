class Hint:
    '''
    Hint()

    Usages:
        len(Hint()) -> The count of hint.

        Hint()[n] -> return n_th hint.

        for hint in Hint():
            print(hint)
    '''

    hints = ["공격자 정보를 저장할 변수하나 선언",
             "가위 바위 보 결과 누군가 승리할 경우는 해당 승자가 공격자로 바뀜",
             "승패가 결정될 수 있는 경우는 가위 바위 보 결과가 비긴 경우 밖에 없음",
             "가위 바위 보 결과가 비긴 경우 공격자가 정해져 있다면 공격자가 이김\n \
             그렇지 않다면(공격자가 결정되어있지 않다면) 선공을 다시 정해야 함",
             "승패가 결정되면 다음 반복을 위해 공격자 변수를 초기화 시킴"]

    def __init__(self):
        self.idx = 0

    def __len__(self):
        return len(self.hints)

    def __getitem__(self, position):
        return self.hints[position]

    def __iter__(self):
        return self.hints.__iter__()

    def next_hint(self):
        if self.idx > len(self.hints):
            print("더 이상 힌트가 없습니다.")
            print
            self.idx = 0
        else:
            print(self.hints[self.idx])
            self.idx += 1
