class ArrayBuilder:
    """
    The program takes 4 inputs, where each input consists of 2 numbers
    in the format x,y. Then it prints a two-dimensional array
    having x rows and y columns for each input.
    The elements of the arrays are whole numbers starting
    from 1 and incrementing by 1.
    """
    __condition = "The program takes 4 inputs, " \
                  "where each input consists of 2 numbers in the format x,y."

    def __init__(self):
        self.__values_validation()

    def __values_validation(self) -> None:
        while True:
            self.__pairs_x_y = []
            try:
                self.__entering_values()
            except ValueError:
                print(self.__condition)
            else:
                self.__pairs_x_y = tuple(self.__pairs_x_y)
                break

    def __entering_values(self) -> None:
        for i in range(4):
            values = input().split(',')
            if len(values) != 2:
                raise ValueError(self.__condition)
            self.__pairs_x_y.append(tuple(map(int, values)))

    @staticmethod
    def __fill_array(pair: tuple) -> list:
        x, y = pair[0], pair[1]
        final_list = [[0 for _ in range(y)] for _ in range(x)]
        counter = 1
        for i in range(x):
            for j in range(y):
                final_list[i][j] = counter
                counter += 1
        return final_list

    def print_arrays(self) -> None:
        for pair in self.__pairs_x_y:
            print(self.__fill_array(pair))


if __name__ == '__main__':
    array_builder = ArrayBuilder()
    array_builder.print_arrays()
