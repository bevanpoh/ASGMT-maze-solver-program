class Math:
    def elementwise_addition(direction_tup1, direction_tup2):
        return (
            direction_tup1[0] + direction_tup2[0],
            direction_tup1[1] + direction_tup2[1],
        )

    def manhattan_distance(node1, node2):
        x1, y1 = node1
        x2, y2 = node2

        return abs(x1 - x2) + abs(y1 - y2)

    def elementwise_subtraction(direction_tup1, direction_tup2):
        return (
            direction_tup1[0] - direction_tup2[0],
            direction_tup1[1] - direction_tup2[1],
        )
