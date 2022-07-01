from typing import List

# LC 1710 EASY


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sorted_boxes = sorted(boxTypes, key=lambda x: [x[1], x[0]], reverse=False)
        # sorted_boxes = sorted(boxTypes, key=lambda x: x[1], reverse=False)
        boxTypes.sort(key=lambda x: x[1], reverse=False)
        # using boxTypes.sort(key=..) turned out to be slightly faster than storing sorted(), and it uses less memories

        # sorted boxType ascending
        result = 0
        while truckSize > 0:
            try:
                box_number, box_size = boxTypes.pop()
            except:
                break
            # pop the rightmost element which is the largest in box size
            if box_number > truckSize:
                result += truckSize * box_size
                break
            else:
                truckSize -= box_number
                result += box_number * box_size
        return result


def main():
    solver = Solution()
    tests = [
        {"boxTypes": [[1, 3], [2, 2], [3, 1]], "truckSize": 4, "result": 8},
        {"boxTypes": [[5, 10], [2, 5], [4, 7], [3, 9]], "truckSize": 10, "result": 91},
        {
            "boxTypes": [
                [1, 3],
                [5, 5],
                [2, 5],
                [4, 2],
                [4, 1],
                [3, 1],
                [2, 2],
                [1, 3],
                [2, 5],
                [3, 2],
            ],
            "truckSize": 35,
            "result": 76,
        },
    ]
    i = 0
    for test in tests:
        i += 1
        output = solver.maximumUnits(test["boxTypes"], test["truckSize"])
        assert test["result"] == output
        print("Passed Test #{}!".format(i))


if __name__ == "__main__":
    main()
